import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

from sivo.core.sivo import Sivo
from sivo.core.infographic import Infographic
from sivo.svg.parser import SVGParser
from sivo.core.project import SivoProject

dense_map = os.path.join(os.path.dirname(__file__), 'dense_map.svg')
exploded_map = os.path.join(os.path.dirname(__file__), 'exploded_map.svg')

with open(dense_map, 'w') as f:
    f.write('''<svg width="600" height="400" xmlns="http://www.w3.org/2000/svg">
        <rect id="bg" width="600" height="400" fill="#f1f5f9" />
        <g id="dense_cluster">
            <rect id="r1" x="280" y="180" width="20" height="20" fill="#3b82f6" stroke="white" stroke-width="2" />
            <rect id="r2" x="300" y="180" width="20" height="20" fill="#ef4444" stroke="white" stroke-width="2" />
            <rect id="r3" x="280" y="200" width="20" height="20" fill="#10b981" stroke="white" stroke-width="2" />
            <rect id="r4" x="300" y="200" width="20" height="20" fill="#f59e0b" stroke="white" stroke-width="2" />
        </g>
        <rect id="explode_btn" x="450" y="340" width="130" height="40" rx="8" fill="#1e293b" cursor="pointer" />
        <text x="515" y="365" font-family="Arial" font-size="14" fill="white" text-anchor="middle" font-weight="bold" pointer-events="none">Explode Map</text>
        <text x="300" y="50" font-family="Arial" font-size="20" text-anchor="middle" fill="#333" font-weight="bold">Dense Population Center</text>
    </svg>''')

with open(exploded_map, 'w') as f:
    f.write('''<svg width="600" height="400" xmlns="http://www.w3.org/2000/svg">
        <rect id="bg2" width="600" height="400" fill="#f1f5f9" />
        <g id="grid_cluster">
            <path id="r1_exp" d="M150 150 l50 0 l25 43 l-25 43 l-50 0 l-25 -43 Z" fill="#3b82f6" stroke="white" stroke-width="4" />
            <path id="r2_exp" d="M300 150 l50 0 l25 43 l-25 43 l-50 0 l-25 -43 Z" fill="#ef4444" stroke="white" stroke-width="4" />
            <path id="r3_exp" d="M150 250 l50 0 l25 43 l-25 43 l-50 0 l-25 -43 Z" fill="#10b981" stroke="white" stroke-width="4" />
            <path id="r4_exp" d="M300 250 l50 0 l25 43 l-25 43 l-50 0 l-25 -43 Z" fill="#f59e0b" stroke="white" stroke-width="4" />
        </g>
        <rect id="reset_btn" x="450" y="340" width="130" height="40" rx="8" fill="#1e293b" cursor="pointer" />
        <text x="515" y="365" font-family="Arial" font-size="14" fill="white" text-anchor="middle" font-weight="bold" pointer-events="none">Back to Map</text>
        <text x="300" y="50" font-family="Arial" font-size="20" text-anchor="middle" fill="#333" font-weight="bold">Hexbin Stylized View</text>
    </svg>''')

# Create SivoProject
project = SivoProject(initial_view_id="dense_view")

# Add Dense View
s1 = Sivo(Infographic(parser=SVGParser(dense_map)))
s1.map("explode_btn", explode_to="exploded_view", explode_duration_ms=600, tooltip="Click to Peel-Back")
project.add_view("dense_view", s1)

# Add Exploded View
s2 = Sivo(Infographic(parser=SVGParser(exploded_map)))
s2.map("reset_btn", explode_to="dense_view", explode_duration_ms=600, tooltip="Go Back")
s2.map("r1_exp", tooltip="District A (Expanded)", footnote="Detailed demographics available here.")
project.add_view("exploded_view", s2)

output_path = os.path.join(os.path.dirname(__file__), 'output.html')
project.to_html(output_path)
print(f"Generated exploded view example at: {output_path}")
