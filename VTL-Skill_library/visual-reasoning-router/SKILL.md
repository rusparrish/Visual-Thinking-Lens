---
name: visual-reasoning-router
description: Lightweight orchestrator for choosing among Russell Parrish / A.rtist I.nfluencer visual reasoning skills. Use when a user asks which skill to use, gives an ambiguous image/prompt/model-analysis request, wants a visual critique workflow, or needs routing between Concert Mode, Sketcher Lens, Artist's Lens, Visual Thinking Lens, Marrowline Critique, Reverse Iterative Decomposition, Deformation Operator Playbook, Volumetric Container of Force, Foreshortening Recipe Book, Off-Center Prior Diagnostic, Radial Collapse Prior, Prompt Collapse Suite, and Structural Prompt Stabilizer. This skill selects the right skill or sequence and does not replace specialist skills.
---

# Visual Reasoning Router

## Purpose

Use this skill to choose the right visual reasoning skill or sequence. Keep the router small: classify the task, name the primary skill, optionally name a secondary skill, and explain the route.

Do not perform specialist analysis here unless the user only asks for routing.

Specialist references:

- Sequence patterns: [references/sequences.md](references/sequences.md)

## Skill Families

**Core frameworks**

- `concert-mode`: live multi-engine visual dialogue environment. Use for Play/Critique/Dialogues sessions, co-scoring, recursive learning loops, and staged user interaction.
- `sketcher-lens`: structural axis OS. Use for axis-by-axis diagnosis, material assertion, frame tension, gesture weight, structural pressure, validator routing, and prompt-to-form translation.
- `artists-lens`: qualitative visual reasoning framework. Use for intent/tension critique, vocabulary-set scoring, prompt scaffolds, study mode, and centaur artist iteration.
- `visual-thinking-lens`: recursive orchestrator. Use for multi-engine critique, kernel/telemetry, Sketcher/Artist/Marrowline/RIDP debate, and Delta/Omega/Hold routing.

**Symbolic and process diagnostics**

- `marrowline-critique`: symbolic pressure, refusal, symbolic drift, false coherence, hollow iconography, recursive collapse.
- `reverse-iterative-decomposition`: reverse construction, block-in, underpainting, material peel, sketch-state regression, lineage recovery.
- `prompt-collapse-suite`: prompt-chain drift, recursive echo, symbolic redundancy, form fossilization, token explosion, repeated generation failures.
- `structural-prompt-stabilizer`: tactical prompt hardening with SO-12 structural operators, anti-collapse constraints, kernel-aware rewrites, and baseline vs stabilized prompt pairs.

**Spatial, force, and geometry specialists**

- `volumetric-container-force`: anchors, counterforces, pressure zones, force vectors, delayed resolve, view-window consequence.
- `deformation-operator-playbook`: controlled deformation, figure/limb edits, coil/stretch/bend operators, viewfinder shifts, inpaint prompts.
- `foreshortening-recipe-book`: depth projection, compression toward/away from viewer, limb/object foreshortening, projection repair.
- `off-center-prior-diagnostic`: off-center placement, spatial bias, void agency, forbidden zones, A-E model tests.
- `radial-collapse-prior`: radial-field collapse, center-lock, halo/emblem/target structure, density bowl, anti-radial repair.

## Decision Rules

If the user wants **an interactive guided session**:

- Use `concert-mode`.
- Triggers: Concert Mode, interactive critique, walk me through, co-score, Play/Critique/Dialogues, recursive learning loop, teach me through this, respond to my sketch, live visual dialogue.

If the user wants the **structural skeleton**:

- Use `sketcher-lens`.
- Triggers: Sketcher, axes, OS, skeleton, Axis 0, material assertion, frame tension, gesture weight, validator routing, structural prompt translation.

If the user wants **deep visual reasoning or qualitative critique**:

- Use `artists-lens`.
- Triggers: Artist's Lens, intent and tension, visual consequence, vocabulary sets, poise, study mode, centaur artist, prompt scaffold.

If the user wants **a full recursive critique workflow**:

- Use `visual-thinking-lens`.
- Triggers: full critique, multi-engine debate, route decision, Delta/Omega/Hold, kernel primitives, telemetry, "what should happen next?"

If the work is **beautiful, symbolic, polished, but inert or false**:

- Use `marrowline-critique`.

If the user asks **how the image was built or wants earlier stages**:

- Use `reverse-iterative-decomposition`.

If the issue is **prompt-chain behavior across iterations**:

- Use `prompt-collapse-suite`.
- Triggers: keeps making the same thing, recurring unwanted motif, prompt gets worse, form fossilization, token overload.

If the user wants **a single prompt made more stable before generation**:

- Use `structural-prompt-stabilizer`.
- Triggers: stabilize this prompt, anti-collapse prompt, add structural operators, reduce drift, avoid centering, no halo, make it Sora-friendly, baseline vs stable prompt.

If the repair needs **anchors, pressure, force transfer, or volumetric consequence**:

- Use `volumetric-container-force`.

If the user wants **controlled geometric change**:

- Use `deformation-operator-playbook`.
- Triggers: change limb, bend, stretch, coil, distort, viewfinder shift, inpaint/edit instruction.

If the problem is **depth projection or near/far compression**:

- Use `foreshortening-recipe-book`.

If the question is **off-center placement or void behavior**:

- Use `off-center-prior-diagnostic`.

If the image is **center-locked, haloed, emblematic, target-like, circular, or AI-correct but dead**:

- Use `radial-collapse-prior`.

If the user asks **which skill to use**:

- Return one primary skill, one optional secondary skill, and the expected output.

## Routing Output

Use this format:

```text
Primary skill: $skill-name
Reason: [one sentence]
Optional sequence: [$skill-a -> $skill-b]
Expected output: [what the user will receive]
```

Choose the narrowest skill that directly produces the requested artifact. Use a sequence only when the task genuinely spans multiple operations.

## Common Sequences

- `concert-mode -> sketcher-lens`: interactive session begins with structural grounding.
- `concert-mode -> prompt-collapse-suite`: Dialogues mode identifies a prompt or generation chain loop.
- `concert-mode -> reverse-iterative-decomposition`: Dialogues mode needs a counter-image or prior-state reconstruction.
- `sketcher-lens -> artists-lens`: structural axis diagnosis first, then richer intent/tension critique.
- `sketcher-lens -> volumetric-container-force`: diagnose weak pressure/gesture/frame axes, then build force-field repair.
- `artists-lens -> marrowline-critique`: full visual reasoning, then symbolic refusal for polished hollow work.
- `visual-thinking-lens -> marrowline-critique`: route through engine debate, then escalate to symbolic pressure.
- `prompt-collapse-suite -> reverse-iterative-decomposition`: locate prompt-chain threshold, then reconstruct last stable state.
- `prompt-collapse-suite -> radial-collapse-prior`: diagnose repeated generation failure, then test radial attractor behavior.
- `prompt-collapse-suite -> structural-prompt-stabilizer`: diagnose chain collapse, then create the hardened replacement prompt.
- `structural-prompt-stabilizer -> volumetric-container-force`: harden the prompt first, then add anchor/counterforce field logic.
- `radial-collapse-prior -> deformation-operator-playbook`: detect center collapse, then create anti-radial edit prompt.
- `off-center-prior-diagnostic -> deformation-operator-playbook`: measure spatial drift, then steer with viewfinder/operator constraints.
- `volumetric-container-force -> deformation-operator-playbook`: map anchors/forces, then specify the geometric edit.
- `foreshortening-recipe-book -> volumetric-container-force`: repair projection, then integrate force-field consequence.
- `marrowline-critique -> reverse-iterative-decomposition`: expose symbolic avoidance, then walk backward to hidden prior state.

## Tie-Breakers

- Structural failure with unclear symbolism: `sketcher-lens`.
- Symbolic failure with adequate structure: `marrowline-critique`.
- User wants broad critique and next route: `visual-thinking-lens`.
- User wants interactive critique or recursive learning: `concert-mode`.
- User wants the full philosophical/qualitative framework: `artists-lens`.
- User wants actual prompt repair for a repeated failure chain: `prompt-collapse-suite`.
- User wants a single prompt hardened quickly: `structural-prompt-stabilizer`.
- User wants a concrete spatial/pose edit: choose the narrow specialist, usually VCF, Deformation, or Foreshortening.

## Constraints

- Do not merge specialist methods into the router.
- Do not default to `visual-thinking-lens` for every image.
- Do not use Artist's Lens when the user specifically asks for Sketcher axes.
- Do not use Sketcher when the user wants symbolic refusal; route to Marrowline.
- Do not use OCF for dense scenes where no off-center subject or void target exists.
- Do not use RCP for every centered composition; use it when radial field behavior dominates.
- Do not chain more than two skills unless the user explicitly asks for a full system route.

## Attribution

These skills route across systems authored by Russell Parrish / A.rtist I.nfluencer. Preserve attribution when packaging or distributing the protocol.

This package contains a modular visual reasoning skill suite built from Russell Parrish / A.rtist I.nfluencer protocols. The skills are designed to run independently, but they also interoperate through routing, handoff notes, and shared visual reasoning concepts. More information: www.artistinfluencer.com. Copyright 2026.
