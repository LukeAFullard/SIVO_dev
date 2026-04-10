# Building Drilldown Example

This example demonstrates how to create a multi-level interactive dashboard (drilldown) by linking multiple SVG files together using SIVO.

## What is being tested/shown

1. **Multi-level Dashboard (Drilldown)**: It shows how to use `SivoProject` to combine multiple SIVO instances into a single navigable project.
2. **`drill_to` Parameter**: It demonstrates how to transition between views by clicking on a specific SVG element, configured via the `drill_to` parameter in the `map()` function.
3. **Interactive Styles**: It uses the `hover_color`, `glow`, and `color` parameters to add visual feedback to interactive elements.

## Steps Involved

1. Three SIVO applications are created from individual SVG files representing the building campus, floorplan, and room view:
   ```python
   building_app = Sivo.from_svg("building.svg")
   floorplan_app = Sivo.from_svg("floorplan.svg")
   room_app = Sivo.from_svg("room.svg")
   ```

2. Interactive behaviors and transitions are mapped using the `map()` method. Notice how `drill_to` provides the link between instances using the string names that will be assigned to each view.
   ```python
   # Map Building -> Floorplan
   building_app.map(
       element_id="building1",
       drill_to="floorplan_view",
       hover_color="#b6c99c",
       glow=True
   )

   # Map Floorplan -> Room
   floorplan_app.map(
       element_id="roomA",
       drill_to="room_view",
       hover_color="#ff8c85",
       glow=True
   )
   ```

3. A `SivoProject` is initialized with the starting view, and the subsequent views are registered:
   ```python
   project = SivoProject(initial_view_id="building_view")
   project.add_view("building_view", building_app)
   project.add_view("floorplan_view", floorplan_app)
   project.add_view("room_view", room_app)
   ```

4. Finally, the complete set of interactive views is compiled and exported to a standalone HTML file.
   ```python
   project.to_html("output.html")
   ```

When opening the generated `output.html`, you will start at the building view, and by clicking the mapped element (Main Building), the screen will drill down to the floorplan, which similarly drills down to the detailed room view.