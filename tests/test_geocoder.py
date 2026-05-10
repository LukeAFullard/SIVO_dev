import sys
import os
import unittest
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from sivo import Sivo

class TestGeocoder(unittest.TestCase):
    def test_photon_provider(self):
        svg_content = """
        <svg xmlns="http://www.w3.org/2000/svg">
            <rect id="rect1" x="10" y="20" width="30" height="40"/>
        </svg>
        """
        sivo_app = Sivo.from_string(svg_content, enable_geocoder=True, geocode_provider="photon")

        # Test that geocode_provider was set in infographic
        self.assertEqual(sivo_app.infographic.geocode_provider, "photon")

        html_output = sivo_app.to_html()

        # Just look for the photon API URL directly in the HTML output
        self.assertIn("photon.komoot.io", html_output)

if __name__ == '__main__':
    unittest.main()
