import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from sivo.parser import SVGParser

class TestSVGParser(unittest.TestCase):
    def test_svg_parsing(self):
        svg_content = """
        <svg xmlns="http://www.w3.org/2000/svg">
            <path id="test1" d="M10 10"/>
            <rect id="test2" width="10" height="10"/>
        </svg>
        """
        parser = SVGParser(svg_content, is_file=False)
        elements = parser.process_elements()
        self.assertEqual(len(elements), 2)

        self.assertEqual(elements[0]['id'], "test1")
        self.assertEqual(elements[0]['name'], "test1")

        self.assertEqual(elements[1]['id'], "test2")
        self.assertEqual(elements[1]['name'], "test2")

if __name__ == '__main__':
    unittest.main()
