# Runbook

## Basic Use

Run on a single image:

```bash
python scripts/extract_kernel.py /path/to/image.png --out-dir /tmp/vtl_kernel_out
```

Run on a folder:

```bash
python scripts/extract_kernel.py /path/to/images --out-dir /tmp/vtl_kernel_out
```

Output files:

- `kernel_metrics.csv`
- `kernel_metrics.json`

## Dependency Handling

Canonical extraction requires:

- `numpy`
- `pandas`
- `opencv-python` or `opencv-python-headless` importable as `cv2`
- `scipy`
- `scikit-image`

If a dependency is missing:

1. Report the missing dependency.
2. Do not invent metrics.
3. Ask whether to install dependencies if installation is appropriate.

## Reporting

For one image, report the full kernel vector plus QA.

For batches, summarize:

- number of images,
- output paths,
- any `FAIL` or `WARN` masks,
- min/max or top outliers only if useful.

Always preserve:

- `mask_status`
- `mask_mode`
- `quality_note`
- `r_v` field package.

## Comparability

Comparable runs require:

- same script version,
- same constants,
- same preprocessing,
- same dependency behavior,
- same input image bytes.

Use hashes:

- `sha256` identifies input image bytes.
- `mask_sha256` identifies the extracted mask.
- `kernel_vec_sha256` identifies the extracted metric vector.

If hashes differ for the same image under the same conditions, treat the run as drifted.
