# Drillthrough Transitions

This example demonstrates how to create a "drill-through" interaction that transitions between two separate, standalone HTML pages. Unlike a "drill-to" (`SivoProject`), which loads multiple SVG views dynamically within a Single Page Application (SPA), drill-through is essentially a hard link to another external URL or HTML file.

## Features Demonstrated

1. **Multi-File Linking:** Using `drill_through` in `sivo.map()` to navigate from one standalone SIVO instance to another, loading an entirely different page in the browser.
2. **Page Transitions:** Specifying CSS page transition animations using `drill_transition` (e.g., `"flip"` or `"slide-left"`).

## How it works

The python script `main.py` generates two different `Sivo` instances and exports each to its own HTML file: `page1.html` and `page2.html`.

On `page1.html`, clicking the "Go to Page 2" button navigates to `page2.html`.
On `page2.html`, clicking the "Back to Page 1" button navigates to `page1.html`.

## Relevant Code

```python
# Create Sivo instances directly from SVG strings
app1 = Sivo.from_string(svg_page1, disable_panel=True, disable_zoom_controls=True)
app2 = Sivo.from_string(svg_page2, disable_panel=True, disable_zoom_controls=True)

# Map an element to open a specific external URL or HTML file via drill_through
app1.map("btn_next", drill_through="page2.html", drill_transition="flip", hover_color="#b91c1c")
app2.map("btn_back", drill_through="page1.html", drill_transition="slide-left", hover_color="#a16207")

# Save as separate standalone pages
app1.to_html(output_path="page1.html")
app2.to_html(output_path="page2.html")
```

## Running the Example

```bash
PYTHONPATH=src python3 examples/advanced/drillthrough_transitions/main.py
```

After running the script, open `page1.html` in a web browser.
