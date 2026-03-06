from typing import Dict, Optional
from .sivo import Sivo
from ..runtime.bundle_generator import generate_echarts_html

class SivoProject:
    """
    Manages multiple Sivo instances (views) to create a multi-level, standalone interactive HTML bundle.
    """
    def __init__(self, initial_view_id: str):
        self.initial_view_id = initial_view_id
        self.views: Dict[str, Sivo] = {}

    def add_view(self, view_id: str, sivo_app: Sivo):
        """Adds a Sivo instance as a navigable view."""
        self.views[view_id] = sivo_app

    def to_html(self, output_path: Optional[str] = None, custom_css: Optional[str] = None, custom_js: Optional[str] = None) -> str:
        """
        Generates a single interactive HTML string containing all registered views.
        Optionally saves to a file.
        """
        if self.initial_view_id not in self.views:
            raise ValueError(f"Initial view '{self.initial_view_id}' not found in registered views.")

        views_data = {}
        for view_id, app in self.views.items():
            views_data[view_id] = {
                "svg_string": app.infographic.parser.to_string(),
                "mappings": app.get_manifest()["objects"], # we only need the dict of objects
                "overlays": app.infographic.overlays
            }

        return generate_echarts_html(
            views_data=views_data,
            initial_view=self.initial_view_id,
            output_path=output_path,
            custom_css=custom_css,
            custom_js=custom_js
        )
