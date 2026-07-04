# QA and Claim Boundaries

## QA Handling

`valid = 0`:

- Treat as invalid or very low confidence.
- Do not interpret the vector beyond noting what failed.

`mask_status = FAIL`:

- The mass mask is structurally unreliable.
- Do not make strong placement, packing, cohesion, or dispersion claims.

`mask_status = WARN`:

- The vector may still be useful.
- Foreground the likely reason: sparse structure, many components, texture-driven mask, or low-confidence mass field.

`mask_status = PASS`:

- The vector is usable under the device assumptions.
- Still do not treat values as quality judgments.

`mask_mode = REGION_FIELD`:

- More coherent connected mass.
- Better for object-like structural placement reads.

`mask_mode = TEXTURE_FIELD`:

- Fragmented or texture-driven structure.
- Better read as field activity, surface/edge behavior, or generative texture regime.

`mask_mode = INVALID`:

- Do not interpret except as failure/insufficient structure.

## Single-Image Boundary

Allowed:

- "This image is centered in kernel space."
- "The field is gradient-active."
- "The mask is texture-dominant."
- "The mass is broadly dispersed."

Blocked:

- "This image proves collapse."
- "This model has a prior."
- "The composition is bad/good."
- "The prompt failed."
- "The subject is important/unimportant."

## Batch Boundary

Allowed when comparable:

- "The batch has low placement variance."
- "The cohort clusters tightly in kernel space."
- "The model/condition explores a narrow structural range."

Requires caution:

- collapse,
- prior,
- monoculture,
- prompt-response failure.

These need adequate sample size, comparable preprocessing, and preferably semantic/prompt diversity context.

## r_v Boundary

Never report `r_v` as simple empty space without caveat.

Use:

```text
r_v is high, indicating a gradient-quiet field under the absolute threshold.
```

Avoid:

```text
The image has lots of compositional void.
```

Unless the visual context and gradient package support that more specific claim.

## Quality Boundary

Kernel values do not mean:

- correct,
- incorrect,
- good,
- bad,
- authored,
- unauthored,
- beautiful,
- ugly.

They locate observable structure before any downstream judgment.
