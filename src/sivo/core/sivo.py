from typing import Dict, Optional, Union

from .config import ProjectConfig
from .infographic import Infographic

class Sivo:
    """
    SIVO (SVG Interactive Vector Objects) Orchestrator.
    This class serves as the primary declarative Python API for the framework,
    hiding JavaScript complexity and managing the Infographic lifecycle.
    """
    def __init__(self, infographic: Infographic, default_panel_position: str = "right", lock_zoom_out: bool = False):
        self.infographic = infographic
        self.infographic.default_panel_position = default_panel_position
        self.infographic.lock_zoom_out = lock_zoom_out

    @classmethod
    def from_svg(cls, filepath: str, default_panel_position: str = "right", lock_zoom_out: bool = False) -> "Sivo":
        """Initializes a Sivo instance from an SVG file path."""
        info = Infographic.from_svg(filepath)
        return cls(info, default_panel_position=default_panel_position, lock_zoom_out=lock_zoom_out)

    @classmethod
    def from_string(cls, svg_string: str, default_panel_position: str = "right", lock_zoom_out: bool = False) -> "Sivo":
        """Initializes a Sivo instance directly from an SVG string."""
        info = Infographic.from_string(svg_string)
        return cls(info, default_panel_position=default_panel_position, lock_zoom_out=lock_zoom_out)

    @classmethod
    def from_config(cls, config: Union[str, dict, ProjectConfig], base_dir: str = ".") -> "Sivo":
        """
        Creates a Sivo instance from a configuration file, dictionary, or ProjectConfig object.
        """
        return cls(Infographic.from_config(config, base_dir=base_dir))

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
        social: Optional[dict] = None,
        document: Optional[str] = None,
        map_location: Optional[str] = None,
        analytics: Optional[dict] = None,
        datasource: Optional[dict] = None,
        external_form: Optional[dict] = None,
        ecommerce: Optional[dict] = None,
        rich_media: Optional[dict] = None,
        bi: Optional[dict] = None,
        replit: Optional[str] = None,
        echarts_option: Optional[dict] = None,
        panel_position: Optional[str] = None,
        open_by_default: bool = False,
        color: Optional[str] = None,
        hover_color: Optional[str] = None,
        border_width: Optional[float] = None,
        border_color: Optional[str] = None,
        glow: Optional[bool] = None,
        animation: Optional[str] = None
    ):
        """
        Maps an SVG element id (or name) to actions or visual themes.
        This provides a seamless, declarative API.
        """
        self.infographic.map(
            element_id=element_id,
            tooltip=tooltip,
            html=html,
            url=url,
            drill_to=drill_to,
            callback_event=callback_event,
            callback_payload=callback_payload,
            hover_callback_event=hover_callback_event,
            hover_callback_payload=hover_callback_payload,
            video=video,
            gallery=gallery,
            audio=audio,
            markdown=markdown,
            fetch_url=fetch_url,
            form_fields=form_fields,
            form_submit_event=form_submit_event,
            social=social,
            document=document,
            map_location=map_location,
            analytics=analytics,
            datasource=datasource,
            external_form=external_form,
            ecommerce=ecommerce,
            rich_media=rich_media,
            bi=bi,
            replit=replit,
            echarts_option=echarts_option,
            panel_position=panel_position,
            open_by_default=open_by_default,
            color=color,
            hover_color=hover_color,
            border_width=border_width,
            border_color=border_color,
            glow=glow,
            animation=animation
        )

    def bind_data(self, data: Dict[str, Dict[str, float]], key: str, colors: list, min_val: float, max_val: float):
        """
        Binds quantitative data to SVG IDs dynamically and applies a color scale.
        """
        self.infographic.bind_data(data, key, colors, min_val, max_val)

    def apply_choropleth(self, data_map: Dict[str, float], min_color: str = "#ffffff", max_color: str = "#ff0000", show_legend: bool = True):
        """
        Generates a choropleth map by interpolating colors based on a numeric data mapping.
        """
        self.infographic.apply_choropleth(data_map, min_color, max_color, show_legend)

    def add_overlay(self, element_id: str, html: str, offset_x: int = 0, offset_y: int = 0, scale_with_zoom: bool = False):
        """Adds a custom HTML overlay over a specific SVG element's center coordinate."""
        self.infographic.add_overlay(element_id, html, offset_x, offset_y, scale_with_zoom)

    def add_marker(self, element_id: str, icon: str = "📍", label: str = "", offset_x: int = 0, offset_y: int = 0, scale_with_zoom: bool = False):
        """
        Convenience method to drop an icon and label at the center of a specified element.
        """
        html = f"""
        <div style="display: flex; flex-direction: column; align-items: center; transform: translate(-50%, -100%);">
            <span style="font-size: 24px; filter: drop-shadow(0px 2px 2px rgba(0,0,0,0.5));">{icon}</span>
            <span style="background: white; border: 1px solid #ccc; padding: 2px 4px; border-radius: 4px; font-size: 12px; font-family: sans-serif; white-space: nowrap; margin-top: -4px;">{label}</span>
        </div>
        """
        self.infographic.add_overlay(element_id, html, offset_x, offset_y, scale_with_zoom)

    def get_element_center(self, element_id: str) -> Optional[list[float]]:
        """Gets the center coordinate [x, y] of a specific element, useful for programmatic zoom."""
        return self.infographic.get_element_center(element_id)

    def _get_view_data(self) -> Dict:
        """Internal method to extract view data for bundle generation."""
        mappings_dict = {}
        for k, v in self.infographic.mappings.items():
            if hasattr(v, "model_dump"):
                mappings_dict[k] = v.model_dump()
            elif hasattr(v, "dict"):
                mappings_dict[k] = v.dict()
            else:
                mappings_dict[k] = v

        view_data = {
            "svg_string": self.infographic.parser.to_string(),
            "mappings": mappings_dict,
            "overlays": self.infographic.overlays,
            "lock_zoom_out": getattr(self.infographic, "lock_zoom_out", False)
        }
        if self.infographic.data_binding:
            view_data["data_binding"] = self.infographic.data_binding.model_dump()
        return view_data

    def to_html(self, output_path: Optional[str] = None, custom_css: Optional[str] = None, custom_js: Optional[str] = None) -> str:
        """
        Generates the interactive HTML string (bundle) containing the ECharts map,
        Jinja2 template, and mapped behaviors. Optionally saves to a file.
        """
        from ..runtime.bundle_generator import generate_echarts_html

        # Wrap the single view in a dictionary to reuse the multi-view bundle generator
        views_data = {
            "default_view": self._get_view_data()
        }

        return generate_echarts_html(
            views_data=views_data,
            initial_view="default_view",
            output_path=output_path,
            custom_css=custom_css,
            custom_js=custom_js
        )

    def get_manifest(self) -> Dict:
        """Returns the interaction manifest JSON data."""
        return self.infographic.get_manifest()

    def get_metadata(self) -> Dict:
        """Returns metadata (bounding boxes, tags, IDs) of all processed SVG elements."""
        return self.infographic.get_metadata()

    def export_metadata(self, output_path: str):
        """Exports the element metadata to a JSON file."""
        self.infographic.export_metadata(output_path)
