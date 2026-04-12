# Guided Tour Example

This example demonstrates how to create a step-by-step interactive **Guided Tour** using SIVO.

The guided tour capability provides users with sequential, narrative steps overlaying the SVG layout. In this implementation, the `bind_tour()` method creates an interface with **Next** and **Prev** controls to navigate between different view states.

## Key Concepts Shown

- **Declarative Stepping**: Defining a list of dictionaries (`steps`) that contain the state transitions. Each dictionary represents a distinct UI configuration to render per step.
- **Cinematic Zooming**: Using the `zoom_to` key, the map camera automatically centers and scales to the desired target element ID (like `gallery` or `cafe`) at a specified `zoom_level`.
- **Dynamic HTML Tooltips**: When moving from step to step, `show_tooltips` allows the visual tooltips (or rich `html` content popovers) mapped using `sivo_app.map()` to appear programmatically.
- **Native SVG Rendering**: `render_mode="svg"` is specified during initialization `Sivo.from_string()` so text rendering scales appropriately without clipping or pixelation which could happen in a standard canvas context.

## Code Highlights

In `main.py`, the core tour configuration is represented like this:

```python
steps = [
    {
        "content": "<h3>Welcome to the Museum Tour</h3><p>We'll guide you through the main exhibits. Click <b>Next</b> to begin.</p>",
    },
    {
        "content": "<h3>Art Gallery</h3><p>First stop: the main exhibition hall.</p>",
        "zoom_to": "gallery",
        "zoom_level": 2.5,
        "show_tooltips": ["gallery"]
    }
    # ... additional steps ...
]

# Bind the tour to the Sivo app
sivo_app.bind_tour(steps)
```

And mapping the rich HTML popovers (referred to within `show_tooltips`):

```python
sivo_app.map("gallery", html="<h4>Main Art Gallery</h4><p>Featuring modern artists.</p>")
```

## Running the Example

Make sure SIVO is installed (or the `PYTHONPATH` includes the source directory) and run:

```bash
PYTHONPATH=src python3 examples/infographics/guided_tour/main.py
```

This will output `guided_tour.html` in this same directory. You can view the file in your browser to experience the sequential tour.
