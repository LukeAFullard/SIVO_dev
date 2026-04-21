# Template Styles Example

This example demonstrates how to apply global template styles to a Sivo application.

It takes an existing SVG template (`bento_grid_template.svg`) and applies different pre-configured visual styles, such as "dark_mode", "minimalist", "cyberpunk", "glassmorphism", and "neon". It shows how standard Sivo properties like background, borders, and effects are updated automatically by `apply_template_style()`.

## What is being tested/demonstrated
- Loading an SVG template using `Sivo.from_svg()`.
- Applying different preset styles using the `apply_template_style()` method.
- Configuring a default panel position using `default_panel_position="right"`, and also enforcing it in a mapping.
- Verifying that interactivity (e.g., tooltips and side panels via `map()`) works alongside visual styling.

## Running the example
To regenerate the interactive HTML files, simply run the Python script:

```bash
python3 main.py
```

This will produce several `_styled.html` files in this directory, one for each style applied.

## Key Code Snippets

### Setting the panel position and loading the SVG
```python
# Initialize Sivo from an SVG template. We set default_panel_position so that mapped html has a panel.
sivo_app = Sivo.from_svg(template_path, default_panel_position="right")
```

### Applying the template style
```python
# Apply the chosen global style preset
sivo_app.apply_template_style("cyberpunk")
```

### Adding a mapping alongside the style
```python
# Interactivity works alongside the style
sivo_app.map(
    element_id="bento-hero",
    tooltip=f"{style.capitalize()} Hero Section",
    html=f"<h3>{style.capitalize()}</h3><p>This is the {style} template style.</p>",
    glow=True,
    panel_position="right"
)
```
