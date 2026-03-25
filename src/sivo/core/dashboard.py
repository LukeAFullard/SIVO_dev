from typing import Dict, Optional, List
from .sivo import Sivo
from ..runtime.dashboard_generator import generate_dashboard_blocks_html

class SivoDashboard:
    """
    Manages a multi-block responsive dashboard layout (using CSS Grid/Flexbox)
    instead of a monolithic single SVG. Maps specific Sivo instances to layout blocks.
    """
    def __init__(self, title: str = "Dashboard"):
        self.title = title
        self.blocks: Dict[str, Sivo] = {}
        self.html_blocks: Dict[str, str] = {}
        self.details_panels: Dict[str, Dict] = {}
        self.metrics_panels: Dict[str, Dict] = {}
        self.layout_order: List[Dict[str, str]] = []

    def add_sivo_block(self, block_id: str, sivo_app: Sivo):
        """Adds a Sivo instance to a specific block in the dashboard layout."""
        self.blocks[block_id] = sivo_app
        self.layout_order.append({"type": "sivo", "id": block_id})

    def add_html_block(self, block_id: str, html_content: str):
        """Adds raw HTML content to a specific block in the dashboard layout. Useful for custom headers/footers."""
        self.html_blocks[block_id] = html_content
        self.layout_order.append({"type": "html", "id": block_id})

    def add_details_panel(self, block_id: str, title: str = "Details", placeholder: str = "Select an item to view details."):
        """
        Adds a pre-built panel that automatically listens to SIVO canvas clicks and renders
        the clicked element's `html` (tooltip content) mapping.
        """
        self.details_panels[block_id] = {
            "title": title,
            "placeholder": placeholder
        }
        self.layout_order.append({"type": "details", "id": block_id})

    def add_metrics_panel(self, block_id: str, title: str = "Metrics", metrics: List[str] = None):
        """
        Adds a pre-built panel that automatically listens to SIVO canvas clicks and renders
        the specified keys from the clicked element's `callback_payload` mapping.
        """
        if metrics is None:
            metrics = []
        self.metrics_panels[block_id] = {
            "title": title,
            "metrics": metrics
        }
        self.layout_order.append({"type": "metrics", "id": block_id})

    def to_html(self, output_path: Optional[str] = None, custom_js: Optional[str] = None) -> str:
        """
        Generates a responsive HTML dashboard containing the assigned blocks.
        Optionally saves to a file.
        """
        if not self.blocks and not self.html_blocks:
            raise ValueError("No blocks added to the dashboard.")

        views_data = {}
        # We process each block as a "view" using the standard Sivo data extractor
        for block_id, app in self.blocks.items():
            views_data[block_id] = app._get_view_data()

        return generate_dashboard_blocks_html(
            views_data=views_data,
            html_blocks=self.html_blocks,
            details_panels=self.details_panels,
            metrics_panels=self.metrics_panels,
            layout_order=self.layout_order,
            title=self.title,
            output_path=output_path,
            custom_js=custom_js
        )
