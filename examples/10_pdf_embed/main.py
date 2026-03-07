import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from sivo import Sivo

svg_string = """
<svg viewBox="0 0 300 300" xmlns="http://www.w3.org/2000/svg">
  <!-- PDF Document Icon -->
  <g id="btn_pdf" transform="translate(100, 100)">
    <rect width="100" height="120" rx="10" fill="#f43f5e" stroke="#e11d48" stroke-width="2"/>
    <text x="50" y="70" font-family="sans-serif" font-weight="bold" font-size="30" text-anchor="middle" fill="#ffffff">PDF</text>
  </g>
</svg>
"""

sivo_app = Sivo.from_string(svg_string)

# Map the PDF action
# Using a widely accessible sample PDF link for the demo
sivo_app.map("btn_pdf", pdf="https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf", tooltip="View Sample PDF", hover_color="#e11d48", color="#f43f5e")

sivo_app.to_html("examples/10_pdf_embed/output.html")
print("PDF embed test generated at examples/10_pdf_embed/output.html")
