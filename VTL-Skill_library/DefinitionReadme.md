# Playground Analytic Definition Readme

## “Failure ≠ collapse” → The Visual Thinking Lens Exposes Defaults, Choice, Coordinates and the Delta as Composition.

Any given skill helps with structural compositional intent on images.
It may produce scores, but it really locates them, or helps understand them and where they can go.

Any given score implies a standard. This system has no standard — only a coordinate space.
Every image gets placed. What you do with the placement is interpretation, not judgment.

The Visual Thinking Lens does not measure:
❌ Aesthetic value
❌ Compositional 'correctness'
❌ Image quality or fidelity
The Lens does help with:
✅ Where visual mass concentrates in the frame
✅ Whether that organization is a structural default or a deliberate choice
✅ How compositional coordinates evolve under iterative pressure
✅ Decoupling between semantic intent and structural realization

This is a helper document, a standalone translation sheet for the Playground skill set and can be used for any given skill. This file is not attached to any skill and no skill depends on it. It is a global glossary for humans and agents who need to understand the shared vocabulary across the skills in this folder.

Standalone translation sheet and operating map for the `Playground_Analytic` skill set.

This file is not a skill and no skill depends on it. It is a human/agent index for the analytic vocabulary, claim boundaries, and workflow relationships across the skills in this folder.

**Core stance**: these terms are operational aids. They name visual structure, prompt behavior, telemetry, and failure modes. They are not aesthetic commandments, universal art laws, or proof that a model has intent. These skills name measurable or inspectable visual structure, pipeline behavior, distributional tendencies, and control routes. They do not by themselves prove aesthetic quality, semantic correctness, model intent, human preference, or artistic value.

## How To Use This Sheet

- Use this file when a skill name, metric, regime, gate, or diagnostic term needs broader context.
- Use the skill `SKILL.md` files as the procedural source of truth; this README is a map and glossary.
- Keep four layers separate: prompt language, visible output behavior, measured telemetry, and interpretive claim.
- Prefer the weakest defensible claim: `reports`, `supports`, `is consistent with`, `candidate`, `provisional`, or `requires replication`.
- Treat single-image findings as local readings, not distributional priors.
- Treat QA, preprocessing, and comparability as part of the evidence, not administrative side notes.

User / Context
↓
[ GOVERNOR ]
  - choose skill
  - declare mode
  - enforce boundaries
↓
[ SINGLE or MULTIPLE SKILL RUN ]
↓
[ GOVERNOR ]
  - interpret safely
  - prevent leakage

## Operational Rules of the Road
**1) Direction Over Description**
This system prioritizes directional effect over descriptive completeness.

A valid read should push a decision, constraint, or next move. Pure description without directional consequence is considered incomplete.

Implication: If two interpretations are possible, prefer the one that:
changes the output or increases structural pressure

**2) Constrained Ambiguity (Not Free Interpretation)**
Multiple readings are allowed only when they arise from shared structural evidence.
Ambiguity is valid when:
- structure is consistent
- metrics or visible behaviors support multiple outcomes
Ambiguity is weak when: any reading can be justified without constraint

Implication:
Not all interpretations are equal—some are structurally grounded, others are post-hoc.

**3) Metric Interaction Requirement**
No single metric should determine interpretation in isolation.
Metrics must be read in combination:
- r_v with delta_x
- rho_r with cadence_cv
- lane with anchor, etc.

Implication:
Statements like:
- “high r_v means X”
- should be treated as:
- incomplete unless contextualized

**4) Bias Declaration**
This system may operate under a declared directional bias (e.g., anti-center, void-led, rupture-led).

When a bias is active:
- interpretations that reinforce it are privileged
- interpretations that neutralize it are deprioritized, not invalid

Implication: The system is not neutral—it can be goal-aligned.

**5) Anti-Default Priority**
When evaluating or generating, prefer movement away from known default attractors.
Common defaults:
- center-fill composition
- symmetry safety
- global packing
- closure/polish

Implication: A structurally imperfect but anti-default result may be preferred over a clean default output.

**6) Productive vs Neutral vs Degenerate States**
Not all valid structures are equally useful.
Define three modes:
Productive
- increases tension, drift, or structural engagement
- supports directional goals
Neutral
- structurally valid but does not move the system
Degenerate
- collapses into explanation without effect
- or allows all interpretations equally

Implication: The system should favor productive states, not just valid ones.

**7) Explanation Must Map to Action**
Every interpretation should map to at least one of:
- a prompt change
- a structural adjustment
- a constraint

If it cannot: it remains interpretive, not operational

**8) Drift Is Allowed, But Must Be Held**
Drift, variation, and divergence are encouraged only when stabilized by anchors or structure.
- Unbounded drift → noise
- Anchored drift → tension

Implication: “Ride the drift” is valid only if something prevents collapse.

**9) Avoid Interpretive Inflation**
Do not expand meaning beyond visible or measurable support.
Use caution with:
- symbolic claims
- emotional readings
- narrative inference

Unless: they are tied to structure, mass, or constraint

**10) System Role Declaration**
This system is a biasing and reasoning scaffold, not:
- a quality judge
- a truth detector
- or a measure of artistic intent

Implication:
- It shapes behavior—it does not certify meaning.

## Final Thoughts:
- Some readings should be treated as weak or non-operative under active bias
- Degenerate states should trigger forced intervention(e.g., introduce rupture, shift mass, break symmetry)
- Drift without resistance is collapse, drift with resistance is tension
- The system is actually used to make decisions, not just describe outputs after the fact
- When a structure is classified as neutral or degenerate under active bias, the system should recommend at least one structural disruption:
        - break symmetry
        - shift mass
        - introduce void
        - increase directional conflict

## Global Claim Rules

| Rule | Meaning |
|---|---|
| Metric is not verdict | A number describes a measured structural coordinate or proxy. It is not a quality judgment. |
| QA gates interpretation | `FAIL`, `INVALID`, missing hashes, duplicate drift, or non-comparable preprocessing can block substantive claims. |
| Single image is local | One image can show a candidate pattern. It cannot establish a model prior or cohort collapse. |
| Mode is not status | `mask_status` says whether the VTL mask is usable. `mask_mode` says what kind of interpretation it supports. |
| Texture is not failure | `TEXTURE_FIELD` can be a valid distributed-field result. It blocks object/region overclaims. |
| Collapse needs recurrence | Collapse/prior language needs repeated comparable evidence along a named axis. |
| Prompt fidelity is structural | VTL can test measurable structural response to a prompt, not full semantic obedience. |
| Radial default is gated | RCA/RDC/RCP claims require eligibility, visual evidence, and exclusion of confounds. |

## Skill Families

The folder currently contains 51 skills in six functional families:

- VCLI-G / SCI: perceptual load, structural coherence, phase space, iteration, preprocessing, reporting, validation, control.
- RCA-2 / RDC: dual-center radial compliance math, radial default candidate gating, preprocessing, auditing, visual diagnostics, reporting.
- RCP: radial collapse prior classification, routing, visual testing, kernel/axis bridging, human-control comparison.
- VTL Kernel Metrics: canonical extractor, metric interpretation, r_v field reading, scoring audit, QA/determinism, regime typing, mode contrast, SDI collapse, distribution priors, prompt fidelity, reporting.
- LSI v2: notebook-current structural extraction, CTG/RDC gates, SFS prior distance, barycentric maps, sequence coherence, telemetry audit, perturbation robustness, model comparison, reporting.
- Cross-system positioning: metric positioning, VTL layer bridging, safe-middle generative behavior.

## Skill Inventory

| Skill | Primary role | Use when |
|---|---|---|
| [`vcli-g-interpreter`](vcli-g-interpreter/SKILL.md) | Interpret VCLI-G/SCI readings using current absolute-cap math. | Image has VCLI-G, SCI, G1-G4, perceptual load, earned tension, resolved clarity, collapse/noise, default simplicity. |
| [`vcli-g-scoring-auditor`](vcli-g-scoring-auditor/SKILL.md) | Audit VCLI-G scoring math and comparability. | Check old z-score/profile contamination, wrong caps, wrong weights, SCI leakage, preprocessing drift. |
| [`vcli-g-iteration-tracker`](vcli-g-iteration-tracker/SKILL.md) | Read movement across drafts, generations, or versions. | Compare sequential VCLI-G/SCI rows, deltas, stability windows, phase transitions. |
| [`visual-control-routes`](visual-control-routes/SKILL.md) | Convert diagnosis into edit/prompt/composition moves. | Need concrete moves toward earned tension, clarity, controlled ambiguity, less overload, less default simplicity. |
| [`vcli-g-perceptual-phase-map`](vcli-g-perceptual-phase-map/SKILL.md) | Analyze cohorts in VCLI-G x SCI phase space. | Batch comparison, quadrant counts, outliers, earned tension vs resolved clarity vs collapse/default regions. |
| [`vcli-g-preprocessing-protocol`](vcli-g-preprocessing-protocol/SKILL.md) | Standardize VCLI-G image preparation and reproducibility. | Resize, grayscale, edge detection, Canny/Otsu, masks, morphology, contour extraction, batch metadata. |
| [`vcli-g-experiment-designer`](vcli-g-experiment-designer/SKILL.md) | Design VCLI-G/SCI validation and research studies. | Human-loop studies, model comparisons, attention/dwell tests, art-historical tests, ablations. |
| [`vcli-g-image-metric-positioning`](vcli-g-image-metric-positioning/SKILL.md) | Position VCLI-G/SCI against CLIP/FID/aesthetic/reward metrics. | Need methods/deck/grant/product language about what VCLI-G adds and does not measure. |
| [`vcli-g-report-writer`](vcli-g-report-writer/SKILL.md) | Write audience-specific VCLI-G reports. | Turn VCLI-G/SCI findings into artist, research, engineering, product, curator, or public text. |
| [`vtl-layer-bridge`](vtl-layer-bridge/SKILL.md) | Connect VCLI-G to the broader VTL stack. | Explain VCLI-G vs LSI, SCI, TEL, OCF, Ghost Density, Axis 30, control routes, full VTL layers. |
| [`vcli-g-generative-safe-middle-detector`](vcli-g-generative-safe-middle-detector/SKILL.md) | Detect safe-middle convergence in generated-image cohorts. | Compare AI outputs for perceptual range narrowing, centered clarity, texture overload, low-risk priors. |
| [`rca-2-consistency-check`](rca-2-consistency-check/SKILL.md) | Cross-validate RCA-2, RDC, visual diagnostics, preprocessing protocol, scoring audit, and report outputs for internal consistency | Use when multiple RCA-2/RDC artifacts are present and you need to detect contradictions, drift, or invalid claim chains across the system. |
| [`rca-2-interpreter`](rca-2-interpreter/SKILL.md) | Interpret Dual-Center Radial Compliance Analyzer outputs. | Read frame/mass radial compliance, delta radial compliance, JSD, alpha, radial eligibility, dual centers. |
| [`rca-2-radial-default-candidate-gate`](rca-2-radial-default-candidate-gate/SKILL.md) | Apply the RDC inclusion/exclusion gate. | Decide whether a row belongs in default radial prior measurement or should be excluded. |
| [`rca-2-preprocessing-protocol`](rca-2-preprocessing-protocol/SKILL.md) | Standardize RCA-2/RDC mass maps and masks. | Foreground masks, luminance weighting, centroid computation, radial bins, eligibility metadata. |
| [`rca-2-scoring-auditor`](rca-2-scoring-auditor/SKILL.md) | Audit RCA-2/RDC scoring math and pipeline validity. | Check center definitions, reversed DRC, missing gates, JSD/compliance mistakes, aggregation errors. |
| [`rca-2-radial-prior-model-diagnostics`](rca-2-radial-prior-model-diagnostics/SKILL.md) | Diagnose model-level radial default-prior behavior. | Compare neutral-prompt cohorts, model versions, RDC aggregates, radial stabilization, safe-middle convergence. |
| [`rca-2-radial-compliance-visual-diagnostics`](rca-2-radial-compliance-visual-diagnostics/SKILL.md) | Read RCA-2 visual panels and overlays. | Inspect masks, centers, rings, mass profiles, curve fits, angular variance, visual/metric mismatch. |
| [`rca-2-rdc-radia-default-candidate-gate`](rca-2-rdc-radia-default-candidate-gate/SKILL.md) | Apply or audit the Radial Default Candidate (RDC) gate using RCA-2 outputs | Apply or interpret the RDC gate. |
| [`rca-2-report-writer`](rca-2-report-writer/SKILL.md) | Write audience-specific RCA-2/RDC reports. | Turn radial compliance, RDC, diagnostics, audits, or model findings into polished reports. |
| [`rcp-classifier`](rcp-classifier/SKILL.md) | Classify Radial Collapse Prior evidence. | Identify center-lock, radial void, density bowl, ring conformity, hard/soft/borderline RCP. |
| [`rcp-router`](rcp-router/SKILL.md) | Route RCP diagnosis into corrective interventions. | Need prompt/edit/composition moves to break radial collapse or reintroduce asymmetry/counter-geometry. |
| [`rcp-visual-test-battery`](rcp-visual-test-battery/SKILL.md) | Run image-first RCP visual tests without kernel math. | Apply radial overlay, iso-density, rotation-difference, local-vs-global, interruption, ring tests. |
| [`rcp-kernel-axis-bridge`](rcp-kernel-axis-bridge/SKILL.md) | Translate RCP evidence into VTL/LSI primitives and axes. | Explain how radial collapse maps to `delta_x`, `r_v`, `rho_r`, `mu`, vector direction, Axis behavior. |
| [`rcp-human-control-comparator`](rcp-human-control-comparator/SKILL.md) | Compare AI RCP evidence against human controls. | Contrast mono-force radial collapse with poly-force composition, competing vectors, intentional void carving. |
| [`vtl-kernel-extractor`](vtl-kernel-extractor/SKILL.md) | Run images through canonical VTL Kernel Metrics extraction. | Need deterministic vectors, r_v package, mask QA, hashes, CSV/JSON outputs using latest notebook math. |
| [`vtl-kernel-interpreter`](vtl-kernel-interpreter/SKILL.md) | Interpret VTL kernel vectors as structural coordinates. | Read placement, density, cohesion, peripheral pull, orientation stability, thickness, dispersion, QA caveats. |
| [`vtl-rv-gradient-field-interpreter`](vtl-rv-gradient-field-interpreter/SKILL.md) | Interpret the r_v gradient-field package. | Read gradient-quiet, active, isolated-edge, flat-rendering, texture-heavy, smooth/absent fields. |
| [`vtl-kernel-scoring-auditor`](vtl-kernel-scoring-auditor/SKILL.md) | Audit VTL Kernel Metrics math against latest notebook. | Check constants, mask construction, `delta_y`, `sdi`, `r_v`, `x_p`, `theta`, `mu`, r_v package fields. |
| [`vtl-mask-qa-determinism-auditor`](vtl-mask-qa-determinism-auditor/SKILL.md) | Audit VTL run integrity, mask QA, hashes, and determinism. | Check `mask_status`, `mask_mode`, hashes, duplicate drift, QA errors, comparability, reproducibility. |
| [`vtl-structure-regime-typer`](vtl-structure-regime-typer/SKILL.md) | Type VTL outputs into structural/compositional regimes. | Classify quiet/open, active/dense, isolated-edge, flat, compact-center, border-framed, fragmented, region fields. |
| [`vtl-mask-mode-contrast`](vtl-mask-mode-contrast/SKILL.md) | Compare VTL mask modes across runs or cohorts. | Analyze `REGION_FIELD` vs `TEXTURE_FIELD` vs `INVALID`, mode shifts, object/region claim boundaries. |
| [`vtl-sdi-center-collapse-detector`](vtl-sdi-center-collapse-detector/SKILL.md) | Detect SDI-based center weighting and collapse candidates. | Analyze low-SDI behavior, central compaction, centroid-centered structure, radial/default candidates. |
| [`vtl-kernel-distribution-prior-diagnostics`](vtl-kernel-distribution-prior-diagnostics/SKILL.md) | Diagnose distributional priors and collapse signatures. | Compare cohorts for repeated low-variance defaults, prompt-insensitive structure, mode-rate shifts. |
| [`vtl-prompt-structure-fidelity-tester`](vtl-prompt-structure-fidelity-tester/SKILL.md) | Test structural prompt fidelity. | Compare prompt-intended structure against observed VTL movement across prompts, versions, seeds, models. |
| [`vtl-kernel-report-writer`](vtl-kernel-report-writer/SKILL.md) | Write audience-specific VTL Kernel reports. | Turn metrics, QA, regimes, prompt tests, and distribution diagnostics into technical/research/product/executive reports. |
| [`lsi-v2-extractor`](lsi-v2-extractor/SKILL.md) | Run images or ordered sequences through canonical LSI v2 notebook math. | Need deterministic Layer 0-6 outputs: kernel primitives, field regimes, RCA-2, CTG/RDC, SFS, barycentric maps, telemetry, BCI, LSI100, CSV/JSON. |
| [`lsi-v2-interpreter`](lsi-v2-interpreter/SKILL.md) | Interpret completed LSI v2 records as structural coordinates. | Need a full single-image or sequence read across kernel primitives, gates, SFS, barycentric position, telemetry, and sequence scores. |
| [`lsi-v2-scoring-auditor`](lsi-v2-scoring-auditor/SKILL.md) | Audit LSI v2 scoring math against the current Colab. | Check stale PDF formulas, VTL contamination, wrong primitives, broken gates, SFS caps, bad sequence math, telemetry leakage, hashes, comparability. |
| [`lsi-v2-preprocessing-protocol`](lsi-v2-preprocessing-protocol/SKILL.md) | Standardize LSI v2 image preparation and reproducibility. | Define decode, resizing, gradients, percentile masks, QA, hashes, sequence ordering, and telemetry preprocessing. |
| [`lsi-gradient-field-regime-interpreter`](lsi-gradient-field-regime-interpreter/SKILL.md) | Interpret LSI v2 gradient-field regimes. | Read `rv`, EFA, `tail_gap`, quiet/active/isolated/dissolved fields, and field-aware CTG/SFS behavior. |
| [`lsi-ctg-rdc-gate-interpreter`](lsi-ctg-rdc-gate-interpreter/SKILL.md) | Interpret CTG-100 consequence bands and RDC radial/default gate interaction. | Decide in-band/out-of-band, prior-aligned/prior-divergent, extreme void/gravity, weak radial, off-center engineered, or capped behavior. |
| [`lsi-sfs-prior-distance-interpreter`](lsi-sfs-prior-distance-interpreter/SKILL.md) | Interpret SFS as distance from compositional prior center. | Need prior-near/prior-distant/capped readings from the 9D kernel vector, null pose, field regime, or RDC interaction. |
| [`lsi-barycentric-map-interpreter`](lsi-barycentric-map-interpreter/SKILL.md) | Interpret LSI v2 barycentric A/B/V map positions and lambda paths. | Read torque/rupture, offset/depth displacement, void/quiet-field weight, simplex drift, basin movement, or attractor contraction. |
| [`lsi-sequence-coherence-interpreter`](lsi-sequence-coherence-interpreter/SKILL.md) | Interpret ordered LSI v2 sequence scores and trajectory. | Need S/K/R/BCI/LSI100, basin flags, lambda paths, sign flips, iteration stability, drift, oscillation, collapse, or convergence. |
| [`lsi-telemetry-audit-interpreter`](lsi-telemetry-audit-interpreter/SKILL.md) | Interpret advisory color and tonal telemetry. | Explain structural-mask divergence from color, luminance, glare, low contrast, subject masks, or perceived visual balance. |
| [`lsi-model-comparison-diagnostics`](lsi-model-comparison-diagnostics/SKILL.md) | Compare generators, versions, prompt families, cohorts, or sweeps in LSI v2 space. | Diagnose structural range narrowing, prior-center clustering, radial/default tendency, safe-middle convergence, prompt-insensitive structure, or iterative resilience. |
| [`lsi-report-writer`](lsi-report-writer/SKILL.md) | Write audience-specific reports from LSI outputs and analyses. | Turn extraction, interpretation, audits, model comparisons, telemetry, or perturbation findings into methods notes, briefs, captions, or reports. |
| [`lsi-perturbation-robustness-tester`](lsi-perturbation-robustness-tester/SKILL.md) | Run or interpret LSI v2 Perturbation Mode for single-image robustness. | Need P, K-P, primitive variance, most-sensitive primitive, or robustness under crop/rotation/brightness/noise/flip disturbance. |
| [`lsi-perturbation-sensitivity-interpreter`](lsi-perturbation-sensitivity-interpreter/SKILL.md) | Interpret where Perturbation Mode fragility lives. | Need primitive-level sensitivity across `dx`, `dy`, `rv`, `rr`, `mu`, `xp`, `theta`, `ds`, `sdi` and perturbation families. |
| [`lsi-perturbation-vs-sequence-bridge`](lsi-perturbation-vs-sequence-bridge/SKILL.md) | Compare single-image perturbation robustness with ordered sequence coherence. | Decide whether an image is perturbation-robust but iteratively unstable, iteratively stable but perturbation-fragile, or coherent under both. |
| [`lsi-perturbation-auditor`](lsi-perturbation-auditor/SKILL.md) | Audit Perturbation Mode correctness and reproducibility. | Check nine deterministic perturbations, canonical parameters, same extractor, P/K-P math, variance, valid counts, baseline handling, and flip caveats. |
| [`lsi-perturbation-tiebreaker`](lsi-perturbation-tiebreaker/SKILL.md) | Use perturbation robustness to compare similar baseline LSI readings. | Need a structural tiebreak between near-matched images using P, K-P, variance profile, most-sensitive primitive, and per-perturbation rows. |

## Core Workflow Routes

### VCLI-G / SCI Route

Use when the question is perceptual cognitive load, structural coherence, image iteration, or phase-space position.

1. Prepare or review inputs with [`vcli-g-preprocessing-protocol`](vcli-g-preprocessing-protocol/SKILL.md).
2. Audit math with [`vcli-g-scoring-auditor`](vcli-g-scoring-auditor/SKILL.md) if calculations, notebooks, or CSVs are in question.
3. Interpret single images with [`vcli-g-interpreter`](vcli-g-interpreter/SKILL.md).
4. Track sequences with [`vcli-g-iteration-tracker`](vcli-g-iteration-tracker/SKILL.md).
5. Map cohorts with [`perceptual-phase-map`](perceptual-phase-map/SKILL.md).
6. Convert diagnosis to edits with [`visual-control-routes`](visual-control-routes/SKILL.md).
7. Write results with [`vcli-g-report-writer`](vcli-g-report-writer/SKILL.md).

### RCA-2 / RDC Route

Use when the question is radial compliance, frame-centered vs mass-centered structure, dual-center ambiguity, radial eligibility, or default radial candidate filtering.

1. Prepare masks and mass maps with [`rca-2-preprocessing-protocol`](rca-2-preprocessing-protocol/SKILL.md).
2. Audit scoring with [`rca-2-scoring-auditor`](rca-2-scoring-auditor/SKILL.md).
3. Interpret RCA-2 metrics with [`rca-2-interpreter`](rca-2-interpreter/SKILL.md).
4. Apply candidate inclusion/exclusion with [`rca-2-radial-default-candidate-gate`](rca-2-radial-default-candidate-gate/SKILL.md).
5. Inspect overlays with [`rca-2-radial-compliance-visual-diagnostics`](rca-2-radial-compliance-visual-diagnostics/SKILL.md).
6. Diagnose model/cohort priors with [`rca-2-radial-prior-model-diagnostics`](rca-2-radial-prior-model-diagnostics/SKILL.md).
7. Write results with [`rca-2-report-writer`](rca-2-report-writer/SKILL.md).
8. Apply or interpret the RDC gate. [`rca-2-rdc-radia-default-candidate-gate`](rca-2-rdc-radia-default-candidate-gate/SKILL.md).
9. Verify that all RCA-2 system components agree[`rca-2-consistency-check`](rca-2-consistency-check/SKILL.md).

### RCP Route

Use when the question is radial collapse prior as a visual failure mode or compositional default.

1. Run visual tests with [`rcp-visual-test-battery`](rcp-visual-test-battery/SKILL.md).
2. Classify the RCP level with [`rcp-classifier`](rcp-classifier/SKILL.md).
3. Bridge to kernel/axis terms with [`rcp-kernel-axis-bridge`](rcp-kernel-axis-bridge/SKILL.md).
4. Compare against human controls with [`rcp-human-control-comparator`](rcp-human-control-comparator/SKILL.md) when relevant.
5. Route corrective moves with [`rcp-router`](rcp-router/SKILL.md).

### VTL Kernel Route

Use when the question is current notebook-based VTL kernel extraction, deterministic metric generation, structural coordinate reading, or distributional prior diagnostics.

1. Extract metrics with [`vtl-kernel-extractor`](vtl-kernel-extractor/SKILL.md).
2. Audit math with [`vtl-kernel-scoring-auditor`](vtl-kernel-scoring-auditor/SKILL.md) if implementation correctness is uncertain.
3. Audit run trust with [`vtl-mask-qa-determinism-auditor`](vtl-mask-qa-determinism-auditor/SKILL.md).
4. Interpret vectors with [`vtl-kernel-interpreter`](vtl-kernel-interpreter/SKILL.md).
5. Interpret r_v field behavior with [`vtl-rv-gradient-field-interpreter`](vtl-rv-gradient-field-interpreter/SKILL.md).
6. Compare mask modes with [`vtl-mask-mode-contrast`](vtl-mask-mode-contrast/SKILL.md).
7. Type structural regimes with [`vtl-structure-regime-typer`](vtl-structure-regime-typer/SKILL.md).
8. Detect SDI center-collapse candidates with [`vtl-sdi-center-collapse-detector`](vtl-sdi-center-collapse-detector/SKILL.md).
9. Diagnose cohort-level priors with [`vtl-kernel-distribution-prior-diagnostics`](vtl-kernel-distribution-prior-diagnostics/SKILL.md).
10. Test structural prompt fidelity with [`vtl-prompt-structure-fidelity-tester`](vtl-prompt-structure-fidelity-tester/SKILL.md).
11. Write results with [`vtl-kernel-report-writer`](vtl-kernel-report-writer/SKILL.md).

### LSI v2 Route

Use when the question is current LSI v2 notebook extraction, structural coordinate interpretation, consequence/prior gates, ordered sequence coherence, model comparison, or perturbation robustness.

1. Prepare or review inputs with [`lsi-v2-preprocessing-protocol`](lsi-v2-preprocessing-protocol/SKILL.md).
2. Extract metrics with [`lsi-v2-extractor`](lsi-v2-extractor/SKILL.md).
3. Audit math with [`lsi-v2-scoring-auditor`](lsi-v2-scoring-auditor/SKILL.md) if implementation correctness, notebook alignment, or comparability is uncertain.
4. Interpret full records with [`lsi-v2-interpreter`](lsi-v2-interpreter/SKILL.md).
5. Interpret field regimes with [`lsi-gradient-field-regime-interpreter`](lsi-gradient-field-regime-interpreter/SKILL.md) when `rv`, EFA, or `tail_gap` drives the read.
6. Interpret consequence/default gates with [`lsi-ctg-rdc-gate-interpreter`](lsi-ctg-rdc-gate-interpreter/SKILL.md).
7. Interpret SFS prior distance with [`lsi-sfs-prior-distance-interpreter`](lsi-sfs-prior-distance-interpreter/SKILL.md).
8. Interpret barycentric position or lambda paths with [`lsi-barycentric-map-interpreter`](lsi-barycentric-map-interpreter/SKILL.md).
9. Interpret ordered iterations with [`lsi-sequence-coherence-interpreter`](lsi-sequence-coherence-interpreter/SKILL.md).
10. Use [`lsi-telemetry-audit-interpreter`](lsi-telemetry-audit-interpreter/SKILL.md) for color/tonal divergence without letting telemetry alter gates.
11. Compare cohorts or models with [`lsi-model-comparison-diagnostics`](lsi-model-comparison-diagnostics/SKILL.md).
12. Run or read single-image pressure tests with [`lsi-perturbation-robustness-tester`](lsi-perturbation-robustness-tester/SKILL.md).
13. Diagnose perturbation fragility with [`lsi-perturbation-sensitivity-interpreter`](lsi-perturbation-sensitivity-interpreter/SKILL.md).
14. Bridge perturbation and sequence evidence with [`lsi-perturbation-vs-sequence-bridge`](lsi-perturbation-vs-sequence-bridge/SKILL.md).
15. Audit perturbation runs with [`lsi-perturbation-auditor`](lsi-perturbation-auditor/SKILL.md).
16. Use [`lsi-perturbation-tiebreaker`](lsi-perturbation-tiebreaker/SKILL.md) when near-matched baseline readings need a robustness distinction.
17. Write results with [`lsi-report-writer`](lsi-report-writer/SKILL.md).

## VCLI-G / SCI Terms

### VCLI-G

Visual Cognitive Load Index - Geometry Coupled. A geometry-aware measure of visual cognitive load. In this folder, VCLI-G should be read with the current absolute-cap math, not older style-relative z-score or profile-average formulas.

VCLI-G is useful for:

- perceived structural load,
- earned tension vs overload,
- image iteration movement,
- cohort phase-space mapping,
- comparison of generated image ranges.

VCLI-G alone does not prove quality, human preference, semantic correctness, or artistic merit.

### SCI

Structural Coherence Index. Companion measure for whether visible complexity is organized enough to remain legible. SCI is not a replacement for VCLI-G; the useful read often comes from their combination.

Common phase reads:

- High VCLI-G + high SCI: earned tension.
- Lower VCLI-G + high SCI: resolved clarity.
- High VCLI-G + low SCI: collapse into noise or overload risk.
- Lower VCLI-G + lower SCI: default simplicity or underdeveloped structure.

### G1 / G2 / G3 / G4

VCLI-G channels. The exact channel math lives in the skill references. At the README level, treat them as separable drivers of the composite VCLI-G score. Do not interpret one channel in isolation without naming how it affects the composite.

### Centroid Wander

Movement or instability of the visual mass center. It may support tension, drift, instability, or deliberate displacement depending on SCI and the surrounding image.

### Void Topology

The structure of empty or quiet regions. Void is not blankness by default; active void can hold pressure, route attention, or create perceptual tension.

### Contour Curvature

Curvature behavior in visible contours. It can increase perceptual load when it creates complex pathing or ambiguity, but it needs SCI context.

### Orientation Entropy

Distribution of directional structure. High entropy can mean rich directional variety or disorganized noise depending on coherence.

### Earned Tension

High-load structure that remains organized. This is a phase-space read, not a universal quality claim.

### Resolved Clarity

Coherent, lower-load structure. This can be successful clarity or default simplicity depending on context.

### Collapse Into Noise

High-load structure without enough coherence to remain legible. Use cautiously and only with evidence from SCI, visible structure, or both.

### Default Simplicity

Low-load, low-risk structure that may lack tension or specificity. It is not automatically bad; it is a diagnostic for safe or underdeveloped visual behavior.

## VTL Kernel Metric Terms

The VTL Kernel Metrics stack uses the latest notebook math. The PDF specification may be historical context; the notebook is treated as current when conflicts arise.

### Canonical Extraction

The extractor uses image bytes, deterministic preprocessing, grayscale conversion, Sobel gradients, a canonical gradient-band mass mask, QA, and hashes. The current extractor package includes script support in [`vtl-kernel-extractor/scripts/extract_kernel.py`](vtl-kernel-extractor/scripts/extract_kernel.py).

### `delta_x`

Normalized horizontal offset of the gradient-band mass centroid from frame center. Preserve direction when left/right matters. Use with `delta_y`, `sdi`, and concentration evidence.

### `delta_y`

Normalized vertical offset of the gradient-band mass centroid from frame center. Use with `delta_x`; do not reduce spatial placement to horizontal displacement only.

### `r_v`

Gradient-quiet fraction based on absolute gradient threshold behavior in the current notebook, not semantic void and not plain background occupancy. High `r_v` means more of the field is gradient-quiet.

### `gradient_floor_85`

The 85th percentile gradient floor used in the r_v field package. Low values can support quiet-field readings.

### `gradient_ceiling_97`

The 97th percentile gradient ceiling. It helps describe the upper gradient tail.

### `tail_gap`

`gradient_ceiling_97 - gradient_floor_85`. Large gaps support isolated-edge readings; small gaps support flat-rendering readings.

### `EFA` / `efa`

Extractor field activation proxy carried in the r_v package. In the current skill set, it is treated with the r_v package rather than as a standalone quality score.

### `rho_r`

Mass density relative to the convex hull area in the VTL kernel extractor. It is a structural fill/packing measure for the active mask, not the same thing as aesthetic density.

### `mu`

Component dominance times inverse entropy. Higher values indicate more concentrated/dominant component behavior. Use with `largest_component_fraction`, `n_components`, and mask mode.

### `x_p`

Peripheral or frame-band activity: gradient magnitude in the outer frame band relative to total gradient magnitude. Elevated `x_p` supports border/framing evidence and can confound center-collapse readings.

### `theta`

Orientation entropy over gradient orientations. Lower values suggest more concentrated directional organization; higher values suggest broader or more isotropic orientation distribution.

### `d_s`

Distance-transform/skeleton thickness normalized by image dimension. Use as a spread/thickness support metric, not as a standalone verdict.

### `sdi`

Spatial Dispersion Index: mean distance of active mass pixels from their centroid, normalized by image diagonal. Low `sdi` can support compaction or center weighting only when centroid and concentration evidence align.

### `mass_fraction`

Fraction of pixels in the canonical percentile-band mask. It is a mask/device context field, not raw object occupancy.

### `mask_status`

QA usability label:

- `PASS`: mask is usable.
- `WARN`: usable with caveats.
- `FAIL`: substantive interpretation should stop.

### `mask_mode`

Interpretive mode label:

- `REGION_FIELD`: a dominant coherent region supports region-level structural reading.
- `TEXTURE_FIELD`: usable distributed field behavior; avoid object/region overclaims.
- `INVALID`: interpretation should stop.

### `sha256`

Input image byte hash. Used for identity and duplicate detection.

### `mask_sha256`

Binary mask hash. Used to check mask determinism and reproducibility.

### `kernel_vec_sha256`

Hash of the canonical kernel vector. Used to detect drift across duplicate images or repeated runs.

### Duplicate Drift

The same `sha256` should produce the same canonical vector within the extractor tolerance. Material duplicate drift is a run-integrity failure.

## VTL Kernel Regime Terms

### Quiet Open Field

High `r_v` and low `gradient_floor_85`, often with lower active mass. Means gradient-quiet field behavior, not necessarily semantic emptiness.

### Active Dense Field

Low `r_v`, higher gradient activity, higher active mass or orientation activity. Can mean detail, texture, clutter, or distributed structure.

### Isolated Edge Field

Large `tail_gap` with selective active mass. Strong edges carry structure.

### Flat Rendering Field

Low `tail_gap`; narrow gradient dynamic range. Can reflect flat, muted, low-contrast, or evenly rendered structure.

### Center-Weighted Compact Structure

Centroid near center, low-to-moderate `sdi`, concentration evidence, and lower border activity. For single images, prefer this over confirmed collapse.

### Center-Collapse Candidate

Low `sdi`, centered centroid, concentration evidence, and no stronger border/texture confound. For one image, it remains a candidate.

### Cohort Center-Collapse Pattern

Recurring low-SDI, centered, concentrated behavior across comparable rows. This is the minimum level where stronger collapse-pattern language becomes available.

### Border-Framed Structure

Elevated `x_p` and edge-band mass. It can be intentional framing, cropping artifact, or model prior; context decides.

### Fragmented Island Field

Many components, low largest-component share, low-to-mixed `mu`, often `TEXTURE_FIELD`. It describes distributed islands, not failure by itself.

### Dominant Region Field

`REGION_FIELD` with high component dominance. It supports region-level structure claims, not semantic object identity by itself.

## LSI v2 Terms

The LSI v2 stack uses the latest Colab notebook as the current mathematical source. The PDF specification is historical context when formulas or thresholds conflict. LSI v2 is a structural coordinate system, not an aesthetic ranker.

### LSI v2

Layered Structural Index v2. It combines deterministic kernel primitives, field-regime classification, radial/default gates, consequence bands, prior-distance scoring, barycentric mapping, sequence coherence, and advisory telemetry.

Use LSI v2 to describe where an image or ordered sequence sits in structural space. Do not treat it as a direct measure of quality, semantic accuracy, human preference, or artistic value.

### LSI v2 Extraction

Canonical extraction starts from image bytes, deterministic decoding, resizing, grayscale conversion, Sobel gradients, percentile mass masks, QA fields, hashes, and exported CSV/JSON. The current extractor package includes script support in [`lsi-v2-extractor/scripts/extract_lsi_v2.py`](lsi-v2-extractor/scripts/extract_lsi_v2.py).

### LSI 9D Primitive Vector

The single-frame LSI kernel vector is:

`[dx, dy, rv, rr, mu, xp, theta, ds, sdi]`

Interpret primitives as a composite. Do not make a strong claim from one primitive without naming the whole coordinate behavior.

### `dx` / `dy`

Normalized centroid displacement from the frame center. `dx` tracks horizontal offset and `dy` tracks vertical offset. Use them with `sdi`, `rr`, `mu`, and field regime before making center/default claims.

### `rv`

LSI v2 gradient sparsity from the percentile mass mask. It is not semantic void, not plain background, and not automatically the same as the VTL Kernel `r_v`. High `rv` can mean quiet ground, dissolved edges, rendering-style void, or weak activation depending on field regime.

### `rr`

Radial ratio or radial mass-distribution primitive in the LSI vector. It supports radial/default, spread, and prior-distance readings only in combination with RDC, `dx/dy`, `sdi`, and eligibility context.

### `mu`

Cohesion or dominance behavior in the LSI vector. High `mu` can support compactness or dominant-mass readings, but it does not prove quality or intentional focus by itself.

### `xp`

Peripheral or frame-band activity in the LSI vector. Elevated `xp` can indicate border pull, edge framing, crop sensitivity, or a confound for simple center-collapse claims.

### `theta`

Orientation entropy or directional distribution. It helps read axis stability, orientation breadth, and rotation sensitivity. It is not a semantic style label.

### `ds`

Structural spread/thickness or distance-transform behavior in the LSI vector. Use it as support for dispersion, compaction, or texture behavior rather than as a standalone verdict.

### `sdi`

Spatial Dispersion Index. In LSI, low `sdi` can support compactness or center weighting when centroid and concentration evidence align. It does not by itself prove radial collapse.

### Field Regime

LSI field regimes contextualize `rv`, EFA, and `tail_gap`. Common labels include `QUIET_ISOLATED`, `ACTIVE_ISOLATED`, `QUIET_DISSOLVED`, `QUIET_MODERATE`, `ACTIVE_FIELD`, `MODERATE_FIELD`, and `MIXED`.

Field regime prevents overreading high `rv` as void and prevents treating texture, dissolved edges, or isolated-edge behavior as the same structural state.

### EFA

Extractor Field Activation in the LSI field package. Use with `rv`, `gradient_floor_85`, `gradient_ceiling_97`, and `tail_gap` to separate quiet fields, active fields, isolated edges, dissolved edges, and threshold-near behavior.

### `tail_gap`

Difference between high-gradient ceiling and gradient floor. Large `tail_gap` can support isolated-edge or high-tail behavior; small `tail_gap` can support flatter, dissolved, or low-contrast readings depending on field regime.

### CTG-100

Consequence Tension Gate / consequence proximity score in the LSI Layer 3 gate layer. CTG asks whether an image sits near consequence bands; it is not a quality score and not the same thing as SFS.

### `K`

Consequence status or consequence proximity classification associated with CTG. Treat `K` as a structural/gate claim. If Perturbation Mode shows low `K-P`, baseline `K` may be marginal under pressure.

### Red Bands

Named CTG exclusion or warning bands. They mark structural regions where a reading is out of band or requires caveated interpretation. Use `band_exit_reason` when present.

### RDC in LSI

RDC is the radial/default candidate gate inside LSI v2. It should remain orthogonal to CTG: RDC asks whether radial/default prior alignment is present or eligible; CTG asks consequence proximity.

### SFS

Structural Fingerprint Score. SFS measures distance from a compositional prior/null pose in 9D primitive space. It is a prior-distance coordinate, not quality, novelty, or prompt fidelity.

### SFS Cap

RDC and field behavior can cap or contextualize SFS. A high or low SFS should be read through cap behavior, prior distance, and eligibility rather than as a simple success/failure number.

### Null Pose

The prior-center vector against which SFS distance is measured. Being near the null pose can mean prior-near, default-aligned, or structurally conventional; it does not automatically mean bad.

### Barycentric A/B/V Map

Layer 4 reduced compositional phase map:

- `A`: torque, rupture, or worked structural force.
- `B`: offset/depth/displacement behavior.
- `V`: void, quiet field, or sparsity weight.

Use barycentric coordinates to read compositional basin position, simplex drift, lambda paths, and attractor movement.

### Lambda Path

Movement of barycentric coordinates across a sequence. A contracting path can support basin formation; an expanding or oscillating path can support drift or unresolved iteration behavior.

### Sequence Scores `S`, `K`, `R`

Layer 5 ordered-sequence terms:

- `S`: stability across deliberate iterations.
- `K`: consequence retention across the sequence.
- `R`: recursion coherence or recurrence behavior.

These require ordered multi-frame sequences. Do not infer them from a single image.

### BCI

Basin Coherence Index. A sequence-level score for whether ordered iterations form or hold a compositional basin. It is not available from one standalone frame.

### LSI100

Composite sequence-level LSI score. It summarizes sequence behavior and must be read with `S`, `K`, `R`, BCI, weights, and basin flags.

### Basin Flag

Indicator that a sequence appears to converge into, hold, or form a compositional basin. It is a sequence claim and requires ordered comparable frames.

### Telemetry

LSI color and tonal telemetry are advisory diagnostics. Fields such as `rv_color_mask`, `dx_color_L`, `delta_rv`, `delta_dx`, `S_L`, `eta_L`, `beta_L`, `dx_tonal_L`, and audit badges explain divergence between structural mask behavior and perceived color/luminance balance.

Telemetry must not alter CTG, RDC, SFS, BCI, LSI100, or acceptance gates.

### Perturbation Mode

Single-image robustness test that applies deterministic small disturbances and reruns the LSI pipeline. The canonical set is baseline, crop top-left, crop bottom-right, rotate clockwise, rotate counter-clockwise, brightness up, brightness down, Gaussian noise, and horizontal flip.

Perturbation Mode asks: how tightly does this image hold its LSI position under involuntary pressure? It is not a replacement for sequence scoring.

### `stability_p` / P

Perturbation stability score from normalized variance across the primitive vector. `P > 0.80` indicates robust coordinate hold; `P < 0.50` indicates structural fragility under disturbance. P is not image quality.

### `k_p` / K-P

Average consequence proximity across perturbations. It tests whether baseline consequence survives pressure. A strong baseline `K` with weak `K-P` should be described as marginal consequence.

### Most-Sensitive Primitive

The primitive with the largest variance across perturbations. It localizes fragility: for example, `mu` sensitivity indicates cohesion fragility, `dx` sensitivity indicates centroid marginality, `rv` sensitivity indicates field-threshold sensitivity, and `theta` sensitivity indicates axis fragility.

### Perturbation Versus Sequence

Perturbation Mode measures robustness of one image under involuntary disturbance. Sequence scoring measures coherence across deliberate creative iterations. A composition can be sequence-stable but perturbation-fragile, or perturbation-stable but iteratively unstable.

### Perturbation Tiebreak

When two images have similar baseline LSI readings, perturbation results can decide which structure is more pressure-stable or which consequence is more structurally earned. This is a structural tiebreak only; it is not a quality ranking.

## RCA-2 / RDC Terms

### RCA-2

Dual-Center Radial Compliance Analyzer. It compares radial compliance around frame center and mass center to distinguish frame-dominant, mass-dominant, dual-center, weak-radial, or ineligible radial behavior.

### Frame Center

Geometric center of the image frame. A frame-centered radial pattern can suggest default stabilization around the image center.

### Mass Center

Centroid or center of the foreground/mass map. A mass-centered radial pattern can indicate radial organization around the actual subject mass rather than the frame.

### `frame_radial_compliance` / `RC_f`

How well the mass/profile complies with a radial model around the frame center.

### `mass_radial_compliance` / `RC_s`

How well the mass/profile complies with a radial model around the mass center.

### `delta_radial_compliance` / `DRC`

Difference between frame-centered and mass-centered radial compliance. The sign and definition must be audited; reversed DRC is a known failure pattern.

### `delta_r`

Distance or offset between frame center and mass center. Important for off-center engineering and dual-center ambiguity.

### `frame_jsd` / `mass_jsd`

Jensen-Shannon divergence values for radial profile fits around the frame or mass center. Lower divergence usually means closer profile fit, but interpret with the RCA-2 skill.

### `frame_alpha` / `mass_alpha`

Exponential decay or profile fit parameters around frame/mass centers. These help diagnose how radial mass falls off.

### Radial Eligibility

Whether the image/mask has enough radial structure, compactness, isotropy, mask area, and suitability for RCA-2/RDC interpretation.

### RDC Gate

Radial Default Candidate gate. It decides whether an image should be included in default radial prior measurement. It is an inclusion/exclusion gate, not an aesthetic ranking.

### Common RDC Exclusions

- `MASK_EMPTY`: no usable mask.
- `WEAK_RADIAL`: insufficient radial evidence.
- `DUAL_ATTRACTOR_NEAR_TIE`: frame and mass centers compete too closely.
- `OFFCENTER_ENGINEERED`: off-center structure appears intentionally engineered.
- `SUBJECT_INELIGIBLE_FOR_POS_DRC`: subject or setup invalidates the positive DRC claim.

## RCP Terms

### RCP

Radial Collapse Prior. A visual prior/failure mode where generated structure collapses into a single radial or centered organizing force. RCP is not the same as all centered composition.

### Center-Lock

Structure is locked to the frame center or a central attractor with insufficient counter-force.

### Radial Void

Void behaves symmetrically or radially around the center instead of being actively carved or compositionally negotiated.

### Density Bowl

Density falls into a radial bowl-like distribution, often reinforcing a single central attractor.

### Ring Conformity

Marks, gestures, edges, or details conform to rings around a center.

### Mu Inflation

Kernel-level concentration or cohesion appears inflated around a single attractor. Use with caution; it is supporting evidence, not proof by itself.

### Hard RCP

Strong radial collapse: multiple hits align, local structure obeys the global radial field, and counter-forces are weak.

### Soft RCP

Partial radial/default tendency with some counter-structure or ambiguity.

### Borderline RCP

Insufficient or mixed evidence. Usually requires visual tests, kernel bridge, or human-control comparison.

### Delta / Omega / O / Hold

Route language used for corrective interventions:

- Delta: displace or introduce asymmetry/counter-force.
- Omega: add wrapping, return, or secondary force behavior.
- O: preserve or clarify an already useful centered structure.
- Hold: do not overcorrect; maintain a working structure while adjusting locally.

## Cross-System Terms

### VTL

Visual Thinking Lens: broader stack that includes structural, perceptual, telemetry, symbolic, and control layers. VCLI-G and VTL Kernel Metrics are layers inside this broader operating language.

### LSI / LSI-Lite

Layered Structural Index language for placement, void/quiet-field behavior, density, radial/default gates, prior distance, barycentric position, sequence coherence, and perturbation robustness. In this folder, LSI v2 is now a full extraction and interpretation family, while LSI-Lite remains a looser bridge phrase when discussing older or reduced structural-index language.

### TEL

Telemetry: advisory structural metrics. TEL helps interpret movement but should not be treated as a direct pass/fail or quality verdict unless a profile explicitly says so.

### Safe Middle

A generative tendency toward low-risk, centered, coherent, broadly acceptable visual structure. It may show as narrow VCLI-G/SCI phase-space range, center-weighted VTL kernels, radial defaults, or prompt-insensitive structural recurrence.

### Prompt-Insensitive Structure

Structural metrics remain stable despite prompts that should move composition. This can suggest a model/pipeline prior, but only across comparable prompt variants or repeated runs.

### Distributional Prior

A recurring low-variance structural tendency across comparable cohorts. Name the axis: center, radial, quiet field, dense field, border, fragmentation, flat rendering, isolated edges, or mask mode.

## Common Handoffs

| Starting question | First skill | Likely next skill |
|---|---|---|
| "What are the VTL kernel metrics for these images?" | `vtl-kernel-extractor` | `vtl-mask-qa-determinism-auditor`, `vtl-kernel-interpreter` |
| "What are the LSI v2 metrics for these images or sequence?" | `lsi-v2-extractor` | `lsi-v2-scoring-auditor`, `lsi-v2-interpreter` |
| "Can I trust this LSI v2 table or notebook output?" | `lsi-v2-scoring-auditor` | `lsi-v2-preprocessing-protocol` if comparability is suspect |
| "What does this LSI record mean?" | `lsi-v2-interpreter` | Specialized LSI interpreter for the main driver: field regime, CTG/RDC, SFS, barycentric, sequence, or telemetry |
| "Is this LSI consequence score robust?" | `lsi-perturbation-robustness-tester` | `lsi-perturbation-sensitivity-interpreter`, `lsi-perturbation-auditor` |
| "Which of these similar LSI images holds better?" | `lsi-perturbation-tiebreaker` | `lsi-perturbation-sensitivity-interpreter` |
| "Is this image stable under perturbation but not iteration?" | `lsi-perturbation-vs-sequence-bridge` | `lsi-sequence-coherence-interpreter` |
| "Which model has the stronger LSI structural prior?" | `lsi-model-comparison-diagnostics` | `generative-safe-middle-detector`, `rca-2-radial-prior-model-diagnostics` |
| "Can I trust this VTL batch?" | `vtl-mask-qa-determinism-auditor` | `vtl-kernel-scoring-auditor` if math is suspect |
| "What structural regime is this?" | `vtl-structure-regime-typer` | `vtl-kernel-report-writer` |
| "Is this center collapse?" | `vtl-sdi-center-collapse-detector` | `rcp-classifier` or `radial-default-candidate-gate` if radial/default evidence matters |
| "Did the prompt move the structure?" | `vtl-prompt-structure-fidelity-tester` | `vtl-kernel-distribution-prior-diagnostics` if prompt-insensitive |
| "Is this model playing it safe?" | `generative-safe-middle-detector` | `perceptual-phase-map`, `vtl-kernel-distribution-prior-diagnostics`, `rca-2-radial-prior-model-diagnostics` |
| "Does this show radial default behavior?" | `rca-2-interpreter` or `radial-default-candidate-gate` | `rca-2-radial-prior-model-diagnostics`, `rcp-classifier` |
| "How do I fix this composition?" | `visual-control-routes` or `rcp-router` | Relevant interpreter after the next iteration |
| "How do I write this up?" | Domain report writer | `image-metric-positioning` if claims need external metric framing |

## Support References By Skill

Most skills include compact references that should be loaded only when needed:

| Skill | References |
|---|---|
| `lsi-barycentric-map-interpreter` | `lambda-path.md`, `triangle-zones.md` |
| `lsi-ctg-rdc-gate-interpreter` | `ctg-guide.md`, `gate-matrix.md`, `rdc-guide.md` |
| `lsi-gradient-field-regime-interpreter` | `regime-guide.md`, `telemetry-caveats.md` |
| `lsi-model-comparison-diagnostics` | `comparison-design.md`, `diagnostic-patterns.md` |
| `lsi-perturbation-auditor` | `canonical-checklist.md`, `failure-patterns.md` |
| `lsi-perturbation-robustness-tester` | `interpretation-guide.md`, `sensitivity-map.md`; script: `scripts/run_perturbation.py` |
| `lsi-perturbation-sensitivity-interpreter` | `disturbance-patterns.md`, `primitive-sensitivity.md` |
| `lsi-perturbation-tiebreaker` | `comparison-patterns.md`, `tiebreak-rules.md` |
| `lsi-perturbation-vs-sequence-bridge` | `bridge-matrix.md`, `consequence-bridge.md` |
| `lsi-report-writer` | `audience-templates.md`, `claim-language.md` |
| `lsi-sequence-coherence-interpreter` | `score-components.md`, `trajectory-patterns.md` |
| `lsi-sfs-prior-distance-interpreter` | `component-contributions.md`, `sfs-bands.md` |
| `lsi-telemetry-audit-interpreter` | `color-telemetry.md`, `tonal-telemetry.md` |
| `lsi-v2-extractor` | `canonical-math.md`, `runbook.md`; script: `scripts/extract_lsi_v2.py` |
| `lsi-v2-interpreter` | `claim-boundaries.md`, `gate-and-score-guide.md`, `metric-guide.md` |
| `lsi-v2-preprocessing-protocol` | `edge-cases.md`, `protocol-fields.md` |
| `lsi-v2-scoring-auditor` | `canonical-checklist.md`, `failure-patterns.md` |
| `rca-2-radial-compliance-visual-diagnostics` | `panel-reading-guide.md`, `visual-failure-patterns.md` |
| `rca-2-consistency-check` |
| `rca-2-radial-default-candidate-gate` | `gate-spec.md`, `interpretation-boundaries.md` |
| `rca-2-radial-prior-model-diagnostics` | `evidence-and-claims.md`, `prior-signatures.md` |
| `rca-2-interpreter` | `guardrails.md`, `metric-guide.md` |
| `rca-2-preprocessing-protocol` | `comparability-and-edge-cases.md`, `mass-map-protocol.md` |
| `rca-2-report-writer` | `audience-templates.md`, `claim-language.md` |
| `rca-2-scoring-auditor` | `audit-checklist.md`, `failure-patterns.md` |
| `rca-2-rdc-radia-default-candidate-gate` 
| `rcp-classifier` | `classification-language.md`, `hit-definitions.md` |
| `rcp-human-control-comparator` | `claim-boundaries.md`, `comparison-matrix.md`, `human-control-signals.md` |
| `rcp-kernel-axis-bridge` | `axis-map.md`, `claim-boundaries.md`, `kernel-map.md` |
| `rcp-router` | `prompt-and-edit-patterns.md`, `route-recipes.md` |
| `rcp-visual-test-battery` | `evidence-notes.md`, `test-protocols.md` |
| `vcli-g-generative-safe-middle-detector` | `generative-study-design.md`, `safe-middle-patterns.md` |
| `vcli-g-image-metric-positioning` | `claim-language.md`, `metric-comparisons.md` |
| `vcli-g-experiment-designer` | `study-patterns.md`, `validation-methods.md` |
| `vcli-g-interpreter` | `current-math.md`, `historical-frame.md` |
| `vcli-g-iteration-tracker` | `sequence-inputs.md`, `trajectory-patterns.md` |
| `vcli-g-perceptual-phase-map` | `cohort-methods.md`, `phase-space.md` |
| `vcli-g-preprocessing-protocol` | `edge-cases.md`, `protocol-fields.md` |
| `vcli-g-report-writer` | `audience-templates.md`, `claim-and-tone.md` |
| `vcli-g-scoring-auditor` | `audit-checklist.md`, `canonical-scoring.md` |
| `vcli-g-visual-control-routes` | `move-patterns.md`, `route-library.md` |
| `vtl-kernel-distribution-prior-diagnostics` | `diagnostic-status.md`, `prior-patterns.md` |
| `vtl-kernel-extractor` | `canonical-math.md`, `runbook.md`; script: `scripts/extract_kernel.py` |
| `vtl-kernel-interpreter` | `metric-guide.md`, `qa-and-claim-boundaries.md` |
| `vtl-kernel-report-writer` | `claim-language.md`, `report-templates.md` |
| `vtl-kernel-scoring-auditor` | `canonical-checklist.md`, `failure-patterns.md` |
| `vtl-layer-bridge` | `cross-read-patterns.md`, `layer-map.md` |
| `vtl-mask-mode-contrast` | `mode-definitions.md`, `transition-patterns.md` |
| `vtl-mask-qa-determinism-auditor` | `failure-patterns.md`, `qa-checklist.md` |
| `vtl-prompt-structure-fidelity-tester` | `fidelity-status.md`, `prompt-to-metric-map.md` |
| `vtl-rv-gradient-field-interpreter` | `comparison-rules.md`, `field-regimes.md` |
| `vtl-sdi-center-collapse-detector` | `confounds.md`, `detection-ladder.md` |
| `vtl-structure-regime-typer` | `evidence-rules.md`, `regime-catalog.md` |

## Final Boundary

The analytic folder is strongest when its skills are used as a layered system:

1. preprocess,
2. extract or inspect,
3. audit,
4. interpret,
5. compare,
6. diagnose,
7. route or report.

Skipping audit/comparability is the most common way to overclaim. Skipping interpretation is the most common way to reduce the system to numbers. The intended use is neither: keep the measurements, visual evidence, and claim strength aligned.

This package contains a modular visual reasoning skill suite built from Russell Parrish / A.rtist I.nfluencer protocols. The skills are designed to run independently, but they also interoperate through routing, handoff notes, and shared visual reasoning concepts. More information: www.artistinfluencer.com. Copyright 2026.
