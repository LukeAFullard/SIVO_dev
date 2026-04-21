# Progress Bar Example

This example demonstrates how to configure and display interactive progress bars within SIVO side panels when a user clicks on an SVG element.

## Features Demonstrated

1.  **Panel Positioning**: We must set a side panel position, either globally in `Sivo.from_svg()` using `default_panel_position` or per-element using the `panel_position` keyword argument. SIVO defaults to `panel_position='none'`, meaning click interactions won't automatically trigger a panel unless specified.

    ```python
    # Setting global panel position to 'right'
    sivo_app = Sivo.from_svg(svg_path, title="Progress Bar Overlay", default_panel_position="right")
    ```

2.  **Progress Bar Data Dictionary**: In `sivo_app.map()`, you can pass a `progress_bar` keyword argument. It expects a dictionary with details about the progress configuration: `title`, `progress` (a float between 0.0 and 100.0), and `color`.

    ```python
    sivo_app.map(
        "sun",
        progress_bar={
            "title": "Donations Collected",
            "progress": 75.5,
            "color": "#10b981" # Green
        },
        panel_position="right"  # Ensures the panel opens to display this content
    )
    ```

## Usage

Run the Python script to generate an interactive HTML file containing the SIVO configuration:

```bash
python3 main.py
```

Open the resulting `output.html` in your browser. Click on the "sun" or "house" elements to see the right panel open and display the progress bars and HTML content associated with each element.
