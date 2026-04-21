# Drilldown Aspect Ratios SIVO Project

This example demonstrates how to create a multi-view `SivoProject`, enabling navigation (drilldowns) between different templates that have varying aspect ratios (1:1, 3:2, 4:3, 16:10, and mobile 4:7).

## Key Features Demonstrated

1.  **Multi-View Architecture (`SivoProject`)**: Creates a central project instance and registers multiple individual Sivo applications (views) using `project.add_view()`.
2.  **Handling Different Aspect Ratios**: Showcases loading various SVG templates representing different screen proportions:
    *   Home View: 1:1 Aspect Ratio
    *   View 2: 3:2 Aspect Ratio
    *   View 3: 4:3 Aspect Ratio
    *   View 4: 16:10 Aspect Ratio
    *   View 5: 4:7 Mobile Portrait
3.  **Interactive Drilldowns**: Uses the `drill_to` parameter in the `app.map()` method to create navigational links between the views. Clicking specific elements transitions the user interface to the target view.
4.  **Global View Configuration**: Applies common settings across views, such as `lock_zoom_out=True` and enforcing a default interactive panel position (`default_panel_position="overlay"`).
5.  **Hit Area Optimization**: Demonstrates creating transparent, interactive bounding boxes (`app.add_shape()`) overlaid onto `<g>` elements to ensure reliable interaction targets for ECharts event mapping (e.g., in the 3:2 layout).

## Example Code Highlights

**Defining Navigational Links:**

```python
# In the Home App:
home_app.map("node_1_card", drill_to="view_3_2", tooltip="Drilldown to a 3:2 layout.")
home_app.map("node_2_card", drill_to="view_4_3", tooltip="Drilldown to a 4:3 layout.")

# In a Child App (returning home):
app_4_3.map("background", drill_to="home", tooltip="Go back home")
```

**Project Compilation:**

```python
project = SivoProject(initial_view_id="home")
project.add_view("home", home_app)
project.add_view("view_3_2", app_3_2)
project.add_view("view_4_3", app_4_3)
# ...
project.to_html("drilldown_aspect_ratios.html")
```
