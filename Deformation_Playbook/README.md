# Deformation Operator Playbook (Python + CLI)

## What this is
A small, production-ready toolkit that turns the **Deformation Operator Playbook** into code. It mirrors the OS flow:
**Anchors → Select → Transforms → Constraints → Viewfinder**

Export capsule specs (YAML/JSON), lint them, and generate **engine-ready prompts** (Sora/Gemini/GPT, MidJourney, OpenArt/SDXL).

## Contents
- `Deformation_Operator_Framework.py` — core library (operators, templates, validators, adapters)
- `vcf_cli.py` — command-line wrapper
- `README.md` — this file
- `LICENSE-MIT.txt` — MIT license for code/DSL snippets
- `LICENSE-NONCODE.txt` — All Rights Reserved notice for non-code content

**Operators covered (QS 0–8):** 0 Segmented Coil · 1 Vector Extension · 2 Log Scaling (neck) · 3 Rotational Transform · 4 Fibonacci Coil · 5 Parabolic Extension · 6 Depth Tug (inverse-square) · 7 Sine Modulation · 8 Ghost Density (Viewfinder)

## Requirements
- Python 3.9+
- Optional: `pyyaml` (nicer YAML output) → `pip install pyyaml`

## Quick start
```bash
# List templates
python vcf_cli.py list

# Export YAML (stdout)
python vcf_cli.py gen --template depth_tug

# Export YAML to file
python vcf_cli.py gen --template parabolic_extension --yaml parabolic_extension.yaml

# Sora/Gemini prompt
python vcf_cli.py prompt --template parabolic_extension --engine sora

# MidJourney prompt
python vcf_cli.py prompt --template rotation_forearm --engine midjourney

# OpenArt two-step prompts
python vcf_cli.py prompt --template fibonacci_coil --engine openart

# Validate
python vcf_cli.py validate --template rotation_forearm

# Bundle (YAML + prompt files)
python vcf_cli.py bundle --template depth_tug --engine sora --outdir out/
python vcf_cli.py bundle --template parabolic_extension --engine openart --outdir out_openart/ --json
```

## How it maps to the Playbook
- **StyleBinder** → binder (charcoal/lighting/background/pose)
- **Anchors/Selections** → named points + semantic parts
- **Transforms** → operators 0–8 with thickness/topology locks
- **Constraints** → real-world avoid list (rope/bracelet/armor/segments/**thin_wrist_collapse**/etc.)
- **Viewfinder** → explicit, non-deforming framing (QS-8)

## Engine adapters
- **Sora/Gemini/GPT** — plain-English, binder-first prompts; parameters **semanticized** (“nearly double,” “a small turn”) with **acceptance cues**.
- **MidJourney** — single string with `--style raw`, low stylize, strong negatives; suited to **Vary (Region)**.
- **OpenArt/SDXL** — two-step export: **BASE** (neutral figure) + **EDIT** (inpaint) with negatives and settings hints.

## Validation & reproducibility
- `vcf_cli.py validate` checks anchors, required joints/centers, selections.
- Every capsule can carry `meta` (engine/model/seed) in YAML/JSON.

## Troubleshooting
- Adds objects (rope/armor)? → strengthen negatives; say “the arm itself deforms; not wrapping.”
- Wrist collapses? → include “keep wrist full; no thin-wrist collapse.”
- Depth tug reads as generic foreshortening? → add “upper arm frozen; camera unchanged; denser wrist creases; narrow under-forearm shadow.”
- MJ repairs the edit? → expand the inpaint mask to include elbow + wrist; lower stylize/CFG; re-run.

## Disclaimer
Results vary by engine, version, settings, and randomness—**expect iteration**. Many vendors treat strong deformations as “collapse” and may retune models to suppress them without notice. Use only material you have rights to and follow each platform’s terms.

## License
- **Code & DSL snippets:** MIT License (see `LICENSE-MIT.txt`).
- **All other content (text, diagrams, images, frameworks):** All Rights Reserved (see `LICENSE-NONCODE.txt`).