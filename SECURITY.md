# Security Scan — `roboflow-inference`

> Best-effort static scan by `repo-archaeologist`. This is **not** a substitute for a real SAST/DAST tool (bandit, semgrep, gitleaks, dependabot). It is a first-pass 'is there anything obviously scary here?' check.

## Summary

| Severity | Count |
|---|---:|
| 🟠 HIGH | 51 |
| 🟡 MEDIUM | 21 |
| 🔵 LOW | 51 |

**Total findings:** 123

## Findings

### 🟠 HIGH (51)

| File | Line | Category | Message |
|---|---:|---|---|
| `inference/core/interfaces/camera/stream_error_codes.py` | 8 | secret | Possible secret assigned to `STREAM_AUTH_FAILED` |
| `inference/core/interfaces/stream_manager/manager_app/entities.py` | 40 | secret | Possible secret assigned to `AUTHORISATION_ERROR` |
| `inference/core/roboflow_api.py` | 125 | secret | Possible secret assigned to `ASSUME_IDENTITY_ACCESS_TOKEN_HEADER` |
| `inference/core/roboflow_api.py` | 126 | secret | Possible secret assigned to `ASSUME_IDENTITY_AUTHORISED_WORKSPACE_HEADER` |
| `inference/enterprise/stream_management/manager/entities.py` | 23 | secret | Possible secret assigned to `AUTHORISATION_ERROR` |
| `inference/landing/src/app/components/Examples.tsx` | 25 | secret | Possible secret assigned to `api_key` |
| `inference/landing/src/app/components/Examples.tsx` | 46 | secret | Possible secret assigned to `api_key` |
| `inference/landing/src/app/components/Examples.tsx` | 62 | secret | Possible secret assigned to `api_key` |
| `inference/landing/src/app/components/Examples.tsx` | 76 | secret | Possible secret assigned to `api_key` |
| `inference_models/inference_models/runtime_introspection/core.py` | 300 | dangerous-call | subprocess with `shell=True` |
| `inference_models/inference_models/runtime_introspection/core.py` | 348 | dangerous-call | subprocess with `shell=True` |
| `inference_models/inference_models/runtime_introspection/core.py` | 373 | dangerous-call | subprocess with `shell=True` |
| `inference_models/inference_models/weights_providers/core.py` | 77 | secret | Possible secret assigned to `api_key` |
| `inference_models/tests/unit_tests/models/auto_loaders/test_core.py` | 5395 | secret | Possible secret assigned to `effective_api_key` |
| `inference_models/tests/unit_tests/models/auto_loaders/test_core.py` | 5534 | secret | Possible secret assigned to `effective_api_key` |
| `inference_models/tests/unit_tests/models/auto_loaders/test_core.py` | 5927 | secret | Possible secret assigned to `effective_api_key` |
| `modal/deploy_modal_app.py` | 15 | secret | Possible secret assigned to `MODAL_TOKEN_SECRET` |
| `modal/utils.py` | 49 | secret | Possible secret assigned to `MODAL_TOKEN_SECRET` |
| `tests/inference/unit_tests/core/interfaces/camera/test_camera_log_credential_redaction.py` | 27 | secret | Possible secret assigned to `SECRET` |
| `tests/inference/unit_tests/core/interfaces/http/test_http_api.py` | 1444 | secret | Possible secret assigned to `api_key` |
| `tests/inference/unit_tests/core/interfaces/http/test_http_api.py` | 1460 | secret | Possible secret assigned to `api_key` |
| `tests/inference/unit_tests/core/interfaces/webrtc_worker/test_start_worker_region_enforcement.py` | 73 | secret | Possible secret assigned to `api_key` |
| `tests/inference/unit_tests/core/test_roboflow_api.py` | 5282 | secret | Possible secret assigned to `secret_api_key` |
| `tests/inference/unit_tests/usage_tracking/test_decorator_helpers.py` | 107 | secret | Possible secret assigned to `api_key` |
| `tests/inference/unit_tests/usage_tracking/test_decorator_helpers.py` | 128 | secret | Possible secret assigned to `api_key` |
| `tests/inference/unit_tests/usage_tracking/test_decorator_helpers.py` | 297 | secret | Possible secret assigned to `api_key` |
| `tests/inference/unit_tests/usage_tracking/test_decorator_helpers.py` | 304 | secret | Possible secret assigned to `usage_api_key` |
| `tests/inference/unit_tests/usage_tracking/test_decorator_helpers.py` | 316 | secret | Possible secret assigned to `api_key` |
| `tests/workflows/integration_tests/execution/test_existing_blocks_modal_compatibility.py` | 9 | secret | Possible secret assigned to `MODAL_TOKEN_SECRET` |
| `tests/workflows/integration_tests/execution/test_workflow_with_custom_python_block_modal.py` | 10 | secret | Possible secret assigned to `MODAL_TOKEN_SECRET` |
| `tests/workflows/integration_tests/execution/test_workflow_with_onvif.py` | 419 | secret | Possible secret assigned to `token` |
| `tests/workflows/integration_tests/execution/test_workflow_with_onvif.py` | 550 | secret | Possible secret assigned to `token` |
| `tests/workflows/unit_tests/core_steps/common/test_openrouter.py` | 72 | secret | Possible secret assigned to `api_key` |
| `tests/workflows/unit_tests/core_steps/sinks/test_email_v2.py` | 466 | secret | Possible secret assigned to `api_key` |
| `tests/workflows/unit_tests/core_steps/sinks/test_email_v2.py` | 511 | secret | Possible secret assigned to `api_key` |
| `tests/workflows/unit_tests/core_steps/sinks/test_email_v2.py` | 548 | secret | Possible secret assigned to `api_key` |
| `tests/workflows/unit_tests/core_steps/sinks/test_email_v2.py` | 585 | secret | Possible secret assigned to `api_key` |
| `tests/workflows/unit_tests/core_steps/sinks/test_email_v2.py` | 622 | secret | Possible secret assigned to `api_key` |
| `tests/workflows/unit_tests/core_steps/sinks/test_email_v2.py` | 659 | secret | Possible secret assigned to `api_key` |
| `tests/workflows/unit_tests/core_steps/sinks/test_email_v2.py` | 699 | secret | Possible secret assigned to `api_key` |
| `tests/workflows/unit_tests/core_steps/sinks/test_email_v2.py` | 737 | secret | Possible secret assigned to `api_key` |
| `tests/workflows/unit_tests/core_steps/sinks/test_email_v2.py` | 775 | secret | Possible secret assigned to `api_key` |
| `tests/workflows/unit_tests/core_steps/sinks/test_email_v2.py` | 1161 | secret | Possible secret assigned to `api_key` |
| `tests/workflows/unit_tests/core_steps/sinks/test_email_v2.py` | 1211 | secret | Possible secret assigned to `api_key` |
| `tests/workflows/unit_tests/core_steps/sinks/test_email_v2.py` | 1378 | secret | Possible secret assigned to `api_key` |
| `tests/workflows/unit_tests/core_steps/sinks/test_email_v2.py` | 1429 | secret | Possible secret assigned to `api_key` |
| `tests/workflows/unit_tests/core_steps/sinks/test_email_v2_inline_images.py` | 209 | secret | Possible secret assigned to `api_key` |
| `tests/workflows/unit_tests/core_steps/sinks/test_email_v2_inline_images.py` | 265 | secret | Possible secret assigned to `api_key` |
| `tests/workflows/unit_tests/core_steps/sinks/test_email_v2_inline_images.py` | 315 | secret | Possible secret assigned to `api_key` |
| `tests/workflows/unit_tests/core_steps/sinks/test_email_v2_inline_images.py` | 373 | secret | Possible secret assigned to `api_key` |
| `tests/workflows/unit_tests/core_steps/sinks/test_email_v2_inline_images.py` | 421 | secret | Possible secret assigned to `api_key` |

### 🟡 MEDIUM (21)

| File | Line | Category | Message |
|---|---:|---|---|
| `development/stream_interface/rfdetr_coco_same_shape_parity.py` | 305 | dangerous-call | Use of `pickle.load(s)` — deserializing untrusted pickle is unsafe |
| `development/stream_interface/rfdetr_coco_same_shape_parity.py` | 416 | dangerous-call | Use of `pickle.load(s)` — deserializing untrusted pickle is unsafe |
| `development/stream_interface/rfdetr_preprocess_microbenchmark.py` | 396 | dangerous-call | Use of `pickle.load(s)` — deserializing untrusted pickle is unsafe |
| `development/stream_interface/rfdetr_rle_postprocess_microbenchmark.py` | 350 | dangerous-call | Use of `pickle.load(s)` — deserializing untrusted pickle is unsafe |
| `development/stream_interface/rfdetr_rle_to_poly_microbenchmark.py` | 241 | dangerous-call | Use of `pickle.load(s)` — deserializing untrusted pickle is unsafe |
| `development/stream_interface/rfdetr_workflow_video_parity.py` | 377 | dangerous-call | Use of `pickle.load(s)` — deserializing untrusted pickle is unsafe |
| `docs/scripts/macros.py` | 22 | dangerous-call | Use of `exec()` |
| `inference/core/cache/redis.py` | 209 | dangerous-call | Use of `pickle.load(s)` — deserializing untrusted pickle is unsafe |
| `inference/core/utils/image_utils.py` | 353 | dangerous-call | Use of `pickle.load(s)` — deserializing untrusted pickle is unsafe |
| `inference/core/workflows/execution_engine/v1/dynamic_blocks/block_scaffolding.py` | 432 | dangerous-call | Use of `exec()` |
| `inference/enterprise/parallel/entrypoint.py` | 33 | dangerous-call | Use of `os.system()` |
| `inference/landing/out/404.html` | 1 | secret | High-entropy string literal (entropy=4.6) |
| `inference/landing/out/_not-found.html` | 1 | secret | High-entropy string literal (entropy=4.6) |
| `inference/landing/out/dashboard.html` | 1 | secret | High-entropy string literal (entropy=4.6) |
| `inference/landing/out/index.html` | 1 | secret | High-entropy string literal (entropy=4.6) |
| `inference/landing/out/notebook-instructions.html` | 1 | secret | High-entropy string literal (entropy=4.6) |
| `modal/modal_app.py` | 233 | dangerous-call | Use of `exec()` |
| `modal/modal_app.py` | 234 | dangerous-call | Use of `exec()` |
| `tests/workflows/integration_tests/execution/control_flow_with_side_effects/test_rfdetr_sliced_workflow_main_parity.py` | 780 | dangerous-call | Use of `pickle.load(s)` — deserializing untrusted pickle is unsafe |
| `tests/workflows/integration_tests/execution/stub_plugins/rock_paper_scissor_plugin/expression.py` | 67 | dangerous-call | Use of `exec()` |
| `theme/js/segment.js` | 1 | secret | High-entropy string literal (entropy=4.6) |

### 🔵 LOW (51)

| File | Line | Category | Message |
|---|---:|---|---|
| `docker/scripts/build_opencv.sh` | 101 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `inference/core/workflows/core_steps/transformations/image_slicer/v1.py` | 199 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `inference/core/workflows/core_steps/visualizations/common/fonts/registry.py` | 88 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `inference/core/workflows/core_steps/visualizations/common/fonts/registry.py` | 90 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `inference/core/workflows/core_steps/visualizations/common/fonts/registry.py` | 100 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `inference/core/workflows/core_steps/visualizations/common/fonts/registry.py` | 102 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `inference/core/workflows/core_steps/visualizations/common/fonts/registry.py` | 112 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `inference/core/workflows/core_steps/visualizations/common/fonts/registry.py` | 114 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `inference/core/workflows/core_steps/visualizations/common/fonts/registry.py` | 124 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `inference/core/workflows/core_steps/visualizations/common/fonts/registry.py` | 126 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `inference/core/workflows/core_steps/visualizations/common/fonts/registry.py` | 136 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `inference/core/workflows/core_steps/visualizations/common/fonts/registry.py` | 138 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `inference/core/workflows/core_steps/visualizations/common/fonts/registry.py` | 148 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `inference/core/workflows/core_steps/visualizations/common/fonts/registry.py` | 150 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `inference/core/workflows/core_steps/visualizations/common/fonts/registry.py` | 160 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `inference/core/workflows/core_steps/visualizations/common/fonts/registry.py` | 162 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `inference/core/workflows/core_steps/visualizations/common/fonts/registry.py` | 172 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `inference/core/workflows/core_steps/visualizations/common/fonts/registry.py` | 174 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `inference/core/workflows/core_steps/visualizations/common/fonts/registry.py` | 184 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `inference/core/workflows/core_steps/visualizations/common/fonts/registry.py` | 186 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `inference/core/workflows/core_steps/visualizations/common/fonts/registry.py` | 196 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `inference/core/workflows/core_steps/visualizations/common/fonts/registry.py` | 198 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `inference/core/workflows/core_steps/visualizations/common/fonts/registry.py` | 208 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `inference/core/workflows/core_steps/visualizations/common/fonts/registry.py` | 210 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `inference/core/workflows/core_steps/visualizations/common/fonts/registry.py` | 220 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `inference/core/workflows/core_steps/visualizations/common/fonts/registry.py` | 222 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `inference/core/workflows/core_steps/visualizations/common/fonts/registry.py` | 232 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `inference/core/workflows/core_steps/visualizations/common/fonts/registry.py` | 234 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `inference/core/workflows/core_steps/visualizations/common/fonts/registry.py` | 244 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `inference/core/workflows/core_steps/visualizations/common/fonts/registry.py` | 246 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `inference/core/workflows/core_steps/visualizations/common/fonts/registry.py` | 256 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `inference/core/workflows/core_steps/visualizations/common/fonts/registry.py` | 258 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `inference/core/workflows/core_steps/visualizations/common/fonts/registry.py` | 268 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `inference/core/workflows/core_steps/visualizations/common/fonts/registry.py` | 270 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `inference/core/workflows/core_steps/visualizations/common/fonts/registry.py` | 280 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `inference/core/workflows/core_steps/visualizations/common/fonts/registry.py` | 282 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `inference/core/workflows/core_steps/visualizations/common/fonts/registry.py` | 292 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `inference/core/workflows/core_steps/visualizations/common/fonts/registry.py` | 294 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `inference/models/perception_encoder/vision_encoder/tokenizer.py` | 115 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `inference_models/inference_models/models/perception_encoder/vision_encoder/tokenizer.py` | 112 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `inference_models/inference_models/models/rfdetr/projector.py` | 31 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `requirements/requirements.cosmos.txt` | 14 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `requirements/requirements.sam3_3d.txt` | 1 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `requirements/requirements.sam3_3d.txt` | 2 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `requirements/requirements.sam3_3d.txt` | 14 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `requirements/requirements.sam3_3d.txt` | 15 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `requirements/requirements.sam3_3d.txt` | 22 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `requirements/requirements.sam3_3d.txt` | 23 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `requirements/requirements.sam3_3d.txt` | 24 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `requirements/requirements.transformers.txt` | 9 | secret | Possible 40-hex token (legacy GitHub SHA or token) |
| `tests/workflows/integration_tests/execution/conftest.py` | 150 | secret | Possible 40-hex token (legacy GitHub SHA or token) |

## What this scan checks

- **Secrets**: AWS access keys, AWS secret keys, GitHub tokens, Slack tokens, Google API keys, JWT literals, private key blocks, and high-entropy strings assigned to secret-looking variable names.
- **Deprecated packages**: a small offline list of widely-abandoned packages from `requirements.txt`, `pyproject.toml`, and `package.json`.
- **Dangerous calls**: `eval`, `exec`, `os.system`, `subprocess` with `shell=True`, `pickle.load`, `mktemp`, and JS `new Function` / `child_process` with `shell: true`.

_False positives are expected. Triage by severity, then verify each hit._
