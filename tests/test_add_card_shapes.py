import unittest
from sivo.core.sivo import Sivo
from sivo.core.infographic import Infographic
import xml.etree.ElementTree as ET

class TestAddCardShapes(unittest.TestCase):
    def test_add_card_shapes_and_styles(self):
        svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
            <rect id="test_rect" x="10" y="10" width="80" height="80" />
        </svg>"""

        # We need to initialize it using Sivo.from_string which creates the underlying parser
        sivo = Sivo.from_string(svg_content)

        # Test basic new shape
        sivo.add_card("test_rect", "Hex Card", shape="hexagon")
        bytes_val = sivo.infographic.parser.to_string().encode('utf-8')
        self.assertTrue(b"polygon" in bytes_val)
        self.assertTrue(b"points" in bytes_val)

        # Test shadow and gradient
        sivo.add_card("test_rect", "Style Card", shape="rect", shadow=True, gradient_bg="#f00,#00f", dasharray="5,5")
        bytes_val = sivo.infographic.parser.to_string().encode('utf-8')
        self.assertTrue(b"feDropShadow" in bytes_val)
        self.assertTrue(b"linearGradient" in bytes_val)
        self.assertTrue(b"stroke-dasharray" in bytes_val)

if __name__ == '__main__':
    unittest.main()
