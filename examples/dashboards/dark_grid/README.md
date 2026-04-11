# Dark Grid Dashboard Example

This example demonstrates how to build a high-contrast, dark-mode dashboard using the `SivoDashboard`.
It creates a sleek, modern UI suitable for Operations Centers, live system monitoring, or technical readouts, using
ECharts' dark theme support and a custom CSS Grid.

## Key Features Demonstrated

- **Grid Layout**: Setting up a responsive custom grid using `dashboard.set_grid_layout()`.
- **Theme**: Applying a dark theme via `theme="dark"` in `Sivo.from_template()`.
- **HTML Block**: Using `dashboard.add_html_block()` to insert an HTML header spanning across the grid.
- **Metrics Panel**: Using `dashboard.add_metrics_panel()` to automatically render structured `callback_payload` data.
- **Details Panel**: Using `dashboard.add_details_panel()` to render `tooltip` content natively on canvas clicks.

## How to run

Ensure you have dependencies installed, then run:

```bash
PYTHONPATH=src python3 examples/dashboards/dark_grid/main.py
```

Open `output.html` in your browser.
