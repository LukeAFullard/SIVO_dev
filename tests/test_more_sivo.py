import sys
import os
import unittest
import tempfile

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from sivo import Sivo
from sivo.core.infographic import Infographic
import json

class TestMoreSivo(unittest.TestCase):
    def test_sivo_from_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            Sivo.from_svg("not_a_real_file.svg")

    def test_sivo_from_template_not_found(self):
        with self.assertRaises(FileNotFoundError):
            Sivo.from_template("not_a_real_template")

    def test_sivo_map_edge_cases(self):
        sivo = Sivo.from_string('<svg><rect id="r"/></svg>')
        sivo.map("r", color="#fff", tooltip="hi", panel_position="left")
        self.assertEqual(sivo.infographic.mappings["r"].theme.color, "#fff")

        from sivo.core.actions import URLAction
        action = URLAction(url="https://example.com")
        sivo.infographic.mappings["r"].actions.append(action)
        self.assertEqual(len(sivo.infographic.mappings["r"].actions), 3)  # Hover/Click Panel added by map() plus URLAction

    def test_build_bundle(self):
        sivo = Sivo.from_string('<svg><rect id="r"/></svg>')
        html = sivo.to_html()
        self.assertIn("echarts", html)
        self.assertIn("default_view", html)

    def test_fetch_image_base64_invalid(self):
        # We test SSRF protection block
        with self.assertRaises(ValueError):
            Sivo.fetch_image_base64("http://localhost/image.png")
        with self.assertRaises(ValueError):
            Sivo.fetch_image_base64("file:///etc/passwd")

    def test_sivo_from_url_impl(self):
        # Just catching that it isn't implemented (we know from memory)
        with self.assertRaises(AttributeError):
            Sivo.from_url("http://google.com")

if __name__ == '__main__':
    unittest.main()
