
# Batch Scoring — Notebook & Script

## What it is - Image Evaluation/Generative Image Analysis
Modern image evaluation metrics measure semantic alignment, distributional fidelity, and aesthetic preference, but none quantify temporal demand or how long an image resists perceptual resolution. VCLI-G (Visual Cognitive Load Index - Geometry Coupled) addresses this gap by measuring cognitive effort through four geometric channels: centroid wander, void topology, curvature torque, and occlusion entropy. Paired with the Structural Coherence Index (SCI), the system maps images into a 2D perceptual space that distinguishes earned complexity from chaotic noise, and intentional simplicity from default outputs. This framework enables researchers to detect when generative models converge on safe patterns, allows artists to quantify attention gravity as geometry, and provides a measurement basis for perceptual engagement independent of aesthetic judgment. VCLI-G treats high cognitive load as a controllable state rather than a failure mode, making it applicable across contexts from UI optimization to gallery curation.


This folder includes two ways to score many images with VCLI‑G/SCI:

- **Notebook:** `GITHUB_BATCH_of_Initial_v2_VCLI_G.ipynb` (Colab‑ready)
- **Script:** `github_batch_of_initial_v2_vcli_g.py` (local/CLI)

## What it does
VCLI-G is a research-grade scoring system designed to measure how much perceptual and cognitive work an image demands — not how “pretty” it is, not how similar it is to training data, and not how well it matches a text prompt. It couples perceptual arrest (how hard an image is to resolve or “let go of”) with geometric signals extracted directly from the composition.

It’s meant to answer a single, difficult question:

How much does this image make me think?

### Minimal CSV schema

```
path, profile, VCLI_G,
G1_L, G1_K, G2_V, G2_chi, G2_AR, G2_cut, G3_kvar, G3_infl, G4_H,
SCI, SCI_regional, SCI_angle, SCI_scale, SCI_rhythm,
z_z1, z_z2, z_z3, z_z4, z_raw
```

## Notebook (Colab) usage

1. Open the notebook in Colab.
2. Run the dependency install cell (if needed).
3. Upload a few images in the **Upload** cell.
4. Set a **profile** in the “SET PROFILE” cell.
5. Run the **results table** cell — it prints and saves the CSV.

Easy upload batches
- Loads images (JPG/PNG/WebP)
- Extracts geometric features (G1..G4) and SCI submetrics
- Normalizes features, combines z‑channels into **VCLI‑G**, and writes a **CSV**

## Script usage

```bash
python github_batch_of_initial_v2_vcli_g.py   --input /path/to/images   --output results.csv   --profile physical_neutral   --recursive
```

## Profiles

- `ai_conservative` — penalizes “cheap” complexity (void/texture spam), tight z‑clip.
- `physical_neutral` — balanced baseline.
- `physical_balanced_plus` — rewards earned figure/ground and curvature tension a bit more.

File presently set to: ai_conservative

## Usage
Compare scores to understand viewer effort or attention gravity across images or runs.

Use it alongside structural tools to reveal where and why perceptual strain occurs — but don’t confuse high scores with aesthetic merit

Two Metrics, One System
VCLI-G is now paired with SCI (Structural Coherence Index) to form a 2D perceptual space:

VCLI-G (0.0 – 5.0): How much cognitive work does the image demand? SCI (0.0 – 5.0): How organized is that work?

They're independent axes that together describe different kinds of visual complexity:

High VCLI-G, High SCI → Earned tension (Cézanne, deliberate ambiguity) High VCLI-G, Low SCI → Chaotic complexity (glitch, noise, productive accidents) Low VCLI-G, High SCI → Resolved clarity (Vermeer, intentional simplicity) Low VCLI-G, Low SCI → Default simplicity (gradient + centered object)

⚠️ Neither axis is a quality score. Low SCI doesn't mean "bad" — it means emergent/process-driven (like Pollock). High SCI doesn't mean "good" — it means systematic/composed. Context determines which is appropriate.

## Notes

- PNG/JPG/WebP supported (8‑bit). Very small images may be upscaled by your environment before upload.
- If you enable the **occlusion DAG** option in code, expect slower runs.
- Results are deterministic per image & profile (no random seeds needed).
