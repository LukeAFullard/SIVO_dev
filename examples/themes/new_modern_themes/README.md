# Modern Themes Example

This example demonstrates the usage of the clean and modern themes in SIVO: `monochrome`, `ocean`, `forest`, `sunset`, and `pastel`.

The core feature being demonstrated here is `apply_template_style(theme)`, which alters the visual representation of elements dynamically. Additionally, the setup uses `default_panel_position="none"` and specifies `panel_position` for mapped items.

## What it demonstrates

The `main.py` script initializes a complex dashboard template (`gis_digital_twin_dashboard_2026`) and iteratively applies each of the 5 new themes using `sivo_app.apply_template_style(theme)`.

It generates an individual `.html` output file for each theme, allowing you to visually inspect how the theme engine dynamically rewrites the inline SVG fills, strokes, and backgrounds to achieve completely different aesthetic tones.

## Relevant Code

```python
# Create sivo instance with default panel position set to none
sivo_app = Sivo.from_svg(template_path, default_panel_position="none")

# Map elements, providing custom panel positions for each
sivo_app.map(
    element_id="metric-iot-1",
    html="<h1>IoT Sensor 1</h1><p>Detailed metrics for IoT Sensor 1.</p>",
    panel_position="right"
)

# Apply style dynamically
sivo_app.apply_template_style(theme)
```

## Running the Example

```bash
python main.py
```

This will produce `output_monochrome.html`, `output_ocean.html`, `output_forest.html`, `output_sunset.html`, and `output_pastel.html` in the same directory.
