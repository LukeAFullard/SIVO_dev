---
Last Updated: 2026-04-09
SIVO Version: 0.1.0
---

# Annotator Server API Reference

The `AnnotatorHandler` and associated functions in `src/sivo/cli/tools/annotator.py` provide a local web-based tool for inspecting and annotating SVG files. The tool consists of a local HTTP server that serves a bundled HTML application.

## Overview

The annotator server is started via the SIVO CLI:

```bash
sivo annotate --port 8080 --host 127.0.0.1
```

By default, the server binds to `127.0.0.1` to prevent unintended local network exposure.

## Architecture

The server uses Python's built-in `http.server` and `socketserver` modules. It serves a single HTML file (`annotator.html`) that contains the frontend logic for the annotation tool.

### `AnnotatorHandler`

A custom HTTP request handler that extends `http.server.SimpleHTTPRequestHandler`.

*   **Security Feature**: Overrides `translate_path(self, path)` to prevent directory traversal attacks. It uses `os.path.realpath` to resolve symlinks and `os.path.commonpath` to ensure the requested file resides strictly within the current working directory.
*   **Routing**: Intercepts requests to `/` or `/index.html` and serves the bundled `annotator.html` tool. Other requests fall back to the standard file serving mechanism, allowing the frontend to load local SVG images from the directory where the command was run.

### `ReusableTCPServer`

A custom TCP server that extends `socketserver.TCPServer`. Sets `allow_reuse_address = True` to avoid "Address already in use" errors during rapid restarts.

### `run_annotator_server(port=8080, host="127.0.0.1")`

Starts the HTTP server and automatically opens the user's default web browser to the correct URL (if running on localhost).

### `cmd_annotate(args)`

The CLI entry point for the `sivo annotate` command. Parses arguments and calls `run_annotator_server`. Catches `KeyboardInterrupt` to handle graceful shutdowns.
