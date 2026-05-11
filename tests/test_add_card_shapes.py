import sys
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
        self.assertIn('<polygon', out)

    def test_add_octagon_card(self):
        self.sivo.add_card(element_id="dummy", title="Oct", shape="octagon")
        out = self.sivo.infographic.parser.to_string()
        self.assertIn('<polygon', out)

    def test_add_diamond_card(self):
        self.sivo.add_card(element_id="dummy", title="Dia", shape="diamond")
        out = self.sivo.infographic.parser.to_string()
        self.assertIn('<polygon', out)

    def test_add_triangle_card(self):
        self.sivo.add_card(element_id="dummy", title="Tri", shape="triangle")
        out = self.sivo.infographic.parser.to_string()
        self.assertIn('<polygon', out)

    def test_add_card_styling_gradient(self):
        self.sivo.add_card(element_id="dummy", title="Grad", gradient_bg="#ff0000,#00ff00")
        out = self.sivo.infographic.parser.to_string()
        self.assertIn('<linearGradient', out)
        self.assertIn('<stop', out)
        self.assertIn('#ff0000', out)

    def test_add_card_styling_shadow(self):
        self.sivo.add_card(element_id="dummy", title="Shadow", shadow=True)
        out = self.sivo.infographic.parser.to_string()
        self.assertIn('<filter', out)
        self.assertIn('<feDropShadow', out)

    def test_add_card_styling_glass(self):
        self.sivo.add_card(element_id="dummy", title="Glass", glass=True)
        out = self.sivo.infographic.parser.to_string()
        self.assertIn('<filter', out)
        self.assertIn('<feGaussianBlur', out)
        self.assertIn('<feColorMatrix', out)

    def test_add_card_styling_dasharray(self):
        self.sivo.add_card(element_id="dummy", title="Dash", dasharray="5,5")
        out = self.sivo.infographic.parser.to_string()
        self.assertIn('stroke-dasharray="5,5"', out)

if __name__ == '__main__':
    unittest.main()
