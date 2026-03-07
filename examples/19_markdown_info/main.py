import os
from sivo import Sivo

def main():
    svg_path = os.path.join(os.path.dirname(__file__), "sample.svg")

    sivo_app = Sivo.from_svg(svg_path)

    markdown_content = """
# SIVO Markdown Support

This is a **bold** statement. You can write easily formatted info panels:
- Bullet points
- `Inline code`
- [Links](https://github.com)

```python
print("Hello SIVO!")
```
    """

    sivo_app.map(
        element_id="play_button",
        tooltip="Click for Markdown Details",
        markdown=markdown_content.strip(),
        panel_position="bottom",
        hover_color="#8b32a8",
        glow=True
    )

    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    sivo_app.to_html(output_path)
    print(f"Exported Markdown interactive HTML to {output_path}")

if __name__ == "__main__":
    main()
