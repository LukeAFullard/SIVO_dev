import os
import json
from typing import Dict, Optional, Union
from pydantic import BaseModel

from ..svg.parser import SVGParser
from .actions import InteractionMapping, TooltipAction, URLAction, DrillDownAction, CallbackAction, ThemeOverride, HoverCallbackAction, VideoAction, GalleryAction, AudioAction, MarkdownAction, FetchAction, FormAction
from .config import ProjectConfig, ElementConfig
from ..runtime.bundle_generator import generate_echarts_html

class Infographic:
    def __init__(self, parser: SVGParser):
        self.parser = parser
        self.elements = self.parser.process_elements()
        self.mappings: Dict[str, InteractionMapping] = {}
        self._element_lookup: Dict[str, dict] = {}
        self.overlays: Dict[str, dict] = {}

        # Initialize default mappings
        for elem in self.elements:
            self.mappings[elem['name']] = InteractionMapping(id=elem['id'])
            self._element_lookup[elem['id']] = elem
            self._element_lookup[elem['name']] = elem

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
                    hover_callback_event=elem_config.hover_callback_event,
                    hover_callback_payload=elem_config.hover_callback_payload,
                    panel_position=elem_config.panel_position,
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
        hover_callback_event: Optional[str] = None,
        hover_callback_payload: Optional[dict] = None,
        video: Optional[str] = None,
        gallery: Optional[list[str]] = None,
        audio: Optional[str] = None,
        markdown: Optional[str] = None,
        fetch_url: Optional[str] = None,
        form_fields: Optional[list[dict]] = None,
        form_submit_event: Optional[str] = None,
        panel_position: Optional[str] = None,
        color: Optional[str] = None,
        hover_color: Optional[str] = None,
        border_width: Optional[float] = None,
        border_color: Optional[str] = None,
        glow: Optional[bool] = None,
        animation: Optional[str] = None
    ):
        """
        Maps an SVG element id (or name) to actions or visual themes.
        """
        target_elem = self._element_lookup.get(element_id)
        if not target_elem:
            raise ValueError(f"Element with id/name '{element_id}' not found in SVG.")

        elem_name = target_elem['name']
        mapping = self.mappings[elem_name]

        if html or tooltip:
            mapping.actions.append(TooltipAction(
                title=tooltip,
                content=html if html else f"<h3>{tooltip}</h3>" if tooltip else "",
                panel_position=panel_position or "right"
            ))

        if url:
            mapping.actions.append(URLAction(url=url))

        if drill_to:
            mapping.actions.append(DrillDownAction(target_svg=drill_to))

        if callback_event:
            mapping.actions.append(CallbackAction(event_name=callback_event, payload=callback_payload))

        if hover_callback_event:
            mapping.actions.append(HoverCallbackAction(event_name=hover_callback_event, payload=hover_callback_payload))

        if video:
            mapping.actions.append(VideoAction(video_url=video))

        if gallery:
            mapping.actions.append(GalleryAction(images=gallery))

        if audio:
            mapping.actions.append(AudioAction(audio_url=audio))

        if markdown:
            mapping.actions.append(MarkdownAction(markdown_text=markdown, panel_position=panel_position or "right"))

        if fetch_url:
            mapping.actions.append(FetchAction(fetch_url=fetch_url, panel_position=panel_position or "right"))

        if form_fields and form_submit_event:
            mapping.actions.append(FormAction(form_fields=form_fields, submit_event=form_submit_event, panel_position=panel_position or "right"))

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

        if animation:
            mapping.theme.animation = animation

    def apply_choropleth(self, data_map: Dict[str, float], min_color: str = "#ffffff", max_color: str = "#ff0000", show_legend: bool = True):
        """
        Generates a choropleth map by interpolating colors based on a numeric data mapping.
        Optionally displays a legend overlay.
        """
        if not data_map:
            return

        min_val = min(data_map.values())
        max_val = max(data_map.values())
        range_val = max_val - min_val if max_val > min_val else 1.0

        def hex_to_rgb(h):
            h = h.lstrip('#')
            if len(h) == 3:
                h = ''.join([c*2 for c in h])
            return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

        def rgb_to_hex(r, g, b):
            return f"#{int(r):02x}{int(g):02x}{int(b):02x}"

        min_rgb = hex_to_rgb(min_color)
        max_rgb = hex_to_rgb(max_color)

        for elem_id, value in data_map.items():
            ratio = (value - min_val) / range_val
            r = min_rgb[0] + (max_rgb[0] - min_rgb[0]) * ratio
            g = min_rgb[1] + (max_rgb[1] - min_rgb[1]) * ratio
            b = min_rgb[2] + (max_rgb[2] - min_rgb[2]) * ratio

            color_hex = rgb_to_hex(r, g, b)

            # Map the color to the element. We don't want to overwrite existing tooltips,
            # so we try to catch missing elements and map only the color.
            try:
                self.map(elem_id, color=color_hex)
            except ValueError:
                pass # Element might not exist in SVG, skip it

        if show_legend:
            legend_html = f"""
            <div style="background: rgba(255,255,255,0.9); padding: 10px; border-radius: 5px; border: 1px solid #ccc; font-family: sans-serif; font-size: 12px; display: flex; align-items: center; gap: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); user-select: none;">
                <span>{min_val:.1f}</span>
                <div style="width: 100px; height: 15px; background: linear-gradient(to right, {min_color}, {max_color}); border: 1px solid #999; border-radius: 3px;"></div>
                <span>{max_val:.1f}</span>
            </div>
            """
            # To add an absolute positioned legend that isn't tied to an SVG bounding box,
            # we need to append it directly to the document. We can use a special "fixed" overlay.
            self.overlays["sivo_choropleth_legend"] = {
                "html": legend_html,
                "fixed": True,
                "position": "bottom-left"
            }

    def add_overlay(self, element_id: str, html: str, offset_x: int = 0, offset_y: int = 0):
        """
        Adds a custom HTML overlay positioned over a specific SVG element's center coordinate.
        """
        target_elem = self._element_lookup.get(element_id)
        if not target_elem:
            raise ValueError(f"Element with id/name '{element_id}' not found in SVG.")

        if 'bbox' not in target_elem or not target_elem['bbox']:
            raise ValueError(f"Cannot calculate overlay position: Element '{element_id}' has no bounding box.")

        bbox = target_elem['bbox']
        center_x = (bbox[0] + bbox[2]) / 2.0
        center_y = (bbox[1] + bbox[3]) / 2.0

        self.overlays[element_id] = {
            "html": html,
            "coord": [center_x, center_y],
            "offset": [offset_x, offset_y]
        }

    def get_element_center(self, element_id: str) -> Optional[list[float]]:
        target_elem = self._element_lookup.get(element_id)
        if target_elem and 'bbox' in target_elem and target_elem['bbox']:
            bbox = target_elem['bbox']
            return [(bbox[0] + bbox[2]) / 2.0, (bbox[1] + bbox[3]) / 2.0]
        return None

    def to_echarts_html(self, output_path: Optional[str] = None, custom_css: Optional[str] = None, custom_js: Optional[str] = None) -> str:
        """
        Generates interactive HTML string.
        Optionally writes to output_path.
        """
        mappings_dict = {}
        for k, v in self.mappings.items():
            if hasattr(v, "model_dump"):
                mappings_dict[k] = v.model_dump()
            elif hasattr(v, "dict"):
                mappings_dict[k] = v.dict()
            else:
                mappings_dict[k] = v

        views_data = {
            "default_view": {
                "svg_string": self.parser.to_string(),
                "mappings": mappings_dict,
                "overlays": self.overlays
            }
        }
        return generate_echarts_html(views_data, "default_view", output_path, custom_css, custom_js)

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
