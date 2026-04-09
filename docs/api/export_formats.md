---
Last Updated: 2026-04-09
SIVO Version: 0.1.0
---

# T-04: Export Formats API Reference

This document details the various output and export formats supported by SIVO, including programmatic HTML file generation, client-side images and PDFs, and JSON project serialization.

## 1. HTML Export (`sivo.to_html()`)

The primary mechanism for generating interactive SIVO content is compiling the Python configuration down into a standalone HTML file.

*Note: The core API uses `to_html()`. The method `sivo.save()` is invalid and not implemented.*

### Standalone Capabilities
- SIVO outputs are entirely self-contained within the HTML file (except for optional CDN-loaded scripts like ECharts, DOMPurify, or remote media sources).
- They require no backend Python server to run, making them ideal for static hosting (GitHub Pages, S3, Netlify) or embedding as `<iframe>` widgets in external CMS platforms.

### Usage
```python
# For single maps
app = Sivo.from_svg("map.svg")
app.to_html("output_map.html")

# For multi-block dashboards
dash = SivoDashboard(title="My Dash")
dash.to_html("output_dashboard.html")
```

---

## 2. Image Export

SIVO maps are rendered client-side on an HTML5 `<canvas>` (via ZRender/ECharts). SIVO supports extracting static images of the current interactive state.

### Client-Side (User Driven)
- **Built-in Export Button:** If configured via `Sivo.map(enable_export=True)`, the frontend displays a UI control to download the map.
- **Underlying Mechanism:** The client calls the native ECharts API `myChart.getDataURL({ type: 'png', pixelRatio: 2, backgroundColor: '#fff' })`.
- **Formats:** PNG or JPEG are standard. The pixel ratio is artificially increased (e.g., `2`) to ensure high-DPI (Retina) quality.

### Server-Side / Headless (Automated)
SIVO does not include native Python-level image rasterization. To generate screenshots programmatically on a server, use Headless browser testing tools (e.g., Playwright).

**Example Playwright Script:**
```python
from playwright.sync_api import sync_playwright

def snapshot_sivo(html_path, output_image):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"file://{html_path}")

        # Wait for the canvas to render
        page.wait_for_selector("canvas")

        # Take screenshot
        page.screenshot(path=output_image)
        browser.close()
```
*Note: Ensure any local test side-effects (like generating `output_map.html`) are reverted before committing.*

---

## 3. PDF Export (jsPDF)

SIVO integrates the `jsPDF` library on the frontend to support generating multi-page documents or static snapshot reports directly from the browser.

### Tour/Scrollytelling PDF Export
- When utilizing features like Guided Tours (`bind_tour`), the user may be presented with an option to download the tour as a PDF.
- SIVO dynamically detects the usage of these features via `determine_dependencies` in `bundle_generator.py` and injects the `jspdf` CDN script.
- The runtime code (`echarts.html`) verifies if `window.jspdf` is loaded and throws an alert if it is missing before attempting to initialize a `new jsPDF()` document.

---

## 4. JSON State Serialization

For tooling and authoring purposes, SIVO configurations and manual user edits can be serialized into JSON.

### Annotator Tool (`sivo annotate`)
- The local browser-based annotation tool (`src/sivo/cli/tools/annotator.html`) tracks a history of modifications (limited to 50 states to save memory) for undo/redo functionality.
- **Saving Projects:** The UI includes a `Save` button (`#save-project-btn`) which serializes the current SVG and mapping metadata into a JSON format.
- **Pyodide Integration:** In serverless Pyodide environments, there is a dedicated "Save to Pyodide FS" button (`#save-idbfs-btn`) to persist these JSON states across browser reloads using IndexedDB (`idbfs`).
