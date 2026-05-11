import sys

content = """import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from sivo import Sivo

class TestAddCardShapesAndStyles(unittest.TestCase):
    def setUp(self):
        self.svg_template = '<svg xmlns="http://www.w3.org/2000/svg"><rect id="dummy" x="10" y="10" width="100" height="100"/></svg>'
        self.sivo = Sivo.from_string(self.svg_template)

    def test_add_hexagon_card(self):
        self.sivo.add_card(element_id="dummy", title="Hex", shape="hexagon")
        out = self.sivo.infographic.parser.to_string()
        self.assertIn(b'<polygon', out)

    def test_add_octagon_card(self):
        self.sivo.add_card(element_id="dummy", title="Oct", shape="octagon")
        out = self.sivo.infographic.parser.to_string()
        self.assertIn(b'<polygon', out)

    def test_add_diamond_card(self):
        self.sivo.add_card(element_id="dummy", title="Dia", shape="diamond")
        out = self.sivo.infographic.parser.to_string()
        self.assertIn(b'<polygon', out)

    def test_add_triangle_card(self):
        self.sivo.add_card(element_id="dummy", title="Tri", shape="triangle")
        out = self.sivo.infographic.parser.to_string()
        self.assertIn(b'<polygon', out)

    def test_add_card_styling_gradient(self):
        self.sivo.add_card(element_id="dummy", title="Grad", gradient_bg="#ff0000,#00ff00")
        out = self.sivo.infographic.parser.to_string()
        self.assertIn(b'<linearGradient', out)
        self.assertIn(b'<stop', out)
        self.assertIn(b'#ff0000', out)

    def test_add_card_styling_shadow(self):
        self.sivo.add_card(element_id="dummy", title="Shadow", shadow=True)
        out = self.sivo.infographic.parser.to_string()
        self.assertIn(b'<filter', out)
        self.assertIn(b'<feDropShadow', out)

    def test_add_card_styling_glass(self):
        self.sivo.add_card(element_id="dummy", title="Glass", glass=True)
        out = self.sivo.infographic.parser.to_string()
        self.assertIn(b'<filter', out)
        self.assertIn(b'<feGaussianBlur', out)
        self.assertIn(b'<feColorMatrix', out)

    def test_add_card_styling_dasharray(self):
        self.sivo.add_card(element_id="dummy", title="Dash", dasharray="5,5")
        out = self.sivo.infographic.parser.to_string()
        self.assertIn(b'stroke-dasharray="5,5"', out)

    def test_add_speech_bubble_left(self):
        self.sivo.add_card(element_id="dummy", title="Bubble", shape="speech_bubble_left")
        out = self.sivo.infographic.parser.to_string()
        self.assertIn(b'<path', out)
        self.assertIn(b'd="M ', out)

    def test_add_speech_bubble_top(self):
        self.sivo.add_card(element_id="dummy", title="Bubble", shape="speech_bubble_top")
        out = self.sivo.infographic.parser.to_string()
        self.assertIn(b'<path', out)
        self.assertIn(b'd="M ', out)

    def test_add_fish(self):
        self.sivo.add_card(element_id="dummy", title="Fish", shape="fish")
        out = self.sivo.infographic.parser.to_string()
        self.assertIn(b'<path', out)
        self.assertIn(b'd="M ', out)

    def test_add_eel(self):
        self.sivo.add_card(element_id="dummy", title="Eel", shape="eel")
        out = self.sivo.infographic.parser.to_string()
        self.assertIn(b'<path', out)

    def test_add_koura(self):
        self.sivo.add_card(element_id="dummy", title="Koura", shape="koura")
        out = self.sivo.infographic.parser.to_string()
        self.assertIn(b'<path', out)

    def test_add_title_above(self):
        self.sivo.add_card(element_id="dummy", title="Above", shape="fish", title_above=True)
        out = self.sivo.infographic.parser.to_string().decode('utf-8')

        # We need to extract the 'y' coordinate of the text element "Above" to ensure it's < 10 (since dummy rect y="10")
        import xml.etree.ElementTree as ET
        root = ET.fromstring(out)
        text_node = root.find(".//{http://www.w3.org/2000/svg}text")
        y_val = float(text_node.attrib['y'])

        # Top of the rect is 10. We expect it to be placed above it (e.g., 10 - font_size * 0.5)
        self.assertTrue(y_val < 10)

    def test_add_tap_splash(self):
        self.sivo.add_card(element_id="dummy", title="Splash", shape="tap_splash")
        out = self.sivo.infographic.parser.to_string()
        self.assertIn(b'<path', out)

    def test_add_mobile_phone(self):
        self.sivo.add_card(element_id="dummy", title="Mobile", shape="mobile_phone")
        out = self.sivo.infographic.parser.to_string()
        self.assertIn(b'<rect', out)
        self.assertIn(b'<circle', out) # home button

    def test_add_internet(self):
        self.sivo.add_card(element_id="dummy", title="Net", shape="internet")
        out = self.sivo.infographic.parser.to_string()
        self.assertIn(b'<path', out)

    def test_add_globe(self):
        self.sivo.add_card(element_id="dummy", title="Globe", shape="globe")
        out = self.sivo.infographic.parser.to_string()
        self.assertIn(b'<circle', out)
        self.assertIn(b'<ellipse', out)
        self.assertIn(b'<line', out)

    def test_add_custom_path_card(self):
        path_str = "M 10 10 L 110 110 L 10 110 Z"
        self.sivo.add_card(element_id="dummy", title="Custom", custom_path_d=path_str)
        out = self.sivo.infographic.parser.to_string()
        self.assertIn(b'<path', out)
        self.assertIn(b'd="M 10 10 L 110 110 L 10 110 Z"', out)

if __name__ == '__main__':
    unittest.main()
"""

with open('tests/test_add_card_shapes.py', 'w') as f:
    f.write(content)
