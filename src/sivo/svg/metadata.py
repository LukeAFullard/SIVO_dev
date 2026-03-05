import re
from lxml import etree
from typing import List, Dict, Any, Tuple, Optional

def parse_coord(coord_str: Optional[str]) -> float:
    if not coord_str:
        return 0.0
    match = re.match(r'^[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', coord_str.strip())
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

            # Ensure an even number of coordinates to prevent misalignment
            if len(coords) % 2 != 0:
                coords = coords[:-1]

            xs = coords[0::2]
            ys = coords[1::2]
            return [min(xs), min(ys), max(xs), max(ys)]
        elif tag_name == 'path':
            d_str = elem.get('d', '')
            if not d_str:
                return None

            return calculate_path_bbox(d_str)
    except Exception:
        pass
    return None

class PathBBoxCalculator:
    def __init__(self):
        self.min_x = float('inf')
        self.min_y = float('inf')
        self.max_x = float('-inf')
        self.max_y = float('-inf')
        self.current_x = 0.0
        self.current_y = 0.0

    def update_bounds(self, *coords):
        for i in range(0, len(coords), 2):
            x, y = coords[i], coords[i+1]
            self.min_x = min(self.min_x, x)
            self.max_x = max(self.max_x, x)
            self.min_y = min(self.min_y, y)
            self.max_y = max(self.max_y, y)

    def handle_M_L_T(self, x, y, is_relative):
        if is_relative:
            x += self.current_x
            y += self.current_y
        self.current_x, self.current_y = x, y
        self.update_bounds(x, y)

    def handle_H(self, x, is_relative):
        if is_relative:
            x += self.current_x
        self.current_x = x
        self.update_bounds(x, self.current_y)

    def handle_V(self, y, is_relative):
        if is_relative:
            y += self.current_y
        self.current_y = y
        self.update_bounds(self.current_x, y)

    def handle_C(self, x1, y1, x2, y2, x, y, is_relative):
        if is_relative:
            x1 += self.current_x; y1 += self.current_y
            x2 += self.current_x; y2 += self.current_y
            x += self.current_x; y += self.current_y

        self.update_bounds(self.current_x, self.current_y, x1, y1, x2, y2, x, y)
        self.current_x, self.current_y = x, y

    def handle_S_Q(self, xc, yc, x, y, is_relative):
        if is_relative:
            xc += self.current_x; yc += self.current_y
            x += self.current_x; y += self.current_y

        self.update_bounds(self.current_x, self.current_y, xc, yc, x, y)
        self.current_x, self.current_y = x, y

    def handle_A(self, rx, ry, x_rot, large_arc, sweep, x, y, is_relative):
        if is_relative:
            x += self.current_x; y += self.current_y

        self.update_bounds(self.current_x, self.current_y, x, y)
        self.current_x, self.current_y = x, y


def calculate_path_bbox(d_str: str) -> Optional[List[float]]:
    """
    Calculates an approximate bounding box for an SVG path data string.
    This tracks current points to handle relative commands and finds the min/max of all explicit coordinate points.
    It does not compute precise geometric bounding boxes for cubic/quadratic curves, but rather uses their control points
    and endpoints as a fast, conservative approximation.
    """
    # Tokenize the path data. Find commands (letters) and numbers.
    tokens = re.findall(r'[A-Za-z]|[-+]?(?:\d*\.\d+|\d+)(?:[eE][-+]?\d+)?', d_str)

    if not tokens:
        return None

    calc = PathBBoxCalculator()
    i = 0
    current_cmd = ''

    while i < len(tokens):
        token = tokens[i]

        if token.isalpha():
            current_cmd = token
            i += 1
            if current_cmd.upper() == 'Z':
                continue
        else:
            # If no command was set previously, the implied command is M (which acts as L for subsequent pairs)
            if not current_cmd:
                current_cmd = 'M'

        cmd_upper = current_cmd.upper()
        is_relative = current_cmd.islower()

        if cmd_upper in ['M', 'L', 'T']:
            if i + 1 >= len(tokens): break
            x, y = float(tokens[i]), float(tokens[i+1])
            i += 2
            calc.handle_M_L_T(x, y, is_relative)
            if cmd_upper == 'M':
                current_cmd = 'l' if is_relative else 'L'

        elif cmd_upper in ['H']:
            if i >= len(tokens): break
            x = float(tokens[i])
            i += 1
            calc.handle_H(x, is_relative)

        elif cmd_upper in ['V']:
            if i >= len(tokens): break
            y = float(tokens[i])
            i += 1
            calc.handle_V(y, is_relative)

        elif cmd_upper in ['C']:
            if i + 5 >= len(tokens): break
            x1, y1 = float(tokens[i]), float(tokens[i+1])
            x2, y2 = float(tokens[i+2]), float(tokens[i+3])
            x, y = float(tokens[i+4]), float(tokens[i+5])
            i += 6
            calc.handle_C(x1, y1, x2, y2, x, y, is_relative)

        elif cmd_upper in ['S', 'Q']:
            if i + 3 >= len(tokens): break
            xc, yc = float(tokens[i]), float(tokens[i+1])
            x, y = float(tokens[i+2]), float(tokens[i+3])
            i += 4
            calc.handle_S_Q(xc, yc, x, y, is_relative)

        elif cmd_upper in ['A']:
            if i + 6 >= len(tokens): break
            rx, ry = float(tokens[i]), float(tokens[i+1])
            x_rot = float(tokens[i+2])
            large_arc = float(tokens[i+3])
            sweep = float(tokens[i+4])
            x, y = float(tokens[i+5]), float(tokens[i+6])
            i += 7
            calc.handle_A(rx, ry, x_rot, large_arc, sweep, x, y, is_relative)
        else:
            break

    if calc.min_x == float('inf'):
        return None

    return [calc.min_x, calc.min_y, calc.max_x, calc.max_y]
