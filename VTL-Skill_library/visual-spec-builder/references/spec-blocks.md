# Spec Blocks

Use these blocks to turn visual intention into testable generation instructions.

## Intent

Purpose: define what the image should do beyond depicting a subject.

Ask:

- What pressure should the image carry?
- What should the viewer have to negotiate?
- What should be withheld?
- What is the consequence of the scene?

Template:

```text
Desired effect: [visible/interpretive effect]
Refusal: [default outcome to resist]
Primary consequence: [what must change in the image because of the intent]
```

## Anchors

Purpose: identify load-bearing elements.

Good anchors:

- figure posture
- hand/tool relation
- doorway/window/mirror
- object acting as witness
- void or empty area
- light source
- shadow boundary
- material edge
- foreground obstruction

Template:

```text
Anchor: [element]
Job: [what it must do structurally or symbolically]
Risk: [how it may become decorative]
```

## Invariants

Purpose: protect what must survive revision.

Use invariants for:

- camera angle
- spatial topology
- figure count
- one clear overlap
- exact relationship between two elements
- light direction
- material thickness
- unresolved ambiguity
- no change to subject identity

Template:

```text
Must preserve: [condition]
Why: [reason]
Failure if: [visible violation]
```

## Transformations

Purpose: state what changes from the base.

Useful transformation verbs:

- shift
- compress
- obstruct
- split
- delay
- invert
- thicken
- reduce
- misalign
- reroute
- strip
- repeat
- fracture
- suspend

Template:

```text
Transform [element] by [action] so that [visible consequence].
```

Examples:

- Transform the window light by making it miss the figure and strike the empty wall.
- Compress the room around the seated figure so the architecture carries pressure.
- Delay the gesture by freezing the hand before contact.

## Constraints

Purpose: make the generation obey field logic.

Constraint categories:

- `spatial`: placement, scale, depth, figure-ground, edge pressure.
- `light`: source, direction, contradiction, what is revealed or concealed.
- `material`: texture, opacity, residue, thickness, surface decision.
- `gesture`: pose, delay, resistance, incomplete action.
- `symbolic`: object relation, ambiguity, recursion, contradiction.
- `narrative`: what is known, withheld, contradicted, or implied.

Template:

```text
[Category] constraint: [specific visible rule].
```

## Negatives

Purpose: block default escape routes.

Good negatives:

- no centered harmony unless explicitly needed
- no decorative symbolism
- no clean mirror logic
- no sentimental light rescue
- no extra props that explain the scene
- no style quotation as substitute for structure
- no chaos without a visible cause
- no texture overlay that does not change form
- no fully resolved narrative

Template:

```text
Avoid [default] because it would [failure].
```

## Viewfinder

Purpose: specify the viewing conditions.

Controls:

- camera distance
- camera height
- angle
- crop
- foreground obstruction
- what is off-frame
- edge pressure
- depth relation
- viewer access

Template:

```text
Viewfinder: [camera/crop/angle]. The viewer can see [allowed information] but not [withheld information].
```

## Acceptance Checks

Purpose: create visible QA.

Good checks:

- "The mirror/reflection must not match the figure exactly."
- "The brightest light must land away from the subject."
- "The foreground obstruction must cover part of the main action."
- "The empty object must affect composition, not sit as a prop."
- "The material texture must change an edge or form."
- "One contradiction must remain unresolved."

Bad checks:

- "It should look deep."
- "Make it powerful."
- "It should feel artistic."
- "The composition should be better."

Template:

```text
Pass if: [visible condition].
Fail if: [default or violation].
```

## Generation Prompt Assembly

Assemble the final prompt in this order:

1. Medium and subject.
2. Anchors and spatial relation.
3. Transformations.
4. Light/material/gesture constraints.
5. Symbolic or narrative constraint.
6. Negatives.
7. Acceptance-oriented final sentence.

Template:

```text
[Medium/subject]. Place [anchors] in [spatial relation]. Transform [element] by [action] so [consequence]. Use [light/material/gesture constraints]. Let [symbolic/narrative pressure] remain unresolved. Avoid [negatives]. The result must visibly satisfy [acceptance check].
```

## Example

Loose intent:

```text
A painter in a studio, but make it less cozy and more psychologically tense.
```

Compiled spec:

```markdown
Intent:
- Desired effect: the studio should pressure the act of painting.
- Refusal: no cozy artist-at-work mood.
- Primary consequence: the room must interrupt the gesture.

Anchors:
- Painter's hand: delayed before contact with canvas.
- Second canvas: witness object, larger than expected.
- Window light: misses the subject and strikes the wall.

Invariants:
- Keep one painter, one main canvas, one secondary canvas.
- Preserve believable studio space.

Transformations:
- Compress the room around the figure.
- Shift light away from the expected focal point.
- Obstruct part of the painter through the foreground canvas.

Constraints:
- Spatial: foreground canvas must cover part of the figure.
- Light: warm/cold light sources must disagree.
- Gesture: brush hand is paused before contact.
- Symbolic: second canvas acts as witness, not decoration.

Negatives:
- No cozy glow.
- No extra art props explaining the theme.
- No centered harmony.

Acceptance Checks:
- Pass if the brightest light misses the painter.
- Pass if the second canvas changes the composition.
- Fail if the studio reads as warm, safe, and complete.
```

Generation prompt:

```text
An oil painting of a painter in a small studio. Place the painter, the main canvas, and a larger secondary canvas in a compressed triangular relation. The painter's brush hand pauses before touching the canvas, partly blocked by the foreground canvas. Window light misses the figure and strikes the back wall, while a colder side light cuts across the floor. The second canvas acts as a witness object, not a prop. Avoid cozy glow, decorative art supplies, centered harmony, and explanatory symbolism. The image must show the room interrupting the act of painting.
```
