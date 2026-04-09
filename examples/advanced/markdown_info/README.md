# Markdown Info

## Description
SIVO Markdown Support

## Relevant Code
```python
    sivo_app = Sivo.from_svg(svg_path)
    sivo_app.map(
        element_id="play_button",
        tooltip="Click for Markdown Details",
        markdown=markdown_content.strip(),
        panel_position="bottom",
        hover_color="#8b32a8",
        glow=True
    )
    sivo_app.to_html(output_path)
```
