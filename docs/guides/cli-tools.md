---
Last Updated: 2026-04-09
SIVO Version: 0.1.0
---

# SIVO CLI Tools Guide

SIVO provides a robust Command-Line Interface (CLI) to help you manage your interactive SVG projects. The CLI offers commands to quickly initialize projects, validate configurations, export fully interactive HTML bundles, and annotate SVGs visually via a local web server.

This guide covers the core CLI commands: `init`, `validate`, `export`, and `annotate`.

## 1. Introduction

The `sivo` command is the main entry point for interacting with SIVO from your terminal.

You can view the available commands by running:
```bash
sivo --help
```

## 2. Core Commands

### `sivo init`

**Purpose:** Creates a new SIVO project configuration (JSON format) from an existing SVG file. This command automatically parses the SVG, extracts all elements with valid `id` attributes, and creates an initial configuration file that you can further customize.

**Usage:**
```bash
sivo init <svg_file> [options]
```

**Options:**
- `-o, --output <file>`: The path to save the generated JSON configuration file. (Default: `project.json`)
- `-f, --force`: Overwrite the output file if it already exists.

**Example:**
```bash
sivo init my_map.svg -o my_project.json
```
This will read `my_map.svg` and generate `my_project.json` containing a boilerplate configuration with placeholders for tooltips and HTML content for each identified element.

### `sivo validate`

**Purpose:** Validates an existing SIVO project configuration file and its associated SVG. This ensures that the structure is correct according to the internal Pydantic models and that the configuration correctly references elements within the SVG.

**Usage:**
```bash
sivo validate <config_file>
```

**Example:**
```bash
sivo validate my_project.json
```
If the configuration is valid, SIVO will output a success message. If there are errors (e.g., malformed JSON, invalid schema, or referencing non-existent SVG elements), it will output a detailed error message and exit with a non-zero status code.

### `sivo export`

**Purpose:** Compiles a SIVO configuration and its associated SVG into a standalone, interactive HTML bundle. This file contains everything needed (HTML, CSS, JS, SVG data) to run the interactive experience in a web browser without requiring a backend server.

**Usage:**
```bash
sivo export <config_file> [options]
```

**Options:**
- `-o, --output <file>`: The path to save the exported HTML bundle. (Default: `output.html`)

**Example:**
```bash
sivo export my_project.json -o interactive_map.html
```

### `sivo annotate`

**Purpose:** Starts a local web-based annotation tool to visually inspect SVGs and generate interactive templates. This is a secure local HTTP server running at `127.0.0.1` by default, protecting your system against unintended local network exposure.

The annotator provides a visual interface for mapping data directly to the SVG elements and is incredibly useful for visually verifying mappings before exporting.

**Usage:**
```bash
sivo annotate [options]
```

**Options:**
- `-p, --port <port>`: The port on which to run the local web server. (Default: `8080`)
- `--host <host>`: The host IP to bind the local server to. (Default: `127.0.0.1`)

**Security Note:**
The annotator server actively overrides path translation to ensure the fully resolved real path (`os.path.realpath`) falls strictly within the current working directory, preventing prefix confusion and path traversal vulnerabilities.

**Example:**
```bash
# Starts the annotator on the default host and port (127.0.0.1:8080)
sivo annotate

# Starts the annotator on a specific port
sivo annotate --port 3000
```
