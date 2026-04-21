# Professional Polish Example

This example demonstrates how to apply professional polish features to a SIVO instance. It showcases the utilization of overall presentation elements such as titles, subtitles, watermarks, attributions, and advanced controls including full-screen, data download, export, and search features.

Additionally, this example explores interactive panel positioning, overriding the default behavior (`panel_position="none"`) by setting a global `default_panel_position="right"`, while mapping specific UI elements to reveal side panels at different positions (e.g., left, right, bottom).

## Key Features Demonstrated

- **Metadata Setup**: Titles, subtitles, attribution, and a watermark.
- **Controls Configuration**: Enablement of full-screen, sharing, search, and export options.
- **Panel Positioning**: Demonstrates how to handle side panels containing custom HTML to present contextual information without obstructing the main map.

## Relevant Code Snippets

```python
sivo_app = Sivo.from_svg(
    svg_path,
    title="Global Demographic Insights",
    subtitle="An interactive exploration of 2024 population density.",
    attribution="Data Source: World Bank | Powered by SIVO",
    watermark="Confidential & Proprietary",
    enable_fullscreen=True,
    enable_share=True,
    enable_data_download=True,
    enable_export=True,
    enable_search=True,
    default_panel_position="right",
    theme="dark"
)

# Example of an element mapped with HTML content and a specific panel position.
sivo_app.map(
    element_id="sun",
    tooltip="The Sun",
    color="gold",
    hover_color="yellow",
    html="""
    <div style='padding:15px; font-family:sans-serif;'>
        <h3 style='color:#333; border-bottom:1px solid #ccc; padding-bottom:5px;'>Solar Impact</h3>
        <p style='color:#555;'>Solar energy is a key factor in the demographic growth of this region.</p>
    </div>
    """,
    panel_position="left"
)
```

## How to Run

1. Make sure you are in the project root.
2. Run the main python script to generate `output.html`.
   ```bash
   python examples/styling/professional_polish/main.py
   ```
3. Open `output.html` in your web browser.
