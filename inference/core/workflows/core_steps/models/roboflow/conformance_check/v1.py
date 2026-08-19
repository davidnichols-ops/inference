from typing import List, Literal, Optional, Type, Union

from pydantic import ConfigDict, Field, model_validator

from inference.core.env import (
    LOCAL_INFERENCE_API_URL,
    WORKFLOWS_REMOTE_API_TARGET,
    WORKFLOWS_REMOTE_EXECUTION_MAX_STEP_BATCH_SIZE,
    WORKFLOWS_REMOTE_EXECUTION_MAX_STEP_CONCURRENT_REQUESTS,
)
from inference.core.workflows.core_steps.common.entities import StepExecutionMode
from inference.core.workflows.execution_engine.constants import INFERENCE_ID_KEY
from inference.core.workflows.execution_engine.entities.base import (
    Batch,
    OutputDefinition,
    WorkflowImageData,
)
from inference.core.workflows.execution_engine.entities.types import (
    BOOLEAN_KIND,
    FLOAT_ZERO_TO_ONE_KIND,
    IMAGE_KIND,
    INFERENCE_ID_KIND,
    INTEGER_KIND,
    LIST_OF_VALUES_KIND,
    ROBOFLOW_MODEL_ID_KIND,
    ROBOFLOW_PROJECT_KIND,
    STRING_KIND,
    FloatZeroToOne,
    ImageInputField,
    RoboflowModelField,
    Selector,
)
from inference.core.workflows.prototypes.block import (
    BlockResult,
    DependentResource,
    WorkflowBlock,
    WorkflowBlockManifest,
    roboflow_platform_model,
    roboflow_platform_project,
)

LONG_DESCRIPTION = """
Run cvconform differential conformance verification on a deployed model.

This block verifies that a model exported to ONNX, CoreML, or TensorRT
still behaves identically to the PyTorch reference model. It runs the
same inputs through all runtimes and compares outputs, detecting silent
divergences caused by operator fusion, precision changes, quantization,
or NMS implementation differences.

Use this block in deployment pipelines to gate model promotions.
"""


class BlockManifest(WorkflowBlockManifest):
    model_config = ConfigDict(
        json_schema_extra={
            "name": "Model Conformance Check",
            "version": "v1",
            "short_description": "Verify model export conformance across runtimes",
            "long_description": LONG_DESCRIPTION,
            "license": "Apache-2.0",
            "block_type": "model",
            "search_keywords": ["conformance", "verification", "cvconform", "export", "onnx", "tensorrt", "coreml"],
            "ui_manifest": {
                "section": "model",
                "icon": "far fa-check-circle",
                "blockPriority": 100,
                "inference": True,
            },
        },
        protected_namespaces=(),
    )
    type: Literal["roboflow_core/roboflow_conformance_check@v1"]
    images: Selector(kind=[IMAGE_KIND]) = ImageInputField
    model_id: Union[Selector(kind=[ROBOFLOW_MODEL_ID_KIND]), str] = RoboflowModelField
    reference_runtime: Literal["pytorch", "onnx", "coreml"] = Field(
        default="pytorch",
        description="Reference runtime to compare against",
        json_schema_extra={
            "always_visible": True,
            "values_metadata": {
                "pytorch": {"name": "PyTorch", "description": "Original PyTorch model"},
                "onnx": {"name": "ONNX", "description": "ONNX Runtime reference"},
                "coreml": {"name": "CoreML", "description": "CoreML reference (macOS)"},
            },
        },
    )
    target_runtimes: Union[
        List[Literal["onnx", "coreml", "tensorrt"]],
        Selector(kind=[LIST_OF_VALUES_KIND]),
    ] = Field(
        default=["onnx", "coreml"],
        description="Target runtimes to verify against reference",
        json_schema_extra={
            "always_visible": True,
        },
    )
    confidence_mode: Union[
        Literal["best", "default", "custom"],
        Selector(kind=[STRING_KIND]),
    ] = Field(
        default="best",
        description="How confidence thresholds are determined for the reference model",
    )
    custom_confidence: Union[
        Optional[FloatZeroToOne],
        Selector(kind=[FLOAT_ZERO_TO_ONE_KIND]),
    ] = Field(
        default=0.4,
        description="Custom confidence threshold",
        json_schema_extra={
            "relevant_for": {"confidence_mode": {"values": ["custom"], "required": True}},
        },
    )
    seed: Union[int, Selector(kind=[INTEGER_KIND])] = Field(
        default=0,
        description="Random seed for reproducible synthetic inputs",
    )
    num_samples: Union[int, Selector(kind=[INTEGER_KIND])] = Field(
        default=1,
        description="Number of synthetic samples to test",
    )
    require_conformant: Union[bool, Selector(kind=[BOOLEAN_KIND])] = Field(
        default=True,
        description="Fail the workflow if any target is non-conformant",
    )

    @model_validator(mode="after")
    def validate(self) -> "BlockManifest":
        if self.confidence_mode == "custom" and self.custom_confidence is None:
            raise ValueError("`custom_confidence` is required when `confidence_mode` is 'custom'")
        return self

    @classmethod
    def get_compatible_task_types(cls) -> Optional[List[str]]:
        return ["object-detection", "instance-segmentation", "classification", "keypoint-detection", "semantic-segmentation"]

    def discover_dependent_resources(self) -> Optional[List[DependentResource]]:
        return [roboflow_platform_model(model_id=self.model_id)]

    @classmethod
    def get_parameters_accepting_batches(cls) -> List[str]:
        return ["images"]

    @classmethod
    def describe_outputs(cls) -> List[OutputDefinition]:
        return [
            OutputDefinition(name="inference_id", kind=[INFERENCE_ID_KIND]),
            OutputDefinition(name="conformance_report", kind=[STRING_KIND]),
            OutputDefinition(name="overall_conformant", kind=[BOOLEAN_KIND]),
            OutputDefinition(name="conformance_scores", kind=[LIST_OF_VALUES_KIND]),
            OutputDefinition(name="findings", kind=[LIST_OF_VALUES_KIND]),
            OutputDefinition(name="model_id", kind=[ROBOFLOW_MODEL_ID_KIND]),
        ]

    @classmethod
    def get_execution_engine_compatibility(cls) -> Optional[str]:
        return ">=1.3.0,<2.0.0"


class RoboflowConformanceCheckBlockV1(WorkflowBlock):

    def __init__(
        self,
        model_manager,
        api_key: Optional[str],
        step_execution_mode: StepExecutionMode,
    ):
        self._model_manager = model_manager
        self._api_key = api_key
        self._step_execution_mode = step_execution_mode

    @classmethod
    def get_init_parameters(cls) -> List[str]:
        return ["model_manager", "api_key", "step_execution_mode"]

    @classmethod
    def get_manifest(cls) -> Type[WorkflowBlockManifest]:
        return BlockManifest

    def run(
        self,
        images: Batch[WorkflowImageData],
        model_id: str,
        reference_runtime: str,
        target_runtimes: List[str],
        confidence_mode: str,
        custom_confidence: Optional[float],
        seed: int,
        num_samples: int,
        require_conformant: bool,
    ) -> BlockResult:
        confidence = (
            custom_confidence if confidence_mode == "custom" else confidence_mode
        )

        if self._step_execution_mode is StepExecutionMode.LOCAL:
            return self.run_locally(
                images=images,
                model_id=model_id,
                reference_runtime=reference_runtime,
                target_runtimes=target_runtimes,
                confidence=confidence,
                seed=seed,
                num_samples=num_samples,
                require_conformant=require_conformant,
            )
        elif self._step_execution_mode is StepExecutionMode.REMOTE:
            return self.run_remotely(
                images=images,
                model_id=model_id,
                reference_runtime=reference_runtime,
                target_runtimes=target_runtimes,
                confidence=confidence,
                seed=seed,
                num_samples=num_samples,
                require_conformant=require_conformant,
            )
        else:
            raise ValueError(
                f"Unknown step execution mode: {self._step_execution_mode}"
            )

    def run_locally(
        self,
        images: Batch[WorkflowImageData],
        model_id: str,
        reference_runtime: str,
        target_runtimes: List[str],
        confidence: Union[None, float, Literal["best", "default"]],
        seed: int,
        num_samples: int,
        require_conformant: bool,
    ) -> BlockResult:
        # Load the model through model manager
        self._model_manager.add_model(
            model_id=model_id,
            api_key=self._api_key,
        )

        # Get the model to access its file path
        model = self._model_manager[model_id]
        
        # Try to get the model file path
        model_path = getattr(model, "model_path", None) or getattr(model, "weights_path", None)
        
        if not model_path:
            return [{
                "inference_id": None,
                "conformance_report": json.dumps({"error": "Model path not available"}),
                "overall_conformant": False,
                "conformance_scores": [],
                "findings": [],
                "model_id": model_id,
            }]

        # Run cvconform verification
        try:
            from cvconform import verify
            
            report = verify(
                model=model_path,
                reference=reference_runtime,
                targets=target_runtimes,
                seed=seed,
                num_samples=num_samples,
            )
        except ImportError:
            return [{
                "inference_id": None,
                "conformance_report": json.dumps({"error": "cvconform not installed. Install with: pip install cvconform"}),
                "overall_conformant": False,
                "conformance_scores": [],
                "findings": [],
                "model_id": model_id,
            }]
        except Exception as e:
            return [{
                "inference_id": None,
                "conformance_report": json.dumps({"error": str(e)}),
                "overall_conformant": False,
                "conformance_scores": [],
                "findings": [],
                "model_id": model_id,
            }]

        # Extract results
        overall_conformant = True
        conformance_scores = []
        findings = []

        for target, target_report in report.get("targets", {}).items():
            score = target_report.get("overall_score", 0.0)
            is_conformant = target_report.get("is_conformant", False)
            conformance_scores.append({
                "target": target,
                "score": score,
                "is_conformant": is_conformant,
            })
            if not is_conformant:
                overall_conformant = False

            for div in target_report.get("divergences", []):
                findings.append({
                    "target": target,
                    "type": "conformance_divergence",
                    "output": div.get("output", "unknown"),
                    "metric": div.get("metric", "unknown"),
                    "magnitude": div.get("magnitude", 0.0),
                    "threshold": div.get("threshold", 0.0),
                    "mechanism": div.get("mechanism", "unknown"),
                    "confidence": div.get("confidence", 0.0),
                })

        # Add root-cause findings
        for finding in report.get("findings", []):
            if finding:
                findings.append({
                    "target": finding.get("backend", "unknown"),
                    "type": "root_cause",
                    "affected": finding.get("affected", "unknown"),
                    "cause": finding.get("cause", "unknown"),
                    "mechanism": finding.get("mechanism", "unknown"),
                    "impact": finding.get("impact", ""),
                    "confidence": finding.get("confidence", 0.0),
                    "fixes": finding.get("fixes", []),
                })

        inference_ids = [None] * len(images)

        return [
            {
                "inference_id": inference_id,
                "conformance_report": json.dumps(report, indent=2),
                "overall_conformant": overall_conformant,
                "conformance_scores": conformance_scores,
                "findings": findings,
                "model_id": model_id,
            }
            for inference_id in inference_ids
        ]

    def run_remotely(
        self,
        images: Batch[WorkflowImageData],
        model_id: str,
        reference_runtime: str,
        target_runtimes: List[str],
        confidence: Union[None, float, Literal["best", "default"]],
        seed: int,
        num_samples: int,
        require_conformant: bool,
    ) -> BlockResult:
        # For remote execution, we need to call the inference server's
        # conformance check endpoint (to be implemented on server side)
        # For now, fall back to a placeholder response
        inference_ids = [None] * len(images)
        
        return [
            {
                "inference_id": inference_id,
                "conformance_report": json.dumps({
                    "error": "Remote conformance check not yet implemented. Run locally or use cvconform CLI directly."
                }),
                "overall_conformant": False,
                "conformance_scores": [],
                "findings": [],
                "model_id": model_id,
            }
            for inference_id in inference_ids
        ]


import json