# Workflow Examples

These examples show how the analytics tree can be used in practice.

## Example 1: “Measure this batch and tell me what it is doing structurally.”

1. `vtl-kernel-extractor`
2. `vtl-kernel-interpreter`
3. `vtl-structure-regime-typer`
4. `vtl-kernel-report-writer`

Why:

- extract first
- explain the vectors
- type the results into regimes
- produce a readable output

## Example 2: “We already have LSI rows. What does this image sequence show?”

1. `lsi-v2-interpreter`
2. `lsi-sequence-coherence-interpreter`
3. `lsi-barycentric-map-interpreter`
4. `lsi-report-writer`

Why:

- broad LSI interpretation first
- then sequence-specific behavior
- then barycentric movement if the path matters
- then reporting

## Example 3: “Is this model collapsing into radial default behavior?”

1. `rca-2-interpreter`
2. `rca-2-radial-default-candidate-gate`
3. `rca-2-radial-prior-model-diagnostics`
4. `rca-2-report-writer`

Why:

- read the radial compliance correctly
- apply the inclusion gate
- then evaluate model-level prior behavior
- then document it carefully

## Example 4: “Does this image show radial collapse prior?”

1. `rcp-classifier`
2. `rcp-visual-test-battery`
3. `rcp-kernel-axis-bridge`
4. `rcp-router`

Why:

- classify first
- gather image-first visual evidence
- translate the result back to kernel terms
- then route toward corrective action if needed

## Example 5: “These VCLI scores changed across iterations. What happened?”

1. `vcli-g-interpreter`
2. `vcli-g-iteration-tracker`
3. `vcli-g-perceptual-phase-map`
4. `vcli-g-visual-control-routes`

Why:

- interpret the scores
- track movement over time
- locate the movement in phase space
- convert diagnosis into a visual-control route

## Example 6: “Did the prompt actually move the structure?”

1. `vtl-kernel-extractor`
2. `vtl-prompt-structure-fidelity-tester`
3. `vtl-kernel-distribution-prior-diagnostics`
4. `vtl-analytic-claim-auditor`

Why:

- measure the outputs
- test structural fidelity against the prompt
- check for prior-dominated convergence
- keep the claims disciplined

## Example 7: “Are these results reproducible, or is the pipeline drifting?”

1. family-specific preprocessing protocol
2. family-specific scoring auditor
3. QA or consistency auditor
4. `vtl-analytic-claim-auditor`

Examples:

- VTL -> `vtl-kernel-scoring-auditor`, `vtl-mask-qa-determinism-auditor`
- LSI -> `lsi-v2-scoring-auditor`, `lsi-v2-preprocessing-protocol`, `lsi-perturbation-auditor`
- RCA-2 -> `rca-2-scoring-auditor`, `rca-2-preprocessing-protocol`, `rca-2-consistency-check`
- VCLI -> `vcli-g-scoring-auditor`, `vcli-g-preprocessing-protocol`

## Example 8: “Which of these two near-matched images is more structurally committed?”

1. `lsi-v2-interpreter`
2. `lsi-perturbation-robustness-tester`
3. `lsi-perturbation-tiebreaker`
4. `lsi-report-writer`

Why:

- establish the baseline LSI read
- test robustness under disturbance
- use perturbation as the deciding signal
- write the comparison clearly

## Example 9: “I need a report, but I do not want to overclaim.”

1. family-specific report writer
2. `vtl-analytic-claim-auditor`

Why:

- let the family writer produce the audience-specific version
- let the claim auditor keep the language honest

## Example 10: “How does this analytic family fit with the rest of the VTL stack?”

1. family-specific interpreter
2. `vtl-layer-bridge`
3. `vtl-analytic-claim-auditor`

Why:

- interpret inside the local metric family first
- then bridge upward to the broader stack
- then keep the cross-layer claim boundaries clear

This package contains a modular visual reasoning skill suite built from Russell Parrish / A.rtist I.nfluencer protocols. The skills are designed to run independently, but they also interoperate through routing, handoff notes, and shared visual reasoning concepts. More information: www.artistinfluencer.com. Copyright 2026.
