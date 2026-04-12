# Breaking News Infographic Example

This example demonstrates how to create a professional, interactive "breaking news" style infographic using Sivo. It simulates an architectural/engineering aesthetic typical of news desk graphic reports.

## What is being shown
- A schematic diagram of a structural collapse incident at a port terminal.
- A timeline of events.
- Interactive hotspots ("zones") highlighting critical areas (e.g., damaged crane, crushed containers).
- Clicking on a hotspot opens a side panel with rich HTML content and integrated ECharts.

## What is being tested
- **Custom CSS:** The use of `custom_css` injected during `sivo_app.to_html()` to override default styles, creating a unique, branded look (e.g., `#info-panel` with a red border).
- **SVG String Rendering:** Constructing the entire visual component as an SVG string directly in Python and using `Sivo.from_string()` to render it.
- **Interactive Mapping:** Using `sivo_app.map()` to target specific SVG IDs (`hotspot_crane`, `hotspot_cargo`).
- **Rich HTML Tooltips:** Utilizing the `html` argument inside `sivo_app.map()` to populate the side panel when an element is clicked.
- **Embedded ECharts:** Embedding a mini bar chart within the side panel by passing a configuration to `echarts_option` inside `sivo_app.map()`.
- **Default Panel Position:** Using the `default_panel_position="right"` configuration setting to display the interactive content in a side panel.

## Key Code Snippets

**Initializing the App with an SVG String & Setting Default Panel Position**
```python
sivo_app = Sivo.from_string(
    svg_content,
    title="Incident Report: Pier 42",
    panel_width="450px",
    disable_zoom_controls=True,
    bounding_coords=[[0, 1414], [1000, 0]],
    default_panel_position="right" # Sets the panel to appear on the right when clicked
)
```

**Mapping an Interactive Element with HTML & ECharts**
```python
sivo_app.map(
    element_id="hotspot_cargo",
    hover_color="#fde68a", glow=True,
    html="""
    <h3>Cargo Impact & Hazmat</h3>
    <p>The falling boom crushed three stacked containers...</p>
    """,
    echarts_option={
        "title": {"text": "Estimated Financial Damages (Millions USD)"},
        # ... additional ECharts config ...
        "series": [
            {"type": "bar", "data": [12.5, 4.2, 1.8, 3.5]}
        ]
    }
)
```

**Injecting Custom CSS**
```python
custom_css = \"\"\"
body { background-color: #f8fafc; }
#chart-container { display: flex; justify-content: center; padding: 40px 0; ... }
.sivo-canvas-wrapper { min-height: 1414px; max-width: 1000px !important; ... }
#info-panel { background: #ffffff !important; border-left: 4px solid #dc2626 !important; ... }
\"\"\"
sivo_app.to_html(output_path, custom_css=custom_css)
```