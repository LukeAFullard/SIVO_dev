import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from sivo.svg.parser import SVGParser

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

    def test_xxe_vulnerability_prevention(self):
        # This XML attempts to include an external entity
        malicious_svg = """
        <!DOCTYPE svg [
          <!ENTITY xxe SYSTEM "file:///etc/passwd">
        ]>
        <svg xmlns="http://www.w3.org/2000/svg">
            <text id="malicious">&xxe;</text>
        </svg>
        """
        parser = SVGParser(malicious_svg, is_file=False)
        elements = parser.process_elements()
        # Ensure the parser doesn't crash, but it also shouldn't resolve the entity.
        # It should just have a text tag without resolving &xxe; or throw an error based on lxml behaviour with resolve_entities=False
        text_elems = parser.root.xpath('.//svg:text', namespaces=parser.namespaces)
        self.assertEqual(len(text_elems), 1)
        # Because entity resolution is disabled, it will be blank or literal '&xxe;' depending on lxml version.
        self.assertNotIn("root:x", text_elems[0].text or "")

if __name__ == '__main__':
    unittest.main()
