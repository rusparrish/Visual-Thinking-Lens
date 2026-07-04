---
name: ghost-density-basin
description: "Create, critique, and revise image prompts toward the Ghost Density basin: off-center structural mass, wide but active negative space, fractured light, unresolved edges, half-present forms, residual traces, and cohesion without closure. Use when a user wants a haunted but compositionally stable image, ghost density, edge entropy vs saliency mismatch, one-sixth frame displacement, two-thirds weighted void, or metric-aware targeting around delta_x 0.12-0.20, r_v 0.62-0.68, and rho_r 0.28-0.40."
---

# Ghost Density Basin

Use this skill to move an image idea into the Ghost Density basin: a stable off-center field where the image gathers visual mass without fully resolving. The basin is not "make it spooky." It is a spatial recipe: displaced mass, weighted void, fractured continuity, and traces that remain underdetermined.

Core target:

- `delta_x`: `0.12-0.20` absolute mass-centroid offset, about one-sixth of the frame.
- `r_v`: `0.62-0.68`, roughly two-thirds void or gradient-quiet field.
- `rho_r`: `0.28-0.40` normalized rupture/packing density. If using notebook `rho_r` on a `0-100` scale, compare as `28-40`.

I. The Workflow: Mechanical Engineering
1. Identify Subject: Figure, interior, object, or landscape.
2. Displace Mass (delta_x): Shift the entire structural weight 1/6th frame left or right; keep the center undercharged.
3. Pressure the Void (r_v): Shape a 2/3rds band of negative space that "presses" through traces, light, or echoes.
4. Calibrate Rupture (rho_r): Use smudges, broken contours, or tonal seams to interrupt continuity without losing form.
5. Apply Stabilizer: Select one anchor from the Stabilizer Taxonomy to hold the field without recentering.

II. Stabilizer Taxonomy (Mechanical Anchors)
To prevent the image from dissolving into noise or collapsing to the center, select one:
1. Tonal Spine: A vertical or horizontal band of value that anchors the displaced mass.
2. Diagonal Brace: An angled edge (shadow, floor line, architecture) that crosses the void.
3. Material Grain: Consistent surface texture (charcoal grit, film grain, paper tooth) providing overall cohesion.
4. Shadow Path: A directional shadow that connects the subject to the edge of the frame.

III. Drift Recovery Protocol (Anti-Symmetry)
If the model drifts toward centered symmetry or decorative minimalism, apply these Negative Constraints:
1. Discard: centered subject, perfect symmetry, balanced weight, empty background.
2. Suppress: fog, haze, smoke (unless used as a textured rupture).
3. Command: "Undercharge the center. Move the centroid further off-axis."

IV. Output Pattern & Self-Critique
**Basin Mapping**
- **Subject:** [Target]
- **Mass Offset ($delta_x$):** [Target 0.12-0.20]
- **Void Pressure ($r_v$):** [Target 0.62-0.68]
- **Rupture Density ($rho_r$):** [Target 0.28-0.40]
- **Mechanical Stabilizer:** [Spine/Brace/Grain/Path]

Guardrails & Logic
1. Mass != Subject: Ensure the visual weight (shadows, furniture, secondary forms) moves with the subject.
2. Avoid Cliché: "Ghostly" comes from structural withholding, not ghosts or fog.
3. Breathable Density: Too much $rho_r$ (rupture) becomes clutter; too little becomes empty.

**Prompt**
[Medium/Subject]. [Displacement instruction]. [Void behavior]. [Rupture instruction]. [Stabilizer instruction]. No literal ghosts, no centered symmetry.

**Drift Check (Self-Critique)**
- **Center Collapse?** [Yes/No - if Yes, push mass further]
- **Empty Void?** [Yes/No - if Yes, add trace/light echo]
- **Ghost Trap?** [Yes/No - if Yes, remove spook tropes, return to structure]

## Basin Logic

Ghost Density holds when:

- The subject or dominant mass is displaced from center.
- The opposite void is broad but not empty.
- Edges are incomplete, fractured, softened, or overwritten.
- Forms feel half-present without dissolving into noise.
- Texture interrupts continuity without destroying cohesion.
- The center remains undercharged.
- The image feels haunted because structure withholds closure and because void and displacement carry pressure, not just absence. And **not because it adds literal ghosts.**

**Basin Validity**
Before accepting:
- is void active, not decorative?
- is displacement structural, not compositional trick?
- is rupture interrupting continuity, not texture fill?

If not: False Basin → metric match without structural behavior

**Void Activity**
Ask:
- does void:
- redirect gaze?
- carry trace, echo, or tension?
- influence composition?

If not: Inactive Void → collapse to minimalism

**Mass Alignment**

Check: do shadows, furniture, edges, secondary forms move with subject?

If not: Fake Offset → subject moved, mass stayed centered

**Rupture Quality**
- valid → breaks continuity, redirects structure
- weak → decorative texture
- overload → noise

If weak: Cosmetic Rupture → increase structural interruption

If overload: Rupture Flood → reduce density, restore hierarchy

**Stabilizer Test**
Remove stabilizer mentally:
- does the image collapse?

If no: Stabilizer Decorative → replace with structural anchor

**Ghost Trap**

Reject if:
- ghost = figure, silhouette, or trope
- atmosphere = fog/horror shorthand

**Cohesion Threshold**
- strong → structure holds under displacement
- weak → form dissolves into noise
- false → structure replaced by symmetry/default

If weak: Cohesion Failure → add spine/brace/path

**Drift Types**
- center drift → mass returns inward
- void drift → void becomes empty
- rupture drift → texture spreads everywhere
- stabilizer drift → anchor recenters composition

**Variant Routing**
Based on failure:
- too stable → use Fracture Basin
- too diffuse → use Residual Trace
- too literal → use Liminal Drift
- too quiet → use Echo-Void
- too flat → use Oblique Silence

This turns variants into: targeted correction tools, not style options

**False Stability**
If:
- image holds
- but:
  - centered tension remains
  - void inactive
  - rupture decorative
Stable but Invalid → push displacement or void activation

## Workflow

1. Identify the base subject.
   - Figure, still life, interior, object, landscape, abstract field, etc.

2. Displace structural mass.
   - Move the mass about one-sixth frame left or right.
   - Specify mass placement, not just subject placement.

3. Weight the void.
   - Use a broad negative-space band occupying about two-thirds of the frame.
   - The void should pull, press, echo, or contain traces.

4. Add rupture density.
   - Use fractured light, broken contours, smudges, underdrawing, blurred boundaries, erased edges, or texture seams.
   - Keep density moderate; too little becomes empty, too much becomes clutter.

5. Preserve cohesion without closure.
   - Add one stabilizer: tonal spine, diagonal, edge anchor, material grain, shadow path, or repeated trace.
   - Do not let the image become centered, literal, or fully explained.

For variants and prompt fragments, read [references/ghost-density-variants.md](references/ghost-density-variants.md).

## Output Pattern

```markdown
**Ghost Density Target**
- Subject:
- Mass offset:
- Void behavior:
- Rupture density:
- Stabilizer:

**Prompt**
...

**Failure Checks**
- Center collapse:
- Empty void:
- Literal ghost trap:
- Overpacked texture:
- Lost cohesion:

**Optional Metric Read**
- delta_x:
- r_v:
- rho_r:
- Correction:
```

## Prompt Template

```text
[Medium/subject]. Displace the primary structural mass about one-sixth of the frame [left/right], leaving the center undercharged. Let a broad band of negative space occupy nearly two-thirds of the composition, but make the void active through [trace/light/shadow/residue/echo]. Fracture continuity with [broken contours/smudges/tonal seams/unsettled light], keeping the form half-present and cohesive without closing. Avoid literal ghosts, centered symmetry, decorative emptiness, and fully resolved edges.
```

## Metric Correction Rules

- `delta_x` too low: push mass farther from center; remove central stabilizers.
- `delta_x` too high: add a faint counterweight so the field holds without recentering.
- `r_v` too low: open the frame, reduce filler, widen the quiet field.
- `r_v` too high: activate the void with traces, edge residue, fractured light, or ghost layering.
- `rho_r` too low: increase broken contour density, surface rupture, mark commitment, or visible seams.
- `rho_r` too high: thin texture, reduce scratch density, restore breathable void.

## Guardrails

- Do not make "ghost" literal unless the user asks.
- Do not fill the void with background detail.
- Do not confuse subject offset with mass offset.
- Do not over-darken the image as a shortcut.
- Do not let haze erase all structure; the basin needs density.
- Do not treat metrics as aesthetic scores. They locate the basin.

This package contains a modular visual reasoning skill suite built from Russell Parrish / A.rtist I.nfluencer protocols. The skills are designed to run independently, but they also interoperate through routing, handoff notes, and shared visual reasoning concepts. More information: www.artistinfluencer.com. Copyright 2026.
