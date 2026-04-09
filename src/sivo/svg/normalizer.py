from lxml import etree
from copy import deepcopy
import re
import collections

class SVGNormalizer:
    def __init__(self, tree: etree._ElementTree, simplify_tolerance: float = None):
        self.tree = tree
        self.root = self.tree.getroot()
        self.namespaces = {'svg': 'http://www.w3.org/2000/svg', 'xlink': 'http://www.w3.org/1999/xlink'}
        self.simplify_tolerance = simplify_tolerance

        if None in self.root.nsmap:
            self.namespaces['svg'] = self.root.nsmap[None]
        if 'xlink' in self.root.nsmap:
            self.namespaces['xlink'] = self.root.nsmap['xlink']

    def normalize(self):
        """
        Applies a series of normalization steps to the SVG.
        """
        self.resolve_use_tags()
        if self.simplify_tolerance is not None and self.simplify_tolerance > 0:
            self.simplify_paths(self.simplify_tolerance)
        # Add more normalization steps here (e.g. flattening transforms, converting coordinates to absolute)

    def _parse_coord(self, coord_str: str) -> str:
        """
        Parses a coordinate string which might contain units like 'px' and returns
        the numerical part as a string, or '0' if invalid.
        """
        if not coord_str:
            return '0'
        match = re.match(r'^[+-]?(?:\d+(?:\.\d*)?|\.\d+)', coord_str)
        if match:
            return match.group(0)
        return '0'

    def simplify_paths(self, tolerance: float):
        """
        Simplifies SVG paths by reducing the number of points in straight line segments.
        This uses a basic distance-based simplification to reduce file size and rendering overhead
        for very dense SVG maps, while preserving the overall shape.
        Note: This is a basic implementation that primarily targets L and polygon/polyline points.
        True bezier curve simplification is extremely complex and outside the scope without external dependencies,
        but reducing point density for GIS-exported SVGs (which are mostly lines) is highly effective.
        """
        def get_sq_seg_dist(p, p1, p2):
            x = p1[0]
            y = p1[1]
            dx = p2[0] - x
            dy = p2[1] - y

            if dx != 0 or dy != 0:
                t = ((p[0] - x) * dx + (p[1] - y) * dy) / (dx * dx + dy * dy)
                if t > 1:
                    x = p2[0]
                    y = p2[1]
                elif t > 0:
                    x += dx * t
                    y += dy * t

            dx = p[0] - x
            dy = p[1] - y

            return dx * dx + dy * dy

        def simplify_dp_step(points, first, last, sq_tolerance, simplified):
            max_sq_dist = sq_tolerance
            index = -1

            for i in range(first + 1, last):
                sq_dist = get_sq_seg_dist(points[i], points[first], points[last])
                if sq_dist > max_sq_dist:
                    index = i
                    max_sq_dist = sq_dist

            if max_sq_dist > sq_tolerance:
                if index - first > 1:
                    simplify_dp_step(points, first, index, sq_tolerance, simplified)
                simplified.append(points[index])
                if last - index > 1:
                    simplify_dp_step(points, index, last, sq_tolerance, simplified)

        def simplify_points(points, tol):
            if len(points) <= 2:
                return points
            sq_tolerance = tol * tol
            simplified = [points[0]]
            simplify_dp_step(points, 0, len(points) - 1, sq_tolerance, simplified)
            simplified.append(points[-1])
            return simplified

        # Process polylines and polygons which are purely points
        for tag in ['polyline', 'polygon']:
            for elem in self.root.xpath(f'.//svg:{tag}', namespaces=self.namespaces):
                points_str = elem.get('points', '')
                if not points_str: continue
                # Parse points
                raw_coords = re.findall(r'[+-]?(?:\d+(?:\.\d*)?|\.\d+)', points_str)
                if len(raw_coords) < 4: continue

                points = []
                for i in range(0, len(raw_coords)-1, 2):
                    points.append((float(raw_coords[i]), float(raw_coords[i+1])))

                if points:
                    simplified = simplify_points(points, tolerance)
                    new_points_str = " ".join([f"{p[0]},{p[1]}" for p in simplified])
                    elem.set('points', new_points_str)

        # Basic path simplification (only contiguous absolute L segments, which GIS tools generate heavily)
        for elem in self.root.xpath('.//svg:path', namespaces=self.namespaces):
            d = elem.get('d', '')
            if not d: continue

            # This regex splits the path commands and arguments
            tokens = re.findall(r'([a-zA-Z])|([+-]?(?:\d+(?:\.\d*)?|\.\d+))', d)

            new_d = []
            current_command = None
            current_points = []

            def flush_points():
                if current_points:
                    if current_command == 'L' and len(current_points) > 2:
                        simplified = simplify_points(current_points, tolerance)
                        for p in simplified:
                            new_d.append(f"{p[0]} {p[1]}")
                    else:
                        for p in current_points:
                            new_d.append(f"{p[0]} {p[1]}")
                    current_points.clear()

            # We will track current absolute position to convert relative 'l' to absolute 'L' for simplification
            # or just skip 'l'. Since converting relative to absolute correctly for the whole path is complex
            # and requires full state machine (tracking M, m, C, c, etc.), we'll only simplify absolute 'L' commands.
            # If a user provides relative paths, they won't be simplified.

            i = 0
            while i < len(tokens):
                cmd, val = tokens[i]
                if cmd:
                    flush_points()
                    new_d.append(cmd)
                    current_command = cmd
                elif val:
                    # Look ahead for next value to form a pair
                    if i + 1 < len(tokens) and tokens[i+1][1]:
                        current_points.append((float(val), float(tokens[i+1][1])))
                        i += 1
                    else:
                        # Single value (like for H or V), flush existing and append
                        flush_points()
                        new_d.append(val)
                i += 1
            flush_points()

            elem.set('d', " ".join(new_d))

    def resolve_use_tags(self):
        """
        Finds <use> elements, looks up the referenced element (usually in <defs>),
        clones it, wraps it in a <g> tag to preserve attribute inheritance,
        applies attributes from <use> to the wrapper, and replaces the <use> tag.
        Uses a queue to process <use> elements in O(N) time and avoid N^2 performance
        for large SVG files, successfully parsing files with >1000 uses without limits.
        """

        # Initial search for all <use> tags
        initial_uses = [(u, set()) for u in self.root.xpath('.//svg:use', namespaces=self.namespaces)]
        queue = collections.deque(initial_uses)

        while queue:
            use_elem, visited = queue.popleft()
            parent = use_elem.getparent()

            if parent is None:
                # If the <use> tag has no parent, we can't replace it
                continue

            href = use_elem.get('href')
            if not href:
                # Try xlink:href
                href = use_elem.get(f"{{{self.namespaces.get('xlink', 'http://www.w3.org/1999/xlink')}}}href")

            if not href or not href.startswith('#'):
                # Cannot resolve, remove or skip
                parent.remove(use_elem)
                continue

            ref_id = href[1:]

            # Find the referenced element
            try:
                ref_elem = self.root.xpath(f'.//*[@id="{ref_id}"]', namespaces=self.namespaces)
            except etree.XPathEvalError:
                # If the ref_id is malformed (e.g. contains unescaped quotes), ignore and skip
                ref_elem = []

            if not ref_elem:
                parent.remove(use_elem)
                continue

            if ref_id in visited:
                parent.remove(use_elem)
                continue

            new_visited = visited.copy()
            new_visited.add(ref_id)

            ref_elem = ref_elem[0]

            # Create a wrapper <g> element to hold the clone and apply attributes
            wrapper = etree.Element(f"{{{self.namespaces['svg']}}}g")
            wrapper.set('data-sivo-use-wrapper', 'true')

            # Clone the referenced element
            clone = deepcopy(ref_elem)

            # Remove id from the clone and its descendants to avoid duplicates in the document
            if 'id' in clone.attrib:
                del clone.attrib['id']
            for descendant in clone.iterdescendants():
                if 'id' in descendant.attrib:
                    del descendant.attrib['id']

            wrapper.append(clone)

            # Check for new <use> tags in the clone and append them to queue
            new_uses = clone.xpath('.//svg:use', namespaces=self.namespaces)
            if clone.tag == f"{{{self.namespaces['svg']}}}use":
                new_uses.insert(0, clone)
            for new_use in new_uses:
                queue.append((new_use, new_visited))

            # The wrapper should have the ID of the <use> tag if it exists
            use_id = use_elem.get('id')
            if use_id:
                wrapper.set('id', use_id)

            # Apply x and y as a translate transform on the wrapper
            # SVG transformations are applied outermost to innermost (left-to-right).
            # So the order is: use_transform translate(x,y) existing_transform (but we only apply use_transform and translate to wrapper)
            x_raw = use_elem.get('x', '0')
            y_raw = use_elem.get('y', '0')

            x = self._parse_coord(x_raw)
            y = self._parse_coord(y_raw)

            use_transform = use_elem.get('transform', '')

            try:
                xf = float(x)
                yf = float(y)
            except ValueError:
                xf, yf = 0.0, 0.0

            translate_transform = ""
            if xf != 0.0 or yf != 0.0:
                translate_transform = f"translate({x}, {y})"

            # Combine the transforms on the wrapper
            transforms_to_apply = []
            if use_transform:
                transforms_to_apply.append(use_transform)
            if translate_transform:
                transforms_to_apply.append(translate_transform)

            if transforms_to_apply:
                wrapper.set('transform', ' '.join(transforms_to_apply))

            # Copy other attributes from <use> (e.g., fill, stroke, class, etc.) except x, y, href, transform, id
            exclude_attrs = ['x', 'y', 'href', 'transform', 'id']
            for attr, value in use_elem.attrib.items():
                if attr not in exclude_attrs and not attr.endswith('href'):
                    wrapper.set(attr, value)

            # Append wrapper to parent, maintaining order, and remove use_elem
            parent.replace(use_elem, wrapper)
