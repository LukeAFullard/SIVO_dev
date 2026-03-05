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
        infographic.map("test1", tooltip="Test Path", color="#ff0000", glow=True, border_width=2.5)
        infographic.map("test2", url="https://example.com", drill_to="other.svg")

        manifest = infographic.get_manifest()

        self.assertIn("test1", manifest["objects"])
        self.assertEqual(manifest["objects"]["test1"]["theme"]["glow"], True)
        self.assertEqual(manifest["objects"]["test1"]["theme"]["border_width"], 2.5)

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

    def test_metadata_extraction(self):
        svg_content = """
        <svg xmlns="http://www.w3.org/2000/svg">
            <rect id="rect1" x="10" y="20" width="30" height="40"/>
            <circle id="circle1" cx="100" cy="100" r="50"/>
            <polygon id="poly1" points="0,0 10,0 10,10 0,10"/>
        </svg>
        """
        infographic = Infographic.from_string(svg_content)
        metadata = infographic.get_metadata()

        self.assertIn("objects", metadata)
        objects = {obj["id"]: obj for obj in metadata["objects"]}

        self.assertIn("rect1", objects)
        self.assertEqual(objects["rect1"]["type"], "rect")
        self.assertEqual(objects["rect1"]["bbox"], [10.0, 20.0, 40.0, 60.0])

        self.assertIn("circle1", objects)
        self.assertEqual(objects["circle1"]["type"], "circle")
        self.assertEqual(objects["circle1"]["bbox"], [50.0, 50.0, 150.0, 150.0])

        self.assertIn("poly1", objects)
        self.assertEqual(objects["poly1"]["type"], "polygon")
        self.assertEqual(objects["poly1"]["bbox"], [0.0, 0.0, 10.0, 10.0])

if __name__ == '__main__':
    unittest.main()
