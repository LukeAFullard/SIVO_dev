# 06 HTML Overlays

This example demonstrates how to add dynamic HTML overlays over map coordinates. Overlays can display HTML content positioned relative to an SVG element.

### Key Code

```python
# Add HTML overlays over the map coordinates dynamically
sivo_app.add_overlay(
    element_id="sun",
    html="<div style='background: white; padding: 2px 4px; border-radius: 4px; font-weight: bold;'>☀️ 30°C</div>",
    offset_x=20, # offset from the center
    offset_y=-30
)
```
