# Seasonal Ambient Effects

This example demonstrates how to apply global **ambient effects** to your SIVO maps to create visually engaging, full-screen particle overlays based on different seasons or themes.

## What it does
The script generates four separate HTML files (`spring_effect.html`, `summer_effect.html`, `fall_effect.html`, and `winter_effect.html`). Each iteration uses the same base SVG but passes a different ambient effect keyword into the project configuration to demonstrate the resulting visual output.

## Key Code Snippet

The `ambient_effect` property is set globally in the `ProjectConfig`. Valid options include `'snow'`, `'rain'`, `'particles'`, `'fireflies'`, `'summer'`, `'winter'`, `'spring'`, `'fall'`, `'wind'`, `'water'`, `'plants'`, and `'tree'`.

```python
from sivo import Sivo, ProjectConfig

# Iterate through different seasons and configure ambient effects
seasons = ["spring", "summer", "fall", "winter"]

for season in seasons:
    config = ProjectConfig(
        svg_file=svg_path,
        ambient_effect=season, # This applies the full-screen effect
        title=f"{season.capitalize()} Ambient Effect",
        subtitle="SIVO Custom Ambient Effects",
        theme="dark" if season in ["summer", "winter"] else "light",
        default_panel_position="none" # Disable empty side panel defaults
    )

    sivo_app = Sivo.from_config(config)

    sivo_app.map("house", tooltip=f"Enjoy the {season}!")

    sivo_app.to_html(f"{season}_effect.html")
```
