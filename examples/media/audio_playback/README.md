# Audio Playback Example

## Purpose
This example demonstrates how to add audio playback to an interactive SVG element using SIVO. By binding a sound file to an element via the `Sivo.map()` function, users can hear a sound whenever they click the associated shape. This is useful for building interactive learning tools, ambient soundscapes, or providing pronunciation samples.

Additionally, this example shows how to configure an associated sliding side panel to display descriptive HTML content when the audio triggers.

## Steps Involved
1. **Load SVG**: Start by loading a base SVG file (e.g., `sample.svg`) containing a button element with a specific ID (in this case, `"play_button"`).
2. **Initialize Sivo App**: Use `Sivo.from_svg()` to process the base SVG.
3. **Map the Element**: Apply interactivity using `sivo_app.map()`, binding an audio source URL via the `audio` keyword argument. Note that we must also supply `html` and `panel_position` so the default "none" behavior is overridden and an informational panel is displayed simultaneously.
4. **Export**: Call `sivo_app.to_html()` to generate an interactive `output.html` file containing the audio-capable dashboard.

## Key Code Snippet
```python
# Click the shape to play a sound
sivo_app.map(
    element_id="play_button",
    tooltip="Click to hear a sound",
    audio="https://actions.google.com/sounds/v1/alarms/beep_short.ogg",
    html="<h2>Audio Playback Example</h2><p>You clicked the button and should hear a short beep.</p>",
    panel_position="right",
    hover_color="#32a852",
    glow=True
)
```
