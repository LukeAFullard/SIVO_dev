---
Last Updated: 2026-04-09
SIVO Version: 0.1.0
---

# T-03: Template Engine API Reference

This document covers the Jinja2 template engine and the logic used to inject Python state into the JavaScript frontend runtime.

## 1. Bundle Generator (`src/sivo/runtime/bundle_generator.py`)

The `bundle_generator.py` file contains the primary logic for taking configured Python view objects, formatting them for JavaScript consumption, and injecting them into HTML templates.

### `format_views_data(views_data: Dict[str, Dict]) -> Dict[str, Dict]`
Re-structures the raw configuration dictionary into a format strictly expected by the JS runtime. This step is critical because:
- It processes complex Pydantic models (like `InteractionMapping` and `Action` objects) by safely converting them to standard dictionaries using `.model_dump()`, `.dict()`, or fallbacks.
- It automatically handles mapping structure differences between single views and Multi-view `SivoProject` configurations.
- It transforms Python styling and theme dictionaries into ECharts-compliant `itemStyle` and `emphasis` objects for each element mapping.
- It resolves visual effects like glows, color maps, and auto-scaling logic into the data series format required by ECharts SVG maps.

### `determine_dependencies(formatted_views: Dict[str, Dict]) -> Dict[str, bool]`
Scans the formatted view configuration to dynamically load required CDN libraries to reduce bundle size.
- **Dependencies detected:** `echarts_stat`, `echarts_wordcloud`, `echarts_liquidfill`, `marked`, `lottie`, `confetti`, `jspdf`.
- **Note:** `dompurify` is strictly enforced to `True` globally to secure dynamic HTML generation, regardless of view configuration.

### `generate_echarts_html(...) -> str`
Compiles the final HTML string.
- Takes the fully formatted views, initial view ID, optional custom CSS/JS, and an output path.
- Injects standard data using the `echarts.html` template.

#### JSON Sanitization Pipeline
When injecting the `views_data` into the Jinja2 template, the output JSON string is aggressively sanitized to prevent Cross-Site Scripting (XSS) breakouts.

```python
views_data=json.dumps(formatted_views, separators=(',', ':'))
    .replace("<", "\\u003c")
    .replace(">", "\\u003e")
    .replace("&", "\\u0026")
```
This ensures that user-defined string content cannot inadvertently close `<script>` tags or inject malicious payloads directly into the global JavaScript namespace.

---

## 2. Jinja2 Template Context

The templates receive several dynamic context variables during the `.render()` process:

### Single View (`echarts.html`) Context:
- `views_data`: Sanitized JSON string containing all views and mappings.
- `initial_view`: Sanitized string ID of the first view to display.
- `custom_css`: Raw user-defined CSS string.
- `custom_js`: Raw user-defined JS string.
- `build_js`: Boolean indicating if `sivo.min.js` should be bundled inline rather than via CDN.
- `bundled_js_content`: String content of the locally minified JS bundle.
- Dependency Flags: Booleans (e.g., `marked`, `lottie`, `dompurify`) toggling specific library script tags.

### Dashboard View (`dashboard_blocks.html`) Context:
Dashboard projects receive all the single view context plus structural layout data.
- `views_data`: Same as above.
- `layout_order`: A list of objects detailing the type and ID of each block layout unit.
- `html_blocks`: Dictionary mapping block IDs to their literal HTML content strings.
- `details_panels`: Dictionary mapping block IDs to tooltip/detail logic.
- `metrics_panels`: Dictionary mapping block IDs to metric logic.
- `title`: The Dashboard title string.
- `columns`: Default column integer configuration for grids.
- `desktop_grid` / `mobile_grid`: Optional CSS grid template area string strings for layout control.

---

## 3. Template Directory Structure (`src/sivo/runtime/templates/`)

All HTML files rendered by SIVO exist in this directory.

### `echarts.html`
This is the core, single-view client runtime for standard SIVO maps and projects.
- Injects the `window.SivoData` object.
- Initializes the `viewHistory` state manager for multi-level drilldowns.
- Implements the primary `ECharts` instantiation bound to the `sivo-main-container`.
- Runs post-DOMPurify node injection logic (handling iframes and strict CSP boundaries).

### `dashboard_blocks.html`
This runtime extends the core functionality to support multi-block CSS Grid Builder applications.
- Dynamically iterates over `layout_order` to construct multiple HTML containers (e.g., `sivo-block-xxx`, `html-block-xxx`).
- Iterates to bind discrete ECharts instances to the appropriate dynamically generated grid boxes.
- Synchronizes interactions and tooltip content states between individual ECharts maps and static metric/details panels.

### `sivo_bundle.js`
The entrypoint for local client-side script building. Uses module bundlers (if local execution `build_js` is required) to package dependencies like DOMPurify directly.