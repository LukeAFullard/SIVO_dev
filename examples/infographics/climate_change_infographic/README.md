# Climate Change Infographic Example

This example demonstrates how to build an interactive, glassmorphic climate change dashboard using SIVO.
It utilizes the `glassmorphic_radial_dashboard_2026.svg` template to create a visually appealing interface.

## What is being tested/shown

1. **SVG Template Instantiation:** Initializing `Sivo` with a complex, pre-designed SVG template (`glassmorphic_radial_dashboard_2026.svg`) while locking the canvas and disabling zoom controls for a dashboard-like experience.
2. **Template Styling:** Applying a premium `glassmorphism` style using `app.apply_template_style()`.
3. **Dynamic Text Injection (`fill_template_zone`):** Natively injecting perfectly-scaled SVG `<text>` elements into predefined placeholder zones (e.g., `header-title-top-placeholder`, `center-value-placeholder`) to populate the dashboard with data like CO2 levels, Sea Level Rise, etc. This ensures text scales naturally on all devices without HTML overlay issues.
4. **Interactive Chart Mapping:**
    * Mapping a **Line Chart** (`map_line_chart`) to `glass-card-1` showing Historical CO2 Emissions.
    * Mapping a **Bar Chart** (`map_bar_chart`) to `glass-card-2` showing Global Sea Level Rise.
    * Mapping a **Trendline Scatter Chart** (`map_trendline_chart`) to `glass-card-3` showing Global Surface Temperature Anomaly.
5. **Rich Tooltips (`html`):** Mapping rich HTML content to the `center-hub` element to provide more context about the 1.5°C target when hovered/clicked.
6. **Side Panels (`panel_position`):** Demonstrating the use of `panel_position` (e.g., `"left"`, `"right"`) to explicitly render charts in side panels upon interaction, as the default is `"none"`.

## Running the Example

Run the script from the root directory:

```bash
PYTHONPATH=src python3 examples/infographics/climate_change_infographic/main.py
```

This will output an interactive HTML file at `examples/infographics/climate_change_infographic/climate_change_dashboard.html`.
