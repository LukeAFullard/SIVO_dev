---
Last Updated: 2026-04-09
SIVO Version: 0.1.0
---

# T-01: Sivo Class API Reference

This document provides a comprehensive API reference for the main `Sivo` class located in `src/sivo/core/sivo.py`.

The `Sivo` class serves as the primary declarative Python API for the framework, managing the lifecycle of importing SVGs, mapping data, and bundling output without requiring users to write JavaScript.

## `Sivo`

### Class Attributes

The `Sivo` class delegates most of its operations to the `Infographic` instance.

### Instantiation Methods

#### `from_svg(filepath: str, **kwargs) -> Sivo`
Initializes a new SIVO instance from a local SVG file.
*   **filepath**: Path to the SVG file.
*   **kwargs**: Additional configuration settings (e.g., `theme`, `lock_canvas`).

#### `from_string(svg_string: str, **kwargs) -> Sivo`
Initializes a new SIVO instance directly from an SVG string.
*   **svg_string**: The raw SVG content.
*   **kwargs**: Additional configuration settings.

#### `from_template(template_name: str, **kwargs) -> Sivo`
Initializes a SIVO instance using one of the built-in aspect-ratio templates (e.g., `'16_10'`, `'1_1'`).
*   **template_name**: The name of the built-in template.
*   **kwargs**: Additional configuration settings.

### Core Methods

#### `map(element_id: str, **kwargs) -> Sivo`
Maps interactive behaviors and styling to a specific SVG element (via its `id`).
*   **element_id**: The `id` attribute of the SVG element (`<path>`, `<g>`, etc.).
*   **kwargs**: Parameters mapping to `ElementConfig` and various action models (e.g., `tooltip`, `color`, `drilldown_target`).
*   **Returns**: `self` for method chaining.

#### `get_center(element_id: str) -> Optional[list[float]]`
Gets the center coordinate `[x, y]` of a specific element, useful for programmatic zoom.

#### `to_html(output_path: Optional[str] = None, custom_css: Optional[str] = None, custom_js: Optional[str] = None) -> str`
Generates the interactive HTML string (bundle) containing the ECharts map, Jinja2 template, and mapped behaviors.
*   **output_path**: Optional file path to save the generated HTML.
*   **custom_css**: Optional CSS string to inject. Must be sanitized.
*   **custom_js**: Optional JS string to inject.
*   **Returns**: The bundled HTML string.

#### `to_svg(output_path: Optional[str] = None) -> str`
Returns the processed SVG as a string.
*   **output_path**: Optional file path to save the SVG.
*   **Returns**: The SVG string.

#### `to_html_compare(other_sivo: 'Sivo', output_path: Optional[str] = None, custom_css: Optional[str] = None, custom_js: Optional[str] = None) -> str`
Generates a specialized interactive HTML string that renders TWO Sivo canvases with a native before/after drag slider separating them natively.
*   **other_sivo**: Another `Sivo` instance to compare against.

#### `get_manifest() -> Dict`
Returns the interaction manifest JSON data containing structure and mappings.

#### `get_metadata() -> Dict`
Returns metadata (bounding boxes, tags, IDs) of all processed SVG elements.

#### `export_metadata(output_path: str)`
Exports the element metadata to a JSON file.

### Static Methods

#### `fetch_image_base64(url: str) -> str`
Fetches an image from a URL and returns it as a base64 data URI. This includes SSRF protection to block local network access.
