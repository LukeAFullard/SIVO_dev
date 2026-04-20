# Lottie Animation Embed

This example demonstrates how to embed a Lottie animation within an interactive side panel using SIVO.

## Key Concepts
- **Lottie Embedding**: How to pass a Lottie JSON URL (or a local file path) to be rendered as an interactive animation using the `lottie` dictionary parameter.
- **Interactive Side Panel**: Demonstrates opening a side panel upon clicking an SVG region by setting `panel_position="right"`.
- **HTML Content**: Combining a Lottie animation with custom HTML content in the same side panel.

## Code Snippet
The following snippet from `main.py` shows how the Lottie animation is mapped to the "river" SVG element:

```python
    sivo_app.map(
        "river",
        tooltip="Cafeteria",
        panel_position="right",
        lottie={
            "lottie_url": "animation.json", # A sample lottie
            "loop": True,
            "autoplay": True
        },
        html="<p>Enjoy a nice hot cup of coffee at our cafeteria.</p>"
    )
```

## Running the Example
Execute the Python script to generate the interactive output:
```bash
python main.py
```
This will generate an `output.html` file in the same directory. Open `output.html` in your web browser and click on the "river" section of the SVG to view the Lottie animation in the side panel.
