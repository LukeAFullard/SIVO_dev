# Minimap Export

## Description
Enable minimap and export capabilities

## Relevant Code
```python
sivo_app = Sivo.from_string(svg_content, enable_minimap=True, enable_export=True)
sivo_app.map("zone_nw", tooltip="North West Zone", hover_color="#94a3b8")
sivo_app.map("zone_ne", tooltip="North East Zone", hover_color="#94a3b8")
sivo_app.map("zone_sw", tooltip="South West Zone", hover_color="#94a3b8")
sivo_app.map("zone_se", tooltip="South East Zone", hover_color="#94a3b8")
sivo_app.map("center_core", tooltip="Core Facility", glow=True)
sivo_app.to_html(output_path)
```
