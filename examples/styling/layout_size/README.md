# SIVO Layout Size Example

This example demonstrates how to use the `layout_size` attribute in SIVO to create a responsive, scalable graphic that automatically adapts to the container size, preventing massive blank borders.

## What is being shown
- Setting the `layout_size` parameter in `Sivo.from_string()` to allow the graphic to fill a percentage of the screen dimensions automatically.
- Mapping an interactive side panel to display HTML content, demonstrating the need to set the `panel_position` parameter, as its default value is `"none"`.

## Code Example

```python
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

from sivo import Sivo

svg_content = """<svg viewBox="0 0 500 500" xmlns="http://www.w3.org/2000/svg">
    <rect id="background" width="500" height="500" fill="#f0f0f0" stroke="#cccccc" stroke-width="5" />
    <circle id="center_dot" cx="250" cy="250" r="50" fill="#ff5722" />
    <text x="250" y="350" font-family="Arial" font-size="24" text-anchor="middle" fill="#333333">
        SIVO Layout Size Example
    </text>
    <text x="250" y="380" font-family="Arial" font-size="16" text-anchor="middle" fill="#666666">
        This shape scales to 99% of the container size automatically!
    </text>
</svg>"""

# Using layout_size="99%" ensures that no matter the screen size (mobile, desktop, ultrawide),
# the SVG will scale so its longest dimension takes up exactly 99% of the screen.
# This prevents the graphic from looking tiny with massive blank white borders.
app = Sivo.from_string(
    svg_content,
    layout_size="99%",
    title="Responsive Layout Demo"
)

app.map(
    element_id="center_dot",
    hover_color="#e64a19",
    html="<h3>Center</h3><p>This is the center of the scalable graphic.</p>",
    panel_position="right"
)

# Render to an HTML file
output_path = os.path.join(os.path.dirname(__file__), "layout_demo.html")
with open(output_path, "w") as f:
    f.write(app.to_html())
```

## Running the example

Run the script to generate the HTML file:
```bash
python app.py
```

Open the generated `layout_demo.html` in your web browser to see the results.
