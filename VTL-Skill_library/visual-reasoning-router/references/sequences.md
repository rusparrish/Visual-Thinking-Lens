# Sequence Patterns

Use a sequence only when one skill diagnoses and another skill performs a distinct next action. Prefer one skill for simple requests.

## Core Framework Routes

```text
concert-mode -> sketcher-lens
```

Use when an interactive session starts with user participation and needs structural grounding.

```text
concert-mode -> prompt-collapse-suite
```

Use when Dialogues mode reveals a prompt or generation chain loop.

```text
concert-mode -> reverse-iterative-decomposition
```

Use when Dialogues mode needs a counter-image, prior-state reconstruction, or collapse ancestry.

```text
sketcher-lens -> artists-lens
```

Use when a request needs structural axis diagnosis first, then richer qualitative intent/tension language.

```text
visual-thinking-lens -> marrowline-critique
```

Use when a broad recursive critique should escalate into symbolic refusal.

```text
sketcher-lens -> visual-thinking-lens
```

Use when structural axis failure needs broader Delta/Omega/Hold routing.

## Prompt Chain Routes

```text
prompt-collapse-suite -> reverse-iterative-decomposition
```

Use when a prompt or generation chain collapsed and the user needs the last stable state reconstructed.

```text
prompt-collapse-suite -> marrowline-critique
```

Use when repeated prompt failure is caused by hollow symbols, recurring icons, or referential drift.

```text
prompt-collapse-suite -> radial-collapse-prior
```

Use when repeated outputs keep becoming centered, haloed, target-like, or emblematic.

```text
prompt-collapse-suite -> structural-prompt-stabilizer
```

Use when a prompt chain has been diagnosed and the next artifact should be a hardened replacement prompt.

```text
structural-prompt-stabilizer
```

Use alone when the user has one prompt and wants it made more stable before generation.

## Spatial Repair Routes

```text
sketcher-lens -> volumetric-container-force
```

Use when weak axes involve Spatial Pressure, Frame Tension, Gesture Weight, Distributed Pressure Field, or Compositional Gravity.

```text
volumetric-container-force -> deformation-operator-playbook
```

Use when force mapping is clear and the user needs an edit/inpaint/operator prompt.

```text
structural-prompt-stabilizer -> volumetric-container-force
```

Use when a prompt first needs anti-collapse operators, then richer anchors, counterforces, and pressure zones.

```text
foreshortening-recipe-book -> volumetric-container-force
```

Use when near/far projection must be repaired and then integrated into a larger pressure field.

```text
radial-collapse-prior -> deformation-operator-playbook
```

Use when center-lock or halo structure needs a concrete anti-radial edit.

```text
off-center-prior-diagnostic -> deformation-operator-playbook
```

Use when a model's placement bias needs to be measured and then corrected with viewfinder/operator constraints.

## Process and Refusal Routes

```text
marrowline-critique -> reverse-iterative-decomposition
```

Use when symbolic refusal exposes a hidden prior state, avoided premise, or ghost-stage.

```text
artists-lens -> reverse-iterative-decomposition
```

Use when qualitative critique identifies construction history as the next useful artifact.

```text
sketcher-lens -> reverse-iterative-decomposition
```

Use when structural axes collapse and the user needs a block-in, underdrawing, or material regression.

## Research Stack

Use only for explicit research, benchmark, or system-audit requests:

```text
prompt-collapse-suite
-> sketcher-lens
-> radial-collapse-prior or off-center-prior-diagnostic
-> deformation-operator-playbook
-> visual-thinking-lens
```

Purpose:

1. Diagnose prompt-chain behavior.
2. Identify structural axis failure.
3. Test the relevant spatial prior.
4. Create controlled intervention.
5. Critique whether the intervention worked.

Avoid this stack for casual critique or simple prompt repair.
