import os
import json
from typing import Dict, Optional, Union
from pydantic import BaseModel

from ..svg.parser import SVGParser
from .actions import InteractionMapping, TooltipAction, URLAction, DrillDownAction, CallbackAction, ThemeOverride
from ..runtime.bundle_generator import generate_echarts_html

class Infographic:
    def __init__(self, parser: SVGParser):
        self.parser = parser
        self.elements = self.parser.process_elements()
        self.mappings: Dict[str, InteractionMapping] = {}

        # Initialize default mappings
        for elem in self.elements:
            self.mappings[elem['name']] = InteractionMapping(id=elem['id'])

    @classmethod
    def from_svg(cls, filepath: str) -> "Infographic":
        parser = SVGParser(filepath, is_file=True)
        return cls(parser)

    @classmethod
    def from_string(cls, svg_string: str) -> "Infographic":
        parser = SVGParser(svg_string, is_file=False)
        return cls(parser)

    def map(
        self,
        element_id: str,
        tooltip: Optional[str] = None,
        html: Optional[str] = None,
        url: Optional[str] = None,
        drill_to: Optional[str] = None,
        color: Optional[str] = None,
        hover_color: Optional[str] = None
    ):
        """
        Maps an SVG element id (or name) to actions or visual themes.
        """
        target_elem = None
        for elem in self.elements:
            if elem['id'] == element_id or elem['name'] == element_id:
                target_elem = elem
                break

        if not target_elem:
            raise ValueError(f"Element with id/name '{element_id}' not found in SVG.")

        elem_name = target_elem['name']
        mapping = self.mappings[elem_name]

        if html or tooltip:
            mapping.actions.append(TooltipAction(
                title=tooltip,
                content=html if html else f"<h3>{tooltip}</h3>" if tooltip else ""
            ))

        if url:
            mapping.actions.append(URLAction(url=url))

        if drill_to:
            mapping.actions.append(DrillDownAction(target_svg=drill_to))

        if color:
            mapping.theme.color = color

        if hover_color:
            mapping.theme.hover_color = hover_color

    def to_echarts_html(self, output_path: Optional[str] = None) -> str:
        """
        Generates interactive HTML string.
        Optionally writes to output_path.
        """
        svg_string = self.parser.to_string()
        return generate_echarts_html(svg_string, self.mappings, output_path)

    def get_manifest(self) -> Dict:
        """
        Returns the interaction manifest.
        """
        manifest = {"objects": {}}
        for name, mapping in self.mappings.items():
            if mapping.actions or mapping.theme.color or mapping.theme.hover_color:
                manifest["objects"][name] = mapping.model_dump()
        return manifest
