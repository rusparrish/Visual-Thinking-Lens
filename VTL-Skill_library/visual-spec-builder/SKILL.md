---
name: visual-spec-builder
description: "Convert fuzzy image ideas, prompts, critiques, and creative direction into standalone visual specifications with intent, anchors, selections, invariants, transformations, constraints, negatives, viewfinder instructions, material rules, failure checks, and acceptance criteria. Use when a user wants a structured prompt, prompt repair, engine-agnostic visual spec, constraint stack, visual QA checklist, or a way to compile artistic intention into testable generation instructions without relying on any larger visual framework."
---

# Visual Spec Builder

Use this skill to compile loose visual intention into a structured specification that a generative image model or human collaborator can follow and verify. The deliverable is not a poetic description. It is a compact operating spec: what must be present, what may change, what must not happen, and how the result will be judged.

Core rule: every important phrase must become either an anchor, constraint, transformation, negative, or acceptance check.

## Workflow

1. Extract intent.
   - What should the image do?
   - What should it refuse?
   - What visual consequence matters most?

2. Define anchors.
   - Name 2-5 load-bearing elements: figure, object, void, light source, architecture, gesture, material, symbol, or frame.
   - Each anchor must have a job.

3. Define invariants.
   - What must survive every revision?
   - Use invariants for camera, topology, composition, relation, gesture, lighting logic, material behavior, or symbolic pressure.

4. Define transformations.
   - What should change from the current/base idea?
   - Transform structure before style: shift, compress, obstruct, split, delay, invert, thicken, reduce, misalign, or reroute.

5. Define constraints and negatives.
   - Constraints tell the image how to behave.
   - Negatives prevent default escape routes.

6. Define the viewfinder.
   - Camera, crop, angle, distance, occlusion, foreground/background relation, edge pressure, and what the viewer is allowed to see.

7. Define acceptance checks.
   - Use visible criteria that can be confirmed in the output.
   - Avoid subjective checks like "looks powerful" unless tied to a visible condition.

For block definitions and examples, read [references/spec-blocks.md](references/spec-blocks.md).

## Output Pattern

```markdown
**Intent**
- Desired effect:
- Refusal:
- Primary consequence:

**Anchors**
- Anchor 1:
- Anchor 2:
- Anchor 3:

**Invariants**
- Must preserve:
- Must not alter:

**Transformations**
- Change:
- Pressure:
- Delay or rupture:

**Constraints**
- Spatial:
- Light:
- Material:
- Symbolic:

**Negatives**
- Avoid:
- No:

**Viewfinder**
- Camera:
- Crop:
- Occlusion:
- Edge/void behavior:

**Acceptance Checks**
- Check 1:
- Check 2:
- Check 3:

**Generation Prompt**
...
```

## Prompt Compilation Rules

- Convert adjectives into visible duties.
  - Weak: "haunting."
  - Strong: "the mirror shows a delayed posture that the figure does not match."

- Convert style into behavior.
  - Weak: "surreal."
  - Strong: "architecture remains believable, but the corridor depth contradicts the room scale."

- Convert symbols into structural jobs.
  - Weak: "a symbolic empty chair."
  - Strong: "the empty chair blocks the figure's path and receives the brightest light."

- Convert quality goals into acceptance checks.
  - Weak: "make it more tense."
  - Strong: "at least one light source must contradict the subject's gesture."

## Spec Quality Bar

A good visual spec should be:

- specific enough to verify
- flexible enough to generate
- resistant to default beauty
- clear about what may not change
- clear about what must remain unresolved
- portable across engines and image-makers

If the final prompt reads like mood description, recompile it into anchors, constraints, and checks.

## Guardrails

**Alignment**
Ask:
do all blocks: reinforce the same pressure?

If not: Conflicting Constraints → internal cancellation

**Primary Pressure**
Primary pressure: [what dominates the image]

If missing: Diffuse Spec → weak output

**Anchor Priority**
- primary (must dominate)
- secondary (support)
- tertiary (optional)

If all equal: Flat Anchor System → no hierarchy

**Transformation Alignment**
Ask:
do transformations: point in the same direction?

If not: Multi-directional Drift → weak consequence

**Constraint Priority**
- must
- should
- optional

If all “must”: Overconstrained → model collapse risk

**Escape Check**
Ask:
what default behaviors: are still unblocked?

If any: Open Escape Route

**Failure Modes**
- anchor failure
- invariant violation
- constraint conflict
- negative escape
- acceptance miss

This package contains a modular visual reasoning skill suite built from Russell Parrish / A.rtist I.nfluencer protocols. The skills are designed to run independently, but they also interoperate through routing, handoff notes, and shared visual reasoning concepts. More information: www.artistinfluencer.com. Copyright 2026.
