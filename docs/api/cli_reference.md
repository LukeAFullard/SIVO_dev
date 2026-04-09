---
Last Updated: 2026-04-09
SIVO Version: 0.1.0
---

# CLI API Reference

The SIVO Command Line Interface (CLI) provides a set of tools for initializing, validating, building, and annotating SIVO projects.

The CLI is invoked via the `sivo` command.

## Commands

### `sivo init`

Initializes a new SIVO project configuration based on an input SVG file. It extracts the IDs of elements found within the SVG and builds an initial `project.json` mapping configuration.

**Usage:**
```bash
sivo init <svg_file> [options]
```

**Positional Arguments:**
* `svg_file`: The path to the source SVG file you want to use.

**Options:**
* `-o, --output <file>`: Output JSON file path. Defaults to `project.json`.
* `-f, --force`: Overwrite the output file if it already exists.

---

### `sivo validate`

Validates a SIVO project configuration file (`project.json`) to ensure it maps correctly to its associated SVG and is well-formed.

**Usage:**
```bash
sivo validate <config_file>
```

**Positional Arguments:**
* `config_file`: Path to the `project.json` configuration file to validate.

---

### `sivo export`

Exports a SIVO project configuration to an interactive HTML bundle. This compiles the SVG and the configuration into a standalone HTML file ready for deployment or embedding.

**Usage:**
```bash
sivo export <config_file> [options]
```

**Positional Arguments:**
* `config_file`: Path to the `project.json` configuration file to export.

**Options:**
* `-o, --output <file>`: Output HTML file path. Defaults to `output.html`.

---

### `sivo annotate`

Starts the local web-based SVG template generation and annotation tool. This server allows you to visually inspect SVGs and generate interactive configuration templates.

**Note on Security:** By default, the server binds only to `127.0.0.1` to prevent unintended access from your local network.

**Usage:**
```bash
sivo annotate [options]
```

**Options:**
* `-p, --port <port>`: Port to run the local server on. Defaults to `8080`.
* `--host <host>`: Host to bind the local server to. Defaults to `127.0.0.1` for security.
