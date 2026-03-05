import unittest
from lxml import etree
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from sivo.svg.metadata import get_bounding_box, calculate_path_bbox, parse_coord

class TestMetadata(unittest.TestCase):
    def test_parse_coord(self):
        self.assertEqual(parse_coord(" 10.5 "), 10.5)
        self.assertEqual(parse_coord("10px"), 10.0)
        self.assertEqual(parse_coord("-5.2em"), -5.2)
        self.assertEqual(parse_coord(" .5 "), 0.5)
        self.assertEqual(parse_coord(None), 0.0)
        self.assertEqual(parse_coord(""), 0.0)
        self.assertEqual(parse_coord("1e2"), 100.0)
        self.assertEqual(parse_coord("-1E2"), -100.0)
        self.assertEqual(parse_coord("1.5e-2"), 0.015)

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

    def test_path_bbox_curves(self):
        # C x1 y1, x2 y2, x y
        d = "M 10 10 C 20 0, 30 0, 40 10"
        bbox = calculate_path_bbox(d)
        self.assertEqual(bbox, [10.0, 0.0, 40.0, 10.0])

    def test_path_bbox_arcs(self):
        d = "M 10 10 A 5 5 0 0 1 20 10"
        bbox = calculate_path_bbox(d)
        self.assertEqual(bbox, [10.0, 10.0, 20.0, 10.0])

    def test_path_bbox_relative_curves(self):
        d = "M 10 10 c 10 -10, 20 -10, 30 0"
        bbox = calculate_path_bbox(d)
        self.assertEqual(bbox, [10.0, 0.0, 40.0, 10.0])

    def test_path_bbox_relative_m(self):
        d = "m 10 10 10 10" # m 10 10 l 10 10
        bbox = calculate_path_bbox(d)
        self.assertEqual(bbox, [10.0, 10.0, 20.0, 20.0])

    def test_path_bbox_negative_coords(self):
        d = "M -10 -10 L -20 -20"
        bbox = calculate_path_bbox(d)
        self.assertEqual(bbox, [-20.0, -20.0, -10.0, -10.0])

    def test_path_bbox_exponential(self):
        d = "M 1e1 1E1 L 2e1 2E1"
        bbox = calculate_path_bbox(d)
        self.assertEqual(bbox, [10.0, 10.0, 20.0, 20.0])

if __name__ == '__main__':
    unittest.main()
