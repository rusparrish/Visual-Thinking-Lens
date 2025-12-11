# Visual Thinking Lens  
**Recursive Critique for AI-Generated Imagery**

---

## Overview

The **Visual Thinking Lens (VTL)** is a Recursive Lab for Visual Intelligence. Don’t just make images. Make images that speak. Most AI images form through default mimicry and aesthetic averages, not authorship. The Lens is a role-structured, multi-engine scaffold that combines named feature concepts (axes), causal/consistency checks (validators), and contrastive casework to make models explain, test, and repair their own judgments.

## What the Lens Is
The Visual Thinking Lens is a multi-engine, recursive critique field that works by applying structural intelligence to prompts, compositions, and symbolic logic. It (re)builds imagery in the ways defaults cannot see. It interrogates images **not by style, but by structure**. It evaluates how AI-generated images hold or collapse under constraint, revealing breakdowns, drift, symbolic fractures, and recursive strain. So don’t just make images, interrogate them and then remake them into images that speak. Most AI images aren’t composed, they form through default mimicry, not authorship, this Lab is out to change that. 

This is not a toolkit. It is a **lens**: a reasoning engine that turns glitch into architecture, and failure into consequence. A set of tools that apply pressure to the underlying structure of diffusion, prompting, composition and remaking of almost any type of images (real or AI). It is a:

- Recursive prompt-pressure engine for generative image collaboration. 
- Diagnostic layer that reverse-engineers structural alternatives in AI-generated and human made imagery.
- Symbolic/structural critique lens that rivals or exceeds native model feedback.
- Scoring systems that create pressure loops not found in aesthetics-first systems.
- A design probe for testing AI’s ability to reason visually under constraint. 

---

## Why It Exists

Most AI-generated imagery defaults to aesthetic gloss.  
VTL was developed to see what machines miss:

- Structural weakness masked by polish  
- Semantic instability under recursion  
- Pattern collapse disguised as coherence  
- Symbolic voids where meaning should strain  

Ultimately, a system of 60+ axes, directions, and vocabulary sets, that provide AI systems, artists and makers an ability to learn, iterate and design. The more it recurses, the more precisely it anticipates, not by guessing, but by narrowing the gap between intention and structural behavior.

---

### 🧪 Kernel Metrics for Compositional Analysis

Current evaluation metrics for generative image models (FID, CLIP, T2I-CompBench) measure semantic correctness and feature-space realism, but they miss a fundamental dimension: spatial reasoning. Models can satisfy prompts while exhibiting distinct compositional priors—habitual patterns in placement, void allocation, packing density, and mass distribution. This repository introduces a minimal geometric kernel (Δx, rᵥ, ρᵣ, μ, xₚ) that quantifies these spatial behaviors, revealing stable "compositional basins" where different engines naturally operate. Testing across 300+ images and 14 platforms shows that GPT and Sora cluster in right-biased, high-void regimes while MidJourney exhibits left-weighted compression, and these signatures remain stable across prompt variations. Critically, perturbation experiments demonstrate that geometric structure degrades before semantic failure—void ratio and cohesion decay provide early collapse signals invisible to semantic metrics. The framework is designed for practical adoption: geometric primitives computed from standard mask extraction, compatible with existing benchmarks, and applicable to version regression detection, model comparison, safety monitoring, and architectural fingerprinting. Full implementation notebooks, validation protocols, and cross-engine comparative studies are included for independent verification and extension.

---

### 🧪 LSI-lite: A Composition Analysis Tool (`/LSI_Image_Quality_Tools`)

LSI-lite (MVP) measures how an image behaves under compositional structure using three primitives: Δx (off-center gravity), rᵥ (void ratio), ρᵣ (rupture/mark energy) and tells you if it sits within intended bands for its class. It’s built to study stability, not to crown winners. Balance (Δx): How far the visual center is from the geometric center Density (rᵥ): The ratio of empty space to filled space Detail (ρᵣ): The amount of edge energy and texture density in key areas It combines these measurements into a 0-100 score for how an image lines up or "passes" basic structural compositional criteria. It helps distinguish delta in AI and human default.

- Balance (Δx): How far the visual center is from the geometric center
- Density (rᵥ): The ratio of empty space to filled space
- Detail (ρᵣ): The amount of edge energy and texture density in key areas
- It combines these measurements into a 0-100 score and tells you whether an image "passes" basic compositional criteria structural exploration test.

Why researchers use it (not FID/CLIP/SSIM).
Resemblance and caption metrics can’t answer: will this composition hold when pushed? LSI-lite is a composition structural exploration test and a quick, profiled gate you can log across Baseline → Pressure → Collapse-trigger runs. It is in collaboration, not competitive.

This tool while only only a MVP, the same folder has a release v3--> lets LSI look in color alongside grayscale—purely for diagnostics. 

---

### 🧪 Kernel Metrics Spec and Instrument (`/kernel-metrics-spec-and-instrument`)

Precise Mapping: Kernel Metrics → Gradient-Field Operations defines a deterministic framework for measuring spatial priors in images and pairs it with a working instrument. The document formalizes seven compositional kernel metrics—Δx, rᵥ, ρᵣ, μ, xₚ, θ, ds—and shows how each is instantiated as an operation on the gradient field |∇I|, treating every image as a force field of mass, void, and pull rather than a bag of objects. The accompanying notebook turns that specification into a diagnostic tool: given any image, it builds gradient and skeleton fields, void and mass masks, multi-panel overlays, and compositional fingerprints, then outputs the kernel metrics as a compact summary of how the frame is structured. Together, they provide a coherent way to see, quantify, and compare the spatial priors of both human and model-generated images—without touching training data or model internals.

---

### 🧪 The Visual Cognitive Load Index (VCLI-G) (`/Visual_Cognitive_Load_Index`)

The Visual Cognitive Load Index (VCLI-G) is a way to measure how much visual effort an image asks from a viewer. It looks at structure — balance, voids, and tension — not beauty or subject matter. In simple terms, it tells you whether a picture’s complexity is “earned” (coherent, intentional) or just “busy.” By combining geometric cues like curvature, layering, and void control, it turns what artists sense intuitively into a number you can track or compare. It’s like having a visible dial for visual tension and compositional focus. It estimates earned complexity: how effectively structure sustains cognitive engagement without collapsing into noise. Paired with SCI (Structural Coherence Index), it provides a two-axis framework for analyzing and steering visual organization across human and AI-generated imagery.

---

## Repository Contents

### 📘 Core Documents (`/docs`)

## Read-only whitepapers and conceptual briefs outlining the framework:

## System Explainers: Documents that help explain what the Lens is and what it does.
- **Visual Thinking Lens Stack** – Overview of recursive architecture for image reasoning. [PDF](docs/visual-thinking-lens-stack.pdf)
- **Introduction: Sketcher Lens** – Philosophy of the structural critique engine (no internals disclosed). [PDF](docs/introduction-sketcher-lens.pdf)
- **Sketcher as Scaffold: How the Lens Rewrites GPT's Reflex** - Sketcher Lens interrupts GPT’s generative reflex by applying prompt-level scaffolding that forces structural consequence into the image. [PDF](docs/Sketcher_Scaffold_The_Lens_Rewrites_GPT_Reflex.pdf)
- **Artist's Lens (Brief Explanation)** – Poise, restraint, and delay as structural forces. [PDF](docs/artist-lens-brief-explanation.pdf)
- **A Constraint Dialectic Engine for Recursive Image + Symbolic Critique** – How the Lens engine is unique and why it is different. [PDF](docs/Dialectic_Engine_Recursive_Symbolic_Critiques.pdf)

## Core Theory & Architecture: Defines the system’s architecture, logic, and grounding.
- **Working Theory** – Structural consequence as a measure of visual intelligence. [PDF](docs/visual-thinking-lens-working-theory.pdf)
- **Foundational Architecture for Recursive Visual Intelligence** - The system doesn’t improve images, it interrogates their ability to hold structure. This isn’t a toolkit for artists, it’s a pressure engine for aligning large language models with visual consequence. [PDF](docs/Foundational_Architecture_Recursive_Visual_Intelligence.1.pdf)
- **Constraint Layer & Logic Tags** – How structured prompts behave differently from descriptive ones. [PDF](docs/constraint-layer-and-logic-tags.pdf)

## Stability, Drift, and Collapse: Formalizing drift, collapse, and constraint basins as reproducible fields.
- **Off-Center Fidelity: Drift as Creative Control** – Drift and collapse can be reframed as reproducible constraint basins—stable off-center zones defined by Δx, r_v, and ρ_r—that act as interpretable control levers rather than failures. [PDF](docs/Off-Center_Fidelity_Constraint.pdf)
- **Failure Taxonomy: Evidence for Generative Model Collapse Modes** - Systematically categorizing evidences of failure modes in generative outputs, using the Sketcher Lens and CLIP, for diagnosing and understanding collapse patterns. [PDF](docs/Failure-Taxonomy-Generative-Collapse-Modes.pdf)
- Constraint Gravity: Thirty Figures Without Collapse \ This study tests how stable an AI figure can be across thirty recursive generations. What emerges is not novelty, but refined pressure memory and a glimpse of machine restraint observed as memory. [PDF](docs/Constraint_Gravity_Thirty_Figures_Without_Collapse.pdf)
- **μ Negotiation: Off-Center Fidelity in Generative Models** – Exposing how fidelity emerges off-center, in the unstable edge between coherence and fracture. [PDF](docs/μ-Negotiation_Off-Center-Fidelity-Generative-Models-c.pdf)

## Interpretability and Research Probes: Bridging Lens logic with AI interpretability and research tool use.
- **How Models Fake Seeing** – Diagnosing simulated vision in generative systems. [PDF](docs/how-models-fake-seeing.pdf)
- **Introduction: Recursive Image Scoring for AI-Generated Art** - This framework introduces a new scoring system designed to evaluate AI-generated images based on structural integrity, symbolic recursion, and decision making logic, not polish or aesthetics. [PDF](docs/Recursive_Image_Scoring_AI-Generated_Art_Framework-c.pdf)
- **Whisperer Walk: Recursive Compression into Spatial Realization** – AI image study showing symbolic recursion under structured visual critique. [PDF](docs/Recursive-Compression-Spatial-Realization.pdf)
- **Recursive Intelligence Under Constraint** – Canonical artifact showing collapse as structure. [PDF](docs/recursive-intelligence-under-constraint.pdf)

## Artistic Extensions: Pushing into symbolic recursion, refusal, and design philosophy.
- **Visual Systems at the Edge of Contradiction** – Materializing tension and refusal. [PDF](docs/visual-systems-at-the-edge-of-contradiction.pdf)
- **Concept Note: Volumetric Container of Force** – A validator concept for visual strain detection. [PDF](docs/concept-note-volumetric-container-of-force.pdf)
- **Prompting Against Collapse (Dialectic Structures)** – Principles for tension-driven prompting. [PDF](docs/prompting-against-collapse-dialectic-structures.pdf)
- **Bending the Tokens: Structural Pressure for AI Imagery** - Deconstructing generative images to reshape underlying architecture. [PDF](docs/Bending_the_Tokens.pdf)

---

### 🧪 Off-Center Fidelity (OCF): Constraint Basins for Stability & Drift in Generative Models (`/Off_Center_Protocol`)

Most models collapse to *safe center*. OCF reframes that as **geography**: there are reproducible *attractor basins* where off-center images remain coherent. By measuring Δx, rᵥ, ρᵣ and applying small, engine-aware nudges (plus a one-click crop), you can hit those basins **reliably**—and explain *why* a result passed or failed. This repository accompanies the proposal and packages it as a **conversational protocol** you can run in any chat interface to get consistent, measurable results across engines. [PDF](Off_Center_Protocol/Off-Center_Fidelity_Constraint_Basins_Stability_Drift_Proposal+Conversational_Protocol.pdf)

---

### 🧪 Deformation Operator Playbook (`/Deformation_playbook`)

The Deformation Operator Playbook is a practical prompting framework for intentional, repeatable figure warps that treats distortion as the body itself, guided by the flow Anchors → Select → Transforms → Constraints → Viewfinder. It offers a small set of operators (extension, coils, parabolic arc, depth tug, sine modulation, logarithmic scaling, rotation, and viewfinder shifts) with locks to preserve thickness, topology, and continuity—so edits stay anatomical rather than turning into props or glitches. It’s engine-agnostic, expects iteration, and can be audited with light metrics while acknowledging that some platforms may suppress strong deformations over time. [PDF](Deformation_Playbook/Deformation_Operator_Playbook_c.pdf)

---

### 🧪 Examples (`/examples`)

Visual Thinking Lens is a modular cognitive architecture for visual reasoning. It hosts adaptive specialists that applies a compact kernel (Δx (placement), rᵥ (void), ρᵣ (packing), plus validator guards to pressure-test images before polish. The system treats images as negotiations, not styles: diagnose → validate → route (Δ/Ω) → regenerate → rescore. It’s refusal-native (kills unearned emblems), consequence-first, and reproducible.

- Δ prior-undo (reduce collapse, restore near-miss tension),
- Ω refusal spike (second geometry / occlusion / counter-light)
- Small, legible kernel instead of black-box scores.
- Refusal as first-class control (not failure).

It turns image generation into a measurable negotiation loop. Prioritizing consequence over resemblance, logs provenance like a lab, and explains differences with advisory telemetry instead of aesthetic scores.

It turns “taste” debates into structure-first discussions.

The architecture: routes and governs modules.
- Kernel (LSI / LSI-Lite): Δx, rᵥ, ρᵣ + validators (Prompt Pressure, Compositional Predictability, Sequence Drift Lock, Inversion Drift Check, Symbolic Gravity Flags).
- Specialists:
-- Sketcher (structure/pressure; chooses Δ prior-undo or Ω refusal).
-- Artist’s Lens (attunement/delay; governs poise and timing).
-- Marrowline (symbolic disruption; demotes trope to event).
-- RIDP (reverse/failure tracing; reveals compositional collapse paths).
- TEL (advisory): corridor₉₀ (lane breadth) and cadence_cv (row rhythm) explain why two PASS frames feel different, but it never gates.
- Basins & Hulls: cluster the kernel space; convex hull gives exploration envelope; reported with pass-rate, safety margins, anisotropy (eigen-ratio), and RHA@K resampling to avoid sample-size hype.

Cognitive Load & Coherence Layer (VCLI-G / SCI):
- Extends the kernel into perceptual space. VCLI-G measures cognitive load (z₁–z₄: wander, void, torque, occlusion); SCI tracks structural coherence (continuity, regularity, rhythm).
- Together they form a phase map of visual reasoning, showing whether tension is earned, overstressed, prematurely resolved, or default simple.
- Profiles (AI Conservative / Physical Neutral / Physical Balanced+) act as control regimes, adjusting sensitivity between tension and order.

Library of before/after images in examples folder and at: https://www.artistinfluencer.com/library

Unlike Midjourney, DALL·E, Stable Diffusion Sora, Runway, Gen-2, the Lens works by analyzing images and the prompts that formed them, tracking breakdowns, then, it reverse-engineers fixes, layer by layer, token by token, through real-time critique cycles.

Prompt interpretation linked to logic axis-aware failure detection. Other systems don’t say: “Your prompt caused spatial collapse” or “This token triggers overuse.”

They may let you change the prompt, but they don’t tell you why it failed structurally.
---

## What This Is Not

- ❌ A style guide  
- ❌ A prompt recipe library  

This project is **recursive intelligence under constraint**, not image generation or style tuning.

---

## License

All content © 2025 Russell Parrish / A.rtist I.nfluencer.  
Protected under a **CC BY-NC-ND** license.  
No commercial use, derivative generation, or dataset scraping permitted without explicit permission.

See `/legal/LICENSE.md`, `/legal/visual-assets-license.md`, and `/NOTICE.md` for full terms.

---

## Research Use
 
If you’re working on **LLM visual alignment, interpretability tooling, or structural image reasoning**, you can reach out via:

📧 russellgparrish@gmail.com  
🌐 [www.artistinfluencer.com](http://www.artistinfluencer.com)
ORCID: 0009-0008-9781-7995

---

**Visual Thinking Lens**  
*Not generated. Diagnosed.*
