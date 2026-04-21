# Scratch-off Map Reveal

This example demonstrates how to add an interactive scratch-off reveal layer to a SIVO infographic. This feature provides a gamified experience by covering the entire map with a solid color or image that the user can "scratch off" with their mouse or touch to reveal the contents underneath.

## Key Features Demonstrated

- **`sivo_app.enable_scratchoff(color="#1e293b", brush_size=50)`**: Enables the scratch-off layer.
  - `color`: Sets the solid color of the scratch-off mask (a dark slate gray in this example).
  - `brush_size`: Determines the size (in pixels) of the "brush" used to reveal the map when scratching.

## Running the Example

```bash
python3 main.py
```
This will generate an `output.html` file in the current directory. Open it in a web browser to see the effect!
