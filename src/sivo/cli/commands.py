import argparse
import sys
import os
import json
from ..core.sivo import Sivo
from ..core.config import ProjectConfig

def cmd_init(args):
    """Initializes a new SIVO project configuration based on an SVG file."""
    svg_path = args.svg_file
    if not os.path.exists(svg_path):
        print(f"Error: SVG file '{svg_path}' not found.", file=sys.stderr)
        sys.exit(1)

    output_path = args.output or "project.json"
    if os.path.exists(output_path) and not args.force:
        print(f"Error: Output file '{output_path}' already exists. Use --force to overwrite.", file=sys.stderr)
        sys.exit(1)

    try:
        # Load the SVG to extract elements
        sivo_app = Sivo.from_svg(svg_path)
        metadata = sivo_app.get_metadata()

        mappings = {}
        for obj in metadata.get("objects", []):
            mappings[obj["id"]] = {
                "tooltip": f"{obj['id']} tooltip",
                "html": f"<h3>{obj['id']}</h3><p>Description goes here.</p>"
            }

        # Create the initial config
        config = {
            "svg_file": os.path.basename(svg_path),
            "mappings": mappings
        }

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=2)

        print(f"Successfully initialized SIVO project at '{output_path}'.")

    except Exception as e:
        print(f"Error initializing project: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_validate(args):
    """Validates an SVG file and its configuration."""
    config_path = args.config_file
    if not os.path.exists(config_path):
        print(f"Error: Configuration file '{config_path}' not found.", file=sys.stderr)
        sys.exit(1)

    try:
        # Load config and validate the mapping against the SVG
        sivo_app = Sivo.from_config(config_path)
        print(f"Success: Configuration '{config_path}' and its associated SVG are valid.")
    except Exception as e:
        print(f"Validation failed: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_export(args):
    """Exports a SIVO configuration to an interactive HTML bundle."""
    config_path = args.config_file
    if not os.path.exists(config_path):
        print(f"Error: Configuration file '{config_path}' not found.", file=sys.stderr)
        sys.exit(1)

    output_path = args.output or "output.html"

    try:
        sivo_app = Sivo.from_config(config_path)
        sivo_app.to_html(output_path)
        print(f"Successfully exported interactive HTML to '{output_path}'.")
    except Exception as e:
        print(f"Export failed: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="SIVO (SVG Interactive Vector Objects) CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # init command
    parser_init = subparsers.add_parser("init", help="Initialize a project.json from an SVG file")
    parser_init.add_argument("svg_file", type=str, help="Path to the source SVG file")
    parser_init.add_argument("-o", "--output", type=str, default="project.json", help="Output JSON file path")
    parser_init.add_argument("-f", "--force", action="store_true", help="Overwrite output file if it exists")
    parser_init.set_defaults(func=cmd_init)

    # validate command
    parser_validate = subparsers.add_parser("validate", help="Validate a SIVO project configuration")
    parser_validate.add_argument("config_file", type=str, help="Path to the project.json configuration file")
    parser_validate.set_defaults(func=cmd_validate)

    # export command
    parser_export = subparsers.add_parser("export", help="Export a SIVO project configuration to an HTML bundle")
    parser_export.add_argument("config_file", type=str, help="Path to the project.json configuration file")
    parser_export.add_argument("-o", "--output", type=str, default="output.html", help="Output HTML file path")
    parser_export.set_defaults(func=cmd_export)

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        sys.exit(1)

    args.func(args)

if __name__ == "__main__":
    main()
