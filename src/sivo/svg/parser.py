from lxml import etree
from typing import List, Dict, Any
from .normalizer import SVGNormalizer
from .metadata import get_bounding_box

class SVGParser:
    def __init__(self, filepath_or_string: str, is_file: bool = True):
        # Explicitly secure the parser against XXE
        parser = etree.XMLParser(resolve_entities=False, no_network=True)

        if is_file:
            with open(filepath_or_string, 'rb') as f:
                self.tree = etree.parse(f, parser=parser)
            self.root = self.tree.getroot()
        else:
            self.root = etree.fromstring(filepath_or_string.encode('utf-8'), parser=parser)
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
            if tag_name in ['path', 'rect', 'circle', 'g', 'polygon', 'polyline', 'text', 'tspan']:
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

    def add_shape(self, tag: str, attributes: Dict[str, str]):
        """
        Programmatically adds a new SVG shape to the root element.
        """
        # Get the namespace
        ns = "http://www.w3.org/2000/svg"
        if None in self.root.nsmap:
            ns = self.root.nsmap[None]

        # Create element with fully qualified tag
        qname = f"{{{ns}}}{tag}"
        elem = etree.SubElement(self.root, qname)

        # Handle special text content key
        text_content = attributes.pop('text_content', None)
        if text_content is not None:
            elem.text = text_content

        # Set attributes
        for key, value in attributes.items():
            elem.set(key, str(value))

        # ECharts requires a 'name' attribute matching 'id'
        elem_id = attributes.get('id')
        if elem_id and 'name' not in attributes:
            elem.set('name', elem_id)

    def to_string(self) -> str:
        return etree.tostring(self.tree, encoding='unicode')
