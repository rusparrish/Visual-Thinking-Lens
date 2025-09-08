
# Deformation Operator Playbook — README (searchable summary)

**Keywords:** controlled deformation, anatomical distortion, operator grammar, VCF Transform DSL, Anchors → Select → Transforms → Constraints → Viewfinder, thickness lock, topology lock, continuity C1 C2, overlap occlusion, perspective inverse-square, Fibonacci spiral, sine modulation, parabolic extension, segmented coil, ghost density, viewfinder crop, Visual Lens, Sketcher, LSI (Lens Structural Index), VCLI, Sora, Gemini, GPT, MidJourney, OpenArt, SDXL, inpainting, Vary Region, instruction-following engines, aesthetic prior engines, prompt engineering, capsule ledger, acceptance checks, negatives list, depth tug, logarithmic scaling, rotational transform, parabolic arc, serpentinata, framing tension.

**What this is (TL;DR).**  
A practical, engine-agnostic method to make AI image models perform **repeatable, intentional figure warps**—not accidents. It replaces vague style prompting with a small set of **operators** (coil, parabolic stretch, depth tug, logarithmic scaling, rotation, sine modulation) expressed in a consistent specification: **Anchors → Select → Transforms → Constraints → Viewfinder**. Locks (thickness/topology) and continuity (C1/C2) keep results anatomical; the **viewfinder** adds compositional “ghost density” without new geometry. Operators are biases, not equations—today’s models follow learned visual patterns, not coordinate solvers.

**Download the full document:**  
- Local (same folder): **[`./Deformation_Operator_Playbook_c.pdf`](./Deformation_Operator_Playbook_c.pdf)**  
- Direct download (from this workspace): **[Deformation_Operator_Playbook_c.pdf](sandbox:/mnt/data/Deformation_Operator_Playbook_c.pdf)**

---

## Why it matters
Most models normalize or “pretty up” anatomy. This playbook re-opens the space for **purposeful distortions** (elongation, graceful coils, depth pulls) with **acceptance checks** and **negatives** to keep the body reading as itself (no ropes, props, extra limbs). It’s fast to learn, auditable, and portable across engines that honor instructions.

---

## Core flow (OS model)
**Anchors** (e.g., `shoulder_L`, `elbow_L`, `wrist_L`) → **Select** (semantic region like `left_arm_forearm_hand`) →  
**Transforms** (one named deformation) → **Constraints** (locks, avoid list, material consistency) →  
**Viewfinder** (crop/shift/zoom for framing tension, “ghost density”).

---

## Operator set (QS 0–8)
- **0) Segmented Coil** — limb coils on itself; one visible overlap; avoid “rope” literalization.  
- **1) Vector Extension** — elbow-anchored lengthening along a defined vector; preserve thickness and hand volume.  
- **2) Logarithmic Scaling (Neck)** — gradual vertical stretch (more near base), width preserved.  
- **3) Rotational Transform** — rotate the forearm around the elbow (parent frozen); add subtle spiral skin folds.  
- **4) Fibonacci Coil** — tight-proximal/open-distal torsion; one overlap; the **arm itself** coils (not wrapping).  
- **5) Parabolic Extension** — graceful arc with the elbow as crest; inner-curve occlusion shading; no “ballooning.”  
- **6) Inverse-Square Perspective Tug (Depth Pull)** — **camera unchanged**; localized convergence toward a right-side point; wrist fullness protected; micro-compression cues.  
- **7) Sine Modulation** — one gentle serpentine wave from elbow→hand; pins on elbow and wrist; limb mass follows the wave.  
- **8) Viewfinder “Ghost Density”** — framing shift/zoom to heighten edge tension; **no new geometry**.

---

## Quick start (5 steps)
1. **Style binder** (e.g., “charcoal drawing, soft diffused light, short-sleeved figure, textured paper”).  
2. **Anchors** (2–4 per limb).  
3. **Select** the target region.  
4. **Apply one transform** (e.g., parabolic, coil, depth tug) with locks and continuity.  
5. **Viewfinder** shift/zoom to center the deformation and suppress artifacts.

---

## Engine adapters & prompting stance
- **Instruction-following (Sora / Gemini / GPT):** binder-first plain English; numeric parameters **semanticized** (“nearly double,” “small turn”); include **acceptance checks** (“upper arm unchanged,” “one overlap,” “no camera change”).  
- **Aesthetic-prior (MidJourney / OpenArt / SDXL):** stronger **negatives**; two-step **BASE/EDIT (inpaint)** or **Vary Region**; mask includes elbow + wrist; lower stylize/CFG; explicit “**the limb itself deforms; not wrapping.**”

---

## Acceptance checks (examples)
- **Coil:** one visible overlap; continuous arm mass; no rope/bracelet; smooth elbow handoff.  
- **Vector extension:** elbow pinned; direction clear; hand size intact.  
- **Depth tug:** convergence strongest at wrist; **upper arm untouched**; narrow under-forearm shadow; denser wrist crease spacing.  
- **Sine:** single crest/trough; limb volume follows the wave; wrist remains full.

---

## Common failure → fast fix
- **Rope/props appear:** “the coil is the arm itself; not wrapping; no objects.”  
- **Wrist collapse:** “keep wrist full; no thin-wrist collapse” (use thickness/topology locks).  
- **Depth reads as generic foreshortening:** “upper arm frozen; camera unchanged,” plus micro-compression cues and a soft under-forearm shadow.  
- **Wave becomes surface wrinkle:** “the limb’s **mass** follows the wave; not just skin.”

---

## Why this isn’t literal math
Models match **visual priors**, not solve equations; parameters act as **nudges**, not hard constraints. Success is measured by **visible acceptance criteria**, optionally with light metrics (LSI/VCLI) after the fact—not by curve-fitting proofs. Treat this as a **translation layer** for repeatability across engines.

---

## License & use
- **Code & DSL snippets:** MIT (permissive).  
- **All other content (text/diagrams/images/frameworks):** All Rights Reserved.  
Use only materials you have rights to; some platforms label strong deformations as “collapse” and may change behavior over time. Expect iteration.
