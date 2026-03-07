import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from sivo import Sivo

svg_string = """
<svg viewBox="0 0 500 300" xmlns="http://www.w3.org/2000/svg">
  <!-- Document Icon (PPTX/PDF/DOCX) -->
  <g id="btn_doc" transform="translate(100, 100)">
    <rect width="100" height="120" rx="10" fill="#f43f5e" stroke="#e11d48" stroke-width="2"/>
    <text x="50" y="70" font-family="sans-serif" font-weight="bold" font-size="24" text-anchor="middle" fill="#ffffff">DOC</text>
  </g>

  <!-- Map Icon -->
  <g id="btn_map" transform="translate(300, 100)">
    <rect width="100" height="120" rx="10" fill="#10b981" stroke="#059669" stroke-width="2"/>
    <circle cx="50" cy="50" r="20" fill="none" stroke="#ffffff" stroke-width="4"/>
    <path d="M50 70 L50 90 M40 80 L60 80" stroke="#ffffff" stroke-width="4"/>
    <text x="50" y="110" font-family="sans-serif" font-weight="bold" font-size="16" text-anchor="middle" fill="#ffffff">MAP</text>
  </g>
</svg>
"""

sivo_app = Sivo.from_string(svg_string)

# Map the Document action (e.g., a PDF or PPTX)
sivo_app.map("btn_doc", document="https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf", tooltip="View Document via Google Docs Viewer", hover_color="#e11d48", color="#f43f5e")

# Map the Map action (Interactive Google Maps embed)
sivo_app.map("btn_map", map_location="Eiffel Tower, Paris, France", tooltip="View Location on Google Maps", hover_color="#059669", color="#10b981")

sivo_app.to_html("examples/10_document_and_map_embed/output.html")
print("Document and Map embed test generated at examples/10_document_and_map_embed/output.html")
