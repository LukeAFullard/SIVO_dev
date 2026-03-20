# Hello World

This example demonstrates the basic usage of SIVO. It loads an SVG file, maps interactions to a few elements, and exports the result to an interactive HTML file.

Key features shown:
- Loading an SVG (`Sivo.from_svg(svg_path, enable_search=True, layout_size="99%")`)
- Mapping interactions with tooltips and HTML content (`sivo_app.map(...)`)
- Customizing hover colors and glow effects
- Exporting to HTML (`sivo_app.to_html(...)`)
