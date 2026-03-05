import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from sivo.svg.parser import SVGParser
from sivo.core.infographic import Infographic
from lxml import etree

class TestSVGNormalizer(unittest.TestCase):
    def test_use_tag_resolution(self):
        svg_content = """
        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
            <defs>
                <rect id="base_rect" width="10" height="10" fill="red"/>
            </defs>
            <use id="use_rect" href="#base_rect" x="20" y="30" fill="blue"/>
            <use id="use_rect2" xlink:href="#base_rect" x="50" y="50" transform="scale(2)"/>
        </svg>
        """
        parser = SVGParser(svg_content, is_file=False)
        elements = parser.process_elements()

        # Check that 'use_rect' and 'use_rect2' are now g elements (wrappers)
        use_rect_elem = next((e for e in elements if e['id'] == 'use_rect'), None)
        self.assertIsNotNone(use_rect_elem)
        self.assertEqual(use_rect_elem['tag'], 'g')

        use_rect2_elem = next((e for e in elements if e['id'] == 'use_rect2'), None)
        self.assertIsNotNone(use_rect2_elem)
        self.assertEqual(use_rect2_elem['tag'], 'g')

        # Check attributes of the wrapper element in the tree
        root = parser.root
        namespaces = {'svg': 'http://www.w3.org/2000/svg'}

        wrapper1 = root.xpath('.//svg:g[@id="use_rect"]', namespaces=namespaces)[0]
        rect1 = wrapper1.xpath('./svg:rect', namespaces=namespaces)[0]
        self.assertEqual(rect1.get('width'), '10')
        self.assertEqual(rect1.get('height'), '10')

        # fill goes to the wrapper
        self.assertEqual(wrapper1.get('fill'), 'blue')
        self.assertEqual(wrapper1.get('transform'), 'translate(20, 30)')

        wrapper2 = root.xpath('.//svg:g[@id="use_rect2"]', namespaces=namespaces)[0]
        self.assertEqual(wrapper2.get('transform'), 'scale(2) translate(50, 50)')

    def test_transform_order(self):
        svg_content = """
        <svg xmlns="http://www.w3.org/2000/svg">
            <defs>
                <rect id="base" transform="rotate(45)"/>
            </defs>
            <use id="test_use" href="#base" x="10" y="20" transform="scale(2)"/>
        </svg>
        """
        parser = SVGParser(svg_content, is_file=False)
        root = parser.root
        namespaces = {'svg': 'http://www.w3.org/2000/svg'}
        wrapper = root.xpath('.//svg:g[@id="test_use"]', namespaces=namespaces)[0]
        # Order on wrapper should be use_transform and translate(x,y).
        self.assertEqual(wrapper.get('transform'), 'scale(2) translate(10, 20)')
        # The inner rect still has rotate(45)
        rect = wrapper.xpath('./svg:rect', namespaces=namespaces)[0]
        self.assertEqual(rect.get('transform'), 'rotate(45)')

    def test_nested_use_tags_and_duplicate_ids(self):
        svg_content = """
        <svg xmlns="http://www.w3.org/2000/svg">
            <defs>
                <rect id="inner_rect" width="5" height="5"/>
                <g id="outer_group">
                    <use id="inner_use" href="#inner_rect" x="5" y="5"/>
                    <circle id="inner_circle" r="10"/>
                </g>
            </defs>
            <use id="main_use" href="#outer_group" x="10" y="10"/>
        </svg>
        """
        parser = SVGParser(svg_content, is_file=False)
        root = parser.root
        namespaces = {'svg': 'http://www.w3.org/2000/svg'}

        # Check that main_use became a group
        g = root.xpath('.//svg:g[@id="main_use"]', namespaces=namespaces)
        self.assertEqual(len(g), 1)

        # Inside the group, inner_use should have been resolved to a rect
        # and the id 'inner_use' and 'inner_rect', 'inner_circle' should be stripped from descendants
        rects = root.xpath('.//svg:g[@id="main_use"]//svg:rect', namespaces=namespaces)
        self.assertEqual(len(rects), 1)
        self.assertIsNone(rects[0].get('id'))

        circles = root.xpath('.//svg:g[@id="main_use"]//svg:circle', namespaces=namespaces)
        self.assertEqual(len(circles), 1)
        self.assertIsNone(circles[0].get('id'))

        # The inner use transform should combine correctly
        # The inner use had x=5, y=5. The wrapper should have translate(5, 5).
        # We wrapped the clone in a <g> tag, so let's find that <g> tag.
        # main_use wrapper -> outer_group (cloned) -> inner_use wrapper -> inner_rect (cloned)
        inner_wrapper = root.xpath('.//svg:g[@id="main_use"]//svg:g[@data-sivo-use-wrapper="true"]', namespaces=namespaces)[0]
        self.assertEqual(inner_wrapper.get('transform'), 'translate(5, 5)')

    def test_circular_dependency(self):
        svg_content = """
        <svg xmlns="http://www.w3.org/2000/svg">
            <defs>
                <g id="a">
                    <use href="#b"/>
                </g>
                <g id="b">
                    <use href="#a"/>
                </g>
            </defs>
            <use id="main" href="#a"/>
        </svg>
        """
        # This shouldn't hang
        parser = SVGParser(svg_content, is_file=False)
        self.assertIsNotNone(parser.root)

    def test_svg_units_parsing(self):
        svg_content = """
        <svg xmlns="http://www.w3.org/2000/svg">
            <defs>
                <rect id="test_rect" width="10" height="10"/>
            </defs>
            <use id="test_use" href="#test_rect" x="10px" y="-5.5%"/>
        </svg>
        """
        parser = SVGParser(svg_content, is_file=False)
        root = parser.root
        namespaces = {'svg': 'http://www.w3.org/2000/svg'}
        wrapper = root.xpath('.//svg:g[@id="test_use"]', namespaces=namespaces)[0]
        self.assertEqual(wrapper.get('transform'), 'translate(10, -5.5)')

    def test_svg_units_parsing_no_leading_zero(self):
        svg_content = """
        <svg xmlns="http://www.w3.org/2000/svg">
            <defs>
                <rect id="test_rect" width="10" height="10"/>
            </defs>
            <use id="test_use" href="#test_rect" x="-.5" y=".25"/>
        </svg>
        """
        parser = SVGParser(svg_content, is_file=False)
        root = parser.root
        namespaces = {'svg': 'http://www.w3.org/2000/svg'}
        wrapper = root.xpath('.//svg:g[@id="test_use"]', namespaces=namespaces)[0]
        self.assertEqual(wrapper.get('transform'), 'translate(-.5, .25)')

    def test_large_number_of_uses(self):
        uses = "\n".join([f'<use id="use_{i}" href="#dot" x="{i}" y="{i}"/>' for i in range(2000)])
        svg_content = f"""
        <svg xmlns="http://www.w3.org/2000/svg">
            <defs>
                <circle id="dot" r="5"/>
            </defs>
            {uses}
        </svg>
        """
        parser = SVGParser(svg_content, is_file=False)
        root = parser.root
        namespaces = {'svg': 'http://www.w3.org/2000/svg'}

        # Check that all 2000 uses were resolved to groups (wrappers)
        wrappers = root.xpath('.//svg:g[@data-sivo-use-wrapper="true"]', namespaces=namespaces)
        self.assertEqual(len(wrappers), 2000)

    def test_attribute_inheritance(self):
        svg_content = """
        <svg xmlns="http://www.w3.org/2000/svg">
            <defs>
                <rect id="test_rect" width="10" height="10" fill="red"/>
            </defs>
            <use id="test_use" href="#test_rect" fill="blue"/>
        </svg>
        """
        parser = SVGParser(svg_content, is_file=False)
        root = parser.root
        namespaces = {'svg': 'http://www.w3.org/2000/svg'}
        wrapper = root.xpath('.//svg:g[@id="test_use"]', namespaces=namespaces)[0]

        # Wrapper should have fill="blue"
        self.assertEqual(wrapper.get('fill'), 'blue')

        # Clone should still have fill="red"
        rect = wrapper.xpath('./svg:rect', namespaces=namespaces)[0]
        self.assertEqual(rect.get('fill'), 'red')

if __name__ == '__main__':
    unittest.main()
