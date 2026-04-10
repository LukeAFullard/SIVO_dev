# API Fetch

This example demonstrates how to dynamically fetch data from an external API when an SVG element is clicked and display it in a side panel.

The `main.py` script maps an interaction to the element with ID `play_button`:
- When clicked, it fetches a random cat fact from `https://catfact.ninja/fact`
- Using `fetch_data_path="fact"`, SIVO automatically parses the JSON response and extracts only the text value of the `fact` key, rather than displaying the raw JSON block.
- The fetched data is displayed in a panel positioned at the top.
- The element also features a hover color and a glow effect.

Relevant code:
```python
    sivo_app.map(
        element_id="play_button",
        tooltip="Click to fetch cat fact",
        fetch_url="https://catfact.ninja/fact",
        fetch_data_path="fact",
        panel_position="top",
        hover_color="#e68a00",
        glow=True
    )
```
