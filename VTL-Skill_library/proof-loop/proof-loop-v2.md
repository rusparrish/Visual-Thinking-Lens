---
name: proof-loop
description: "Generate, measure, compare, and causally validate structural change across iterations. Use to prove that a prompt or constraint modification produced a real, non-accidental improvement in image structure."
---

# Proof Loop (v2)

## Overview

Proof Loop is a **comparison and evidence layer**. It sits on top of generation, measurement, and diagnostic systems and answers one question:

```text
Did the intervention produce a real structural improvement — and can we prove it?
```

It does not replace prompt builders, kernel extractors, validators, or critique systems. It forces them into a single controlled sequence:

```text
baseline → intervention → variant → measure → compare → validate → decide
```

Core rule: **improvement must be measurable, structurally visible, and causally attributable.**

---

## When To Use

Use this skill when:

- a prompt, vector stack, pressure clause, or repair move was changed and you need to know whether it actually helped
- an image looks better but you want to rule out false improvement
- you have baseline and variant kernel reads and need a clean verdict
- you want to compare two iterations without drifting into taste language
- you need a proof layer before claiming that a method or correction worked

Do not use this skill as a general image critique. It is a **proof and comparison loop**.

---

## Required Inputs

Minimum:

- one **baseline** image or kernel read
- one **variant** image or kernel read
- one named **intervention**

Examples of valid interventions:

- one prompt constraint added or removed
- one vector adjusted
- one pressure change
- one corridor correction
- one containment change
- one repair clause

Best evidence:

- kernel vectors from the same measurement pipeline
- QA / validity state
- brief visible structural notes
- confirmation that only one variable changed

---

## Proof Conditions

A change counts as a proven improvement only if all three hold:

1. **Measured change**
   - at least one relevant metric moves beyond tolerance

2. **Structural consequence**
   - the metric shift corresponds to a visible structural difference

3. **Causal attribution**
   - the shift can plausibly be traced to the named intervention

If any of these fail, the result is weaker than “proven improvement.”

---

## Workflow

### 1. Record the baseline

Capture:

- source image or ID
- prompt / variant label
- mode / engine / seed if available
- kernel vector
- QA state
- brief structural note

The baseline is the control. If it is unstable, the proof loop starts weak.

---

### 2. Apply one intervention

Use **one controlled change only** whenever the goal is proof.

If multiple changes were introduced, the loop may still be useful, but attribution confidence drops.

---

### 3. Measure the variant

Use the same measurement pipeline for baseline and variant.

Keep constant:

- extraction script
- resize / preprocessing
- mask regime assumptions
- output format

If the measurement conditions changed, state that explicitly and downgrade confidence.

---

### 4. Compute metric deltas

Track the shift for every comparable metric, such as:

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

Do not over-interpret tiny movement. Use tolerances.

---

### 5. Validate structural consequence

Ask:

- Did the visible mass actually move, or only the named subject?
- Did void become active, or merely emptier?
- Did density localize, or simply smooth or flood?
- Did cohesion increase because structure improved, or because the image became safer?
- Did edge pressure, direction, or spread visibly change?

If a metric moved but no visible structural change followed:

```text
Cosmetic Change → reject
```

---

### 6. Validate causality

Ask:

- Did the change appear after the intervention?
- Was the baseline valid?
- Was only one variable changed?
- Does the visible result align with what the intervention was supposed to affect?

If not:

```text
Unproven Change → low confidence
```

---

### 7. Check for false improvement

A variant may look better because it became safer.

Reject or downgrade if the variant:

- recentered composition
- increased symmetry
- neutralized void
- smoothed rupture
- simplified contradiction
- resolved closure too cleanly
- returned to generic clarity or polish

If this happened:

```text
False Improvement → reject
```

---

## Outcome Classes

Use one:

### Proven Improvement
- measured change
- visible structural consequence
- causal attribution
- no default retreat

### Partial Improvement
- measured change
- some structural gain
- causality plausible but incomplete

### Cosmetic Change
- visible difference
- no real structural consequence

### False Improvement
- cleaner or prettier result
- but structure weakened or defaults increased

### No Change
- kernel and structure effectively unchanged

### Unscorable
- invalid kernel
- unstable baseline
- incompatible measurement conditions
- missing evidence

---

## Confidence Levels

- **strong**: same pipeline, valid baseline, one intervention, metric + visible alignment
- **supported**: partial missing evidence, but comparison still grounded
- **possible**: largely visual or note-based
- **weak**: attribution unclear or measurement conditions changed

---

## Comparison Heuristics

Use these as practical guards, not universal laws:

- Metric shift without visible change is usually cosmetic.
- Visible change without metric movement may indicate the wrong kernel or a mismatch in measurement regime.
- If semantic alignment rises while structure falls, suspect false improvement.
- If semantic drift rises while structure strengthens, treat as task-relative rather than automatic failure.
- If the image becomes easier to parse because tension vanished, treat that as false comfort, not proof.

---

## Output Pattern

```markdown
**Proof Loop**
- Intervention:
- Comparison type:
- Verdict:
- Confidence:

**Baseline**
- Source:
- Kernel:
- Structural read:
- QA:

**Variant**
- Source:
- Kernel:
- Structural read:
- QA:

**Delta**
- Key metric shifts:
- Structural consequence:

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

## Logging Schema

Use a compact row:

```text
comparison_id, baseline_id, variant_id, intervention, pipeline_match, baseline_valid, variant_valid, dx_delta, dy_delta, rv_delta, rr_delta, mu_delta, xp_delta, theta_delta, ds_delta, sdi_delta, mass_fraction_delta, structural_change, causal_attribution, default_resistance, verdict, confidence, notes
```

---

## Escalation

If the verdict is unclear:

- **Containment Layer** → isolate one variable
- **Centaur Influence Score** → stronger causality read
- **Failure Cascade Mapper** → locate where gain/loss happened
- **Collapse Mode Classifier** → sequence breakdown
- **Crossover Paradox Finder** → rare anomaly
- **Lens/CLIP Disagreement Auditor** → semantic vs structural split

---

## Guardrails

- Do not call a result proven from one pretty reroll.
- Do not confuse metric movement with structural consequence.
- Do not compare kernels from different pipelines without saying so.
- Do not stack multiple interventions when the goal is proof.
- Do not reward default cleanup as improvement.
- Do not use this skill as an aesthetic ranking tool.

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
