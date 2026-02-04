# Visual Thinking Lens - A.rtist I.nfluencer 
**AI generates infinite subjects.
It repeats the same structure.**

Applied AI evaluation framework for generative systems, measuring compositional bias and structural behavior across major platforms.

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

### 🧪 Off-Center Fidelity (OCF): Constraint Basins for Stability & Drift in Generative Models (`/Off_Center_Protocol`)

OCF identifies stable off-center compositional basins where images remain coherent instead of collapsing to center defaults. Using Δx, rᵥ, and ρᵣ with small engine-aware nudges and controlled cropping, the protocol enables repeatable off-center placement and explains why results pass or fail. Includes a chat-compatible workflow for consistent cross-engine testing. [PDF](Off_Center_Protocol/Off-Center_Fidelity_Constraint_Basins_Stability_Drift_Proposal+Conversational_Protocol.pdf)

---

### 🧪 Deformation Operator Playbook (`/Deformation_playbook`)

A structured prompting framework for controlled figure deformation. Defines a small operator set (extension, arc, coil, depth tug, rotation, scaling, view shifts) with continuity and topology locks to preserve anatomy and structural coherence. Designed for iterative, engine-agnostic use and compatible with lightweight metric auditing. [PDF](Deformation_Playbook/Deformation_Operator_Playbook_c.pdf)

---

### 🧪 Examples (`/examples`)

This folder contains reference image sets used to test and demonstrate Visual Thinking Lens evaluation workflows.

Each example follows a simple loop: Generate → Locate → Measure → Regenerate → Re-evaluate

The goal is to observe how compositional structure responds to prompt variation, constraint pressure, and geometric steering. Examples highlight:
- Baseline compositional priors
- Stability under perturbation
- Structural drift and collapse patterns
- Differences between semantic change and geometric change

These examples are designed for reproducibility and comparison, not aesthetic ranking.

A larger curated library is available at:
https://www.artistinfluencer.com/library

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
