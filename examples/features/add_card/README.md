# Adding Dynamic Information Cards

This example demonstrates how to use the `add_card()` API to dynamically inject perfectly-scaled SVG information cards into specific named regions of a template.

## Overview
The `add_card()` method computes bounding box coordinates of a target SVG element (such as a dashboard quadrant or an isolated region on a map) and dynamically draws an SVG `<g>` group containing a styled `<rect>` background and properly scaled multiline `<text>` nodes representing a title, primary value, and optional subtitle.

Because the injected cards are rendered natively as SVGs, they smoothly pan and zoom along with the ECharts canvas without causing visual misalignment during user interaction.

## Key Code Snippets

```python
# Add a styled card to the center of "quadrant_1"
sivo_app.add_card(
    "quadrant_1",           # Target element ID
    title="Revenue",        # Card title
    value="$1.2M",          # Main value
    subtitle="+12% YoY",    # Optional subtitle
    width="80%",            # Width relative to target element
    height="60%",           # Height relative to target element
    left="10%",             # X offset relative to target element
    top="20%",              # Y offset relative to target element
    bg_color="#ffffff",
    border_color="#3b82f6",
    border_width="2px",
    rx="12",                # Corner border radius
    title_color="#64748b",
    value_color="#0f172a",
    subtitle_color="#10b981"
)
```

## Running the Example
Run the script to generate the interactive bundle:
```bash
python main.py
```
Then open `output.html` in your web browser.
