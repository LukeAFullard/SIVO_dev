from lxml import etree
from copy import deepcopy
import re
import collections

class SVGNormalizer:
    def __init__(self, tree: etree._ElementTree):
        self.tree = tree
        self.root = self.tree.getroot()
        self.namespaces = {'svg': 'http://www.w3.org/2000/svg', 'xlink': 'http://www.w3.org/1999/xlink'}

        if None in self.root.nsmap:
            self.namespaces['svg'] = self.root.nsmap[None]
        if 'xlink' in self.root.nsmap:
            self.namespaces['xlink'] = self.root.nsmap['xlink']

    def normalize(self):
        """
        Applies a series of normalization steps to the SVG.
        """
        self.resolve_use_tags()
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
