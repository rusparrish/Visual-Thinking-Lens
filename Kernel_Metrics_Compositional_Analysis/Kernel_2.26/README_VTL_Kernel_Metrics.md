# Visual Thinking Lens --- Kernel Metrics & Gradient-Field Instrument

A deterministic framework and diagnostic tool for measuring spatial
priors in generative image systems using geometry-first field analysis.

------------------------------------------------------------------------

## Overview

Generative image models often produce structurally consistent outputs
even when prompts attempt to push them elsewhere. These behaviors
reflect **spatial inductive biases** learned during training.

Most evaluation metrics measure:

-   Semantic correctness\
-   Perceptual similarity\
-   Text alignment\
-   Feature-space realism

This repository introduces a complementary approach:

> Treat images as force fields of mass, void, and structural pull ---
> and measure how models compose space.

The system defines a compact set of **Kernel Metrics** derived directly
from image gradient fields and exposes reproducible signatures of
compositional behavior across human and AI-generated imagery.

------------------------------------------------------------------------

## What This Project Provides

### 1. Kernel Metric Specification

  Metric   Meaning
  -------- -----------------------------------------
  Δx       Horizontal mass displacement
  Δy       Vertical mass displacement
  rᵥ       Void ratio (unused structural space)
  ρᵣ       Packing density / mass cohesion
  μ        Structural cohesion and continuity
  xₚ       Peripheral pull (edge attraction field)
  θ        Orientation stability
  ds       Structural thickness continuity

Together, these form a measurable spatial fingerprint of an image's
compositional logic.

------------------------------------------------------------------------

### 2. Gradient-Field Instrument

The notebook converts the specification into a working diagnostic
pipeline:

-   Gradient magnitude extraction \|∇I\|
-   Mass / void segmentation
-   Skeleton and topology tracing
-   Peripheral force mapping
-   Structural fingerprint visualization
-   Batch evaluation support

------------------------------------------------------------------------

### 3. Cross-Model Behavioral Fingerprinting

The framework can detect:

-   Compositional attractors\
-   Structural collapse modes\
-   Prompt drift resilience\
-   Snap-back to learned priors\
-   Stability envelopes across model versions

------------------------------------------------------------------------

## Why This Matters

Generative models are not limited by training data volume.

They are limited by **how they reason spatially during inference**.

Kernel Metrics allow researchers and practitioners to measure:

-   Where models place visual mass
-   How void space is regulated
-   How composition resists or yields to prompt pressure
-   When structural complexity is earned vs accidental

------------------------------------------------------------------------

## Relationship to Existing Metrics

Kernel Metrics do NOT replace perceptual or semantic evaluation. They
extend it into geometric reasoning.

  Metric Family        Measures
  -------------------- -----------------------------------------
  FID / IS / KID       Dataset realism
  CLIP / T2I metrics   Text alignment
  LPIPS / SSIM         Perceptual similarity
  Kernel Metrics       Structural composition & spatial priors

------------------------------------------------------------------------

## Repository Structure

    /notebooks
        VTL_Kernel_Metrics_—_Canonical_Gradient_Field_Extractor_Canon_3
        vtl_kernel_metrics_—_canonical_gradient_field_extractor_canon_3.py

    /docs
        Kernel Metrics Specification
        Methodology papers
        Case studies

    /examples
        Sample evaluation outputs
        Visualization overlays

------------------------------------------------------------------------

## Quick Start

### Requirements

Python 3.9+\
OpenCV\
NumPy\
SciPy\
scikit-image\
matplotlib

------------------------------------------------------------------------

### Install Dependencies

    pip install opencv-python numpy scipy scikit-image matplotlib

------------------------------------------------------------------------

### Run Notebook

Open:

    VTL_Kernel_Metrics_Gradient_Field_Extractor.ipynb

Load an image and execute all cells to generate:

-   Gradient maps
-   Mass/void masks
-   Skeleton topology
-   Peripheral pull fields
-   Kernel metric summary output

------------------------------------------------------------------------

## Output Example

### Structural Visualizations

-   Gradient field overlays
-   Void distribution maps
-   Skeleton flow topology
-   Edge pull heatmaps

### Quantitative Fingerprint

    Δx = 0.083
    Δy = -0.041
    rᵥ = 0.64
    ρᵣ = 0.29
    μ = 0.71
    xₚ = 0.38
    θ = Stable
    ds = Moderate

------------------------------------------------------------------------

## Interpretation Guide

### Δx / Δy --- Mass Displacement

Measures center bias vs compositional asymmetry across horizontal and
vertical axes.

### rᵥ --- Void Ratio

Measures spatial breathing room and structural openness.

### ρᵣ --- Packing Density

Measures mass compression and clustering.

### μ --- Cohesion

Measures continuity of structural flow.

### xₚ --- Peripheral Pull

Measures attraction toward frame boundaries.

### θ --- Orientation Stability

Measures directional bias and alignment stability.

### ds --- Structural Thickness

Measures continuity of stroke or mass thickness.

------------------------------------------------------------------------

## Primary Research Applications

-   Model Evaluation
-   Prompt Engineering Research
-   Generative Model Benchmarking
-   Creative Tool Diagnostics
-   Failure Analysis

------------------------------------------------------------------------

## Design Philosophy

### Determinism

All metrics are derived from measurable geometric properties.

### Interpretability

Every metric corresponds to visible structural behavior.

### Model Independence

No training data access or model introspection required.

------------------------------------------------------------------------

## Conceptual Model

Images are treated as **force fields**, not object containers.

Mass = high gradient energy\
Void = low structural occupancy\
Pull = boundary attraction forces\
Topology = skeletonized structure flow

------------------------------------------------------------------------

## Future Extensions

-   Video temporal field analysis
-   Control signal effectiveness scoring
-   Multi-scale topology mapping
-   Hybrid perceptual + geometric evaluation
-   Stability basin clustering
-   Integration with cognitive load metrics (VCLI)

------------------------------------------------------------------------

## Author

Russell Parrish\
https://www.artistinfluencer.com

---

## 📄 Citation

If used in research or development:

```
Russell Parrish. Visual Thinking Lens: Kernel-Based Compositional Metrics, 2026.
www.artistinfluencer.com
russellgparrish@gmail.com
ORCID: 0009-0008-9781-7995
```

---

## 🧭 Purpose

The VTL Kernel Metrics framework is part of the broader  
**Visual Thinking Lens (VTL)** system — a modular architecture for analyzing generative behavior, inductive bias, and spatial reasoning in AI models.

This toolkit is intended for:

- ML researchers  
- model evaluators  
- prompt engineers  
- visual computing practitioners  


---

## Acknowledgments

Developed as part of ongoing research into **geometric inductive bias**, **spatial priors**,and **model‑agnostic evaluation techniques**.

------------------------------------------------------------------------

## License

Research and educational use permitted.\
No dataset scraping, model training, or derivative training use allowed
without explicit permission.

------------------------------------------------------------------------

## Contact

russellgparrish@gmail.com
