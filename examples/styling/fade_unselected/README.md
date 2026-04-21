# Fade Unselected Example

This example demonstrates how to use the `fade_unselected` styling option in Sivo to dim unselected elements on the map, focusing the user's attention on the selected element.

When you initialize `Sivo`, you can set the `fade_unselected=True` property which causes unmapped objects or objects not currently focused on by the user to fade out.

## Key Code Snippets

### Initializing Sivo with `fade_unselected`

```python
# Initialize Sivo with fade_unselected=True
sivo_app = Sivo.from_string(svg_content, fade_unselected=True, default_panel_position="right")
```

### Mapping Interactive Elements

Here we are mapping three individual shapes out of the total 6 in the SVG. When you click one of the shapes, the remaining objects will be faded to emphasize the selection.

```python
sivo_app.map(
    element_id="rect1",
    tooltip="Blue Rectangle",
    html="<h3>Blue Rectangle</h3><p>Notice how all other shapes fade out when you click me.</p>",
    hover_color="#2980b9"
)

sivo_app.map(
    element_id="circ1",
    tooltip="Red Circle",
    html="<h3>Red Circle</h3><p>Click the background canvas to deselect and close this panel.</p>",
    hover_color="#c0392b"
)

sivo_app.map(
    element_id="poly2",
    tooltip="Orange Triangle",
    html="<h3>Orange Triangle</h3><p>Fading works across all mapped objects automatically.</p>",
    hover_color="#d35400"
)
```

## Running the Example

Run the script to generate the `output.html` file containing the interactive visual.

```bash
python main.py
```
