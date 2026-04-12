# Scrollytelling Audio Example

This example demonstrates how to implement a scrollytelling experience in SIVO that triggers audio events as the user scrolls through a narrative.

## Features Showcased
- **Scrollytelling Binding**: Using `sivo_app.bind_scrollytelling(steps)` to bind scrolling narrative to a SIVO visualization.
- **Audio Triggers**: Using the `audio_url` field in a step's configuration to automatically play an audio track when the step becomes active in the viewport.
- **Zoom Interactions**: Automatically zooming (`zoom_to`, `zoom_level`) and centering on different SVG elements as the user scrolls.
- **Color Mapping**: Dynamically altering SVG element colors (`colors` dict) when navigating the narrative.

## Code Breakdown

1. **Initialization**: We instantiate a SIVO App from a basic SVG string representing three facilities in a network. We explicitly set the `default_panel_position` to `"none"`.
2. **Scrollytelling Config**: We define a list of `steps`, each containing text `content`, target elements to `zoom_to`, a `zoom_level`, highlight `colors`, and an optional `audio_url`.
3. **Audio Playback**: The second and third steps define an `audio_url`. When the user scrolls the narrative side panel to these steps, the SIVO JS runtime automatically triggers the audio.
4. **Mapping Elements**: We use `sivo_app.map` on `"section1"`, `"section2"`, and `"section3"`, using `html` for basic hover tooltips. We also provide `panel_position="none"` to explicitly control visibility behaviour.
5. **Binding**: Finally, we call `sivo_app.bind_scrollytelling(steps)` to attach the narrative configuration to the interactive canvas.

## Running the Example

Make sure `src/` is in your `PYTHONPATH` and run:

```bash
PYTHONPATH=src python3 examples/infographics/scrollytelling_audio/main.py
```

This will generate `scrollytelling_audio.html` in the current directory, which can be opened in any web browser to test the interactive, audio-driven scrolling narrative.
