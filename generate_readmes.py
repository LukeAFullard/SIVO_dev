import os

readme_content = {
    "01_hello_world": """# 01 Hello World

This example demonstrates the basic usage of SIVO. It loads an SVG file and maps simple interactions (tooltips, colors, hover colors, and glow) to specific elements in the SVG.

### Key Code

```python
sivo_app = Sivo.from_svg(svg_path, enable_search=True)

# Map interactions
sivo_app.map(
    element_id="sun",
    tooltip="The Sun",
    html="<h3>The Sun</h3><p>It is very bright and hot.</p>",
    color="gold",
    hover_color="yellow",
    glow=True
)
```
""",
    "02_url_navigation": """# 02 URL Navigation

This example shows how to configure an SVG element to act as a hyperlink. When clicked, it navigates the user to an external URL.

### Key Code

```python
sivo_app.map(
    element_id="sun",
    tooltip="Click to search about the Sun",
    url="https://en.wikipedia.org/wiki/Sun",
    hover_color="yellow",
    glow=True
)
```
""",
    "03_json_config": """# 03 JSON Config

This example demonstrates how to configure a SIVO application declaratively using a JSON configuration file instead of mapping elements programmatically via Python.

### Key Code

```python
# Generate the app from declarative config
sivo_app = Sivo.from_config(config_path)
```

In `config.json`:
```json
{
  "view": {
    "svg_path": "sample.svg"
  },
  "elements": [
    {
      "id": "sun",
      "tooltip": "The Sun (from config)",
      "color": "gold"
    }
  ]
}
```
""",
    "04_drilldowns": """# 04 Drilldowns

This example illustrates the "drill-down" feature. By clicking on a mapped SVG element, SIVO will transition and load another SVG file, simulating navigating into a deeper level of detail (like entering a house).

### Key Code

```python
# Drill down logic - click on the house to load another SVG.
sivo_app.map(
    element_id="house",
    tooltip="Click to enter the house",
    drill_to="floor1.svg",
    hover_color="orange",
    glow=True
)
```
""",
    "05_custom_assets": """# 05 Custom Assets

This example shows how to inject custom CSS and JavaScript into the generated HTML output. This is useful for custom styling of elements like tooltips or adding additional functionality.

### Key Code

```python
# Custom CSS and JS to inject into the HTML template
custom_css = \"\"\"
    .custom-tooltip { background-color: #333; color: #fff; padding: 10px; }
\"\"\"

custom_js = \"\"\"
    console.log('Hello from custom injected JS!');
\"\"\"

sivo_app.to_html(output_path, custom_css=custom_css, custom_js=custom_js)
```
""",
    "06_html_overlays": """# 06 HTML Overlays

This example demonstrates how to add dynamic HTML overlays over map coordinates. Overlays can display HTML content positioned relative to an SVG element.

### Key Code

```python
# Add HTML overlays over the map coordinates dynamically
sivo_app.add_overlay(
    element_id="sun",
    html="<div style='background: white; padding: 2px 4px; border-radius: 4px; font-weight: bold;'>☀️ 30°C</div>",
    offset_x=20, # offset from the center
    offset_y=-30
)
```
""",
    "07_multi_view_standalone": """# 07 Multi-View Standalone

This example showcases how to create an offline, standalone multi-view project using `SivoProject`. It bundles multiple independent SVG views into a single offline HTML file, allowing seamless navigation between them without a server.

### Key Code

```python
# View 1: Main Map
map_view = Sivo.from_svg(map_path)
map_view.map(element_id="house", drill_to="floor_view")

# View 2: Floor Plan
floor_view = Sivo.from_svg(floor_path)

# Bundle multiple views into a single project
project = SivoProject(initial_view_id="map_view")
project.add_view("map_view", map_view)
project.add_view("floor_view", floor_view)

project.to_html(output_path)
```
""",
    "08_data_binding": """# 08 Data Binding

This example demonstrates how to bind external data to SVG elements and automatically color them based on their value using a color scale gradient.

### Key Code

```python
data = {
    "TX": {"sales": 15000},
    "CA": {"sales": 22000}
}

# Bind data to SVG IDs with a color scale
sivo_app.bind_data(
    data=data,
    key="sales",                     # The metric to base the color on
    colors=["#e0f3db", "#43a2ca"],   # Gradient from min to max
    min_val=0,
    max_val=25000
)
```
""",
    "09_animations_markers": """# 09 Animations & Markers

This example illustrates how to apply built-in animations (e.g., pulse, fade) to SVG elements and how to add dynamic markers (like emojis or icons) anchored to specific elements.

### Key Code

```python
# Apply an animation
sivo_app.map(
    element_id="sun",
    animation="pulse",
    color="orange"
)

# Add a marker
sivo_app.add_marker(
    element_id="mountain1",
    icon="⛰️",
    label="Peak 1",
    offset_y=-30
)
```
""",
    "20_api_fetch": """# 20 API Fetch

This example shows how to configure an element to perform an HTTP fetch request when clicked. The fetched data is then dynamically displayed in an interactive side panel.

### Key Code

```python
# Click the shape to dynamically fetch data and display it in the side panel
sivo_app.map(
    element_id="play_button",
    tooltip="Click to fetch cat fact",
    fetch_url="https://catfact.ninja/fact",
    panel_position="top",
    hover_color="#e68a00",
    glow=True
)
```
"""
}

base_dir = "examples/basic"
for folder, content in readme_content.items():
    path = os.path.join(base_dir, folder, "README.md")
    with open(path, "w") as f:
        f.write(content)

print("READMES generated successfully!")
