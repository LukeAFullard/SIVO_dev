# SIVO Wood Burner Example

## Overview
This example demonstrates a SIVO application with an interactive "Wood Burner" infographic. It features a beautifully animated background scene constructed entirely in native SVG (using standard `<animate>` tags for the flames and dark smoke), demonstrating how SIVO can directly use complex SVGs without losing any embedded SMIL animations.

## Key Features
- **Native SVG Animation**: Shows that SIVO supports `<animate>` tags inherently present in SVGs for continuous background animations (thick dark smoke plumes and glowing fire).
- **Interactive Overlay Tooltips (`html` method)**: Employs the `html` configuration within `app.map()` to trigger a rich text overlay to appear when the woodpile is interacted with.
- **Fixed `panel_position` Overlay**: Demonstrates exactly how to override the default `"none"` panel position to dynamically display tooltips or content in a full-screen center-mounted `"overlay"`.
- **Echarts Clipping Prevention**: Shows a best practice for `app.map` where mapping occurs on an invisible `rect` overlaid over group `<g>` components to prevent ECharts from overwriting native white space shapes or coloring group bounds.

## Code Highlights
The significant parts of the Python implementation:
- Defines the raw SVG including nested SMIL animation tags `<animate>` inside of the smoke `<g>`.
- App initialization (`Sivo.from_string(...)`) using custom settings (`transparent_template_lines=True`) to maintain drawing consistency without ECharts boundary rendering.
- Maps interactive interactions to `woodpile_area` allowing clicks to trigger rich text via the `html` parameter.
- Explicitly sets `panel_position="overlay"` for the tooltip overlay window.
