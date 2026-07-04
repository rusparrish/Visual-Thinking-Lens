---
name: mark-stratification-diagnostic
description: "Diagnose whether markmaking, hatching, linework, surface texture, brushwork, engraving marks, drawing marks, or painterly strokes are structurally stratified instead of globally applied. Use when an image or prompt needs material-specific mark vocabularies, varied stroke roles, surface resistance, directional friction, edge discipline, pressure changes, or a critique of uniform texture, decorative hatching, global style passes, and marks that do not carry tonal, spatial, or material consequence."
---

# Mark Stratification Diagnostic

## Overview

Use this skill to decide whether marks are doing different jobs across an image. It detects the common AI failure where every surface receives the same hatch, stroke, grain, brush rhythm, or texture density.

Core principle: **marks must stratify by role. If wood, cloth, flesh, metal, shadow, air, and architecture all receive the same mark logic, the image is wearing style rather than being drawn.**

## Distinction

This skill is not a general beauty critique and does not require any external visual theory. It asks:

- Are marks assigned by material, pressure, edge, direction, and visual role?
- Or are marks globally distributed as a style filter?

Use tonal hierarchy first when the value structure is obviously weak. Use this skill when the main question is whether the surface behavior has enough internal differentiation.

## Workflow

1. **Inventory mark zones.**
   - Name the visible zones: figure, face, clothing, hair, wood, metal, wall, floor, sky, shadow, void, atmosphere, architecture, object cluster.
   - Note whether each zone has a distinct mark vocabulary or shares the same one.

2. **Classify mark roles.**
   - `material`: marks describe surface identity.
   - `volume`: marks model form or weight.
   - `edge`: marks cut, soften, merge, or break boundaries.
   - `pressure`: marks show force, drag, density, tool load, or resistance.
   - `direction`: marks guide the eye or oppose another plane.
   - `atmosphere`: marks dissolve or delay recognition.
   - `suppression`: marks bury detail or erase identity.
   - `anomaly`: one controlled mark event breaks the system and adds authorship.

3. **Detect global-pass texture.**
   - Look for repeated hatch angle, line length, stroke density, brush size, grain, edge softness, and rhythm across unrelated materials.
   - If the same mark can move from face to wood to fabric to shadow without changing function, call it `global-pass texture`.

4. **Check material stratification.**
   - Each major material should have a different mark behavior or a clear reason for sharing one.
   - Do not require realism; require consequence. A face can be erased, wood can become atmospheric, and cloth can become mass if the hierarchy supports it.

5. **Check surface resistance.**
   - Marks should sometimes drag, skip, rupture, thicken, thin, collide, or fail.
   - If marks glide evenly over the image, diagnose `frictionless surface`.

6. **Prescribe stratification moves.**
   - Assign specific mark changes by zone and role.
   - Avoid vague fixes like "add more detail" or "make it more expressive."

## Diagnostic Families

| Family | Meaning |
|---|---|
| `global-pass-texture` | A uniform mark layer covers unrelated surfaces. |
| `material-sameness` | Wood, cloth, flesh, metal, shadow, or atmosphere share the same mark behavior. |
| `obedient-volume-hatching` | Marks only shade form and never argue with it. |
| `directional-monotony` | Hatch/stroke direction repeats across planes. |
| `edge-politeness` | Boundaries are consistently soft, clean, or over-resolved. |
| `pressureless-surface` | No drag, rupture, skip, density shift, or tool resistance appears. |
| `decorative-density` | Marks add busyness without changing hierarchy or material identity. |
| `detail-democracy` | Every area receives similar attention, weight, and finish. |
| `surface-mask` | The image looks styled but the marks do not affect structure. |
| `authorship-gap` | No controlled anomaly, interruption, or selective break gives the marks agency. |

## Material Vocabulary Prompts

Use these as repair levers, not as universal rules:

- `wood`: long grain cuts, broken structural lines, directional drag, splintered edge interruptions.
- `cloth`: clustered softness, fold-pressure bands, loose fiber drift, occasional collapse into shadow.
- `flesh`: restrained marks, soft value turns, selective loss, minimal facial closure unless portrait identity matters.
- `hair`: directional clusters, broken strand masses, density shifts near light.
- `metal`: hard bright cuts, small dark accents, sparse reflection logic, no woolly texture.
- `shadow`: compressed density, detail burial, edge loss, overhatch suppression.
- `architecture`: straighter load-bearing marks, joinery emphasis, plane distinction.
- `floor/ground`: directional pull, perspective pressure, scuffs or grain that guide the eye.
- `air/atmosphere`: sparse drift, broken marks, low object specificity.
- `void`: no mark or nearly no mark; let withholding carry force.

## Scoring

Score out of 12:

- `+2` Major materials or zones have distinct mark vocabularies.
- `+2` Marks vary by role: material, volume, edge, pressure, direction, atmosphere, or suppression.
- `+2` Stroke direction changes across planes or creates meaningful opposition.
- `+2` Surface resistance is visible: drag, rupture, skip, density shift, or pressure change.
- `+1` Edges vary: cut, soften, merge, disappear, or break.
- `+1` Mark density follows hierarchy instead of being evenly distributed.
- `+1` At least one area is withheld rather than filled.
- `+1` A controlled anomaly or interruption prevents mechanical sameness.

Interpretation:

- `10-12`: strongly stratified mark system
- `8-9`: good stratification with one weak zone
- `6-7`: partial stratification; global texture still visible
- `4-5`: mostly global-pass marks
- `0-3`: decorative surface mask; marks do not carry structure

## Repair Moves

- **Split material vocabularies.** Assign wood, cloth, flesh, metal, shadow, and air different mark behaviors.
- **Break the dominant angle.** Add contra-directional marks where planes meet or conflict.
- **Vary mark scale.** Use fine marks for one zone, broad bands for another, sparse marks for another.
- **Change edge contracts.** Cut one edge hard, dissolve one edge, bury one edge, and interrupt one edge.
- **Add pressure gradients.** Let marks thicken, thin, drag, skip, or compress as force changes.
- **Suppress a zone.** Replace detail with density, shadow, or quiet.
- **Withhold a zone.** Let blankness or low-mark areas carry structure.
- **Introduce one anomaly.** Add one controlled rupture, swirl, double mark, overdarkened patch, or broken contour that reveals authorship.

## Prompt Conversion

Use structural mark instructions:

```text
Do not apply one uniform texture pass. Stratify the marks by material and role: wood carries broken directional grain, cloth carries clustered fold pressure, flesh is minimally marked and selectively lost, metal uses sparse hard cuts, shadows compress into dense overhatch, and air remains mostly withheld.
```

For expressive engraving, etching, drawing, charcoal, or ink:

```text
Break the mark discipline across zones. Let one plane use contra-directional hatching, one edge dissolve into shadow, one object cut sharply with sparse marks, and one background area become nearly blank. Marks should show pressure, drag, interruption, and selective refusal rather than evenly describing every surface.
```

## Output Pattern

```markdown
**Mark Stratification**
- Verdict:
- Score:
- Main failure family:
- Best-held mark zone:
- Weakest mark zone:

**Zone Inventory**
- Figure/flesh:
- Fabric/clothing:
- Wood/architecture:
- Metal/object:
- Shadow:
- Atmosphere/void:

**Mark Roles**
- Material:
- Volume:
- Edge:
- Pressure:
- Direction:
- Suppression:
- Anomaly:

**Failure Signals**
- Global-pass texture:
- Material sameness:
- Directional monotony:
- Edge politeness:
- Pressureless surface:

**Repair**
- Split:
- Break:
- Suppress:
- Withhold:
- Add anomaly:
- Revised prompt clause:
```

## Guardrails

- Do not reward busy texture as mark quality.
- Do not require every zone to be highly marked; withholding can be the strongest mark decision.
- Do not confuse material realism with mark stratification. The issue is whether marks have different jobs.
- Do not prescribe more detail when the failure is sameness.
- Do not force marks to obey volume everywhere; expressive marks may argue with form when the hierarchy supports it.
- Keep this skill independent. Do not require VTL terminology, metrics, tonal-hierarchy-builder, or any other skill to use it.

This package contains a modular visual reasoning skill suite built from Russell Parrish / A.rtist I.nfluencer protocols. The skills are designed to run independently, but they also interoperate through routing, handoff notes, and shared visual reasoning concepts. More information: www.artistinfluencer.com. Copyright 2026.
