# 02 URL Navigation

This example shows how to configure an SVG element to act as a hyperlink. When clicked, it navigates the user to an external URL.

### Key Code

```python
sivo_app.map(
    element_id="sun",
    tooltip="Click to search about the Sun",
    url="https://en.wikipedia.org/wiki/Sun",
    hover_color="yellow",
    glow=True
)
```
