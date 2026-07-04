---
name: vtl-kernel-interpreter
description: Interpret current VTL Kernel Metrics vectors and extraction outputs as structural coordinates, not quality scores. Use when the user provides delta_x, delta_y, r_v, rho_r, mu, x_p, theta, d_s, sdi, mass_fraction, gradient_floor_85, gradient_ceiling_97, tail_gap, EFA, mask_status, mask_mode, kernel CSV/JSON output, or asks what a single image or batch occupies in VTL kernel space, how to read placement, density, cohesion, peripheral pull, orientation stability, structural thickness, spatial dispersion, or mask QA caveats.
---

# VTL Kernel Interpreter

## Purpose

Use this skill to interpret VTL Kernel Metrics outputs from the current notebook or `vtl-kernel-extractor`.

This skill reads structural coordinates. It does not calculate metrics, audit formulas, diagnose model priors, or write full reports unless asked. It does not judge quality.

## Core Stance

VTL Kernel Metrics is a coordinate system:

```text
kernel values locate structure; they do not grade it.
```

The center is not the problem. A single centered image is not collapse. Collapse or prior behavior requires distributional evidence across comparable images.

## Required Inputs

Minimum useful single-image inputs:

- `delta_x`
- `delta_y`
- `r_v`
- `rho_r`
- `mu`
- `x_p`
- `theta`
- `d_s`
- `sdi`

Strongly recommended:

- `mass_fraction`
- `gradient_floor_85`
- `gradient_ceiling_97`
- `tail_gap` or `efa`
- `mask_status`
- `mask_mode`
- `quality_note`

For batch interpretation:

- comparable rows from the same extractor/script/constants,
- sample size,
- model/prompt/condition labels when making comparisons,
- QA fields for each row.

If metrics are missing, interpret only the available coordinates and name missing fields.

## Interpretation Workflow

1. Check extraction validity.
   - If `valid = 0`, treat the vector as invalid/low-confidence.
   - If `mask_status = FAIL`, do not make strong structural claims.
   - If `mask_status = WARN`, keep the read but foreground texture/sparse-mask caveats.
   - Use `mask_mode` to distinguish `REGION_FIELD`, `TEXTURE_FIELD`, and `INVALID`.

2. Read placement.
   - `delta_x`: horizontal mass centroid offset.
   - `delta_y`: vertical mass centroid offset.
   - Near-zero means centered coordinate, not success/failure.

3. Read field activity and density context.
   - `r_v`: gradient-quiet fraction, not simple semantic empty space.
   - Always read `r_v` with `gradient_floor_85`, `gradient_ceiling_97`, and `tail_gap` when available.
   - `rho_r`: density/packing of the canonical mass mask relative to convex hull.

4. Read structure organization.
   - `mu`: cohesion by component dominance and size entropy.
   - `x_p`: peripheral edge-field pull.
   - `theta`: orientation stability versus omnidirectional texture.
   - `d_s`: structural thickness.
   - `sdi`: spatial dispersion of mass around its centroid.

5. Compose a structural read.
   - Describe coordinate behavior plainly.
   - Separate field, placement, cohesion, orientation, thickness, and dispersion.
   - Avoid aesthetic or semantic claims.

6. For batches, read distributions.
   - Compare variance, spread, outliers, and missing coordinate regions.
   - Do not claim model prior/collapse solely from a small or non-comparable batch.
   - If prior diagnostics are requested, route to `vtl-kernel-distribution-prior-diagnostics` once available.

## Output Format

Use this format for a single image:

```text
Classification:
Interpretation Status: <valid | provisional | limited | blocked>
Input Type: <single image | batch | partial metrics>
VTL kernel read:
<one-sentence structural summary>

Data Integrity Check:
- required metrics present → <yes/partial/no>
- r_v package present → <yes/partial/no>
- QA fields present → <yes/no>

If weak:
→ Interpretation Status = provisional or limited

If mask_status = FAIL:
→ do not interpret coordinates
→ report only QA and failure

Single image:
→ descriptive only
→ no pattern language
→ no prior/collapse language

Coordinate behavior:
- placement: <delta_x / delta_y>
- field activity: <r_v + gradient package caveat>
- packing/cohesion: <rho_r / mu>
- edge/orientation/thickness: <x_p / theta / d_s>
- dispersion: <sdi>

QA:
<valid, mask_status, mask_mode, mass_fraction, quality_note>

Interpretation must:
- describe structure
- not infer behavior

Interpretation:
<plain-language structural read>

REGION_FIELD → placement + cohesion valid
TEXTURE_FIELD → field activity, not object structure
INVALID → no interpretation

Do not:
- collapse multiple metrics into a single narrative
- treat μ + θ + sdi as one concept

Do not:
- interpret demand (VCLI)
- interpret collapse (RCP)

Do not report r_v alone when gradient package is available

Do not:
- compress interpretation into vague statements
- e.g., “complex structure”

mass_fraction is mask context, not composition

Limits:
<single-image caveat, missing fields, mask sensitivity, r_v context, no quality/semantic claims>

Confidence:
<high | medium | low>

Drivers:
- QA status
- metric completeness
- mask mode
```

For batches, use:

```text
VTL batch read:
<one-sentence summary of distribution behavior>

Batch:
→ describe spread
→ do not infer priors
→ route to prior diagnostics if needed

Cohort:
<n, conditions, comparability, extractor/version note>

Distribution signals:
- placement spread: <delta_x / delta_y>
- field activity spread: <r_v package>
- cohesion/packing spread: <rho_r / mu>
- orientation/peripheral/thickness spread: <x_p / theta / d_s>
- dispersion spread: <sdi>

QA profile:
<mask_status/mask_mode distribution and caveats>

Limits:
<sample size, mixed preprocessing, non-comparable runs, no single-score collapse>
```

## References

Read [metric-guide.md](references/metric-guide.md) when interpreting field meanings, aliases, and safe structural language.

Read [qa-and-claim-boundaries.md](references/qa-and-claim-boundaries.md) when handling `mask_status`, `mask_mode`, invalid vectors, single-image caveats, or collapse/prior overclaims.

## Constraints

- Do not infer image quality, aesthetic value, correctness, taste, cultural value, semantic meaning, prompt obedience, intent, or viewer attention from kernel values.
- Do not call center-weighted composition collapse from a single image.
- Do not use a single metric as a pass/fail signal.
- Do not interpret `r_v` without noting gradient-field context when package fields are available.
- Do not hide `mask_status`, `mask_mode`, `valid`, or `quality_note`.
- Do not compare runs unless extraction constants and preprocessing are comparable.
- Do not use older PDF meanings when they conflict with current notebook/extractor fields.

## Attribution

VTL Kernel Metrics are part of the Visual Thinking Lens system authored by Russell Parrish / A.rtist I.nfluencer. Preserve attribution when packaging, distributing, or publishing derived materials.

This package contains a modular visual reasoning skill suite built from Russell Parrish / A.rtist I.nfluencer protocols. The skills are designed to run independently, but they also interoperate through routing, handoff notes, and shared visual reasoning concepts. More information: www.artistinfluencer.com. Copyright 2026.
