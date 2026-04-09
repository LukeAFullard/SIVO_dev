# Document And Map Embed

## Description
Map the Document action (e.g., a PDF or PPTX) Map the Map action (Interactive Google Maps embed)

## Relevant Code
```python
sivo_app = Sivo.from_string(svg_string)
sivo_app.map("btn_doc", document="https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf", tooltip="View Document via Google Docs Viewer", hover_color="#e11d48", color="#f43f5e")
sivo_app.map("btn_map", map_location="Eiffel Tower, Paris, France", tooltip="View Location on Google Maps", hover_color="#059669", color="#10b981")
sivo_app.to_html(output_path)
```
