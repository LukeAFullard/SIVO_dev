# Layer Toggles

## Description
Must use render_mode="svg" to correctly toggle visibility of unmapped generic <g> layer wrappers Add layer toggles to create an interactive legend Add standard interactive mapping to an element inside a layer

## Relevant Code
```python
sivo_app = Sivo.from_string(svg_content, render_mode="svg")
sivo_app.add_layer_toggle(label="Base Map", element_ids=["layer_basemap"], default_visible=True)
sivo_app.add_layer_toggle(label="Electrical Wiring", element_ids=["layer_wiring"], default_visible=True)
sivo_app.add_layer_toggle(label="HVAC Systems", element_ids=["layer_hvac"], default_visible=False) # Hidden by default
sivo_app.map("wire1", tooltip="Main Power Line")
sivo_app.to_html(output_path)
```
