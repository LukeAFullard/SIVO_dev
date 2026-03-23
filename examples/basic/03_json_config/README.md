# Basic: JSON Configuration

This example illustrates how to build a Sivo application entirely from a declarative JSON configuration file instead of programmatic Python calls.

## What is being tested/demonstrated
* Loading and configuring an interactive SVG project using a JSON configuration file.
* Initializing the app via `Sivo.from_config()`.
* Exporting the resulting app built from the JSON config to a standalone HTML file.

## Key Configuration (config.json)

```json
{
    "svg_path": "sample.svg",
    "enable_search": true,
    "elements": [
        {
            "id": "sun",
            "tooltip": "The JSON Sun",
            "color": "yellow",
            "hover_color": "gold"
        }
    ]
}
```

## Key Code

```python
# Generate the app from declarative config
sivo_app = Sivo.from_config(config_path)

output_path = os.path.join(os.path.dirname(__file__), "output.html")
sivo_app.to_html(output_path)
```
