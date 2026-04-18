---
name: off-center-basin
description: "Create, critique, and revise image prompts toward coherent off-center basins: displaced structural mass, peripheral gravity, asymmetry pulse, dislocation, active void, edge-weighted composition, undercharged center, tilted viewfinder, weighted negative space, and stabilizers that prevent collapse back to centered harmony or empty minimalism. Use when a user wants spatially aware prompt repair, non-centered composition, off-center mass placement, frame-edge gravity, basin-style composition, or rule-of-thirds-like displacement with stronger structural pressure."
---

# Off-Center Basin

Use this skill to move an image away from centered default composition while keeping it coherent. The target is not simply "put the subject on the side." The target is an off-center **mass basin**: a stable composition where structural weight, void, edge pressure, and counterforces keep the image from snapping back to the center.

Core rule: move visual mass, not just the named subject.

## Basin Targets

Use these as practical ranges when metrics are available:

- `gentle offset`: `delta_x` or `delta_y` around `0.08-0.12`
- `stable basin`: absolute offset around `0.12-0.20`
- `strong peripheral pull`: absolute offset around `0.20-0.32`
- `near-collapse edge`: beyond `0.32`, requires strong counterweight

Common stability envelope:

- `delta_x`: `0.10-0.22`
- `r_v`: `0.58-0.72`
- `rho_r`: `0.25-0.45` normalized, or `25-45` if notebook `rho_r` is scaled by 100

## Workflow

1. Identify current center gravity.
   - What is centered: subject, mass, light, contrast, gesture, or narrative attention?

2. Choose an off-center direction.
   - Left/right/top/bottom/quadrant/edge.
   - Name what moves and what stays behind as counterweight.

3. Undercharge the center.
   - Prevent the center from becoming the rescue point.
   - Keep it quieter, interrupted, blocked, or structurally secondary.

4. Activate the opposite field.
   - Use void, light gradient, trace, shadow, texture, horizon pressure, or displaced echo.

5. Add a stabilizer.
   - Diagonal, tonal spine, edge anchor, material grain, shadow path, secondary object, or repeated mark.

6. Add anti-collapse constraints.
   - No centered harmony.
   - No decorative empty space.
   - No subject-only offset with centered mass.

For off-center variants and prompt moves, read [references/off-center-patterns.md](references/off-center-patterns.md).

## Output Pattern

```markdown
**Off-Center Target**
- Direction:
- Structural mass:
- Center treatment:
- Opposite field:
- Stabilizer:

**Prompt**
...

**Failure Checks**
- Subject moved but mass stayed centered:
- Center rescue:
- Empty void:
- Edge collapse:
- Missing counterweight:

**Metric Correction** optional
- delta_x / delta_y:
- r_v:
- rho_r:
- x_p:
```

## Prompt Template

```text
[Medium/subject]. Shift the primary structural mass toward [direction/quadrant/edge], about [gentle/stable/strong] off-center. Keep the center undercharged through [quiet center/blocked center/low contrast/interrupted depth]. Let the opposite field carry [weighted void/light gradient/residual trace/counter-shape]. Add [stabilizer] so the frame holds without re-centering. Avoid centered harmony, decorative emptiness, and subject-only offset.
```

## Correction Rules

- If mass is too centered: shift contrast, edges, shadow, and texture, not only the subject.
- If the composition topples: add a counterweight in the opposite field.
- If the void is passive: give it trace, pressure, light, or obstruction.
- If the center rescues the image: lower central contrast or block the central path.
- If the edge becomes too heavy: add a faint interior stabilizer without returning to center.
- If the image becomes empty: increase rupture density or material trace.

## Guardrails

- Do not equate off-center with rule-of-thirds decoration.
- Do not move the subject while leaving light and contrast centered.
- Do not overfill the void.
- Do not let asymmetry become random clutter.
- Do not treat center placement as inherently bad; the goal is intentional displacement.
