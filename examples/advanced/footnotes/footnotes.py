import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

from sivo.core.sivo import Sivo
from sivo.core.infographic import Infographic
from sivo.svg.parser import SVGParser

svg_path = os.path.join(os.path.dirname(__file__), 'footnote_map.svg')
with open(svg_path, 'w') as f:
    f.write('''<svg width="400" height="300" xmlns="http://www.w3.org/2000/svg">
        <rect id="bg" width="400" height="300" fill="#e2e8f0" />
        <circle id="point1" cx="100" cy="150" r="20" fill="#ef4444" cursor="pointer" />
        <circle id="point2" cx="300" cy="150" r="20" fill="#10b981" cursor="pointer" />
        <text x="200" y="50" font-family="Arial" font-size="16" text-anchor="middle" font-weight="bold">Click points for Data Provenance</text>
    </svg>''')

parser = SVGParser(svg_path)
info = Infographic(parser=parser)
sivo_app = Sivo(info)

sivo_app.map(
    element_id="point1",
    tooltip="Red Data Point",
    footnote="This figure excludes data from Alaska and Hawaii due to reporting differences. Source: U.S. Census Bureau 2023.",
    footnote_title="Methodology Note"
)

sivo_app.map(
    element_id="point2",
    tooltip="Green Data Point",
    footnote="Estimated values based on predictive modeling. Margin of error &plusmn; 4%.",
    footnote_title="Estimation Disclaimer"
)

output_path = os.path.join(os.path.dirname(__file__), 'output.html')
sivo_app.to_html(output_path)
print(f"Generated footnote example at: {output_path}")
