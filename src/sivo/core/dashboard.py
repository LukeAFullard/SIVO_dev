# Copyright (c) 2024 SIVO. All rights reserved.
# Licensed under the MIT License. See LICENSE file in the project root for full license information.

from typing import Dict, Optional, List
from .sivo import Sivo
from ..runtime.dashboard_generator import generate_dashboard_blocks_html

class SivoDashboard:
    """
    Manages a multi-block responsive dashboard layout (using CSS Grid/Flexbox)
    instead of a monolithic single SVG. Maps specific Sivo instances to layout blocks.
    """
    def __init__(self, title: str = "Dashboard", columns: int = 3, template: str = "default", background_image_url: Optional[str] = None, theme: str = "light"):
        """
        Initializes the dashboard.
        :param template: The name of the HTML layout template to use (e.g., 'default', 'sidebar_left', 'hero_top').
        :param background_image_url: URL to a background image for the dashboard body.
        :param theme: Theme of the dashboard (e.g., 'light', 'transparent').
        """
        self.desktop_grid: Optional[str] = None
        self.mobile_grid: Optional[str] = None
        self.title = title
        self.columns = columns
        self.template_name = template
        self.background_image_url = background_image_url
        self.theme = theme
        self.blocks: Dict[str, Sivo] = {}
        self.html_blocks: Dict[str, str] = {}
        self.details_panels: Dict[str, Dict] = {}
        self.metrics_panels: Dict[str, Dict] = {}
        self.layout_order: List[Dict[str, str]] = []

    def add_sivo_block(self, block_id: str, sivo_app: Sivo, col_span: int = 1, slot: str = "main", grid_area: Optional[str] = None):
        """Adds a Sivo instance to a specific block/slot in the dashboard layout."""
        self.blocks[block_id] = sivo_app
        self.layout_order.append({"type": "sivo", "id": block_id, "col_span": col_span, "slot": slot, "grid_area": grid_area})

    def add_html_block(self, block_id: str, html_content: str, col_span: int = 1, slot: str = "main", grid_area: Optional[str] = None):
        """Adds raw HTML content to a specific block/slot in the dashboard layout."""
        self.html_blocks[block_id] = html_content
        self.layout_order.append({"type": "html", "id": block_id, "col_span": col_span, "slot": slot, "grid_area": grid_area})

    def add_details_panel(self, block_id: str, title: str = "Details", placeholder: str = "Select an item to view details.", col_span: int = 1, slot: str = "main", grid_area: Optional[str] = None):
        """
        Adds a pre-built panel that automatically listens to SIVO canvas clicks and renders
        the clicked element's `html` (tooltip content) mapping.
        """
        self.details_panels[block_id] = {
            "title": title,
            "placeholder": placeholder
        }
        self.layout_order.append({"type": "details", "id": block_id, "col_span": col_span, "slot": slot, "grid_area": grid_area})

    def add_metrics_panel(self, block_id: str, title: str = "Metrics", metrics: List[str] = None, col_span: int = 1, slot: str = "main", grid_area: Optional[str] = None):
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
        self.layout_order.append({"type": "metrics", "id": block_id, "col_span": col_span, "slot": slot, "grid_area": grid_area})


    def set_grid_layout(self, desktop: str, mobile: Optional[str] = None):
        """
        Defines the responsive CSS Grid layout using grid-template-areas.
        :param desktop: The CSS grid-template-areas string for desktop views.
        :param mobile: The CSS grid-template-areas string for mobile views.
        """
        self.desktop_grid = desktop
        self.mobile_grid = mobile

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
            columns=self.columns,
            template=self.template_name,
            desktop_grid=self.desktop_grid,
            mobile_grid=self.mobile_grid,
            background_image_url=self.background_image_url,
            theme=self.theme,
            output_path=output_path,
            custom_js=custom_js
        )
