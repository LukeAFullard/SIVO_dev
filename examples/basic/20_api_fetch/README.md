# 20 API Fetch

This example shows how to configure an element to perform an HTTP fetch request when clicked. The fetched data is then dynamically displayed in an interactive side panel.

### Key Code

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
