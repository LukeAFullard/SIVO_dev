# SVG Template Dashboard

This example demonstrates how to use `Sivo.from_template("dashboards/sidebar_layout")` to initialize a dashboard from a pre-built SVG template. It maps content to predefined regions within the template.

## Key Features Demonstrated
- `Sivo.from_template`: Loading built-in SVG templates.
- **Mapping Regions**: Injecting interactive HTML content and tooltips into designated regions of the SVG layout (`sivo_app.map(...)`).
- **Styling Regions**: Applying styles (e.g., `hover_color`) to regions.

## How to Run

```bash
PYTHONPATH=src python examples/dashboards/svg_template_dashboard/main.py
```

This will generate an `output.html` file that you can open in a web browser.
