from typing import Dict, Optional, Union

from .config import ProjectConfig
from .infographic import Infographic

class Sivo:
    """
    SIVO (SVG Interactive Vector Objects) Orchestrator.
    This class serves as the primary declarative Python API for the framework,
    hiding JavaScript complexity and managing the Infographic lifecycle.
    """
    def __init__(self, infographic: Infographic):
        self.infographic = infographic

    @classmethod
    def from_svg(cls, filepath: str) -> "Sivo":
        """Initializes a Sivo instance from an SVG file path."""
        return cls(Infographic.from_svg(filepath))

    @classmethod
    def from_string(cls, svg_string: str) -> "Sivo":
        """Initializes a Sivo instance directly from an SVG string."""
        return cls(Infographic.from_string(svg_string))

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
        color: Optional[str] = None,
        hover_color: Optional[str] = None,
        border_width: Optional[float] = None,
        border_color: Optional[str] = None,
        glow: Optional[bool] = None
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
            color=color,
            hover_color=hover_color,
            border_width=border_width,
            border_color=border_color,
            glow=glow
        )

    def to_html(self, output_path: Optional[str] = None, custom_css: Optional[str] = None, custom_js: Optional[str] = None) -> str:
        """
        Generates the interactive HTML string (bundle) containing the ECharts map,
        Jinja2 template, and mapped behaviors. Optionally saves to a file.
        """
        return self.infographic.to_echarts_html(output_path=output_path, custom_css=custom_css, custom_js=custom_js)

    def get_manifest(self) -> Dict:
        """Returns the interaction manifest JSON data."""
        return self.infographic.get_manifest()

    def get_metadata(self) -> Dict:
        """Returns metadata (bounding boxes, tags, IDs) of all processed SVG elements."""
        return self.infographic.get_metadata()

    def export_metadata(self, output_path: str):
        """Exports the element metadata to a JSON file."""
        self.infographic.export_metadata(output_path)
