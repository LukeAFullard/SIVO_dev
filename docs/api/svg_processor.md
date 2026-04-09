---
Last Updated: 2026-04-09
SIVO Version: 0.1.0
---

# SVG Processor API Reference

This document provides a technical reference for the modules responsible for parsing, normalizing, and manipulating SVG documents, located in the `src/sivo/svg/` directory.

SIVO utilizes `lxml` for robust, secure, and fast XML parsing.

## `SVGParser` (`src/sivo/svg/parser.py`)

The `SVGParser` class is the main entry point for loading and interacting with SVG content.

### Initialization

```python
def __init__(self, filepath_or_string: str, is_file: bool = True, simplify_tolerance: float = None)
```
*   **`filepath_or_string`**: The path to the SVG file or the raw XML string.
*   **`is_file`**: Boolean indicating if the first argument is a file path.
*   **`simplify_tolerance`**: If provided, runs a Douglas-Peucker simplification algorithm on heavy paths to reduce file size.

*Security Note:* The parser is explicitly configured to prevent XML External Entity (XXE) attacks (`resolve_entities=False`, `no_network=True`).

### Key Methods

#### `process_elements()`
Iterates through all relevant SVG nodes (`path`, `rect`, `circle`, `g`, `polygon`, `polyline`, `text`, `tspan`) and extracts their `id`, `name`, tag type, path data (if applicable), and bounding box.
*   **Returns**: `List[Dict[str, str]]`
*   *Side Effect*: If an element has an `id` but no `name`, it automatically injects a `name` attribute matching the `id`, as ECharts relies on `name` for data mapping.

#### `get_viewbox()`
*   **Returns**: `str` representing the SVG's `viewBox` attribute.

#### `add_shape(tag: str, attributes: Dict[str, str])`
Programmatically appends a new SVG node to the root document.
*   **`tag`**: The shape type (e.g., `'rect'`).
*   **`attributes`**: A dictionary of valid SVG attributes. Supports a special `text_content` key for injecting inner text.

#### `to_string()`
*   **Returns**: The fully processed, normalized XML document as a string.

---

## `SVGNormalizer` (`src/sivo/svg/normalizer.py`)

This class is automatically invoked by `SVGParser` upon initialization to prepare raw SVGs for ECharts compatibility.

### `normalize()`
Executes the full normalization pipeline:
1.  **Strips XML Declarations:** Removes `<?xml ... ?>` prefixes if parsing from a string.
2.  **Strips Scripts:** Removes any embedded `<script>` tags for security.
3.  **Applies ViewBox:** If no `viewBox` exists but `width` and `height` are provided, it synthesizes a `viewBox="0 0 width height"`.
4.  **Resolves `<use>` Tags:** See `resolve_use_tags()` below.
5.  **Simplifies Paths:** Runs `simplify_paths()` if a tolerance was provided.

### `resolve_use_tags()`
ECharts' native SVG renderer does not fully support nested SVG `<use>` tags referencing complex `<defs>`.
This method performs an O(N) pass to find all `<use>` tags, locate the referenced element by ID, clone it, wrap it in a `<g>` tag, apply the appropriate coordinate transformations (`x`, `y`, `transform`), and replace the original `<use>` tag in the DOM.

### `simplify_paths(tolerance: float)`
Applies a basic Douglas-Peucker distance-based simplification algorithm to reduce the number of points in straight line segments (`L`), `<polygon>`, and `<polyline>` elements. Extremely useful for reducing the payload size of heavy GIS-exported SVGs.

---

## `metadata` (`src/sivo/svg/metadata.py`)

A collection of utility functions for calculating coordinate bounds.

### `parse_coord(coord_str: Optional[str]) -> float`
Safely parses SVG coordinate strings (which may include scientific notation or pixel suffixes) into floats.

### `get_bounding_box(elem: etree._Element) -> Optional[List[float]]`
Calculates a basic bounding box `[min_x, min_y, max_x, max_y]` for an SVG element.
Supports `rect`, `circle`, `ellipse`, `line`, `polygon`, `polyline`, and `path` tags.
For complex `<path>` elements containing bezier curves (`C`, `S`, `Q`, `T`), it approximates the bounding box using the control points.
