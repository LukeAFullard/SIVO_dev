# Document and Map Embed

This example demonstrates how to embed external documents (e.g. PDF, PPTX, DOCX) and interactive maps (e.g. Google Maps) directly into the information panel of a SIVO application. This provides a way to augment visualizations with rich, external resources.

## What is being tested

1. **Document Embedding (`sivo.map(..., document=...)`):** A dummy PDF document is mapped to the `btn_doc` SVG element. Clicking this element opens the PDF within the Google Docs Viewer embedded in the SIVO side panel.
2. **Map Embedding (`sivo.map(..., map_location=...)`):** A location query ("Eiffel Tower, Paris, France") is mapped to the `btn_map` SVG element. Clicking this element embeds an interactive Google Map centered on that location within the SIVO side panel.

## Relevant Code Bits

The document embedding is configured with:

```python
# Map the Document action (e.g., a PDF or PPTX)
sivo_app.map("btn_doc", document="https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf", tooltip="View Document via Google Docs Viewer", hover_color="#e11d48", color="#f43f5e")
```

The map embedding is configured with:

```python
# Map the Map action (Interactive Google Maps embed)
sivo_app.map("btn_map", map_location="Eiffel Tower, Paris, France", tooltip="View Location on Google Maps", hover_color="#059669", color="#10b981")
```

Both mappings rely on SIVO's iframe injection functionality to securely embed these resources in the dashboard context.
