import os
import json
from jinja2 import Environment, FileSystemLoader, select_autoescape
from pydantic import BaseModel, Field
from typing import Dict, Any, Optional
from .parser import SVGParser

class SivoMapping(BaseModel):
    id: str
    name: str
    html: Optional[str] = None
    tooltip: Optional[str] = None
    color: Optional[str] = None

class Sivo:
    def __init__(self, filepath_or_string: str, is_file: bool = True):
        self.parser = SVGParser(filepath_or_string, is_file)
        # Call this to normalize name attributes in the SVG
        self.elements = self.parser.process_elements()
        self.mappings: Dict[str, SivoMapping] = {}

        # Initialize default mappings
        for elem in self.elements:
            self.mappings[elem['name']] = SivoMapping(id=elem['id'], name=elem['name'])

        # Jinja2 setup
        template_dir = os.path.join(os.path.dirname(__file__), 'templates')
        self.env = Environment(
            loader=FileSystemLoader(template_dir),
            autoescape=select_autoescape(['html', 'xml'])
        )

    def map(self, element_id: str, html: str = None, tooltip: str = None, color: str = None):
        """
        Maps an SVG element id (or name) to HTML content or tooltip.
        """
        # We store mappings by 'name' since ECharts uses 'name' to identify the regions
        # In our parser, if 'name' is not present, it is set to 'id'.

        # Find the element by id or name
        target_elem = None
        for elem in self.elements:
            if elem['id'] == element_id or elem['name'] == element_id:
                target_elem = elem
                break

        if not target_elem:
            raise ValueError(f"Element with id/name '{element_id}' not found in SVG.")

        elem_name = target_elem['name']

        mapping = self.mappings[elem_name]
        if html:
            mapping.html = html
        if tooltip:
            mapping.tooltip = tooltip
        if color:
            mapping.color = color

    def to_echarts_html(self, output_path: str = None) -> str:
        """
        Renders the mapped data and modified SVG into an interactive HTML string.
        Optionally writes to output_path.
        """
        template = self.env.get_template('echarts.html')

        # Prepare the data array for ECharts map series
        echarts_data = []
        html_mappings_dict = {}

        for name, mapping in self.mappings.items():
            data_item = {
                'name': name,
                'value': 1,
            }
            if mapping.tooltip:
                data_item['tooltip'] = mapping.tooltip
            if mapping.color:
                data_item['itemStyle'] = {'areaColor': mapping.color}

            echarts_data.append(data_item)

            if mapping.html:
                html_mappings_dict[name] = mapping.html

        svg_string = self.parser.to_string()

        html_output = template.render(
            svg_string=json.dumps(svg_string), # Serialize as JSON string to safely inject to JS
            echarts_data=json.dumps(echarts_data),
            html_mappings=json.dumps(html_mappings_dict)
        )

        if output_path:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(html_output)

        return html_output
