# Drilldown Transitions

## Description
Add the src directory to the path so we can import sivo 1. Create three simple SVG strings that represent different "pages" or "views" View 1: A blue square with a button to go to View 2 View 2: A green square with buttons to go to View 3 or back to View 1 View 3: A purple square with a button to go back to View 1 2. Initialize Sivo instances for each view 3. Map the elements to trigger drilldowns with specific transition types From View 1 -> View 2 using a 3D "flip" animation From View 2 -> View 3 using a "page-turn" animation From View 2 -> View 1 using a "slide-right" animation (like going back) From View 3 -> View 1 using a "slide-up" animation 4. Combine them into a multi-view application using SivoProject 5. Export to an HTML file

## Relevant Code
```python
    app1 = Sivo.from_string(svg_view1, disable_panel=True, disable_zoom_controls=True)
    app2 = Sivo.from_string(svg_view2, disable_panel=True, disable_zoom_controls=True)
    app3 = Sivo.from_string(svg_view3, disable_panel=True, disable_zoom_controls=True)
```
