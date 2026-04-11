# Bento Box Dashboard Example

This example demonstrates how to build a clean, modern, multi-block dashboard.
It features an auto-fitting CSS Grid layout that naturally arranges panels of different sizes (using `grid_area`)
into an asymmetrical "bento box" style UI.

## Key Features Demonstrated

- **Grid Layout**: Controlling layout spanning with `grid_area` using `dashboard.set_grid_layout()`.
- **Responsive Design**: Passing both `desktop` and `mobile` grid definitions.
- **Cross-block communication**: Clicking elements on the map (like `main_panel`, `metric_box_1`) updates the Details and Metrics panels.
- **HTML Blocks**: Injecting raw HTML using `dashboard.add_html_block()` for headers.
- **Details & Metrics Panels**: Using built-in SIVO panels like `add_details_panel` and `add_metrics_panel`.

## Code Highlights

- `dashboard.set_grid_layout(...)`: Defines the grid template areas.
- `dashboard.add_sivo_block("regional_map", us_map, grid_area="main")`: Adds a SIVO instance to the grid.
- `us_map.map("main_panel", panel_position="right", ...)`: Configures the element to open the right-side panel when clicked. Notice the `panel_position` is explicitly set because the default is `"none"`.

## How to run

Ensure you have SIVO installed and its dependencies (`pip install -r requirements.txt`), then run:

```bash
PYTHONPATH=src python3 examples/dashboards/bento_box/main.py
```

Open `output.html` in your browser.
