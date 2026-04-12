# Audio Guided Tour

This example demonstrates how to use the `bind_tour` feature in SIVO to create an interactive, audio-guided tour of an SVG map. It shows how you can attach royalty-free sound clips or voiceovers to individual steps of the tour that play automatically when the step is reached.

## What is being shown
- Creating an interactive map using `Sivo.from_svg`.
- Setting `default_panel_position="none"` to ensure no extra side panel appears by default.
- Mapping HTML tooltips to elements (`sun`, `house`, `river`) via `sivo_app.map()`.
- Binding a step-by-step tour using `sivo_app.bind_tour()`.
- Configuring `TourStepConfig` via dictionaries with properties like `content`, `audio_url`, `zoom_to`, `zoom_level`, and `show_tooltips`.

## Running the example
To run the example and generate the `output.html` file, execute the following from the root of the repository:

```bash
PYTHONPATH=src python3 examples/infographics/tour_audio/main.py
```

## Relevant Code

The core of the logic happens with `sivo_app.bind_tour()`:

```python
    sivo_app.bind_tour([
        {
            "content": "<h3>Welcome to the Audio Tour!</h3><p>Make sure your volume is turned up.</p>",
            "audio_url": "https://actions.google.com/sounds/v1/water/rain_drips_on_tin_roof.ogg", # Sample ambient/short sound
            "zoom_to": "mountain1",
            "zoom_level": 1.2
        },
        ...
    ])
```
