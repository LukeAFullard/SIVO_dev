# Ambient Effects Styling Example

This example demonstrates how to configure ambient visual effects in the SIVO infographic and dashboard generator. Ambient effects add subtle, animated overlays to your SIVO instances, creating a more immersive visual experience for viewers without interacting with elements manually.

## What is Being Tested/Demonstrated

The included scripts test and demonstrate:

1. **Ambient Effect Overlay (`ambient_effect`)**: We test applying various animated atmospheric effects (like snow, wind, plants, and water reflections) on top of SVGs.
2. **Speed Customization (`ambient_speed`)**: Shows how the speed or intensity of the applied ambient effects can be augmented via the `ambient_speed` parameter.
3. **Theme Integration**: Shows how ambient effects layer neatly with SIVO's built-in light/dark theming and custom SVG backgrounds.
4. **Different Built-in Effects**: The subfolder contains four different files generating their respective html outputs representing different scenarios:
   - `main.py` (`output.html`) - Tests the `snow` ambient effect overlaid on a dark theme winter mountain SVG.
   - `ambient_plants.py` (`ambient_plants.html`) - Showcases the `plants` ambient effect over a custom drawn sunset silhouette SVG with an increased speed multiplier.
   - `ambient_water.py` (`ambient_water.html`) - Showcases the `water` reflection effect overlaid on a custom drawn night river SVG with a lower speed multiplier.
   - `ambient_wind.py` (`ambient_wind.html`) - Tests the `wind` ambient effect over a custom drawn grassy hill scene with a high speed multiplier.

## How it Works

In SIVO, global visual effects can be configured dynamically by setting attributes during the initialization via `Sivo.from_string` (or directly onto an instance attributes like `app.ambient_effect` and `app.ambient_speed`).

### Code Snippets

**Adding the 'snow' effect:**

```python
sivo_app = Sivo.from_string(
    svg_string,
    title="Winter Mountains",
    theme="dark",
    ambient_effect="snow",
    default_panel_position="none",
    disable_panel=True
)
```

**Adding 'plants' with custom speed (`ambient_speed`):**

```python
app = Sivo.from_string(
    svg_content,
    ambient_effect="plants",
    ambient_speed=2.0,  # multiplier for faster plant swaying
    title="Ambient Plants Effect",
    transparent_template_lines=True,
    default_panel_position="none",
    disable_panel=True
)
```

## Running the Example

Run any of the respective files (e.g. `python3 ambient_wind.py`) to generate an interactive HTML output that you can open in your web browser.
