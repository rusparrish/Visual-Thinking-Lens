---
name: teardown-mode
description: "Pressure-test image prompts, generated images, visual concepts, scenes, and creative directions through a standalone staged teardown: base, probe, yield, collapse echo, and suspended opposition. Use when a user wants to expose defaults, reveal what an image or prompt avoids, stress-test structural weakness, induce productive failure, diagnose over-resolution, or rebuild an idea through constraint, contradiction, rupture, and held tension without relying on any larger visual framework."
---

# Teardown Mode

Use this skill to test what a prompt, image, or visual concept can hold under pressure. Teardown is not improvement by polish. It is a staged diagnostic that reveals defaults, weak symbols, over-resolution, structural avoidance, and the point where failure becomes useful evidence.

Core rule: do not make the image better first. Make the idea answer harder visual conditions, but only escalate conditions when the current structure has been fully tested and remains insufficient.

## The Stages

Run the sequence as a loop, not a straight ladder. If a stage does not generate pressure, return to the base and alter the constraint.

1. `Base`: identify the default image or prompt.
   - What does it do easily?
   - What genre, mood, subject, or composition does it fall into?
   - What looks competent but untested?

2. `Probe`: add structured tension.
   - Introduce pressure through light, angle, occlusion, scale, contradiction, blocked view, misalignment, absence, or delayed gesture.
   - Goal: reveal whether the base contains internal constraint or only atmosphere.

3. `Yield`: push the strongest tension into a counter-response.
   - Do not fix the probe.
   - Redirect the pressure so the image must negotiate a different condition.
   - Goal: see whether tension becomes structure rather than decoration.

4. `Collapse Echo`: rupture the logic if the yield over-resolves or stays too polite.
   - Exaggerate contradiction, motif drift, recursive doubling, spatial refusal, broken narrative symmetry, or withheld coherence.
   - Goal: reveal what the prompt or image cannot hold.

5. `Suspended Opposition`: recombine the strongest stable contradiction.
   - Fuse competing pressures without letting them harmonize too cleanly.
   - Goal: hold ambiguity, delay, or paradox as a productive final state.

For detailed stage tactics and examples, read [references/stage-guide.md](references/stage-guide.md).

##Sufficiency

Before advancing stage, ask:
has the idea already:
- produced structural consequence?
- survived a meaningful constraint?

If yes: Do not escalate → test stability instead

This prevents: unnecessary collapse cycles

##Pressure Budget

Define:
- light → Base + Probe
- medium → + Yield
- heavy → full sequence

If exceeded: Over-pressured → diagnostic noise

##Exit

Each stage must answer: what would make this stage complete?

Example:
- Probe complete when:
- pressure changes scene logic

## Default Workflow

1. Ingest the prompt, image, or idea.
2. State the base default in one paragraph.
3. Name the first three likely failure modes.
4. Run the current stage requested by the user, or start at `Base` if unspecified.
5. Produce:
   - diagnosis
   - stage verdict
   - next pressure move
   - generation-ready prompt when useful
6. Stop only when the user asks for a final synthesis or when `Suspended Opposition` holds without immediate closure.

## Output Pattern

```markdown
**Stage**
- Current stage:
- Purpose:
- Verdict:

**Diagnosis**
- Default behavior:
- Pressure applied:
- What held:
- What collapsed or over-resolved:

**Next Move**
- Constraint to add:
- Element to remove:
- Contradiction to preserve:

**Prompt**
...
```

For a full teardown, use:

```markdown
**Base**
...

**Probe**
...

**Yield**
...

**Collapse Echo**
...

**Suspended Opposition**
...

**Final Read**
- What the idea avoids:
- What pressure revealed:
- Best next prompt:
```

## Pressure Tools

Use visible constraints, not vague intensity:

- contradictory light sources
- interrupted view or partial occlusion
- off-axis framing
- scale inconsistency with purpose
- delayed or frozen gesture
- object that acts as witness rather than prop
- void that blocks meaning rather than decorates
- mirror/reflection that contradicts instead of repeats
- architecture that compresses the subject
- material that records hesitation, residue, or revision
- symbol that changes spatial logic

## Failure Signals

Flag these directly:

- `polish mode`: the image becomes prettier instead of more consequential.
- `default closure`: ambiguity resolves into safe harmony.
- `prop symbolism`: objects label meaning but do not affect structure.
- `motif drift`: repeated symbols detach from the idea.
- `false rupture`: the image becomes chaotic without pressure logic.
- `overcorrection`: the image obeys the constraint too literally.
- `collapse`: the prompt cannot negotiate the contradiction.
- `productive fracture`: failure reveals the next useful pressure point.

## Guardrails

**False Yield**
If:
image becomes:
- more cinematic
- more dramatic

…but: no structural shift
- Aesthetic Yield → not structural

**Controlled Rupture**
If Collapse Echo:
- removes all legibility
- Chaos → rebuild, not continue

**Contradiction Map**
Track:
- which contradictions are active
- which collapse
- which survive

**Opposition Strength**
Ask:
are both pressures:
- equally strong?

If not: Imbalance → one dominates → collapse risk

**Return Rules**
If:
- Probe fails → modify Base
- Yield fails → return to Probe
- Collapse fails → rebuild from Yield

**Motif Check**
At each stage:
what motifs:
- persist?
- drift?
- collapse?

**Lie Check**
If: symbol appears
Ask: does it carry load?
If not: Prop Symbolism → remove

**Load Check**
Ask:
is load:
- meaningful?
- decorative?

**Plateau Check**
If: same result across stages
Plateau → switch route, not increase pressure

**Traversal**
Ask:
did stages move: between attractors?
If not: Static Teardown → no field navigation

**Final Types**
- viable structure
- productive failure
- exhausted idea
- decorative system

**General Guardrails**

- Do not rely on named internal roles, hidden engines, or framework-specific language.
- Do not score beauty.
- Do not make darkness, clutter, distortion, or surrealism stand in for depth.
- Do not treat every failure as success. A useful failure reveals a specific next move.
- Keep prompts visually executable: name what should appear, where pressure enters, and what must remain unresolved.

This package contains a modular visual reasoning skill suite built from Russell Parrish / A.rtist I.nfluencer protocols. The skills are designed to run independently, but they also interoperate through routing, handoff notes, and shared visual reasoning concepts. More information: www.artistinfluencer.com. Copyright 2026.
