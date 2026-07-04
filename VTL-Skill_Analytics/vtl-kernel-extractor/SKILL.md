---
name: vtl-kernel-extractor
description: Run images through the canonical VTL Kernel Metrics extractor and return deterministic kernel vectors, r_v gradient-field package values, mask QA, hashes, and CSV/JSON outputs. Use when the user provides image paths, image folders, batches, or generated images and asks to measure VTL kernel metrics, extract delta_x, delta_y, r_v, rho_r, mu, x_p, theta, d_s, sdi, mass_fraction, gradient_floor_85, gradient_ceiling_97, tail_gap, EFA, mask_status, mask_mode, mask_sha256, or kernel_vec_sha256 using the latest notebook math rather than older PDF math.
---

# VTL Kernel Extractor

## Purpose

Use this skill to measure images with the current VTL Kernel Metrics device.

This is an execution skill. Prefer the bundled script over retyping formulas:

```text
scripts/extract_kernel.py
```

The notebook math is canonical. The older PDF is background only when it conflicts with the notebook.

## What It Produces

For each image, produce:

- `delta_x`
- `delta_y`
- `r_v`
- `rho_r`
- `mu`
- `x_p`
- `theta`
- `d_s`
- `sdi`
- `mass_fraction`
- `gradient_floor_85`
- `gradient_ceiling_97`
- `tail_gap`
- `efa`
- `r_v_threshold`
- `valid`
- `quality_note`
- `mask_status`
- `mask_mode`
- `mask_reasons`
- `n_components`
- `largest_component_fraction`
- `sha256`
- `mask_sha256`
- `kernel_vec_sha256`

## Canonical Mode

Use canonical mode when local dependencies are available:

```bash
python scripts/extract_kernel.py <image-or-folder> --out-dir <output-dir>
```

Canonical constants:

- `TARGET_MAX_SIDE = 1536`
- `GRAD_LOW_PCT = 85.0`
- `GRAD_HIGH_PCT = 97.0`
- `EDGE_MARGIN_PX = 2`
- `MIN_MASS_FRAC = 0.001`
- `WARN_MASS_FRAC = 0.03`
- `R_V_ABSOLUTE_THRESHOLD = 0.15`
- `ORIENT_BINS = 8`

The script writes:

- `kernel_metrics.csv`
- `kernel_metrics.json`

## Approximate Mode

Use approximate language only when the script cannot run or an image is inaccessible.

Rules:

- Do not fabricate numeric metrics.
- Do not compare approximate output to canonical notebook output.
- Do not use approximate output for audits, papers, cross-engine claims, or reproducibility claims.
- If partial metrics are available, label missing metrics explicitly.

## Workflow

1. Resolve image inputs.
   - Accept a single image, multiple paths, a folder, or a CSV/list of paths.
   - Supported extensions: `.png`, `.jpg`, `.jpeg`, `.webp`, `.bmp`, `.tif`, `.tiff`.

2. Run `scripts/extract_kernel.py`.
   - Use an output directory in the workspace or `/tmp` unless the user specifies a destination.
   - If dependency failure occurs, report the missing package and do not invent values.

3. Inspect output.
   - Read the CSV or JSON summary.
   - Report the key metrics compactly.
   - Always include the `r_v` field package: `r_v`, `gradient_floor_85`, `gradient_ceiling_97`, `tail_gap` or `efa`.

4. Apply hard stops.
   - If `valid = 0`, report the vector as invalid/low-confidence.
   - If `mask_status = FAIL`, do not over-interpret the image.
   - If comparing images, confirm the same script/constants were used.

5. Route next step if needed.
   - For meaning of values, use `vtl-kernel-interpreter` once available.
   - For `r_v` package nuance, use `vtl-rv-gradient-field-interpreter` once available.
   - For formula/code audit, use `vtl-kernel-scoring-auditor` once available.

## Output Format

For one image:

```text
Classification:
Execution Mode: <canonical | approximate | failed>
Input Type: <single | batch | folder>
Comparability Status: <valid | provisional | invalid>

Data Integrity Check:
- image accessible → <yes/no>
- dependencies available → <yes/no>
- script version known → <yes/no>

If not:
→ force approximate or fail

If canonical mode cannot run:
→ DO NOT output numeric kernel values

Do not interpret r_v without:
- gradient_floor_85
- tail_gap

If mask_status = FAIL:
→ vector is invalid for interpretation
→ report only, do not analyze

Comparability valid only if:
- same script version
- same constants
- same preprocessing
- matching hashes (or expected)

Single image:
→ report only

Batch:
→ allow distribution insight

Do not:
- infer intent
- infer prompt success
- infer aesthetics

If dependency missing:
→ Execution Mode = failed
→ report missing package
→ do not fallback silently

Image:
<filename/path>

Kernel vector:
delta_x=<...>, delta_y=<...>, r_v=<...>, rho_r=<...>, mu=<...>, x_p=<...>, theta=<...>, d_s=<...>, sdi=<...>

r_v field package:
gradient_floor_85=<...>, gradient_ceiling_97=<...>, tail_gap=<...>, efa=<...>, threshold=0.15

QA:
valid=<0/1>, mass_fraction=<...>, mask_status=<PASS/WARN/FAIL>, mask_mode=<REGION_FIELD/TEXTURE_FIELD/INVALID>, reasons=<...>

Artifacts:
<CSV/JSON paths>

Limits:
<dependency, approximation, mask, comparability, or single-image caveat>

If same image produces different hashes:
→ flag drift
→ invalidate comparison

Do not:
- expand beyond kernel + QA + r_v package

VTL Kernel → measurement
VCLI-G / SCI → interpretation layer
RCP → behavior detection

Confidence:
<high | medium | low>

Drivers:
- canonical vs approximate
- mask_status
- dependency completeness
```

For batches, provide the artifact paths and a compact table with:

`filename`, `delta_x`, `delta_y`, `r_v`, `rho_r`, `mu`, `x_p`, `theta`, `d_s`, `sdi`, `tail_gap`, `mask_status`, `mask_mode`.

## References

Read [canonical-math.md](references/canonical-math.md) when checking constants, field definitions, or notebook-source alignment.

Read [runbook.md](references/runbook.md) when deciding how to invoke the script, handle dependency failures, or present outputs.

## Constraints

- Do not infer semantics, intent, prompt obedience, image quality, aesthetic value, viewer attention, or cultural value from extracted metrics.
- Do not treat a single image kernel vector as collapse; collapse is distributional unless a separate detector is used.
- Do not report `r_v` without `gradient_floor_85`, `gradient_ceiling_97`, and `tail_gap`.
- Do not compare runs if constants, preprocessing, dependencies, or script version differ.
- Do not treat `mass_fraction` as compositional occupancy; it is tied to the percentile mask.
- Do not hide `mask_status`, `mask_mode`, or `quality_note`.
- Do not use older PDF math when it conflicts with the current notebook/script.

## Attribution

VTL Kernel Metrics are part of the Visual Thinking Lens system authored by Russell Parrish / A.rtist I.nfluencer. Preserve attribution when packaging, distributing, or publishing derived materials.

This package contains a modular visual reasoning skill suite built from Russell Parrish / A.rtist I.nfluencer protocols. The skills are designed to run independently, but they also interoperate through routing, handoff notes, and shared visual reasoning concepts. More information: www.artistinfluencer.com. Copyright 2026.
