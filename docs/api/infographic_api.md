---
Last Updated: 2026-04-09
SIVO Version: 0.1.0
---

# Infographic API Reference

This document provides the technical API reference for the `Infographic` class (`src/sivo/core/infographic.py`), used for building static and dynamic data visualizations using SVG templates and native ECharts integration.

---

## `Infographic`

The `Infographic` class represents a single SVG-based visualization. It provides methods for mapping interactions, binding data, applying thematic styles, and injecting dynamic UI elements.

### `__init__`

```python
def __init__(
    self,
    parser: SVGParser,
    default_panel_position: str = "none",
    disable_panel: bool = False,
    panel_width: Optional[str] = None,
    panel_height: Optional[str] = None,
    panel_css: Optional[str] = None,
    disable_resizer: bool = False,
    disable_tooltips: bool = False,
    disable_zoom_controls: bool = False,
    lock_scroll_bounds: bool = True,
    lock_zoom_out: bool = False,
    starting_zoom: float = 1.0,
    lock_canvas: bool = False,
    enable_a11y: bool = True,
    render_mode: str = "canvas",
    enable_minimap: bool = False,
    enable_export: bool = False,
    fade_unselected: bool = False,
    theme: str = "light",
    enable_search: bool = False,
    enable_geocoder: bool = False,
    geocode_provider: str = "nominatim",
    geocode_api_key: Optional[str] = None,
    watermark: Optional[str] = None,
    enable_brush_selection: bool = False,
    title: Optional[str] = None,
    subtitle: Optional[str] = None,
    attribution: Optional[str] = None,
    enable_fullscreen: bool = False,
    enable_share: bool = False,
    enable_data_download: bool = False,
    enable_drawing_tools: bool = False,
    ambient_effect: Optional[str] = None,
    bounding_coords: Optional[list[list[float]]] = None,
    graphic: Optional[list[dict]] = None,
    background_image_url: Optional[str] = None,
    background_image_opacity: float = 1.0,
    background_image_grayscale: bool = False,
    svg_background_image_url: Optional[str] = None,
    svg_background_image_opacity: float = 1.0,
    svg_background_image_grayscale: bool = False,
    svg_background_image_insert_after: Optional[str] = None,
    transparent_template_lines: bool = False
)
```

Initializes an `Infographic` instance. Typically, instances are created using class methods like `from_svg`, `from_string`, or `from_config` rather than calling the constructor directly.

### Instantiation Methods

*   **`from_svg(cls, filepath: str, simplify_tolerance: Optional[float] = None) -> "Infographic"`**
    Loads an SVG from a file path.
*   **`from_string(cls, svg_string: str, simplify_tolerance: Optional[float] = None) -> "Infographic"`**
    Loads an SVG from a raw string.
*   **`from_config(cls, config: Union[str, dict, ProjectConfig], base_dir: str = ".") -> "Infographic"`**
    Loads an SVG and applies mappings from a JSON configuration string or dictionary.

### Core Mapping Method

*   **`map(...)`**
    Maps interactions, styles, and data to specific SVG elements. Supports applying actions (e.g., `TooltipAction`, `ClickAction`), hover styles, focus styling, text overlays, and arbitrary callback payloads.

### Dynamic UI and Embedding

*   **`embed_svg(self, element_id: str, filepath_or_string: str, is_file: bool = False, preserve_aspect_ratio: bool = True, keep_target: bool = False, scale_multiplier: float = 1.0)`**
    Embeds another SVG inside the bounding box of a target element.
*   **`add_shape(self, tag: str, attributes: Dict[str, str])`**
    Injects a new raw SVG shape into the canvas.
*   **`add_image_overlay(self, element_id: str, image_url: str, ...)`**
    Positions an HTML `<img>` tag perfectly over an SVG element, useful for responsive image embedding.
*   **`clip_html_to_shape(self, element_id: str, html_str: str, ...)`**
    Uses CSS `clip-path` to perfectly clip a string of raw HTML to the exact shape of an SVG path.
*   **`clip_image_to_shape(self, element_id: str, image_url: str, ...)`**
    A specialized helper that clips an image to an SVG path.
*   **`add_card(self, element_id: str, title: str, ...)`**
    Generates an auto-scaling native SVG card relative to a target element's bounding box.
*   **`add_scalable_progress_bar(self, element_id: str, progress: float, ...)`**
    Generates a responsive SVG progress bar within a target element's bounds.
*   **`add_overlay(self, element_id: str, html: str, ...)`**
    Places absolute-positioned HTML over an element's bounding box center.

### Data Binding and Presentations

*   **`bind_data(self, data: Dict, key: str, colors: list, min_val: float, max_val: float)`**
    Binds static data to element fill colors.
*   **`bind_timeline(self, data: Dict, ...)`**
    Binds time-series data for timeline animations.
*   **`bind_live(self, url: str, topic: str, auth_token: Optional[str] = None)`**
    Binds the map to live data via WebSockets.
*   **`bind_api(self, url: str, polling_interval_ms: int = 5000, ...)`**
    Binds the map to live data via API polling.
*   **`bind_scrollytelling(self, steps: list[Dict])`**
    Configures scrollytelling steps.
*   **`bind_tour(self, steps: list[Dict])`**
    Configures a guided tour presentation.

### Thematic Mapping

*   **`apply_hexbin(...)`**
    Generates a hexbin layer from point data.
*   **`apply_dot_density(...)`**
    Generates a dot density layer.
*   **`apply_proportional_symbols(...)`**
    Generates proportional symbols (circles) over regions based on values.
*   **`apply_spike_map(...)`**
    Generates 3D-like spikes (triangles) based on values.
*   **`apply_flow_map(...)`**
    Generates animated flow lines between coordinates.
*   **`apply_choropleth(...)`**
    Applies a color scale based on a continuous value map.
*   **`apply_value_by_alpha(...)`**
    Bivariate map styling using color for one variable and alpha (opacity) for another.
*   **`apply_categorical_map(...)`**
    Applies discrete colors based on categorical data.

### Utilities

*   **`add_connection(self, source_id: str, target_id: str, ...)`**
    Draws a visual connection line between two elements.
*   **`get_element_center(self, element_id: str) -> Optional[list[float]]`**
    Retrieves the calculated center point of an SVG element.
*   **`to_echarts_html(self, output_path: Optional[str] = None, custom_css: Optional[str] = None, custom_js: Optional[str] = None) -> str`**
    Generates the standalone interactive HTML bundle.
*   **`get_manifest(self) -> Dict`** / **`get_metadata(self) -> Dict`** / **`export_metadata(self, output_path: str)`**
    Utilities for extracting metadata (IDs, bounds) from the parsed SVG.