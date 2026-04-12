# SaaS Metrics Dashboard

This example demonstrates how to build an interactive SaaS metrics dashboard using the `sleek_bento_stats_2026.svg` template. It highlights SIVO's ability to seamlessly integrate textual data filling and ECharts interactive charts into a unified graphical dashboard template.

## What it shows

- **Template Loading**: Loads an SVG template (`3_2/sleek_bento_stats_2026.svg`) from the built-in SIVO templates directory via `Sivo.from_svg()`.
- **Text Injection**: Uses `app.fill_template_zone()` to populate placeholder texts within the SVG with dynamic real-world numbers (like ARR, Conversion rates, and NPS score) while customizing font size, weight, and color.
- **Interactive Charts**:
    - **Bar Chart**: Mapped to `bento-hero` showing quarterly ARR growth. Clicking this zone opens an interactive ECharts bar chart in the side panel (using `panel_position="right"`).
    - **Pie Chart**: Mapped to `bento-top-right` displaying subscription distribution, which also opens in the right panel upon interaction.
    - **Gauge Chart**: Mapped to `bento-bottom-right` presenting the Net Promoter Score, displaying in the left panel (`panel_position="left"`).

## Usage

Ensure dependencies are installed, then run:

```bash
PYTHONPATH=src python examples/infographics/saas_metrics_dashboard/main.py
```

This will generate a `saas_dashboard.html` file in the same directory. Open it in your web browser to explore the interactive SaaS dashboard.

## Key Code Snippets

Loading the specific dashboard template:
```python
app = Sivo.from_svg(
    template_path,
    disable_zoom_controls=True,
    lock_canvas=True,
    theme="dark"
)
app.apply_template_style("dark_mode")
```

Replacing SVG text placeholders with metrics:
```python
app.fill_template_zone("hero-value-placeholder", "$12.4M", font_size=64, font_weight="800", color="#f8fafc")
```

Mapping interactive components to designated SVG zones:
```python
app.map_bar_chart(
    element_id="bento-hero",
    title="ARR Growth by Quarter",
    categories=["Q1", "Q2", "Q3", "Q4"],
    data=[8.2, 9.5, 11.1, 12.4],
    color="#3b82f6",
    tooltip="Click to view quarterly ARR growth ($M)",
    panel_position="right"
)
```
