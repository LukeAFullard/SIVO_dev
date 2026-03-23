# Basic: Multi View Standalone

This example sets up a more complex Sivo application featuring multiple independent SVG views that are bundled together into a single, offline-capable HTML file. It introduces the `SivoProject` class, used to manage applications composed of several views.

## What is being tested/demonstrated
* Creating independent `Sivo` view instances from separate SVG files (`sample.svg` and `floor1.svg`).
* Setting up drill-down interactions between these views using internal view IDs (`drill_to="floor_view"`).
* Compiling multiple `Sivo` views into a cohesive single-page application using the `SivoProject` class.
* Exporting the multi-view application to a single HTML bundle.

## Key Code

```python
# 1. Initialize multiple independent SVG views
# View 1: Main Map
map_view = Sivo.from_svg(map_path)

# Map the house drill-down directly to a view ID ("floor_view")
map_view.map(
    element_id="house",
    tooltip="Enter House",
    drill_to="floor_view",  # Note: mapped to an internal view ID, not a .svg file
    hover_color="orange"
)

# View 2: Floor Plan
floor_view = Sivo.from_svg(floor_path)
floor_view.map(element_id="room101", tooltip="Living Room", color="#aaddff")

# 2. Bundle multiple views into a single, offline HTML project
project = SivoProject(initial_view_id="map_view")

# Add views. The first view added is the default view.
project.add_view("map_view", map_view)
project.add_view("floor_view", floor_view)

# 3. Export to a single bundled HTML file
project.to_html(output_path)
```
