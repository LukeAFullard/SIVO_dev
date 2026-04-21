# Border Image Example

This example demonstrates how to apply styling elements in SIVO, specifically focusing on background and border images, and mapping an element to open a side panel.

## Purpose

1. **Border Image**: Showcases how to add a static image overlay fixed to one side of the layout (in this case, the left edge) using `app.add_border_image()`.
2. **Background Image**: Showcases how to overlay a background image that covers the full canvas using `app.add_background_image()`.
3. **Side Panel**: Demonstrates how to map an interactive SVG element to open a side panel to reveal HTML content. Importantly, it emphasizes setting `panel_position="right"`, because the default value for `panel_position` is `None` (which would otherwise result in no panel opening).

## Key Code Snippets

### Initializing and Styling
```python
# Initialize Sivo
app = Sivo.from_string(svg_str, theme='light')

# Add a background image
app.add_background_image(
    url="https://images.unsplash.com/photo-1557683316-973673baf926?auto=format&fit=crop&q=80&w=1000",
    opacity=0.6,
    grayscale=False
)

# Add a border image along the left-hand side, 10% wide
app.add_border_image(
    url="https://images.unsplash.com/photo-1579546929518-9e396f3cc809?auto=format&fit=crop&q=80&w=200",
    position="left",
    width="10%",
    opacity=1.0,
    grayscale=False
)
```

### Side Panel Mapping
Setting `panel_position` is critical as the default is `None`.

```python
# Map click event to open a side panel
app.map(
    element_id="main_content",
    html="<h2>Panel Content</h2><p>This side panel was opened by clicking the main content area.</p>",
    panel_position="right",
    tooltip="Click to open panel"
)
```

## Running the Example

Execute the python script:

```bash
python3 example_border_image.py
```

This will generate `border_image_demo.html` in the same directory. Open this HTML file in your browser to view the final output.
