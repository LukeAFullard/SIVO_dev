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
            d_str = elem.get('d', '')
            if not d_str:
                return None

            return calculate_path_bbox(d_str)
    except Exception:
        pass
    return None

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

    min_x = float('inf')
    min_y = float('inf')
    max_x = float('-inf')
    max_y = float('-inf')

    current_x = 0.0
    current_y = 0.0

    # SVG path commands taking 2 parameters (x, y) per coordinate point
    # V and H take 1 parameter, A takes 7
    # Z takes 0

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

        # Parse arguments based on command
        cmd_upper = current_cmd.upper()

        if cmd_upper in ['M', 'L', 'T']:
            # 2 args: x, y
            if i + 1 >= len(tokens): break
            x = float(tokens[i])
            y = float(tokens[i+1])
            i += 2

            if current_cmd.islower():
                x += current_x
                y += current_y

            current_x, current_y = x, y

            min_x = min(min_x, current_x)
            min_y = min(min_y, current_y)
            max_x = max(max_x, current_x)
            max_y = max(max_y, current_y)

            # M commands act as L for subsequent coordinate pairs
            if cmd_upper == 'M':
                current_cmd = 'l' if current_cmd == 'm' else 'L'

        elif cmd_upper in ['H']:
            # 1 arg: x
            if i >= len(tokens): break
            x = float(tokens[i])
            i += 1

            if current_cmd.islower():
                x += current_x

            current_x = x
            min_x = min(min_x, current_x)
            max_x = max(max_x, current_x)

        elif cmd_upper in ['V']:
            # 1 arg: y
            if i >= len(tokens): break
            y = float(tokens[i])
            i += 1

            if current_cmd.islower():
                y += current_y

            current_y = y
            min_y = min(min_y, current_y)
            max_y = max(max_y, current_y)

        elif cmd_upper in ['C']:
            # 6 args: x1, y1, x2, y2, x, y
            if i + 5 >= len(tokens): break
            x1 = float(tokens[i])
            y1 = float(tokens[i+1])
            x2 = float(tokens[i+2])
            y2 = float(tokens[i+3])
            x = float(tokens[i+4])
            y = float(tokens[i+5])
            i += 6

            if current_cmd.islower():
                x1 += current_x; y1 += current_y
                x2 += current_x; y2 += current_y
                x += current_x; y += current_y

            # Expand bbox to include control points and endpoints
            min_x = min(min_x, current_x, x1, x2, x)
            min_y = min(min_y, current_y, y1, y2, y)
            max_x = max(max_x, current_x, x1, x2, x)
            max_y = max(max_y, current_y, y1, y2, y)

            current_x, current_y = x, y

        elif cmd_upper in ['S', 'Q']:
            # 4 args: x1/x2, y1/y2, x, y
            if i + 3 >= len(tokens): break
            xc = float(tokens[i])
            yc = float(tokens[i+1])
            x = float(tokens[i+2])
            y = float(tokens[i+3])
            i += 4

            if current_cmd.islower():
                xc += current_x; yc += current_y
                x += current_x; y += current_y

            min_x = min(min_x, current_x, xc, x)
            min_y = min(min_y, current_y, yc, y)
            max_x = max(max_x, current_x, xc, x)
            max_y = max(max_y, current_y, yc, y)

            current_x, current_y = x, y

        elif cmd_upper in ['A']:
            # 7 args: rx, ry, x-axis-rotation, large-arc-flag, sweep-flag, x, y
            if i + 6 >= len(tokens): break
            rx = float(tokens[i])
            ry = float(tokens[i+1])
            x_rot = float(tokens[i+2])
            large_arc = float(tokens[i+3])
            sweep = float(tokens[i+4])
            x = float(tokens[i+5])
            y = float(tokens[i+6])
            i += 7

            if current_cmd.islower():
                x += current_x; y += current_y

            # Very rough approximation for arc bbox
            # We just consider the endpoints and roughly the arc's extent
            # Precise geometric bbox for arcs is complex. Using endpoints + rx/ry expansion is safer.
            # But the arc doesn't necessarily reach current_x - rx, it depends on sweep and flags.
            # As a conservative approximation, we just add the endpoints for now.
            min_x = min(min_x, current_x, x)
            min_y = min(min_y, current_y, y)
            max_x = max(max_x, current_x, x)
            max_y = max(max_y, current_y, y)

            current_x, current_y = x, y
        else:
            # Unknown command or malformed path, break to avoid infinite loop
            break

    if min_x == float('inf'):
        return None

    return [min_x, min_y, max_x, max_y]
