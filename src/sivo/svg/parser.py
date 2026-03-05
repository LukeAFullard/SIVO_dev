from lxml import etree
from typing import List, Dict, Any
from .normalizer import SVGNormalizer
from .metadata import get_bounding_box

class SVGParser:
    def __init__(self, filepath_or_string: str, is_file: bool = True):
        if is_file:
            with open(filepath_or_string, 'rb') as f:
                self.tree = etree.parse(f)
            self.root = self.tree.getroot()
        else:
            self.root = etree.fromstring(filepath_or_string.encode('utf-8'))
            self.tree = etree.ElementTree(self.root)

        self.namespaces = {'svg': 'http://www.w3.org/2000/svg'}
        if None in self.root.nsmap:
            self.namespaces['svg'] = self.root.nsmap[None]

        # Normalize the SVG (e.g., inline <use> references) before processing
        normalizer = SVGNormalizer(self.tree)
        normalizer.normalize()

    def process_elements(self) -> List[Dict[str, str]]:
        """
        Extracts id and name attributes from elements (path, rect, circle, g).
        Injects a 'name' attribute equal to 'id' if 'name' is missing,
        because ECharts uses 'name' to identify regions.
        """
        elements = []

        for elem in self.root.iter():
            try:
                tag_name = etree.QName(elem).localname
            except ValueError:
                # E.g. when elem.tag is a Comment or PI (processing instruction)
                continue
            if tag_name in ['path', 'rect', 'circle', 'g', 'polygon', 'polyline']:
                elem_id = elem.get('id')
                if elem_id:
                    elem_name = elem.get('name')
                    if not elem_name:
                        elem_name = elem_id
                        elem.set('name', elem_name)

                    bbox = get_bounding_box(elem)

                    element_data = {
                        'id': elem_id,
                        'name': elem_name,
                        'tag': tag_name
                    }
                    if bbox:
                        element_data['bbox'] = bbox

                    elements.append(element_data)
        return elements

    def get_viewbox(self) -> str:
        return self.root.get('viewBox', '')

    def to_string(self) -> str:
        return etree.tostring(self.tree, encoding='unicode')
