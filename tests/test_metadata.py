import unittest
from lxml import etree
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from sivo.svg.metadata import get_bounding_box, calculate_path_bbox

class TestMetadata(unittest.TestCase):
    def test_rect_bbox(self):
        elem = etree.Element("rect", x="10", y="20", width="30", height="40")
        bbox = get_bounding_box(elem)
        self.assertEqual(bbox, [10.0, 20.0, 40.0, 60.0])

    def test_circle_bbox(self):
        elem = etree.Element("circle", cx="50", cy="50", r="10")
        bbox = get_bounding_box(elem)
        self.assertEqual(bbox, [40.0, 40.0, 60.0, 60.0])

    def test_polygon_bbox(self):
        elem = etree.Element("polygon", points="0,0 100,0 100,100 0,100")
        bbox = get_bounding_box(elem)
        self.assertEqual(bbox, [0.0, 0.0, 100.0, 100.0])

    def test_path_bbox_absolute(self):
        # M 10 10 L 90 10 L 90 90 Z
        d = "M 10 10 L 90 10 L 90 90 Z"
        elem = etree.Element("path", d=d)
        bbox = get_bounding_box(elem)
        self.assertEqual(bbox, [10.0, 10.0, 90.0, 90.0])

    def test_path_bbox_relative(self):
        # M 10 10 l 80 0 l 0 80 z
        # Should be same as absolute [10, 10, 90, 90]
        d = "M 10 10 l 80 0 l 0 80 z"
        bbox = calculate_path_bbox(d)
        self.assertEqual(bbox, [10.0, 10.0, 90.0, 90.0])

    def test_path_bbox_implicit_l(self):
        # M 10 10 90 10 90 90
        # M 10,10 implies L 90,10 L 90,90
        d = "M 10 10 90 10 90 90"
        bbox = calculate_path_bbox(d)
        self.assertEqual(bbox, [10.0, 10.0, 90.0, 90.0])

    def test_path_bbox_complex(self):
        # M 10 10 H 90 V 90 C 90 100, 100 100, 100 90 Z
        d = "M 10 10 H 90 V 90 C 90 100, 100 100, 100 90 Z"
        bbox = calculate_path_bbox(d)
        self.assertEqual(bbox, [10.0, 10.0, 100.0, 100.0])

if __name__ == '__main__':
    unittest.main()
