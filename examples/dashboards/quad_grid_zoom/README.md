# Quad Grid Zooming Example

This example demonstrates how to use the `SivoDashboard` with a CSS Grid layout (`set_grid_layout`) to create a responsive dashboard while implementing zoom interactivity within individual panels.

Each of the four quadrants is a distinct SIVO block containing a custom SVG. The dashboard layout places them in a 2x2 grid on desktop, and stacks them vertically on mobile.
The SVG has two interactive regions (`main_area` and `detail_area`).
Clicking on `detail_area` uses the SIVO `zoom_to="detail_area"` argument to smoothly transition the view inside that specific block.

### Key Features Used:
- `SivoDashboard()`: Initializes a multi-block responsive dashboard.
- `dashboard.set_grid_layout(...)`: Defines a CSS Grid layout using grid-template-areas, enabling custom positioning for desktop and mobile.
- `Sivo.from_string(...)`: Dynamically generates the blocks using a shared SVG string. Note that `default_panel_position` is explicitly set to `"none"`.
- `zoom_to="target_id"`: Calculates the layout scale for zooming.
- `zoom_to_size="80%"`: Tells the camera what size the target element should fill on screen.
- `panel_position="none"`: Used in `sivo.map()` to ensure that no side panel or overlay opens upon interaction, as the primary goal here is to only zoom on the clicked region.
- `dashboard.add_sivo_block(..., grid_area="...")`: Registers a SIVO block within the dashboard and assigns it to a specific `grid-area` defined in the layout.
