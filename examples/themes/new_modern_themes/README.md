# Modern Themes Example

This example demonstrates the usage of the newly added clean and modern themes in SIVO: `monochrome`, `ocean`, `forest`, `sunset`, and `pastel`.

## What it demonstrates

The `main.py` script initializes a complex dashboard template (`gis_digital_twin_dashboard_2026`) and iteratively applies each of the 5 new themes using `sivo_app.apply_template_style(theme)`.

It generates an individual `.html` output file for each theme, allowing you to visually inspect how the theme engine dynamically rewrites the inline SVG fills, strokes, and backgrounds to achieve completely different aesthetic tones.

## Running the Example

```bash
python main.py
```

This will produce `output_monochrome.html`, `output_ocean.html`, `output_forest.html`, `output_sunset.html`, and `output_pastel.html` in the same directory.
