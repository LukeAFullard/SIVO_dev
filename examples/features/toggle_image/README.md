# Toggle Image Feature

This example demonstrates the `toggle_image` interaction feature in SIVO.

When you click the specified element (in this case, the `button`), it cycles through a provided list of image URLs and applies them as a repeating background fill pattern to the specified target element (`bg`).

The code defines an SVG string with a background rect (`bg`) and a button rect (`button`). We parse this with `Sivo.from_string`, explicitly setting `default_panel_position="none"` so no side panel pops up on click. We then map the `toggle_image` action to the `button` element to target `bg` with an array of images.

## Steps Involved

1. Parse SVG string with `Sivo.from_string` and ensure `default_panel_position` is `"none"`
2. Add text onto the button with `app.add_scalable_text`
3. Map the toggle functionality by using `app.map` on the `button` ID with `toggle_image` arguments containing the `target_id` and the `image_urls`.
4. Run `app.map("bg")` so the target is registered in the SIVO system.
5. Save the output file.

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
    hover_color="#0056b3"
)

# Ensure the target element is mapped so it is tracked in ECharts data natively
app.map("bg")
```