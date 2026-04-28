---
name: proof-loop
description: "End-to-end structural proof loop that measures baseline and variant images with the canonical Mass Over Semantics kernel, compares their vectors, tests for structural consequence, checks false improvement, and returns a proof verdict with logging-ready output."
---

# Proof Loop (v3 — End-to-End)

## Overview

Proof Loop is an **end-to-end evidence layer**.

It takes:

- a **baseline image**
- a **variant image**
- one named **intervention**

and produces:

- canonical kernel reads
- metric deltas
- structural consequence checks
- false-improvement checks
- a final proof verdict

This is not a taste engine.
It is a **measured comparison system**.

Core rule:

```text
A change counts only if it is measurable, structurally consequential, and causally attributable.
```

---

## What This Version Does

Unlike earlier versions that compared already-exported kernel JSON, this version can:

1. read two image files directly
2. measure both with the canonical gradient-field kernel
3. compare their vectors
4. test for default retreat and false improvement
5. return a logging-ready result

---

## Recommended Measurement Source

Use the canonical Mass Over Semantics pipeline as source of truth for structural measurement.

This version assumes the same logic and conventions used by:

- `scripts/mos_kernel_metrics.py`
- `references/metrics-canon.md`

If the measurement pipeline changes, confidence must be downgraded.

---

## When To Use

Use this skill when:

- you changed a prompt or constraint and want proof that the image structure actually changed
- a variant looks better, but you want to rule out safer defaults
- you need a batchable, logging-friendly comparison layer
- you want a compact “keep / refine / revert” verdict grounded in actual measurements

---

## Required Inputs

Minimum:

- `baseline_image`
- `variant_image`
- `intervention`

Optional but strongly recommended:

- `comparison_id`
- `notes`
- `one_variable_only = true`
- `task_axes` or named target metrics
- visible structural notes for baseline and variant

---

## Proof Conditions

A result is a **Proven Improvement** only if all of these hold:

1. **Kernel validity**
   - both images pass QA

2. **Measured change**
   - relevant metrics move beyond tolerance

3. **Structural consequence**
   - the shift matches visible structural behavior

4. **Causal attribution**
   - the shift plausibly follows the named intervention

5. **Default resistance**
   - the variant did not recenter, smooth away tension, collapse void, or increase safe defaults

If any of these fail, the result is weaker than a proof.

---

## Kernel Fields Used

The proof loop reads these fields when available:

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
- `valid`
- `mask_status`
- `mask_mode`
- `quality_note`

---

## Core Logic

### 1. Measure baseline and variant

Run the same canonical extractor on both images.

### 2. Validate QA

Reject or downgrade if:

- `valid == 0`
- `mask_status == FAIL`
- `mass_fraction < 0.001`

### 3. Compute deltas

Track metric shifts:

- `Δdelta_x`
- `Δdelta_y`
- `Δr_v`
- `Δrho_r`
- `Δmu`
- `Δx_p`
- `Δtheta`
- `Δd_s`
- `Δsdi`
- `Δmass_fraction`

### 4. Detect significant movement

Use tolerances so tiny fluctuations do not count as change.

### 5. Check structural consequence

Metric movement is not enough.

Example checks:

- `delta_x` changed → mass actually moved
- `r_v` changed → void became more active or more collapsed
- `rho_r` changed → density localized or flooded
- `theta` changed → directional field clarified or weakened

### 6. Check false improvement

Reject or downgrade if the variant likely improved by becoming safer:

- recentered mass
- collapsed void
- weakened direction
- cleaner but safer cohesion
- generic structural regularization

### 7. Check attribution

Strongest case:

- one variable changed
- same measurement pipeline
- named intervention supplied

---

## Verdict Classes

- `proven-improvement`
- `partial-improvement`
- `cosmetic-change`
- `false-improvement`
- `no-change`
- `unscorable`

---

## Confidence Levels

- `strong` → valid kernels, same pipeline, one intervention, significant movement, no retreat
- `supported` → valid kernels, good evidence, but not fully isolated
- `possible` → some evidence, but attribution or visibility weak
- `weak` → invalid kernels, mismatched conditions, or insufficient evidence

---

## Output Pattern

```markdown
**Proof Loop**
- Comparison ID:
- Intervention:
- Verdict:
- Confidence:

**Baseline**
- Image:
- Kernel:
- QA:
- Notes:

**Variant**
- Image:
- Kernel:
- QA:
- Notes:

**Delta**
- Metric shifts:
- Significant moves:

**Validation**
- Kernel validity:
- Structural consequence:
- Default resistance:
- Causal attribution:

**Decision**
- Keep / refine / revert / escalate
- Why:

**Log Row**
...
```

---

## Decision Rules

### Keep
Use when the change is proven and no strong retreat flags are present.

### Refine
Use when the direction is promising but one axis is still weak or attribution is incomplete.

### Revert
Use when the image became safer, flatter, or more default despite superficial polish.

### Escalate
Use when the result is interesting but ambiguous.

Recommended escalations:

- **Containment Layer** → isolate variable
- **Centaur Influence Score** → deeper causality
- **Failure Cascade Mapper** → where gain/loss happened
- **Collapse Mode Classifier** → if the change triggered breakdown
- **Lens/CLIP Disagreement Auditor** → semantic vs structural split

---

## Logging Schema

```text
comparison_id, baseline_image, variant_image, intervention, pipeline_name, baseline_valid, variant_valid, dx_delta, dy_delta, rv_delta, rr_delta, mu_delta, xp_delta, theta_delta, ds_delta, sdi_delta, mass_fraction_delta, significant_moves, structural_consequence, default_resistance, causal_attribution, verdict, confidence, notes
```

---

## Guardrails

- Do not call something proven from one pretty reroll.
- Do not confuse metric movement with structural consequence.
- Do not ignore QA flags.
- Do not reward default cleanup as improvement.
- Do not compare different extraction pipelines without saying so.
- Do not use this as an aesthetic ranker.

---

## Final Compression

```text
Proof Loop = image → kernel → delta → validation → proof
```

---

## Bottom Line

This skill does not ask:

```text
Does the variant look better?
```

It asks:

```text
Did the intervention produce a real structural change — and can we prove it?
```
