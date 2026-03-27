# Quad Grid Zooming Example

This example demonstrates how to use the `quad_grid` template in a dashboard while implementing zoom interactivity within individual panels.

Each of the four quadrants is a distinct SIVO block containing a custom SVG.
The SVG has two interactive regions (`main_area` and `detail_area`).
Clicking on `detail_area` uses the SIVO `zoom_to="detail_area"` argument to smoothly transition the view inside that specific block.

### Key Features Used:
- `SivoDashboard(template="quad_grid")`: Loads the 2x2 square grid layout.
- `Sivo.from_string(...)`: Dynamically generates the blocks using a shared SVG string.
- `zoom_to="target_id"`: Calculates the layout scale for zooming.
- `zoom_to_size="80%"`: Tells the camera what size the target element should fill on screen.
