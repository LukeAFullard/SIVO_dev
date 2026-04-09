# Drillthrough Transitions

## Description
Add the src directory to the path so we can import sivo Create two separate SVGs to represent distinct HTML pages Page 1: Overview Page 2: Details Link them using drill_through (which loads a new URL) rather than drill_to (which swaps views in a single page app) We use a relative URL here assuming both HTML files are in the same folder.

## Relevant Code
```python
    app1 = Sivo.from_string(svg_page1, disable_panel=True, disable_zoom_controls=True)
    app2 = Sivo.from_string(svg_page2, disable_panel=True, disable_zoom_controls=True)
```
