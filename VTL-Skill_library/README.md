# VTL Skill Analytics README

This README is the index for the `VTL-Skill_Analytics` tree.

It explains:

- what each analytic category is for
- what each skill does
- where to start when the correct analytic tool is unclear

For shared terminology and claim boundaries, use [DefinitionReadme.md](/Users/russellparrish/Documents/1.All_Skills/VTL-Skill_Analytics/DefinitionReadme.md). That file is the glossary. This README is the navigation layer.

## What This Tree Is

This folder is not a prompt library. It is an analytic toolkit.

Its focus is:

- extraction
- interpretation
- auditing
- comparability
- cohort diagnostics
- reporting
- structural claim discipline

The categories are already organized by analytic family:

- `01_lsi`: layered structural intelligence, perturbation, sequence, barycentric, telemetry, and model comparisons
- `02_rca-2`: dual-center radial compliance and radial default candidate analysis
- `03_rcp`: radial collapse prior classification and intervention routing
- `04_vcli`: perceptual load and structural coherence analytics
- `05_vtl`: canonical VTL kernel extraction, interpretation, audits, and cross-layer bridges

## Quick Start

- If you have raw images and want canonical VTL metrics first, start with `vtl-kernel-extractor`.
- If you already have VTL kernel outputs and want them explained, start with `vtl-kernel-interpreter`.
- If you have full LSI outputs and want a broad layered read, start with `lsi-v2-interpreter`.
- If you want radial-compliance analysis, start with `rca-2-interpreter`.
- If you suspect radial collapse in a result, start with `rcp-classifier`.
- If you are working from VCLI-G or SCI scores, start with `vcli-g-interpreter`.
- If you need to audit whether a claim is overstated, start with `vtl-analytic-claim-auditor`.

## 01_lsi

Purpose: layered structural analytics across extraction, interpretation, gates, barycentric maps, sequence coherence, perturbation robustness, telemetry, and model comparison.

- `lsi-v2-extractor`: runs images or ordered sequences through canonical LSI v2 extraction and exports Layer 0-6 outputs.
- `lsi-v2-interpreter`: turns LSI records into a structural read across kernel primitives, gates, SFS, barycentric position, telemetry, and sequence layers.
- `lsi-v2-scoring-auditor`: checks whether LSI scoring math, gates, and pipeline outputs are correct and current.
- `lsi-v2-preprocessing-protocol`: standardizes preprocessing and reproducibility for LSI extraction.
- `lsi-gradient-field-regime-interpreter`: reads field regimes such as quiet, active, isolated, dissolved, and mixed.
- `lsi-ctg-rdc-gate-interpreter`: interprets CTG-100 consequence bands and RDC radial/default gate interaction.
- `lsi-sfs-prior-distance-interpreter`: reads SFS as distance from a compositional prior center.
- `lsi-barycentric-map-interpreter`: interprets LSI barycentric A/B/V positions and lambda-path movement.
- `lsi-sequence-coherence-interpreter`: reads ordered iteration sequences for stabilization, oscillation, collapse, or convergence.
- `lsi-telemetry-audit-interpreter`: explains advisory color and tonal telemetry and structural-mask divergence.
- `lsi-model-comparison-diagnostics`: compares models, prompt families, or cohorts in LSI space.
- `lsi-report-writer`: turns LSI findings into reports, methods notes, briefs, or public explanations.
- `lsi-perturbation-robustness-tester`: runs or interprets single-image perturbation robustness.
- `lsi-perturbation-sensitivity-interpreter`: locates which primitives are fragile under perturbation.
- `lsi-perturbation-vs-sequence-bridge`: compares perturbation robustness with ordered sequence stability.
- `lsi-perturbation-auditor`: audits perturbation mode correctness and reproducibility.
- `lsi-perturbation-tiebreaker`: uses perturbation robustness to distinguish between near-matched images.

## 02_rca-2

Purpose: radial compliance analytics centered on frame/mass radial behavior, radial eligibility, and radial default candidate gating.

- `rca-2-interpreter`: interprets dual-center radial compliance outputs and what they imply structurally.
- `rca-2-preprocessing-protocol`: standardizes masks, mass maps, centroids, and reproducibility for RCA-2/RDC.
- `rca-2-scoring-auditor`: audits RCA-2 and RDC math, gates, and pipeline validity.
- `rca-2-radial-default-candidate-gate`: applies the RDC inclusion/exclusion gate to RCA-2 outputs.
- `rca-2-radial-prior-model-diagnostics`: diagnoses model-level radial default-prior behavior from batches or cohorts.
- `rca-2-radial-compliance-visual-diagnostics`: reads overlays, rings, mass profiles, and visual panels against the metrics.
- `rca-2-rdc-radia-default-candidate-gate`: applies or audits the RDC gate as a standalone decision layer.
- `rca-2-report-writer`: writes audience-specific RCA-2/RDC reports.
- `rca-2-consistency-check`: cross-validates RCA-2 artifacts to detect contradictions, drift, or broken claim chains.

## 03_rcp

Purpose: classify radial collapse prior, inspect it visually, bridge it back to kernel space, and route toward anti-radial fixes.

- `rcp-classifier`: classifies radial collapse prior and strength of evidence.
- `rcp-router`: routes an RCP diagnosis into corrective prompt, edit, or compositional interventions.
- `rcp-visual-test-battery`: runs image-first radial collapse tests without requiring kernel math.
- `rcp-kernel-axis-bridge`: translates RCP evidence into VTL/LSI kernel primitives and axis behavior.
- `rcp-human-control-comparator`: contrasts AI radial collapse patterns against human-made controls.

## 04_vcli

Purpose: analyze perceptual load, structural coherence, safe-middle behavior, cohort phase space, and VCLI-based control routes.

- `vcli-g-interpreter`: interprets VCLI-G and SCI readings for images.
- `vcli-g-scoring-auditor`: audits VCLI-G scoring math and pipeline correctness.
- `vcli-g-iteration-tracker`: analyzes movement across drafts, generations, or recursive sequences.
- `vcli-g-perceptual-phase-map`: reads cohorts in VCLI-G x SCI phase space.
- `vcli-g-preprocessing-protocol`: standardizes VCLI preprocessing and reproducibility.
- `vcli-g-experiment-designer`: designs VCLI-G/SCI validation and research studies.
- `vcli-g-image-metric-positioning`: positions VCLI-G relative to CLIP, FID, aesthetic scores, and related metrics.
- `vcli-g-report-writer`: writes audience-specific reports from VCLI outputs.
- `vcli-g-generative-safe-middle-detector`: detects safe-middle convergence in generative-image cohorts.
- `vcli-g-visual-control-routes`: converts VCLI diagnoses into prompt, edit, or compositional steering moves.

## 05_vtl

Purpose: canonical VTL kernel extraction and interpretation, QA and scoring audits, structure regimes, distribution priors, and cross-system claim discipline.

- `vtl-kernel-extractor`: runs canonical VTL kernel extraction and returns deterministic vectors, field package values, QA, and hashes.
- `vtl-kernel-interpreter`: interprets VTL kernel outputs as structural coordinates rather than quality scores.
- `vtl-kernel-scoring-auditor`: audits kernel math and notebook alignment.
- `vtl-mask-qa-determinism-auditor`: audits run integrity, mask QA, hashes, duplicate drift, and comparability.
- `vtl-rv-gradient-field-interpreter`: interprets the `r_v` gradient-field package.
- `vtl-structure-regime-typer`: classifies VTL outputs into structure regimes and operating zones.
- `vtl-mask-mode-contrast`: compares REGION_FIELD, TEXTURE_FIELD, and INVALID behavior across runs or cohorts.
- `vtl-sdi-center-collapse-detector`: detects SDI-based center weighting and center-collapse candidates.
- `vtl-kernel-distribution-prior-diagnostics`: analyzes cohort-level priors and low-variance default signatures.
- `vtl-prompt-structure-fidelity-tester`: tests whether prompt-intended structure actually moved VTL coordinates.
- `vtl-kernel-report-writer`: turns VTL outputs into technical, research, product, or executive reports.
- `vtl-layer-bridge`: connects VCLI and the broader VTL stack without collapsing layer boundaries.
- `vtl-analytic-claim-auditor`: audits whether reports or interpretations overstate what the analytics support.

## Recommended First Skills

If someone is new to this tree, these are the most useful entry skills:

- `vtl-kernel-extractor`
- `vtl-kernel-interpreter`
- `lsi-v2-interpreter`
- `rca-2-interpreter`
- `rcp-classifier`
- `vcli-g-interpreter`
- `vtl-analytic-claim-auditor`

## Notes

- This analytics tree is strongest when used as a measurement and claim-discipline layer, not as a taste engine.
- Many skills come in families: extractor, interpreter, auditor, protocol, report-writer, and cohort diagnostics.
- If we later connect this tree with the main library, the cleanest bridge will likely be through the shared VTL terms, claim rules, and routing docs rather than merging everything into one flat system.

This package contains a modular visual reasoning skill suite built from Russell Parrish / A.rtist I.nfluencer protocols. The skills are designed to run independently, but they also interoperate through routing, handoff notes, and shared visual reasoning concepts. More information: www.artistinfluencer.com. Copyright 2026.
