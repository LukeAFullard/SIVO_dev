# Overlay Sidebar Example

This example demonstrates how to configure the `default_panel_position` in SIVO to globally specify the default behavior of information panels. By default, SIVO sets `default_panel_position="none"`, which requires explicitly declaring `panel_position` on each `app.map()` call to show the panel when an element is clicked. By configuring `default_panel_position="overlay"`, all elements mapped with interactive content (like `html`) will automatically open an overlay panel upon interaction.

This example also demonstrates how to customize the visual size of the panel overlay by using `panel_width` and `panel_height` initialization arguments.

Additionally, this example shows how to override the global default on a per-element basis by manually declaring `panel_position` inside a specific `app.map()` call.

### Code Highlights

```python
# Initializing Sivo with an overlay panel configured to span 90% width and height
app = Sivo.from_string(
    svg_str,
    default_panel_position="overlay",
    panel_width="90%",
    panel_height="90%",
)

# Mapping elements without having to explicitly define panel_position
app.map(
    "block1",
    html="<h1>Block 1</h1><p>This panel is displayed as an overlay spanning 90% of the screen.</p>"
)

# Overriding the default panel position for a specific element
app.map(
    "block3",
    panel_position="right",
    html="<h1>Block 3</h1><p>This block opens a standard right side panel.</p>"
)
```
