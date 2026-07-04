# Overclaim Patterns

## Metric To Quality

Problem: A structural metric is treated as proof that an image is better, more beautiful, more artistic, more successful, or preferred.

Safer frame: "The metric supports a structural reading of..." or "The image occupies a more pressure-stable / coherent / prior-distant position under this system."

## Single Image To Model Prior

Problem: One image is used to claim a model has a default, bias, collapse pattern, or safe-middle tendency.

Safer frame: "This image is a local candidate for..." or "A model-prior claim would require comparable cohort evidence."

## Cohort Without Comparability

Problem: Model, prompt, or batch comparisons are made without matching preprocessing, extractor versions, prompt families, image dimensions, mask QA, or run metadata.

Safer frame: "Within this comparable subset..." or "The comparison is provisional because..."

## QA As Footnote

Problem: Invalid masks, failed rows, duplicate drift, missing hashes, failed perturbations, or sequence-order uncertainty are mentioned but not allowed to affect the conclusion.

Safer frame: "This blocks the claim" or "This limits the claim to descriptive inspection."

## Telemetry Leakage

Problem: Color or tonal telemetry is used to alter CTG, RDC, SFS, BCI, LSI100, or acceptance.

Safer frame: "Telemetry explains a perceptual divergence; it does not change the structural gate."

## Channel Isolation

Problem: One primitive or channel is interpreted alone as if it proves the full structure.

Safer frame: "This primitive contributes to the composite read, but the claim depends on..."

## VTL And LSI Term Drift

Problem: VTL `r_v` and LSI `rv`, VTL `sdi` and LSI `sdi`, or RCA/RDC and LSI RDC are merged without definitions.

Safer frame: "In the LSI v2 sense..." or "In the VTL Kernel sense..." and then state the definition.

## Perturbation And Sequence Confusion

Problem: Perturbation `P` is treated as sequence stability `S`, or a single-image robustness test is described as iterative resilience.

Safer frame: "P measures single-image robustness under deterministic disturbance. S measures stability across deliberate ordered iterations."

## Collapse From Centering Alone

Problem: Centered composition is treated as radial collapse, RCP, or safe middle without supporting evidence.

Safer frame: "Center-weighted candidate" or "radial-default candidate" if gates/visual tests support it; otherwise "centered structure."

## Prompt Fidelity Overreach

Problem: Structural movement is treated as full semantic prompt obedience.

Safer frame: "The measured structure moved in the prompt-intended direction" or "structural fidelity is supported; semantic fidelity is outside this metric."

## Causal Language

Problem: The text says a metric caused a viewer response, model behavior, or artistic outcome without experimental evidence.

Safer frame: "is consistent with", "may support", "is associated with in this analysis", or "would require validation."
