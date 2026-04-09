---
Last Updated: 2026-04-09
SIVO Version: 0.1.0
---

# Configuration API Reference

This document provides a comprehensive reference for all the configuration models available in the SIVO framework (`src/sivo/core/config.py`). These models dictate how individual elements, bindings, overlays, and overall SIVO projects are configured and rendered.

All configurations are defined as strict Pydantic models.

---

## Element Configuration

### `ElementConfig`
Configuration for a single SVG element's interactions and theme. When creating interaction mappings, this dict defines everything for that single element.

**Attributes:**
- `aria_label` (`Optional[str]`): Screen reader label.
- `role` (`Optional[str]`): ARIA role.
- `tabindex` (`Optional[str]`): Tabindex for keyboard navigation.
- `tooltip` (`Optional[str]`): Simple tooltip text.
- `html` (`Optional[str]`): HTML content.
- `url` (`Optional[str]`): External URL to link to.
- `drill_to` (`Optional[str]`): Target SVG ID for drilling down.
- `drill_through` (`Optional[str]`): Target URL for drilling through.
- `drill_transition` (`Optional[str]`): Transition type for drill actions.
- `callback_event` (`Optional[str]`): Event name to fire on click.
- `callback_payload` (`Optional[Dict[str, Any]]`): Payload to pass to the click callback event.
- `hover_callback_event` (`Optional[str]`): Event name to fire on hover.
- `hover_callback_payload` (`Optional[Dict[str, Any]]`): Payload to pass to the hover callback event.
- `social` (`Optional[Dict[str, str]]`): Dict with `provider` and `url`.
- `document` (`Optional[str]`): URL to an external document.
- `map_location` (`Optional[str]`): Geographic location string.
- `analytics` (`Optional[Dict[str, Any]]`): Analytics mapping (`provider`, `event_name`, `payload`).
- `datasource` (`Optional[Dict[str, str]]`): Datasource connection details.
- `external_form` (`Optional[Dict[str, str]]`): External form integration.
- `ecommerce` (`Optional[Dict[str, str]]`): E-commerce connection.
- `rich_media` (`Optional[Dict[str, str]]`): Media embed details.
- `bi` (`Optional[Dict[str, str]]`): BI dashboard configuration.
- `lottie` (`Optional[Dict[str, Any]]`): Lottie animation settings.
- `compare` (`Optional[Dict[str, str]]`): Before/After image comparison.
- `progress_bar` (`Optional[Dict[str, Any]]`): Progress bar visualization settings.
- `confetti` (`Optional[Dict[str, int]]`): Confetti effect particle count and spread.
- `loading` (`Optional[Dict[str, Any]]`): Loading animation config.
- `echarts_option` (`Optional[Dict[str, Any]]`): ECharts configuration option object.
- `map_name` (`Optional[str]`): Optional map name to register for ECharts.
- `map_data` (`Optional[Union[str, dict]]`): GeoJSON or SVG data string to register for the map.
- `context_menu` (`Optional[List[Dict[str, Any]]]`): Context menu mappings.
- `panel_position` (`Optional[str]`): Panel location (`'right'`, `'left'`, `'top'`, `'bottom'`, `'overlay'`).
- `panel_css` (`Optional[str]`): Custom CSS styling for the element's panel.
- `open_by_default` (`bool`): Defaults to `False`.
- `zoom_on_click` (`bool`): Defaults to `False`.
- `zoom_level` (`float`): Defaults to `2.0`.
- `zoom_duration_ms` (`int`): Defaults to `500`.
- `zoom_to` (`Optional[str]`): Specific Element ID to zoom to.
- `zoom_to_size` (`str`): Defaults to `"90%"`.
- `draggable` (`bool`): Defaults to `False`.
- `color` (`Optional[str]`): Fill color.
- `hover_color` (`Optional[str]`): Hover color.
- `hover_image` (`Optional[str]`): URL to an image for hover state.
- `fill_gradient` (`Optional[Dict[str, Any]]`): ECharts gradient definition.
- `fill_pattern` (`Optional[Dict[str, Any]]`): ECharts pattern definition.
- `border_width` (`Optional[float]`): Element stroke width.
- `border_color` (`Optional[str]`): Element stroke color.
- `transparent_lines` (`Optional[bool]`): Transparency switch for element borders.
- `glow` (`Optional[bool]`): CSS glow effect.
- `morph_to_path` (`Optional[str]`): SVG path string to morph into.
- `morph_duration_ms` (`Optional[int]`): Defaults to `1000`.
- `morph_delay_ms` (`Optional[int]`): Defaults to `0`.
- `morph_easing` (`Optional[str]`): Defaults to `"ease-in-out"`.
- `morph_iterations` (`Optional[float]`): Defaults to `1.0`.
- `filter` (`Optional[str]`): SVG filter ID.
- `clip_path` (`Optional[str]`): SVG clipPath ID.
- `mask` (`Optional[str]`): SVG mask ID.
- `transform` (`Optional[str]`): SVG transform attribute.
- `odometer_value` (`Optional[float]`): Value for odometer counter.
- `odometer_duration_ms` (`Optional[int]`): Defaults to `2000`.
- `odometer_format` (`Optional[str]`): Number format for odometer.

---

## Data and API Binding

### `DataBindingConfig`
Configuration for static choropleth generation.
- `data` (`Dict[str, Dict[str, float]]`): Map of Element IDs to property dictionaries.
- `key` (`str`): The key within the properties to use for the choropleth metric.
- `colors` (`List[str]`): Gradient scale colors.
- `min_val` (`float`): Minimum data value.
- `max_val` (`float`): Maximum data value.

### `TimelineBindingConfig`
Configuration for animating choropleth maps over time.
- `data` (`Dict[str, Dict[str, Dict[str, float]]]`): Mapping structured by timestamp/period.
- `key` (`str`): The metric key.
- `colors` (`List[str]`): Gradient scale colors.
- `min_val` (`float`): Minimum data value.
- `max_val` (`float`): Maximum data value.
- `auto_play` (`bool`): Defaults to `True`.
- `play_interval` (`int`): Defaults to `1000`.
- `show_play_btn` (`bool`): Defaults to `True`.
- `loop` (`bool`): Defaults to `True`.
- `control_position` (`str`): Defaults to `"left"`.
- `symbol` (`str`): Defaults to `"emptyCircle"`.
- `symbol_size` (`Union[int, List[int]]`): Defaults to `10`.
- `bottom` (`Union[int, str]`): Defaults to `20`.

### `LiveBindingConfig`
Configuration for WebSocket/PubSub real-time updates.
- `url` (`str`): WebSocket server URL.
- `topic` (`str`): Topic/channel to subscribe to.
- `auth_token` (`Optional[str]`): Optional authorization token.
- `reconnect_attempts` (`int`): Defaults to `5`.
- `fallback_polling_interval` (`int`): Defaults to `0` (disabled).

### `ApiBindingConfig`
Configuration for Live API & Database Connections via polling.
- `url` (`str`): The API endpoint to poll.
- `polling_interval_ms` (`int`): Defaults to `5000`.
- `method` (`str`): HTTP method (e.g., `'GET'`, `'POST'`). Defaults to `"GET"`.
- `headers` (`Optional[Dict[str, str]]`): Optional HTTP headers.
- `payload` (`Optional[Dict[str, Any]]`): JSON payload for POST.
- `data_path` (`Optional[str]`): Dot-notation path to extract the relevant data array/object from the response.

---

## Advanced Overlays

### `HexbinConfig`
Configuration for hexagonal binning maps.
- `data` (`List[Dict[str, Any]]`): List containing `'coord'` and `'value'`.
- `hex_size` (`float`): Size/radius. Defaults to `15.0`.
- `color_palette` (`List[str]`): Scale colors. Defaults to `["#e0f3f8", "#014636"]`.
- `min_opacity` (`float`): Defaults to `0.3`.
- `max_opacity` (`float`): Defaults to `0.9`.
- `stroke_color` (`str`): Defaults to `"#ffffff"`.
- `stroke_width` (`float`): Defaults to `1.0`.

### `DotDensityConfig`
Configuration for dot density maps.
- `data` (`Dict[str, Dict[str, Any]]`): Element data containing `'value'`, `'coord'`, `'bbox'`, and `'d'`.
- `dot_size` (`float`): Defaults to `3.0`.
- `dot_color` (`str`): Defaults to `"rgba(255, 0, 0, 0.8)"`.
- `dots_per_value` (`float`): Render ratio. Defaults to `1.0`.

### `ProportionalSymbolConfig`
Configuration for proportional symbol maps.
- `data` (`Dict[str, Dict[str, Any]]`): Element data containing `'value'` and `'coord'`.
- `min_size` (`float`): Defaults to `10.0`.
- `max_size` (`float`): Defaults to `50.0`.
- `color` (`str`): Defaults to `"rgba(255, 0, 0, 0.6)"`.
- `is_pulse` (`bool`): Render animated ripples. Defaults to `False`.

### `SpikeMapConfig`
Configuration for spike map overlays.
- `data` (`Dict[str, Dict[str, Any]]`): Element data containing `'value'` and `'coord'`.
- `max_height` (`float`): Defaults to `100.0`.
- `base_width` (`float`): Defaults to `10.0`.
- `color` (`str`): Defaults to `"rgba(255, 0, 0, 0.8)"`.

### `ConnectionConfig`
Configuration for flow and edge connections between elements.
- `source_id` (`str`): The starting Element ID.
- `target_id` (`str`): The destination Element ID.
- `label` (`str`): Edge text label. Defaults to `""`.
- `color` (`str`): Defaults to `"#ff3333"`.
- `width` (`float`): Defaults to `2.0`.
- `animation_speed` (`float`): Defaults to `3.0`.
- `type` (`str`): Line type (e.g., `'solid'`). Defaults to `"solid"`.
- `opacity` (`float`): Defaults to `0.6`.
- `flow_effect` (`bool`): Display animated flow markers. Defaults to `False`.
- `effect_symbol` (`str`): Flow marker symbol. Defaults to `"circle"`.
- `effect_size` (`float`): Flow marker size. Defaults to `3.0`.

---

## Narratives and Modals

### `ScrollytellingStepConfig`
Configuration for a step in a scrollytelling narrative block.
- `content` (`str`): HTML text content.
- `zoom_to` (`Optional[str]`): Target Element ID to zoom.
- `zoom_to_size` (`str`): Viewport fill percentage. Defaults to `"90%"`.
- `zoom_level` (`float`): Magnification level. Defaults to `2.0`.
- `colors` (`Optional[Dict[str, str]]`): Map Element IDs to colors during this step.
- `show_tooltips` (`Optional[List[str]]`): Element IDs to auto-display tooltips for.
- `audio_url` (`Optional[str]`): Voiceover track to play.

### `TourStepConfig`
Configuration for a step in a guided modal tour.
- `content` (`str`): HTML text for the modal.
- `zoom_to` (`Optional[str]`): Target Element ID to zoom.
- `zoom_to_size` (`str`): Viewport fill percentage. Defaults to `"90%"`.
- `zoom_level` (`float`): Magnification level. Defaults to `2.0`.
- `show_tooltips` (`Optional[List[str]]`): Element IDs to auto-display tooltips for.
- `audio_url` (`Optional[str]`): Voiceover track to play.

### `LayerToggleConfig`
Configuration for an interactive legend toggle.
- `label` (`str`): Display name in the legend.
- `element_ids` (`List[str]`): Target SVG Element IDs grouped by this toggle.
- `default_visible` (`bool`): Defaults to `True`.

### `ScratchoffConfig`
Configuration for a "scratch-off" interactive reveal layer.
- `image_url` (`Optional[str]`): Layer image cover.
- `color` (`str`): Solid color fallback. Defaults to `"#cccccc"`.
- `brush_size` (`int`): Radius of the scratch brush. Defaults to `40`.

---

## Global Project Settings

### `ProjectConfig`
The root state container that defines an entire compiled SIVO map or graphic, including global UI toggles, theme configurations, background styling, and data/binding parameters.

**Key Structural Attributes:**
- `svg_file` (`str`): **Required**. Path to the source SVG file.
- `mappings` (`Dict[str, ElementConfig]`): Defines mappings of element IDs to interactive actions.
- `connections` (`List[ConnectionConfig]`): Edge pathways between elements.

**Global UI & Presentation Flags:**
- `theme` (`str`): Visual theme (`'light'`, `'dark'`). Defaults to `"light"`.
- `render_mode` (`str`): Renderer (`'canvas'`, `'svg'`). Defaults to `"canvas"`.
- `default_panel_position` (`str`): Defaults to `"none"`.
- `disable_panel` (`bool`): Suppresses sliding info panels. Defaults to `False`.
- `panel_width` / `panel_height` (`Optional[str]`): Dimension overrides.
- `panel_css` (`Optional[str]`): Global custom CSS injected to the panel wrapper.
- `disable_resizer` (`bool`): Hides panel resizer. Defaults to `False`.
- `disable_tooltips` (`bool`): Disables default hover popovers. Defaults to `False`.
- `disable_zoom_controls` (`bool`): Hides +/- map controls. Defaults to `False`.
- `lock_scroll_bounds` (`bool`): Prevents panning outside standard coordinates. Defaults to `True`.
- `lock_zoom_out` (`bool`): Prevents zooming below baseline level 1.0. Defaults to `True`.
- `layout_size` (`Optional[str]`): Default `"95%"`.
- `starting_zoom` (`float`): Default `1.0`.
- `enable_a11y` (`bool`): Autogenerate ARIA roles. Defaults to `True`.
- `presentation_order` (`Optional[List[str]]`): Explicit element ID sequence for keyboard/presenter navigation.

**Tools & Modules:**
- `enable_minimap` (`bool`): Show contextual corner map. Defaults to `False`.
- `enable_export` (`bool`): Render capture/snapshot button. Defaults to `False`.
- `lock_canvas` (`bool`): Disable map canvas interaction entirely. Defaults to `False`.
- `fade_unselected` (`bool`): Emphasize active elements by fading out the rest. Defaults to `False`.
- `enable_search` (`bool`): Provide an element/tooltip search bar. Defaults to `False`.
- `enable_brush_selection` (`bool`): Multiple selection via lasso. Defaults to `False`.
- `enable_geocoder` (`bool`): Address search bar. Defaults to `False`.
- `geocode_provider` (`str`): Provider to use (`'nominatim'`). Defaults to `"nominatim"`.
- `geocode_api_key` (`Optional[str]`): Authorization for Maps APIs.
- `enable_fullscreen` (`bool`): Viewport toggler. Defaults to `False`.
- `enable_share` (`bool`): Web Share API integration. Defaults to `False`.
- `enable_data_download` (`bool`): CSV export tool. Defaults to `False`.
- `enable_drawing_tools` (`bool`): Annotations overlay tools. Defaults to `False`.

**Backgrounds and Framing:**
- `title`, `subtitle`, `attribution` (`Optional[str]`): Standard mapping headers/footers.
- `watermark` (`Optional[str]`): Fixed overlay (e.g., logo).
- `ambient_effect` (`Optional[str]`): Environment particle overlay (e.g., `'snow'`, `'rain'`).
- `ambient_speed` (`float`): Multiplier for ambient effect speeds. Defaults to `1.0`.
- `bounding_coords` (`Optional[List[List[float]]]`): Global geospatial projection bounds.
- `graphic` (`Optional[List[Dict[str, Any]]]`): Native ECharts graphic instances.
- `border_image_url`, `border_image_position`, `border_image_width`, `border_image_opacity`, `border_image_grayscale`: Settings for a stylized frame around the chart.
- `background_image_url`, `background_image_opacity`, `background_image_grayscale`: Global backdrop layer configuration.
- `svg_background_image_url`, `svg_background_image_opacity`, `svg_background_image_grayscale`, `svg_background_image_insert_after`: Map canvas backdrop layers (these move when panned).
- `transparent_template_lines` (`bool`): Hides structural strokes of SVG templates. Defaults to `False`.

**Overlays and Bindings:**
- `data_binding` (`Optional[DataBindingConfig]`)
- `timeline_binding` (`Optional[TimelineBindingConfig]`)
- `live_binding` (`Optional[LiveBindingConfig]`)
- `api_binding` (`Optional[ApiBindingConfig]`)
- `scrollytelling` (`Optional[List[ScrollytellingStepConfig]]`)
- `tour` (`Optional[List[TourStepConfig]]`)
- `layer_toggles` (`Optional[List[LayerToggleConfig]]`)
- `scratchoff` (`Optional[ScratchoffConfig]`)
- `proportional_symbols` (`Optional[ProportionalSymbolConfig]`)
- `spike_map` (`Optional[SpikeMapConfig]`)
- `hexbin` (`Optional[HexbinConfig]`)
- `dot_density` (`Optional[DotDensityConfig]`)

**Development and Testing Flags:**
- `build_js` (`bool`): Attempt minification/bundling pass. Defaults to `False`.
- `enable_e2e_testing` (`bool`): Provisions scaffold points for Playwright integration tests. Defaults to `False`.
