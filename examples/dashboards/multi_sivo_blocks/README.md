# Multi-SIVO Blocks Dashboard

This example demonstrates how to create a multi-block dashboard containing multiple separate SIVO instances using the `SivoDashboard` class.

## Overview

The `SivoDashboard` class allows you to assemble an arrangement of multiple SIVO interactive SVGs into a single HTML file with a responsive grid layout. Instead of creating a massive, monolithic single SVG, you generate multiple standalone `Sivo` instances and stitch them together.

In this specific example, a mock **Systems Command Center** is built, displaying:
1. **Global Active Nodes** (A world map SVG visualization).
2. **US-East Topology** (An infrastructure tree topology).
3. **Latency Trend** (A timeline metrics graph).

## Key Concepts

- **Independent Blocks:** Three separate `Sivo.from_string()` instances are created, each managing its own internal map and interactions (`tooltip`, `hover_color`, etc.).
- **Grid Setup:** `SivoDashboard(title="Systems Command Center", columns=2)` defines a 2-column grid layout constraint.
- **Column Spanning:** Using `col_span`, you can control the width each visualization occupies:
  - The `global_map` sets `col_span=2`, meaning it will span across the full width (both columns).
  - The `topology` and `latency_metrics` maps both leave `col_span` at 1, causing them to sit side-by-side on the same row.
- **Layout Scaling:** `layout_size` parameter in `Sivo.from_string` allows constraining the relative scaling of each SVG inside its respective dashboard block container (e.g. `layout_size="80%"`).

## Running the Example

Run the script from the repository root:
```bash
PYTHONPATH=src python examples/dashboards/multi_sivo_blocks/main.py
```

This will produce `output.html` in the current directory, demonstrating the responsive dashboard flow.
