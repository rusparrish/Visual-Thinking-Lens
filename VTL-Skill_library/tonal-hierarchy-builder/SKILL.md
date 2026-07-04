---
name: tonal-hierarchy-builder
description: "Diagnose and build tonal hierarchy before expressive markmaking, engraving, drawing, painterly, or black-and-white image critique. Use when an image, image prompt, iteration sequence, or visual concept needs a value backbone: grayscale survival, silhouette/block-value readability, figure-field-focus priority, reserved whites, crushed blacks, midtone restraint, selective visibility, suppression zones, light-path logic, or a readiness check before asking for varied marks or surface style."
---

# Tonal Hierarchy Builder

## Overview

Use this skill to decide whether an image has enough tonal structure to support expressive surface behavior. Treat markmaking as downstream: if the tonal hierarchy is weak, varied marks become noise, global texture, or decorative style.

Core principle: **expressive markmaking begins before the mark is made, but tonal hierarchy must also reinforce spatial and compositional structure, not just value separation. It begins in the silent architecture of tone.**

## Operating Rule

Do not start by asking for richer texture, more crosshatching, painterly finish, woodcut style, engraving style, or expressive marks. First establish:

- what carries light
- what carries mass
- what disappears
- what stays unresolved
- what receives the sharpest contrast
- what must be sacrificed so the focal structure can win

Use the phrase `not ready for expressive markmaking` when the value structure cannot yet hold surface variation.

## Tonal Priority Checks

**Structure Check**
Ask:
does tonal hierarchy:
- reinforce composition?
- or compensate for weak composition?

If compensating: Tonal Compensation → hierarchy present, structure weak

**Light Path**

Ask:
does the eye:
- move intentionally?
- or jump between contrasts?

If jumping: Broken Light Path → hierarchy not guiding perception

**Mass Integrity**

Ask:
do masses:
- hold together?
- or fragment into value noise?

If fragmented: Value Fragmentation → silhouette passed, cohesion failed

**Contrast Roles**
Classify:
- focal contrast
- separating contrast
- atmospheric contrast

If all are equal: Flat Contrast Hierarchy → everything competes

**Void Type**
- active → directs attention
- passive → empty space

If passive: Dead Void → no structural contribution

**Midtone Pressure**
Ask:
are midtones:
- carrying structure?
- or flattening everything?

If flattening: Midtone Collapse → hierarchy diluted

**Edge Budget**
Ask:
are hard edges:
- reserved?
- or overused?

If overused: Edge Inflation → no hierarchy reinforcement

**Focal Protection**
Ask:
is the focal area:
- protected by suppression around it?

If not: Unprotected Focus → contrast wasted

**Visibility Gradient**
Track:
- fully visible
- partially visible
- implied
- erased

If only first two: Weak Visibility Hierarchy

**Over-Control**
If:
everything is:
- too clean
- too separated
- Over-Structured → loss of ambiguity and tension

**Leak**
Ask:
are marks:
- already being implied before hierarchy is stable?
If yes: Premature Markmaking → violating core rule

## Workflow

1. **Name the intended hierarchy.**
   - Identify the primary focus, secondary support, background field, suppressed zones, and visual rest areas.
   - If the prompt treats every subject or prop as equally important, call that out.

2. **Run survival tests.**
   - `grayscale`: Would the image still read without color or style?
   - `silhouette`: Would the major masses still read if reduced to dark/light shapes?
   - `block-value`: Would the image still work as 3-5 value zones?
   - `thumbnail`: Would the focus survive at small size?

3. **Map tonal roles.**
   - `reserved white`: untouched or near-white area that creates force, not empty decoration.
   - `crushed black`: committed dark mass with little or no interior detail.
   - `midtone bridge`: controlled value band that carries atmosphere without flattening the image.
   - `void/rest`: withheld area that lets the eye pause.
   - `edge cut`: hard tonal contrast that separates structure.
   - `soft loss`: edge or form intentionally absorbed into the field.

4. **Assign selective visibility.**
   - Decide what is fully visible, partially visible, implied, buried, or erased.
   - Do not reward universal visibility. In strong images, some things win because other things submit.

5. **Check markmaking readiness.**
   - Marks are ready to vary only after tone gives them a job.
   - If material marks are being requested too early, repair the tonal structure first.

6. **Prescribe repair moves.**
   - Give concrete changes to values, edges, suppression, focus, and light path.
   - Keep style requests secondary to structural instructions.

## Diagnostic Signals

### Strong Tonal Hierarchy

- One dominant light path or value route guides the eye.
- At least one zone is allowed to disappear or remain unresolved.
- The image has committed darks and meaningful whites, not only safe midtones.
- Focal elements are protected by contrast, spacing, edge discipline, or suppression around them.
- Detail is distributed by importance, not by object count.
- Background supports the figure or field instead of narrating equally.
- Mark variation has a reason to exist: material, pressure, direction, weight, or symbolic function.

### Weak Tonal Hierarchy

- Everything sits in a narrow midtone band.
- The image depends on color, texture, or subject recognition to read.
- Every object receives equal clarity.
- The prompt asks for more style instead of more structure.
- Shadows are soft, polite, or over-described instead of weight-bearing.
- Whites are highlights only, not compositional force.
- Background props compete with the intended subject.
- Markmaking is globally applied as a texture pass.

## Scoring

Score out of 12:

- `+2` Focus survives grayscale or black-and-white reduction.
- `+2` Major masses survive silhouette or block-value reduction.
- `+2` There is a clear reserved white, crushed black, or equivalent value anchor.
- `+2` Selective visibility is active: some elements are suppressed, buried, or withheld.
- `+1` Midtones create atmosphere without flattening the composition.
- `+1` Edges vary by structural need: cut, soften, merge, or disappear.
- `+1` Background supports the hierarchy instead of competing.
- `+1` Markmaking or surface behavior has a tonal reason to vary.

Interpretation:

- `10-12`: ready for expressive markmaking
- `8-9`: mostly ready; repair one hierarchy weakness first
- `6-7`: structurally promising but not ready for complex marks
- `4-5`: tonal structure is weak; rebuild value map
- `0-3`: image is style-led or subject-led with no usable tonal backbone

## Repair Moves

Use these moves when the hierarchy is weak:

- **Choose one winner.** Pick the element or mass that gets primary contrast.
- **Crush one zone.** Turn one area into committed shadow with little or no interior detail.
- **Reserve one white.** Let one area remain near-paper-white or near-light, not merely highlighted.
- **Suppress one distraction.** Bury a prop, face, object cluster, or background detail into tone.
- **Open a void.** Leave one area quiet enough to delay resolution.
- **Build a light path.** Connect value accents in a route: floor to figure, hand to face, object to void, or shadow to focal glow.
- **Break democratic detail.** Reduce equal treatment across faces, props, architecture, and texture.
- **Delay identity.** Let a figure remain mass, glow, posture, or pressure before becoming portrait or symbol.

## Prompt Conversion

When converting critique into a generation prompt, prefer structural directives:

```text
Build the image from tonal hierarchy first. Establish one dominant light path, one crushed shadow mass, one reserved white, and one suppressed zone. Let the focal element win through contrast while surrounding details submit into midtone or shadow. Keep markmaking secondary until the value structure holds.
```

For engraving, etching, charcoal, ink, or woodcut prompts:

```text
Do not apply a uniform hatch texture. First separate the image into committed blacks, reserved whites, controlled midtones, and breathing voids. Let marks vary only where the tonal structure gives them a job: edge cutting, form pressure, material resistance, or atmospheric loss.
```

## Output Pattern

```markdown
**Tonal Hierarchy**
- Verdict:
- Score:
- Markmaking readiness:
- Primary focus:
- Supporting field:
- Suppressed zones:

**Survival Tests**
- Grayscale:
- Silhouette:
- Block-value:
- Thumbnail:

**Value Map**
- Reserved white:
- Crushed black:
- Midtone bridge:
- Void/rest:
- Light path:
- Edge logic:

**Failure Signals**
- Midtone flattening:
- Universal visibility:
- Background competition:
- Texture-before-tone:

**Repair**
- Preserve:
- Crush:
- Reserve:
- Suppress:
- Delay:
- Next prompt move:
```

## Guardrails

**Prompt Risk**
If prompt contains:
- “detailed”
- “textured”
- “rich”

without tonal instruction: Style-First Prompt → hierarchy likely weak

**Score Guard**
If:
- score high
- but composition weak
- High Score ≠ Strong Image

**General Guardrails**

- Do not treat beauty, polish, detail, or historical style as proof of tonal hierarchy.
- Do not call an image ready for expressive markmaking if all zones remain equally visible.
- Do not solve weak hierarchy by adding more texture.
- Do not confuse high contrast with hierarchy; contrast must assign roles.
- Do not punish ambiguity when it is structurally assigned.
- Keep this skill independent. Do not require VTL terminology, metrics, or any other skill to use it.

This package contains a modular visual reasoning skill suite built from Russell Parrish / A.rtist I.nfluencer protocols. The skills are designed to run independently, but they also interoperate through routing, handoff notes, and shared visual reasoning concepts. More information: www.artistinfluencer.com. Copyright 2026.
