# 07 Multi-View Standalone

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
