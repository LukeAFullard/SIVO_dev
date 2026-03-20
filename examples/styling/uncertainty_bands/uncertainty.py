import os
import sys

# Add the 'src' directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

from sivo.core.sivo import Sivo
from sivo.core.infographic import Infographic
from sivo.svg.parser import SVGParser

# Create a simple SVG inline
svg_path = os.path.join(os.path.dirname(__file__), 'chart_bg.svg')
with open(svg_path, 'w') as f:
    f.write('''<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg">
        <rect id="bg" width="800" height="600" fill="#f8fafc" />
        <rect id="chart_area" x="50" y="50" width="700" height="500" fill="transparent" />
        <text x="400" y="30" font-family="Arial" font-size="20" font-weight="bold" text-anchor="middle" fill="#333">2024 Election Polling Margin of Error</text>
    </svg>''')

# Initialize SIVO
parser = SVGParser(svg_path)
info = Infographic(parser=parser)
sivo_app = Sivo(info)

# Add a line chart with uncertainty bands
sivo_app.map_line_chart(
    element_id="chart_area",
    title="Candidate Approval Rating",
    categories=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
    data=[45, 46, 48, 47, 49, 51, 52],
    uncertainty_lower=[41, 42, 44, 43, 46, 48, 49],
    uncertainty_upper=[49, 50, 52, 51, 52, 54, 55],
    uncertainty_color="rgba(59, 130, 246, 0.2)",
    color="#3b82f6",
    smooth=True,
    tooltip="Approval Rating"
)

# Generate HTML
output_path = os.path.join(os.path.dirname(__file__), 'output.html')
sivo_app.to_html(output_path)
print(f"Generated uncertainty band example at: {output_path}")
