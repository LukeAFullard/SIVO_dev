# Drilldowns Example

This example demonstrates how to create a multi-level visualization in SIVO using drilldowns. When a user clicks on an element in the top-level SVG map, they are navigated to a completely different SVG view (in this case, going from an exterior view of a house to a floor plan).

## What is being tested/shown

1.  **Multi-View Configuration (`SivoProject`):** Grouping multiple distinct `Sivo` instances into a single project using `SivoProject`, and assigning an `initial_view_id`.
2.  **`drill_to` Action:** Configuring an element to trigger a navigation event using the `drill_to` mapping property. The target is the string ID of the secondary view registered in the project.

## Key Code

**Configuring the Drilldown Action:**
```python
# Main view
main_view = Sivo.from_svg("sample.svg")
main_view.map(
    element_id="house",
    tooltip="Click to enter the house",
    drill_to="floor1_view", # ID of the target view
    hover_color="orange",
    glow=True
)
```

**Registering Views in a Project:**
```python
# Create the secondary view
floor1_view = Sivo.from_svg("floor1.svg")

# Register both views in a SivoProject
project = SivoProject(initial_view_id="main_view")
project.add_view("main_view", main_view)
project.add_view("floor1_view", floor1_view)

# Export the entire project bundle
project.to_html("output.html")
```

## Running the Example

Run this script to generate `output.html`:
```bash
python3 main.py
```
Open `output.html` in your browser. Click on the house shape. The visualization will transition to the secondary floor plan map. In the generated SIVO map, you can use the built-in back button (if available) or the "Back" context menu to return to the parent view.
