# Image Gallery Example

This example demonstrates how to create an interactive image gallery using `Sivo`. Clicking on the targeted SVG element will open a lightbox-style modal containing the images provided.

## What is being shown
- How to link a list of image URLs to an SVG element using the `gallery` argument in `sivo_app.map()`.
- How the `panel_position` parameter, which defaults to `"none"`, behaves with the gallery. The gallery features a built-in modal overlay, so leaving `panel_position="none"` prevents an empty side panel from opening simultaneously.

## Key Code Snapshot
```python
# Click the shape to open a beautiful image lightbox gallery
sivo_app.map(
    element_id="play_button",
    tooltip="Click to view photo gallery",
    gallery=[
        "https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0?q=80&w=1200&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1472214103451-9374bd1c798e?q=80&w=1200&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1469474968028-56623f02e42e?q=80&w=1200&auto=format&fit=crop"
    ],
    panel_position="none", # Explicitly set to none to rely solely on the gallery modal
    hover_color="#0066cc",
    glow=True
)
```

## How to run
Run the example using Python:
```bash
python main.py
```
This will generate an `output.html` file that you can open in your browser to view the interactive gallery.