# Multi-View Standalone Example

This example demonstrates how to create a multi-level interactive experience where users can drill down from a main view to a secondary view, all bundled into a single standalone HTML file.

It uses `SivoProject` to combine multiple `Sivo` instances and link them using the `drill_to` feature.

## Purpose

The main purpose of this example is to show how to build an interactive dashboard or map with multiple views (e.g., a high-level map and a detailed floor plan) that operates entirely offline within a single `.html` file.

## Key Code Components

1. **Initialize Multiple Independent SVG Views**:
   We create two separate `Sivo` instances, one for the main map and one for a floor plan:
   ```python
   map_view = Sivo.from_svg(map_path)
   floor_view = Sivo.from_svg(floor_path)
   ```

2. **Map the Drill-Down Interaction**:
   We link an element in the first view (`map_view`) to the second view by using the `drill_to` parameter in `map_view.map()`. The value of `drill_to` corresponds to an internal view ID we will define later.
   ```python
   map_view.map(
       element_id="house",
       tooltip="Enter House",
       drill_to="floor_view",  # Note: mapped to an internal view ID, not a .svg file
       hover_color="orange"
   )
   ```

3. **Bundle Views into a SivoProject**:
   We create a `SivoProject` and add both views. The `initial_view_id` sets the starting view. The view ID used in `add_view` must match the `drill_to` target.
   ```python
   project = SivoProject(initial_view_id="map_view")
   project.add_view("map_view", map_view)
   project.add_view("floor_view", floor_view)
   ```

4. **Export to a Single HTML Bundle**:
   Finally, we export the entire project, containing all views and interactions, to a single HTML file.
   ```python
   project.to_html(output_path)
   ```

## How to Run

1. Ensure SIVO dependencies are installed.
2. Run the script: `PYTHONPATH=src python examples/basic/multi_view_standalone/main.py`
3. Open `output.html` in your web browser.
4. Hover over the house element and click it to drill down into the floor plan view.