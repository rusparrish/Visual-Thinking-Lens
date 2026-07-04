# Revision Language

## Downgrade Verdicts

Instead of:

- "This image is better."
- "The model understands composition."
- "This proves collapse."
- "The prompt was obeyed."

Use:

- "This image shows stronger structural coherence under the measured frame."
- "The batch shows a repeated structural tendency under comparable prompts."
- "This is consistent with a collapse candidate and needs replicated evidence."
- "The measured structure moved in the prompt-intended direction."

## Scope Markers

Use scope markers whenever evidence is local or conditional:

- "In this image..."
- "For this sequence..."
- "Within this comparable cohort..."
- "Under this extractor version..."
- "Given the available QA fields..."
- "With perturbation rows valid across all nine variants..."
- "As a local candidate rather than a model-level prior..."

## Evidence Markers

Tie claims to evidence:

- "supported by high VCLI-G with high SCI"
- "supported by low SDI with centered centroid and low border confound"
- "supported by CTG in-band behavior and retained K-P"
- "supported by SFS distance from the null pose"
- "supported by repeated RDC pass rates across the cohort"
- "supported by low perturbation variance localized outside the key primitive"
- "supported by stable sequence S with contracting barycentric path"

## Boundary Markers

Use boundary markers when the metric does not cover the broader claim:

- "This is not an aesthetic ranking."
- "This does not establish human preference."
- "This does not prove semantic correctness."
- "This does not establish model intent."
- "This remains local until replicated across comparable rows."
- "Telemetry explains divergence but does not change the gate."

## Clean Claim Templates

Single image:

```text
This image occupies a <structural position> under <metric/system>, supported by <evidence>. The claim is local to this image and does not by itself establish quality or model-level behavior.
```

Sequence:

```text
Across the ordered sequence, the structure <stabilizes/drifts/oscillates/contracts> according to <scores/path evidence>. This supports a sequence-level claim, not a single-frame quality verdict.
```

Cohort/model:

```text
Within the comparable cohort, <model/prompt group> shows a repeated tendency toward <structural behavior>, supported by <aggregate evidence>. The claim is distributional only within this sampled frame.
```

Perturbation:

```text
The baseline reading appears <robust/marginal/fragile> under deterministic perturbation: P=<value>, K-P=<value>, with sensitivity concentrated in <primitive>. This measures single-image pressure stability, not sequence resilience.
```

RCP/RDC:

```text
The image is a <radial/default/RCP> candidate because <gate or visual evidence>. Centering alone is insufficient; the claim depends on <supporting evidence and exclusions>.
```

Prompt fidelity:

```text
The measured structure moved in the prompt-intended direction on <axis/metric>, which supports structural prompt fidelity. Semantic obedience remains outside this metric unless separately evaluated.
```
