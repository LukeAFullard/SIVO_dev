---
Last Updated: 2026-04-09
SIVO Version: 0.1.0
---

# Dashboard and Project API Reference

This document provides the technical API reference for building multi-block dashboards (`SivoDashboard`) and multi-view projects (`SivoProject`) in SIVO.

---

## `SivoDashboard`

`src/sivo/core/dashboard.py`

Manages a multi-block responsive dashboard layout (using CSS Grid/Flexbox) instead of a monolithic single SVG. Maps specific `Sivo` instances to layout blocks.

### `__init__(self, title: str = "Dashboard", columns: int = 3, template: str = "default", background_image_url: Optional[str] = None)`

Initializes the dashboard.

*   **`title`** (`str`): The title of the dashboard.
*   **`columns`** (`int`): The number of columns for the default grid layout.
*   **`template`** (`str`): The name of the HTML layout template to use (e.g., `'default'`, `'sidebar_left'`, `'hero_top'`).
*   **`background_image_url`** (`Optional[str]`): URL to a background image that will be automatically applied as a responsive, fixed background on the dashboard. It will also add a translucent backdrop-filter to the grid cards so the image is visible.
*   **`theme`** (`str`): The theme of the dashboard. Defaults to `'light'`. Set to `'transparent'` to remove all card backgrounds, borders, and glassmorphism blurs.

### `add_sivo_block(self, block_id: str, sivo_app: Sivo, col_span: int = 1, slot: str = "main", grid_area: Optional[str] = None)`

Adds a Sivo instance to a specific block/slot in the dashboard layout.

*   **`block_id`** (`str`): Unique identifier for the block.
*   **`sivo_app`** (`Sivo`): The SIVO application instance to embed.
*   **`col_span`** (`int`): The number of columns this block should span.
*   **`slot`** (`str`): The template slot to place this block in (default: `'main'`).
*   **`grid_area`** (`Optional[str]`): The named grid area from the CSS grid layout, if using `set_grid_layout`.

### `add_html_block(self, block_id: str, html_content: str, col_span: int = 1, slot: str = "main", grid_area: Optional[str] = None)`

Adds raw HTML content to a specific block/slot in the dashboard layout.

*   **`block_id`** (`str`): Unique identifier for the block.
*   **`html_content`** (`str`): The raw HTML string to embed.
*   **`col_span`** (`int`): The number of columns this block should span.
*   **`slot`** (`str`): The template slot to place this block in (default: `'main'`).
*   **`grid_area`** (`Optional[str]`): The named grid area from the CSS grid layout.

### `add_details_panel(self, block_id: str, title: str = "Details", placeholder: str = "Select an item to view details.", col_span: int = 1, slot: str = "main", grid_area: Optional[str] = None)`

Adds a pre-built panel that automatically listens to SIVO canvas clicks and renders the clicked element's `html` (tooltip content) mapping.

*   **`block_id`** (`str`): Unique identifier for the panel block.
*   **`title`** (`str`): The title of the panel.
*   **`placeholder`** (`str`): The placeholder text when no item is selected.
*   **`col_span`** (`int`): The number of columns this block should span.
*   **`slot`** (`str`): The template slot.
*   **`grid_area`** (`Optional[str]`): The named grid area.

### `add_metrics_panel(self, block_id: str, title: str = "Metrics", metrics: List[str] = None, col_span: int = 1, slot: str = "main", grid_area: Optional[str] = None)`

Adds a pre-built panel that automatically listens to SIVO canvas clicks and renders the specified keys from the clicked element's `callback_payload` mapping.

*   **`block_id`** (`str`): Unique identifier for the panel block.
*   **`title`** (`str`): The title of the panel.
*   **`metrics`** (`List[str]`): A list of payload keys to render as metrics.
*   **`col_span`** (`int`): The number of columns this block should span.
*   **`slot`** (`str`): The template slot.
*   **`grid_area`** (`Optional[str]`): The named grid area.

### `set_grid_layout(self, desktop: str, mobile: Optional[str] = None)`

Defines the responsive CSS Grid layout using `grid-template-areas`.

*   **`desktop`** (`str`): The CSS `grid-template-areas` string for desktop views.
*   **`mobile`** (`Optional[str]`): The CSS `grid-template-areas` string for mobile views.

### `to_html(self, output_path: Optional[str] = None, custom_js: Optional[str] = None) -> str`

Generates a responsive HTML dashboard containing the assigned blocks.

*   **`output_path`** (`Optional[str]`): The file path to save the HTML file. If `None`, it only returns the string.
*   **`custom_js`** (`Optional[str]`): Custom JavaScript to append to the bundle.
*   **Returns** (`str`): The generated HTML string.

---

## `SivoProject`

`src/sivo/core/project.py`

Manages multiple `Sivo` instances (views) to create a multi-level, standalone interactive HTML bundle with navigation (drilldowns).

### `__init__(self, initial_view_id: str)`

Initializes the project.

*   **`initial_view_id`** (`str`): The ID of the view that should be rendered first when the project loads.

### `add_view(self, view_id: str, sivo_app: Sivo)`

Adds a `Sivo` instance as a navigable view in the project.

*   **`view_id`** (`str`): Unique identifier for the view.
*   **`sivo_app`** (`Sivo`): The `Sivo` application instance for this view.

### `to_html(self, output_path: Optional[str] = None, custom_css: Optional[str] = None, custom_js: Optional[str] = None) -> str`

Generates a single interactive HTML string containing all registered views.

*   **`output_path`** (`Optional[str]`): The file path to save the HTML file. If `None`, it only returns the string.
*   **`custom_css`** (`Optional[str]`): Custom CSS to inject into the bundle.
*   **`custom_js`** (`Optional[str]`): Custom JavaScript to inject into the bundle.
*   **Returns** (`str`): The generated HTML string.
