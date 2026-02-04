# Visual Thinking Lens  
**Recursive Critique for AI-Generated Imagery**

---

## Overview

The **Visual Thinking Lens (VTL)** is an evaluation and diagnostic framework for generative visual systems. It measures structural and compositional behavior that semantic metrics do not capture.

Most AI image outputs exhibit strong spatial priors and compositional defaults regardless of prompt content. VTL instruments these behaviors through geometry-first kernels, stability analysis, and controlled perturbation testing.

Rather than optimizing aesthetics, the Lens is designed to:
- Expose compositional bias and structural convergence
- Detect early failure modes before semantic collapse
- Compare cross-model spatial behavior
- Enable controlled steering and diagnostic benchmarking

---

## What the Lens Is
The Visual Thinking Lens is a multi-engine evaluation field that analyzes how generative models organize space under constraint.
It focuses on:
- Spatial priors and geometric bias
- Stability basins and operating envelopes
- Structural drift and collapse patterns
- Prompt sensitivity versus model-driven behavior

VTL evaluates images by structure rather than style. It measures how outputs respond to perturbation, variation, and constraint, revealing where models remain stable and where geometry begins to break.

## What This Is Not
This is not a prompt collection or aesthetic tuning toolkit.
- It is a measurement and diagnostic system intended for:
- Model behavior analysis
- Research instrumentation
- Generative system evaluation
- Creative tooling with structural control

## Core Capabilities
The framework provides:
- Geometry-first kernel metrics for spatial behavior
- Cross-model compositional fingerprinting
- Stability envelope and stress testing tools
- Structural regression detection
- Reproducible evaluation pipelines

---

### 🧪 Kernel Metrics for Compositional Analysis

Most evaluation metrics for generative image models (FID, CLIP, T2I-CompBench) measure semantic similarity and feature realism. They do not measure how models organize space.

Generative systems often satisfy prompts while exhibiting strong compositional priors: consistent patterns in placement, void allocation, packing density, and mass distribution. This repository introduces a minimal geometry-first kernel (Δx, rᵥ, ρᵣ, μ, xₚ) that quantifies these spatial behaviors and exposes stable compositional basins where different engines naturally operate.

Across hundreds of measured outputs and multiple platforms, distinct spatial signatures emerge. These patterns remain stable across prompt variation, indicating model-driven structure rather than prompt-driven layout.

Perturbation experiments further show that geometric structure degrades before semantic failure. Void ratio and cohesion decay provide early collapse signals that standard evaluation metrics do not capture.

The framework is designed for practical use. All metrics are computed from standard mask extraction and integrate with existing evaluation pipelines. Use cases include model comparison, regression detection, stability monitoring, and architectural fingerprinting.

Implementation notebooks, validation protocols, and comparative studies are included for reproducibility and extension.

---

### 🧪 LSI-lite: A Composition Analysis Tool (`/LSI_Image_Quality_Tools`)

LSI-lite is a lightweight structural metric for evaluating compositional stability. It measures three primitives: Δx (spatial offset), rᵥ (void ratio), and ρᵣ (edge/mark density), then scores alignment to expected structural bands on a 0–100 scale.

Unlike semantic metrics (FID/CLIP/SSIM), LSI-lite tests whether composition holds under pressure. It’s designed for baseline → perturbation → collapse tracking, not aesthetic ranking.

Includes MVP grayscale pipeline and optional color diagnostic version (v3) for extended analysis.

---

### 🧪 Kernel Metrics Spec and Instrument (`/kernel-metrics-spec-and-instrument`)

Defines a geometry-first framework for measuring spatial priors in images and provides a working diagnostic instrument. The spec formalizes seven kernel metrics (Δx, rᵥ, ρᵣ, μ, xₚ, θ, ds) as operations on the image gradient field. The accompanying notebook computes masks, structural overlays, compositional fingerprints, and kernel summaries for direct comparison across human and model-generated images.

---

### 🧪 The Visual Cognitive Load Index (VCLI-G) (`/Visual_Cognitive_Load_Index`)

VCLI-G measures how much structural effort an image demands from a viewer. It evaluates balance, void control, layering, and tension to estimate “earned complexity” — sustained visual engagement driven by composition rather than surface detail. Paired with the Structural Coherence Index (SCI), it provides a two-axis framework for analyzing and steering visual organization across human and AI-generated imagery.

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

OCF identifies stable off-center compositional basins where images remain coherent instead of collapsing to center defaults. Using Δx, rᵥ, and ρᵣ with small engine-aware nudges and controlled cropping, the protocol enables repeatable off-center placement and explains why results pass or fail. Includes a chat-compatible workflow for consistent cross-engine testing. [PDF](Off_Center_Protocol/Off-Center_Fidelity_Constraint_Basins_Stability_Drift_Proposal+Conversational_Protocol.pdf)

---

### 🧪 Deformation Operator Playbook (`/Deformation_playbook`)

A structured prompting framework for controlled figure deformation. Defines a small operator set (extension, arc, coil, depth tug, rotation, scaling, view shifts) with continuity and topology locks to preserve anatomy and structural coherence. Designed for iterative, engine-agnostic use and compatible with lightweight metric auditing. [PDF](Deformation_Playbook/Deformation_Operator_Playbook_c.pdf)

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
