# JSON Configuration Example

This example demonstrates how to configure a SIVO interactive map purely via a declarative JSON file (`config.json`), rather than programmatically using Python scripts. This is useful for separating configuration from code, allowing non-developers to edit the visualizations, or generating visualizations dynamically from other systems.

## What is being tested/shown

1.  **Declarative Project Setup:** Passing a `config.json` directly to the SIVO Python API to scaffold the interactive instance.
2.  **Element Mapping from JSON:** Applying tooltips, hover colors, and glow effects to specific SVG element IDs (`sun`, `mountain1`) purely through the `mappings` object in the JSON file.

## Key Code

**`config.json`:**
```json
{
  "svg_file": "sample.svg",
  "mappings": {
    "sun": {
      "tooltip": "The Sun configured via JSON",
      "color": "gold",
      "hover_color": "yellow",
      "glow": true
    },
    ...
  }
}
```

**`main.py`:**
```python
# Generate the app from declarative config
config_path = os.path.join(os.path.dirname(__file__), "config.json")
sivo_app = Sivo.from_config(config_path)

# Export the visualization
sivo_app.to_html(output_path)
```

## Running the Example

Run this script to generate `output.html`:
```bash
python3 main.py
```
Open `output.html` in your browser. Hover over the Sun and the left mountain to see the effects and tooltips applied via JSON.
