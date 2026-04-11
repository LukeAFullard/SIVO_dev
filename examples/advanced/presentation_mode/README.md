# Presentation Mode Example

This example demonstrates how to configure SIVO to act as a presentation tool, allowing users to step through a predefined sequence of visual elements using keyboard navigation (Left/Right arrow keys).

## What is being demonstrated?

1. **Keyboard Navigation:** Using the `presentation_order` parameter to define an ordered sequence of elements.
2. **Sequential Zooming:** Combining `presentation_order` with `zoom_on_click=True` inside mapped elements so that SIVO automatically pans and zooms the camera to the active element when the user presses an arrow key.
3. **Information Panel:** Displaying corresponding HTML content in a side panel (`panel_position="right"`) for each active step in the presentation sequence.
4. **Disabling Zoom Controls:** Turning off manual zoom controls (`disable_zoom_controls=True`) to provide a cleaner "slide presentation" interface.

## Relevant Code Snippets

### 1. Setting up the Project Config

The most important setting here is `presentation_order`, which takes a list of SVG element IDs defining the sequence. By setting `disable_zoom_controls=True` and `default_panel_position="right"`, we create a clean, presentation-style interface where details load alongside the zoomed-in focus element.

```python
config = ProjectConfig(
    svg_file="none",
    title="Keyboard Presentation Example",
    subtitle="Demonstrates the presentation_order parameter",
    presentation_order=["step1", "step2", "step3"],
    disable_zoom_controls=True,
    default_panel_position="right",
    # ... mappings ...
)
```

### 2. Element Mappings

In the mappings, setting `zoom_on_click=True` ensures that SIVO will smoothly pan the camera to the element when it becomes active in the presentation sequence.

```python
        "step1": ElementConfig(
            html="<h3>Step 1: Introduction</h3><p>This is the first step in our presentation. We zoomed in on the blue box.</p>",
            zoom_on_click=True,
            zoom_level=2.5,
            panel_position="right",
            hover_color="#2563eb"
        ),
```

## Running the Example

Run the Python script from the root of the repository to generate the HTML output:

```bash
PYTHONPATH=src python3 examples/advanced/presentation_mode/main.py
```

This will create `examples/advanced/presentation_mode/presentation_mode.html`.

Open the generated HTML file in your web browser. Try clicking anywhere to focus the browser window, then use your **Left** and **Right** arrow keys to step forwards and backwards through the numbered boxes. You will see the camera automatically pan and zoom to the targeted element, and the side panel will display the corresponding HTML content.
