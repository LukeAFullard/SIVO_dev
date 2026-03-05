import os
import json
from typing import Dict, Optional, Union
from pydantic import BaseModel

from ..svg.parser import SVGParser
from .actions import InteractionMapping, TooltipAction, URLAction, DrillDownAction, CallbackAction, ThemeOverride
from .config import ProjectConfig, ElementConfig
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

    @classmethod
    def from_config(cls, config: Union[str, dict, ProjectConfig], base_dir: str = ".") -> "Infographic":
        """
        Creates an Infographic from a configuration file, dictionary, or ProjectConfig object.
        """
        if isinstance(config, str):
            with open(config, 'r', encoding='utf-8') as f:
                data = json.load(f)
            # If config is a file path, base_dir is the directory of that file
            base_dir = os.path.dirname(os.path.abspath(config))
            cfg = ProjectConfig(**data)
        elif isinstance(config, dict):
            cfg = ProjectConfig(**config)
        elif isinstance(config, ProjectConfig):
            cfg = config
        else:
            raise ValueError("config must be a file path, dict, or ProjectConfig instance.")

        # Resolve the SVG file path relative to the base directory
        svg_path = os.path.join(base_dir, cfg.svg_file)
        if not os.path.exists(svg_path):
            raise FileNotFoundError(f"SVG file not found: {svg_path}")

        infographic = cls.from_svg(svg_path)

        for element_id, elem_config in cfg.mappings.items():
            try:
                infographic.map(
                    element_id,
                    tooltip=elem_config.tooltip,
                    html=elem_config.html,
                    url=elem_config.url,
                    drill_to=elem_config.drill_to,
                    callback_event=elem_config.callback_event,
                    callback_payload=elem_config.callback_payload,
                    color=elem_config.color,
                    hover_color=elem_config.hover_color,
                    border_width=elem_config.border_width,
                    border_color=elem_config.border_color,
                    glow=elem_config.glow
                )
            except ValueError as e:
                # Log or handle missing elements gracefully, perhaps a warning
                print(f"Warning mapping {element_id}: {e}")

        return infographic

    def map(
        self,
        element_id: str,
        tooltip: Optional[str] = None,
        html: Optional[str] = None,
        url: Optional[str] = None,
        drill_to: Optional[str] = None,
        callback_event: Optional[str] = None,
        callback_payload: Optional[dict] = None,
        color: Optional[str] = None,
        hover_color: Optional[str] = None,
        border_width: Optional[float] = None,
        border_color: Optional[str] = None,
        glow: Optional[bool] = None
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

        if callback_event:
            mapping.actions.append(CallbackAction(event_name=callback_event, payload=callback_payload))

        if color:
            mapping.theme.color = color

        if hover_color:
            mapping.theme.hover_color = hover_color

        if border_width is not None:
            mapping.theme.border_width = border_width

        if border_color:
            mapping.theme.border_color = border_color

        if glow is not None:
            mapping.theme.glow = glow

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
            if (mapping.actions or mapping.theme.color or mapping.theme.hover_color or
                mapping.theme.border_color or mapping.theme.border_width is not None or
                mapping.theme.glow is not None):
                manifest["objects"][name] = mapping.model_dump()
        return manifest

    def get_metadata(self) -> Dict:
        """
        Returns the SVG metadata including bounding boxes and element types.
        """
        metadata = {"objects": []}
        for elem in self.elements:
            obj_data = {
                "id": elem["id"],
                "type": elem["tag"]
            }
            if "bbox" in elem:
                obj_data["bbox"] = elem["bbox"]
            metadata["objects"].append(obj_data)
        return metadata

    def export_metadata(self, output_path: str):
        """
        Exports the SVG metadata to a JSON file.
        """
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(self.get_metadata(), f, indent=2)
