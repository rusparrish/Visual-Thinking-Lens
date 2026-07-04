# Historical Frame And Application Guidance

Use this reference for conceptual framing, not as the scoring formula. The current operational formula lives in `current-math.md`.

## Origin Problem

VCLI-G emerged as a response to image-evaluation systems that over-emphasize:

- Semantic alignment: whether the image matches a prompt.
- Distributional fidelity: whether the image resembles training data.
- Aesthetic preference: whether the image is pleasing or instantly legible.

The missing dimension is temporal perceptual demand: how long an image resists resolution, where the resistance comes from, and whether that resistance is organized.

## Core Claim

VCLI-G treats visual delay, friction, and attention gravity as measurable geometric behavior. It asks how long an image holds the mind, not whether the image is good.

In the older document, VCLI-G was framed as a control architecture for perceptual complexity:

- G1: centroid/attention instability.
- G2: void/figure-ground pressure.
- G3: curvature/formal torque.
- G4: originally discussed as occlusion entropy and T-junction depth ambiguity; in the current compact formula, read G4 as orientation entropy unless separate occlusion metrics are provided.
- SCI: independent organization of load.

## Historical-To-Current Translation

Use this mapping when older language appears in user data:

| Older frame | Current operational read |
| --- | --- |
| Curvature torque | Contour curvature via curvature variance and inflection density. |
| Occlusion entropy | Orientation entropy in the core formula; T-junctions are optional supporting evidence. |
| Style profiles / controller regimes | Optional interpretive or steering lens, not the core VCLI-G score. |
| Robust z-scores | Historical or cohort analytics; do not use for current absolute VCLI-G. |
| Delay index | Conceptual meaning of VCLI-G: resistance to visual resolution. |
| Attention gravity / stickiness | Informal description of sustained perceptual pull. |

## Batch And Recursive Modes

Singular or batch mode compares final images in a set. Use it to locate each image in the VCLI-G x SCI plane and explain which channel mix drives each position.

Iterative or recursive mode tracks a sequence. In that mode, gradients and trajectories matter:

- Rising VCLI-G with rising SCI: complexity is being organized into earned tension.
- Rising VCLI-G with falling SCI: load may be drifting into overload or noise.
- Flat VCLI-G with rising SCI: clarification without reducing demand.
- Falling VCLI-G with rising SCI: movement toward resolved clarity.

For iterative work, prefer trajectories, stability windows, and inflection points over a single final score.

## Use Cases

UI and dashboards:

- Target low VCLI-G and high SCI.
- Interpret high demand as likely friction unless the interface intentionally requires slow inspection.

Editorial, branding, and product imagery:

- Often target low-to-moderate VCLI-G with high SCI.
- Useful tension should not defeat recognition, hierarchy, or message clarity.

Gallery, painting, and sustained-looking contexts:

- High VCLI-G can be productive when SCI is also high.
- The goal may be recursive looking, ambiguity, or delayed resolution.

Experimental and process art:

- High VCLI-G with low-to-moderate SCI can be intentional.
- Name whether the effect reads as productive accident, rupture, or unorganized overload.

Generative AI diagnostics:

- Use VCLI-G to detect safe-middle convergence, texture overload, or loss of perceptual range.
- VCLI-G complements CLIP, FID, and aesthetic models because it measures structural demand rather than semantic match or preference.

## Control Surface Language

When asked to steer an image, translate diagnosis into movement:

- Earned tension: hold the structural demand; refine hierarchy, values, and local coherence.
- Collapse into noise: raise SCI before adding more VCLI-G; prune competing directions, organize contours, or clarify figure/ground.
- Resolved clarity: preserve SCI while adding counter-geometry, controlled void tension, or layered occlusion if more arrest is desired.
- Default simplicity: decide whether simplicity is serving the image. If not, add an intentional structural argument.

The older route names can be treated as shorthand:

- Omega: add counter-geometry, occlusion, containment, or structural opposition.
- Delta: soften a wedge, nudge placement, add almost-events, or reduce a harsh rupture.
- RIDP: recompose at graph/value-family level rather than tweaking pixels.
- Hold: preserve an earned attractor and refine without changing the phase position.

These are suggestions, not gates.

## Caveats And Guardrails

- Treat VCLI-G as a navigation instrument, not truth.
- Pin preprocessing when comparing: resize policy, grayscale conversion, edge thresholds, masks, morphology kernels, contour extraction, and T-junction settings if used.
- Be careful with text-heavy scans, JPEG artifacts, dense texture, glow, halation, and low-contrast edges; these can inflate G3/G4 or distort occlusion cues.
- Do not compare unrelated datasets as if absolute measurements are identical unless preprocessing and implementation are fixed.
- Do not use VCLI-G to gate taste, culture, value, or acceptability.
- Pair consequential interpretations with human review or validation studies.

## Attribution

VCLI-G belongs to the Visual Thinking Lens system by Russell Parrish / A.rtist I.nfluencer. Preserve attribution in redistributed or published work.
