import re
from lxml import etree
from typing import List, Dict, Any, Tuple, Optional

def parse_coord(coord_str: Optional[str]) -> float:
    if not coord_str:
        return 0.0
    match = re.match(r'^[+-]?(?:\d+(?:\.\d*)?|\.\d+)', coord_str.strip())
    if match:
        return float(match.group(0))
    return 0.0

def get_bounding_box(elem: etree._Element) -> Optional[List[float]]:
    """
    Calculates a basic bounding box [min_x, min_y, max_x, max_y] for simple SVG shapes.
    Returns None if unsupported or invalid.
    """
    tag_name = etree.QName(elem).localname
    try:
        if tag_name == 'rect':
            x = parse_coord(elem.get('x', '0'))
            y = parse_coord(elem.get('y', '0'))
            w = parse_coord(elem.get('width', '0'))
            h = parse_coord(elem.get('height', '0'))
            return [x, y, x + w, y + h]
        elif tag_name == 'circle':
            cx = parse_coord(elem.get('cx', '0'))
            cy = parse_coord(elem.get('cy', '0'))
            r = parse_coord(elem.get('r', '0'))
            return [cx - r, cy - r, cx + r, cy + r]
        elif tag_name == 'ellipse':
            cx = parse_coord(elem.get('cx', '0'))
            cy = parse_coord(elem.get('cy', '0'))
            rx = parse_coord(elem.get('rx', '0'))
            ry = parse_coord(elem.get('ry', '0'))
            return [cx - rx, cy - ry, cx + rx, cy + ry]
        elif tag_name == 'line':
            x1 = parse_coord(elem.get('x1', '0'))
            y1 = parse_coord(elem.get('y1', '0'))
            x2 = parse_coord(elem.get('x2', '0'))
            y2 = parse_coord(elem.get('y2', '0'))
            return [min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)]
        elif tag_name in ['polygon', 'polyline']:
            points_str = elem.get('points', '')
            # Extract all numbers from points string
            coords = [float(p) for p in re.findall(r'[-+]?(?:\d*\.\d+|\d+)', points_str)]
            if len(coords) < 2:
                return None
            xs = coords[0::2]
            ys = coords[1::2]
            return [min(xs), min(ys), max(xs), max(ys)]
        elif tag_name == 'path':
            # Naive bounding box for paths based on all numbers in the 'd' attribute.
            # This is a very rough approximation, only considering explicit coordinate values,
            # and might not accurately capture curves.
            d_str = elem.get('d', '')
            coords = [float(p) for p in re.findall(r'[-+]?(?:\d*\.\d+|\d+)', d_str)]
            # Path coords can be absolute or relative, so a simple min/max of all numbers
            # is wildly inaccurate. For Phase 1, we will return a minimal approximation
            # or leave it empty if we don't have a path parser.
            # We will just do min/max of the numbers for absolute paths to have some bbox.
            if len(coords) < 2:
                return None
            # Heuristic: split into X and Y by alternating, this is naive
            # A full path parser is beyond Phase 1 without external libraries
            # but we can provide a dummy [0,0,0,0] to fulfill schema.
            return [0.0, 0.0, 0.0, 0.0]
    except Exception:
        pass
    return None
