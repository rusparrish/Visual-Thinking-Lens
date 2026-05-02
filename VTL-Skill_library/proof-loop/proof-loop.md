---
name: proof-loop
description: "Generate, measure, compare, and causally validate structural change across iterations. Use to prove that a prompt or constraint modification produced a real, non-accidental improvement in image structure."
---

# Proof Loop

## Overview

Proof Loop is a **meta-skill** that sits on top of generation, measurement, and diagnostic tools. It does not replace prompt builders, kernel extractors, or validators. It forces them into a single evidentiary chain:

```text
baseline → variant → measure → compare → validate → decide
```

The goal is not to ask whether an image *looks better*. The goal is to determine whether a change produced a **measurable, structurally visible, causally attributable improvement**.

Core rule: **improvement must be measurable, structurally visible, and causally attributable.**

---

## When To Use

Use this skill when:

- a prompt or constraint was changed and you need to know whether the change really helped
- a generated image looks stronger but you want to rule out false improvement
- you have baseline and variant kernel readings and need a clean verdict
- you want to compare two or more iterations without drifting into taste language
- you need to prove that a change was not accidental, cosmetic, or caused by default behavior

Do not use this skill as a general image critique. It is a **comparison and proof layer**.

---

## Required Inputs

Minimum:

- one **baseline** image or kernel read
- one **variant** image or kernel read
- one named **intervention**
  - prompt change
  - vector adjustment
  - pressure change
  - containment change
  - repair clause

Best evidence:

- kernel vectors from the same measurement pipeline
- QA / validity status
- notes about visible structural change
- confirmation that only one variable was changed

---

## Core Questions

For every comparison, answer these in order:

1. **What changed?**
2. **Did the metrics move?**
3. **Did the structure visibly change?**
4. **Can that change be attributed to the intervention?**
5. **Did the result resist default fallback or merely become cleaner?**

If any of steps 3-5 fail, the change is not yet proven.

---

## Loop Structure

### 1. Baseline

Generate or select the baseline image.

Record:

- image ID or file
- prompt
- mode / engine / seed if available
- kernel vector
- QA state
- brief structural note

The baseline is the control. If the baseline is unstable, the loop is weak before it starts.

---

### 2. Variant

Apply **one controlled change only**.

Valid changes include:

- one prompt constraint
- one vector added or removed
- one pressure adjustment
- one corridor correction
- one containment change

Do not stack multiple changes unless the goal is exploratory rather than evidentiary.

---

### 3. Measure

Run the same measurement pipeline on baseline and variant.

Use the same:

- kernel extractor
- resize / preprocessing
- mask regime assumptions
- output format

If measurement conditions changed, downgrade confidence.

---

### 4. Compare

Compute deltas on key metrics, for example:

- `Δdelta_x`
- `Δdelta_y`
- `Δr_v`
- `Δrho_r`
- `Δmu`
- `Δx_p`
- `Δtheta`
- `Δd_s`
- `Δsdi`

Use only comparable metrics from the same pipeline.

---

### 5. Structural Validation

Metric change is not enough.

Ask whether the metric shift produced a visible structural effect.

Examples:

- `delta_x` changed → mass actually moved, not just the named subject
- `r_v` changed → void became active or collapsed, not merely emptier
- `rho_r` changed → density localized or flooded, not just texture noise
- `mu` changed → cohesion genuinely increased or fragmented
- `theta` changed → directional field became clearer or dissolved

If metric shift has no visible consequence:

```text
Cosmetic Change → reject
```

---

### 6. Causal Attribution

A change counts only if it can be traced to the intervention.

Check:

- Did the change occur after the intervention?
- Was only one variable changed?
- Was the baseline stable enough to compare?
- Does the change align with what the intervention was supposed to affect?

If not:

```text
Unproven Change → low confidence
```

---

### 7. Default Resistance Check

A variant may look improved because it became safer.

Check whether the result:

- recentered composition
- resolved contradiction too cleanly
- smoothed rupture
- neutralized void
- increased symmetry
- returned to generic clarity or cinematic polish

If yes:

```text
False Improvement → reject
```

This is especially important when CLIP-style alignment rises while structural strain falls.

---

## Outcome Classes

Use one:

### Proven Improvement
- metrics move
- structure visibly improves or sharpens
- change is causally attributable
- no default retreat

### Partial Improvement
- metrics move
- some visible gain exists
- causality is plausible but incomplete

### Cosmetic Change
- visible difference exists
- structure does not materially change

### False Improvement
- image looks better
- but structure weakens, defaults increase, or tension disappears

### No Change
- kernel and structure remain effectively the same

### Unscorable
- invalid kernel
- unstable baseline
- missing evidence
- incompatible measurement conditions

---

## Confidence Levels

- **strong**: same pipeline, stable baseline, one intervention, metric + visible alignment
- **supported**: some evidence missing, but comparison still grounded
- **possible**: mostly interpretive or visually inferred
- **weak**: attribution unclear or measurement conditions changed

---

## Comparison Heuristics

These are not hard rules, but useful checks:

- A metric shift with no visible structural effect is usually cosmetic.
- A visible structural change with no measurable shift may reflect measurement mismatch or the wrong kernel for the task.
- If CLIP rises but Lens / kernel structure falls, suspect false improvement.
- If semantic drift increases but structure strengthens, classify carefully; improvement may be real but task-relative.
- If the variant becomes easier to parse because tension vanished, reject it as false comfort.

---

## Output Pattern

```markdown
**Proof Loop**
- Intervention:
- Comparison type:
- Verdict:
- Confidence:

**Baseline**
- Prompt / source:
- Kernel:
- Structural read:

**Variant**
- Prompt / source:
- Kernel:
- Structural read:

**Delta**
- Key metric shifts:
- Visible structural consequence:

**Validation**
- Kernel validity:
- Structural validation:
- Causal attribution:
- Default resistance:

**Decision**
- Keep / refine / revert / escalate
- Why:
```

---

## Decision Rules

### Keep
Use when improvement is proven and stable.

### Refine
Use when change is promising but underpowered or only partially attributable.

### Revert
Use when the variant improved appearance but damaged structure.

### Escalate
Use when the result is interesting but unclear.

Escalation options:

- **Containment Layer** → isolate one variable
- **Centaur Influence Score** → deeper causality test
- **Failure Cascade Mapper** → identify where the gain or loss occurred
- **Collapse Mode Classifier** → sequence breakdown
- **Crossover Paradox Finder** → rare hybrid anomaly
- **Lens/CLIP Disagreement Auditor** → semantic vs structural split

---

## Minimal Logging Schema

```text
comparison_id, baseline_id, variant_id, intervention, pipeline_match, baseline_valid, variant_valid, dx_delta, dy_delta, rv_delta, rr_delta, mu_delta, xp_delta, theta_delta, ds_delta, sdi_delta, structural_change, causal_attribution, default_resistance, verdict, confidence, notes
```

---

## Guardrails

- Do not call a change proven from one pretty reroll.
- Do not confuse metric movement with structural consequence.
- Do not compare kernels from different preprocessing pipelines without saying so.
- Do not stack multiple interventions if the goal is proof.
- Do not reward default cleanup as improvement.
- Do not use this skill to make aesthetic rankings.

---

## Final Compression

```text
Proof Loop = measured change + visible structural consequence + causal proof
```

---

## Bottom Line

This skill does not ask:

```text
Does this look better?
```

It asks:

```text
Did the intervention change the structure — and can we prove it?
```

This package contains a modular visual reasoning skill suite built from Russell Parrish / A.rtist I.nfluencer protocols. The skills are designed to run independently, but they also interoperate through routing, handoff notes, and shared visual reasoning concepts. Copyright 2026.
