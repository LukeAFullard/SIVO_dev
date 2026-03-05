import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from sivo.svg.parser import SVGParser
from sivo.core.infographic import Infographic

class TestSivoRender(unittest.TestCase):
    def test_infographic_render(self):
        svg_content = """
        <svg xmlns="http://www.w3.org/2000/svg">
            <path id="test1" d="M10 10"/>
            <rect id="test2" width="10" height="10"/>
        </svg>
        """
        infographic = Infographic.from_string(svg_content)
        infographic.map("test1", tooltip="Test Path", color="#ff0000")
        infographic.map("test2", url="https://example.com", drill_to="other.svg")

        manifest = infographic.get_manifest()

        self.assertIn("test1", manifest["objects"])
        self.assertIn("test2", manifest["objects"])

        actions_test2 = manifest["objects"]["test2"]["actions"]
        action_types = [a["action_type"] for a in actions_test2]

        self.assertIn("url", action_types)
        self.assertIn("drilldown", action_types)

        html_output = infographic.to_echarts_html()

        # Check that Jinja rendered properly
        self.assertIn("SIVO Interactive Graphic", html_output)
        self.assertIn("echarts.init", html_output)
        self.assertIn("test1", html_output)
        self.assertIn("test2", html_output)
        self.assertIn("https://example.com", html_output)

if __name__ == '__main__':
    unittest.main()
