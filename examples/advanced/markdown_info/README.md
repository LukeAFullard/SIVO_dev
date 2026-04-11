# Markdown Info Panels

This example demonstrates how to attach formatted Markdown content to an interactive SVG element in SIVO. When a user interacts with the targeted SVG element, a panel displaying the rendered markdown content will be shown.

## Purpose

The primary goal of this example is to show how to use the `markdown` attribute in the `Sivo.map()` function. It provides an easy way to show rich, formatted text containing things like bullet points, links, and code snippets without having to write custom HTML.

We also demonstrate how to explicitly specify the `panel_position` to ensure the markdown content renders where we want it (in this case, at the "bottom"). The default `panel_position` in SIVO is `"none"`, so an explicit position is required for the markdown panel to be visible.

## Key Code Snippets

Here is the essential code that binds the Markdown content to an SVG element with the ID `play_button`:

```python
markdown_content = \"\"\"
# SIVO Markdown Support

This is a **bold** statement. You can write easily formatted info panels:
- Bullet points
- `Inline code`
- [Links](https://github.com)

```python
print("Hello SIVO!")
```
\"\"\"

# Map the Markdown content to the "play_button" element
sivo_app.map(
    element_id="play_button",
    tooltip="Click for Markdown Details",
    markdown=markdown_content.strip(),
    panel_position="bottom", # Show panel at the bottom
    hover_color="#8b32a8",
    glow=True
)
```

## Running the Example

To run this example and generate the output HTML, simply execute:

```bash
PYTHONPATH=src python3 examples/advanced/markdown_info/main.py
```

This will create an `output.html` file in the same directory, which you can open in any modern web browser to see the interactive result.
