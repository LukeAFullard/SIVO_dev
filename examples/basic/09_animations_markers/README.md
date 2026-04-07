# 09 Animations & Markers

This example illustrates how to apply built-in animations (e.g., pulse, fade) to SVG elements and how to add dynamic markers (like emojis or icons) anchored to specific elements.

### Key Code

```python
# Apply an animation
sivo_app.map(
    element_id="sun",
    animation="pulse",
    color="orange"
)

# Add a marker
sivo_app.add_marker(
    element_id="mountain1",
    icon="⛰️",
    label="Peak 1",
    offset_y=-30
)
```
