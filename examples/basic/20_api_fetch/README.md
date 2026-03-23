# Basic: API Fetch

This example shows how Sivo elements can interact with live web data by dynamically fetching external JSON sources upon interaction.

## What is being tested/demonstrated
* Binding interaction on an SVG element to fetch data dynamically from an external URL endpoint (`fetch_url`).
* Using the built-in information panel mechanism to automatically format and display the returned JSON data to the user without hardcoded formatting.
* Configuring the panel layout context, e.g., to load at the `top` of the viewport.

## Key Code

```python
# Click the shape to dynamically fetch data and display it in the side panel
sivo_app.map(
    element_id="play_button",
    tooltip="Click to fetch cat fact",
    fetch_url="https://catfact.ninja/fact",
    panel_position="top",
    hover_color="#e68a00",
    glow=True
)
```
