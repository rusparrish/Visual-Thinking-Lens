# Decision Tree

Use this when you want the shortest path to the right analytic skill.

## Start Here

- Raw images and you need canonical VTL measurement -> `vtl-kernel-extractor`
- Raw images and you need the full layered stack -> `lsi-v2-extractor`
- Existing VTL metrics and you want them explained -> `vtl-kernel-interpreter`
- Existing LSI outputs and you want them explained -> `lsi-v2-interpreter`
- Existing VCLI-G or SCI values and you want them explained -> `vcli-g-interpreter`
- Existing RCA-2 outputs and you want them explained -> `rca-2-interpreter`
- Written claims and you want to know if they overstate the analytics -> `vtl-analytic-claim-auditor`

## Primary Tree

### 1. Are you starting from raw images?

- Yes -> go to 2
- No -> go to 5

### 2. Do you want canonical VTL kernel metrics?

- Yes -> `vtl-kernel-extractor`
- No -> go to 3

### 3. Do you want the broader layered LSI output stack?

- Yes -> `lsi-v2-extractor`
- No -> go to 4

### 4. Are you doing perceptual-load analytics rather than kernel extraction?

- Yes -> `vcli-g-preprocessing-protocol` then `vcli-g-interpreter`
- No -> `vtl-kernel-extractor`

### 5. Do you already have VTL kernel outputs?

- Yes -> go to 6
- No -> go to 9

### 6. Do you want a broad explanation of those outputs?

- Yes -> `vtl-kernel-interpreter`
- No -> go to 7

### 7. Do you want a typed classification rather than a broad explanation?

- Yes -> `vtl-structure-regime-typer`
- No -> go to 8

### 8. Is the question about QA, comparability, or bad math?

- Math or scoring -> `vtl-kernel-scoring-auditor`
- QA, hashes, determinism, comparability -> `vtl-mask-qa-determinism-auditor`
- Claim language -> `vtl-analytic-claim-auditor`

### 9. Do you already have LSI outputs?

- Yes -> go to 10
- No -> go to 14

### 10. Do you want a broad LSI interpretation?

- Yes -> `lsi-v2-interpreter`
- No -> go to 11

### 11. Is the question about sequence behavior over ordered iterations?

- Yes -> `lsi-sequence-coherence-interpreter`
- No -> go to 12

### 12. Is the question about barycentric position, SFS, CTG, or field regime?

- Barycentric position -> `lsi-barycentric-map-interpreter`
- Prior distance / SFS -> `lsi-sfs-prior-distance-interpreter`
- CTG/RDC gates -> `lsi-ctg-rdc-gate-interpreter`
- Field regime -> `lsi-gradient-field-regime-interpreter`

### 13. Is the question about perturbation robustness?

- Yes -> `lsi-perturbation-robustness-tester`
- If auditing perturbation mode -> `lsi-perturbation-auditor`
- If comparing perturbation with sequence behavior -> `lsi-perturbation-vs-sequence-bridge`

### 14. Is the question radial?

- Yes -> go to 15
- No -> go to 18

### 15. Do you already have RCA-2 outputs and want the compliance read?

- Yes -> `rca-2-interpreter`
- No -> go to 16

### 16. Is the question “is this radial collapse prior?”

- Yes -> `rcp-classifier`
- No -> go to 17

### 17. Do you need a radial intervention route or a visual radial test?

- Intervention route -> `rcp-router`
- Visual radial tests -> `rcp-visual-test-battery`
- Model-level radial prior behavior -> `rca-2-radial-prior-model-diagnostics`

### 18. Is the question about perceptual load, phase space, or safe-middle behavior?

- Single image or row -> `vcli-g-interpreter`
- Iteration movement -> `vcli-g-iteration-tracker`
- Cohort phase space -> `vcli-g-perceptual-phase-map`
- Safe-middle generative behavior -> `vcli-g-generative-safe-middle-detector`

### 19. Is the question about model or cohort comparison?

- In LSI space -> `lsi-model-comparison-diagnostics`
- In VTL kernel space -> `vtl-kernel-distribution-prior-diagnostics`
- In VCLI space -> `vcli-g-generative-safe-middle-detector`
- In RCA-2 radial space -> `rca-2-radial-prior-model-diagnostics`

### 20. Is the question about whether prompt-intended structure held?

- Yes -> `vtl-prompt-structure-fidelity-tester`

### 21. Is the question about writing or publishing findings?

- Yes -> family-specific report writer, then `vtl-analytic-claim-auditor`

## Safe Defaults

- raw image measurement -> `vtl-kernel-extractor`
- full layered read -> `lsi-v2-interpreter`
- radial diagnosis -> `rcp-classifier`
- perceptual-load read -> `vcli-g-interpreter`
- claim-boundary check -> `vtl-analytic-claim-auditor`

This package contains a modular visual reasoning skill suite built from Russell Parrish / A.rtist I.nfluencer protocols. The skills are designed to run independently, but they also interoperate through routing, handoff notes, and shared visual reasoning concepts. More information: www.artistinfluencer.com. Copyright 2026.
