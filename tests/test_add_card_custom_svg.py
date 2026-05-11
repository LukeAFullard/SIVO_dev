import pytest
from sivo.core.sivo import Sivo
import base64
from lxml import etree

def test_add_card_custom_svg():
    svg_string = """<svg viewBox="0 0 500 500" xmlns="http://www.w3.org/2000/svg">
      <rect id="background" width="500" height="500" fill="#f0f0f0" />
    </svg>"""

    sivo_app = Sivo.from_string(svg_string)

    custom_svg_str = "<svg viewBox='0 0 100 100' xmlns='http://www.w3.org/2000/svg'><polygon points='50,15 61,35 85,35 66,50 73,75 50,60 27,75 34,50 15,35 39,35' fill='#ffcc00'/></svg>"

    card_id = sivo_app.infographic.add_card(
        element_id="background",
        title="Star",
        value="100%",
        subtitle="Custom SVG test",
        custom_svg=custom_svg_str
    )

    # Check if image tag was added
    root = sivo_app.infographic.parser.root
    image_nodes = root.findall('.//{http://www.w3.org/2000/svg}image')
    if not image_nodes:
        image_nodes = root.findall('.//image')

    assert len(image_nodes) == 1, "Expected 1 image node"

    image_node = image_nodes[0]
    href = image_node.get('href')

    assert href is not None
    assert href.startswith("data:image/svg+xml;base64,")

    # decode to check if content matches
    b64_data = href.split(',')[1]
    decoded = base64.b64decode(b64_data).decode('utf-8')
    assert "polygon points='50,15" in decoded
