# Toggle Image Feature

This example demonstrates the `toggle_image` interaction feature in SIVO.

When you click the specified element (in this case, the `button`), it cycles through a provided list of image URLs and applies them as a repeating background fill pattern to the specified target element (`bg`).

## Code snippet

```python
# Map the toggle_image action to the button, targeting the background ('bg')
app.map(
    "button",
    toggle_image={
        "target_id": "bg",
        "image_urls": [
            "https://images.unsplash.com/photo-1470252649378-9c29740c9fa8?w=800&q=80",
            "https://images.unsplash.com/photo-1449824913935-59a10b8d2000?w=800&q=80",
            "https://images.unsplash.com/photo-1550684848-fac1c5b4e853?w=800&q=80"
        ]
    },
    hover_color="#0056b3",
    tooltip="Click to change background"
)

# Ensure the target element is mapped so it is tracked in ECharts data natively
app.map("bg")
```
