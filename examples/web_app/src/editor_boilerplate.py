import os
from sivo import Sivo

# 1. Read the SVG template you just saved in the Annotator
template_path = "/sivo_workspace/sivo_template.svg"

if not os.path.exists(template_path):
    print("Template not found! Please draw a shape in the Annotator and click 'Save to Pyodide FS'.")
else:
    # 2. Load it into SIVO
    app = Sivo.from_svg(template_path)

    # 3. Add a background image (replace with your image URL)
    # app.add_background_image("https://example.com/image.jpg")

    # 4. Map interactions to the shapes you drew
    # Replace 'shape_1' with the actual ID you gave your shape in the Annotator
    app.map("shape_1", tooltip="Hello from WASM!", color="rgba(59, 130, 246, 0.5)", hover_color="rgba(59, 130, 246, 0.8)")

    # 5. Export to HTML string
    html_output = app.to_html()

    # Send the HTML string to Javascript
    import js
    js.renderOutput(html_output)
