#!/usr/bin/env python3
# vcf_cli.py — command-line wrapper for the Deformation Operator Playbook
# Usage examples:
#   python vcf_cli.py list
#   python vcf_cli.py gen --template depth_tug --yaml depth_tug.yaml
#   python vcf_cli.py prompt --template parabolic_extension --engine sora
#   python vcf_cli.py bundle --template parabolic_extension --engine openart --outdir out/
import argparse, json, sys, os
from pathlib import Path
from Deformation_Operator_Framework import DeformationFramework, EngineType

def write_text(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print("Wrote", str(path))

def main():
    fw = DeformationFramework()
    p = argparse.ArgumentParser(prog="vcf", description="VCF Deformation Operator Playbook CLI")
    sub = p.add_subparsers(dest="cmd", required=True)

    # list
    sub.add_parser("list", help="List available templates (0–8)")

    # gen
    g = sub.add_parser("gen", help="Export a capsule to YAML/JSON")
    g.add_argument("--template", required=True, help="Template name (use 'list' to see options)")
    g.add_argument("--yaml", help="Write YAML to file")
    g.add_argument("--json", help="Write JSON to file")

    # prompt
    pr = sub.add_parser("prompt", help="Emit an engine-specific prompt")
    pr.add_argument("--template", required=True, help="Template name (use 'list' to see options)")
    pr.add_argument("--engine", required=True, choices=[e.name.lower() for e in EngineType],
                    help="sora | gemini | gpt_dalle | midjourney | openart")

    # validate
    v = sub.add_parser("validate", help="Validate anchors/selections and required params")
    v.add_argument("--template", required=True, help="Template name (use 'list' to see options)")

    # bundle
    b = sub.add_parser("bundle", help="Export YAML + engine prompt(s) to an output folder")
    b.add_argument("--template", required=True, help="Template name (use 'list' to see options)")
    b.add_argument("--engine", required=True, choices=[e.name.lower() for e in EngineType],
                    help="sora | gemini | gpt_dalle | midjourney | openart")
    b.add_argument("--outdir", default="bundle", help="Output directory (default: bundle/)")
    b.add_argument("--json", action="store_true", help="Also write JSON export")

    args = p.parse_args()

    if args.cmd == "list":
        for name in fw.list_templates():
            print(name)
        return

    # Create capsule from template
    cap = fw.create_capsule(getattr(args, "template", ""))
    if cap is None:
        sys.exit(f"Unknown template: {getattr(args, 'template', '')}")

    if args.cmd == "validate":
        errs = fw.validate(cap)
        if errs:
            print("Validation issues:")
            for e in errs:
                print("-", e)
            sys.exit(1)
        print("OK")
        return

    if args.cmd == "gen":
        wrote = False
        if args.yaml:
            Path(args.yaml).write_text(cap.to_yaml(), encoding="utf-8"); print("Wrote", args.yaml); wrote = True
        if args.json:
            Path(args.json).write_text(cap.to_json(), encoding="utf-8"); print("Wrote", args.json); wrote = True
        if not wrote:
            print(cap.to_yaml())  # default to stdout
        return

    if args.cmd == "prompt":
        engine = EngineType[args.engine.upper()]
        out = fw.make_prompt(cap, engine)
        if isinstance(out, dict):
            print(json.dumps(out, indent=2))
        else:
            print(out)
        return

    if args.cmd == "bundle":
        engine = EngineType[args.engine.upper()]
        outdir = Path(args.outdir)
        # 1) YAML
        yaml_path = outdir / f"{args.template}.yaml"
        write_text(yaml_path, cap.to_yaml())
        # 1b) optional JSON
        if args.json:
            json_path = outdir / f"{args.template}.json"
            write_text(json_path, cap.to_json())
        # 2) Prompts per engine
        out = fw.make_prompt(cap, engine)
        if engine in (EngineType.SORA, EngineType.GEMINI, EngineType.GPT_DALLE, EngineType.MIDJOURNEY):
            prompt_txt = out if isinstance(out, str) else json.dumps(out, indent=2)
            write_text(outdir / f"{args.template}_{args.engine}_prompt.txt", prompt_txt)
        elif engine == EngineType.OPENART:
            # dict with BASE/EDIT positives/negatives + settings
            if not isinstance(out, dict):
                out = {"NOTE": "Unexpected prompt format", "raw": str(out)}
            write_text(outdir / f"{args.template}_openart_BASE_positive.txt", out.get("BASE_positive",""))
            write_text(outdir / f"{args.template}_openart_BASE_negative.txt", out.get("BASE_negative",""))
            write_text(outdir / f"{args.template}_openart_EDIT_positive.txt", out.get("EDIT_positive",""))
            write_text(outdir / f"{args.template}_openart_EDIT_negative.txt", out.get("EDIT_negative",""))
            write_text(outdir / f"{args.template}_openart_README.txt", out.get("settings_hint",""))
        print("Bundle complete in", str(outdir))
        return

if __name__ == "__main__":
    main()
