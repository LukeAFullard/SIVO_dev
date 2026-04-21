# YouTube Video Overlay Example

This example demonstrates how to integrate a YouTube video into an interactive SIVO map, triggering a modal video player overlay when a specific SVG element is clicked.

## Purpose

The main goal of this example is to show how to use the `video` integration feature in SIVO along with setting the `panel_position` to `'overlay'`. It maps a `youtube-nocookie.com` embed link to SVG elements (`play_button` and `play_icon`), allowing users to click and watch a video directly over the interactive graphic without leaving the page.

## How It Works

1. **Initialize SIVO**: The application is initialized using a simple SVG file (`sample.svg`) which contains elements with IDs `play_button` and `play_icon`.
2. **Map the Video**: The `sivo_app.map()` function maps these elements to a video URL.
3. **Panel Position**: We configure `panel_position="overlay"` to specify that the content should be rendered as a modal overlay in the center of the screen instead of being placed in a side panel.
4. **Generate Output**: The layout and bindings are saved to `output.html`.

## Code Snippets

```python
import os
from sivo import Sivo

svg_path = os.path.join(os.path.dirname(__file__), "sample.svg")
sivo_app = Sivo.from_svg(svg_path)

# Video URL using youtube-nocookie.com for better privacy and embedded playback
video_url = "https://www.youtube-nocookie.com/embed/jNQXAC9IVRw?autoplay=1"

# Map to play button
sivo_app.map(
    element_id="play_button",
    tooltip="Click to watch video",
    video=video_url,
    hover_color="#CC0000",
    glow=True,
    panel_position="overlay"
)

# Map to play icon
sivo_app.map(
    element_id="play_icon",
    tooltip="Click to watch video",
    video=video_url,
    hover_color="#f0f0f0",
    glow=True,
    panel_position="overlay"
)

output_path = os.path.join(os.path.dirname(__file__), "output.html")
sivo_app.to_html(output_path)
```

## Running the Example

Simply execute the `main.py` script to regenerate the `output.html` file:

```bash
python main.py
```
