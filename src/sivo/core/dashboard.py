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
    def __init__(self, title: str = "Dashboard", columns: int = 3, template: str = "default", background_image_url: Optional[str] = None, background_image_opacity: float = 1.0, background_image_size: str = "cover", gap: str = "normal", width: str = "100%", mobile_width: str = "100%", lock_canvas: bool = False, theme: str = "light", navigation_menu: Optional[List[Dict[str, str]]] = None, navigation_menu_position: str = 'top-right'):
        """
        Initializes the dashboard.
        :param template: The name of the HTML layout template to use (e.g., 'default', 'sidebar_left', 'hero_top').
        :param background_image_url: URL to a background image for the dashboard body.
        :param background_image_size: CSS background-size property. Default is 'cover'.
        :param gap: Defines the dashboard spacing. Accepts "super tight", "tight", "semi-tight", "normal" (default), or custom CSS valid value (e.g., '1.5rem').
        :param width: CSS max-width for the dashboard container. Default is '100%'.
        :param mobile_width: CSS max-width for the dashboard container on mobile devices. Default is '100%'.
        """
        self.desktop_grid: Optional[str] = None
        self.mobile_grid: Optional[str] = None
        self.title = title
        self.columns = columns
        self.template_name = template
        self.background_image_url = background_image_url
        self.background_image_opacity = background_image_opacity
        self.background_image_size = background_image_size

        if gap == "normal":
            self.gap = "1.5rem"
            self.mobile_gap = "1rem"
        elif gap == "semi-tight":
            self.gap = "1rem"
            self.mobile_gap = "0.75rem"
        elif gap == "tight":
            self.gap = "0.5rem"
            self.mobile_gap = "0.35rem"
        elif gap == "super tight":
            self.gap = "0.25rem"
            self.mobile_gap = "0.15rem"
        else:
            self.gap = gap
            self.mobile_gap = gap

        self.width = width
        self.mobile_width = mobile_width
        self.lock_canvas = lock_canvas
        self.theme = theme
        self.navigation_menu = navigation_menu
        self.navigation_menu_position = navigation_menu_position
        self.blocks: Dict[str, Sivo] = {}
        self.html_blocks: Dict[str, str] = {}
        self.details_panels: Dict[str, Dict] = {}
        self.metrics_panels: Dict[str, Dict] = {}
        self.layout_order: List[Dict[str, str]] = []

    def add_sivo_block(self, block_id: str, sivo_app: Sivo, col_span: int = 1, slot: str = "main", grid_area: Optional[str] = None, overflow_visible: bool = False, min_height: Optional[str] = None):
        """Adds a Sivo instance to a specific block/slot in the dashboard layout."""
        self.blocks[block_id] = sivo_app
        self.layout_order.append({"type": "sivo", "id": block_id, "col_span": col_span, "slot": slot, "grid_area": grid_area, "overflow_visible": overflow_visible, "min_height": min_height})

    def add_html_block(self, block_id: str, html_content: str, col_span: int = 1, slot: str = "main", grid_area: Optional[str] = None, overflow_visible: bool = False, min_height: Optional[str] = None):
        """Adds raw HTML content to a specific block/slot in the dashboard layout."""
        self.html_blocks[block_id] = html_content
        self.layout_order.append({"type": "html", "id": block_id, "col_span": col_span, "slot": slot, "grid_area": grid_area, "overflow_visible": overflow_visible, "min_height": min_height})

    def add_image_block(self, block_id: str, image_url: str, object_fit: str = "cover", border_radius: str = "0.75rem", col_span: int = 1, slot: str = "main", grid_area: Optional[str] = None, url: Optional[str] = None, url_transition: Optional[str] = None, fade_in: bool = False, fade_start_time_ms: int = 0, fade_duration_ms: int = 500, overflow_visible: bool = False, min_height: Optional[str] = None):
        """
        Adds an image block to the dashboard layout.

        Args:
            block_id: Unique identifier for the block.
            image_url: URL or path to the image.
            object_fit: CSS object-fit property (e.g., 'cover', 'contain', 'fill'). Default is 'cover'.
            border_radius: CSS border-radius property. Default is '0.75rem'.
            col_span: Number of columns the block should span.
            slot: The layout slot.
            grid_area: The CSS grid-area string.
            url: A URL to link the image to.
            url_transition: A CSS class name to apply to the body before navigating to the URL.
            fade_in: Whether to animate a fade-in on load.
            fade_start_time_ms: Delay in ms before starting the fade-in animation.
            fade_duration_ms: Duration in ms of the fade-in animation.
        """
        img_tag = f'<img src="{image_url}" style="width: 100%; height: 100%; object-fit: {object_fit}; border-radius: {border_radius};" />'
        if url:
            if url_transition:
                html_content = f'<a href="{url}" onclick="event.preventDefault(); document.body.classList.add(\'{url_transition}\'); setTimeout(() => window.location.href = \'{url}\', 600);" style="display: block; width: 100%; height: 100%; cursor: pointer;">{img_tag}</a>'
            else:
                html_content = f'<a href="{url}" style="display: block; width: 100%; height: 100%;">{img_tag}</a>'
        else:
            html_content = img_tag

        if fade_in:
            fade_style = f"opacity: 0; animation: sivo-fade-in-card {fade_duration_ms/1000.0}s ease-in-out forwards; animation-delay: {fade_start_time_ms/1000.0}s;"
            # We wrap the content in a div to cleanly apply the fade without breaking a-tags or img-tags styling
            html_content = f'<div style="width: 100%; height: 100%; {fade_style}">{html_content}</div>'

        self.add_html_block(block_id, html_content, col_span=col_span, slot=slot, grid_area=grid_area, overflow_visible=overflow_visible, min_height=min_height)

    def add_text_block(self, block_id: str, text: str, font_family: str = "Arial, sans-serif", font_size: str = "36px", font_weight: str = "bold", text_color: str = "#333", background_color: str = "#f0f8ff", border: str = "2px solid #87cefa", border_radius: str = "15px", col_span: int = 1, slot: str = "main", grid_area: Optional[str] = None, url: Optional[str] = None, url_transition: Optional[str] = None, fade_in: bool = False, fade_start_time_ms: int = 0, fade_duration_ms: int = 500, overflow_visible: bool = False, min_height: Optional[str] = None):
        """
        Adds a pre-styled text block to the dashboard layout.

        Args:
            block_id: Unique identifier for the block.
            text: The text to display.
            font_family: CSS font-family string.
            font_size: CSS font-size string.
            font_weight: CSS font-weight string.
            text_color: CSS color for the text.
            background_color: CSS background color for the block.
            border: CSS border property.
            border_radius: CSS border-radius property.
            col_span: Number of columns the block should span.
            slot: The layout slot.
            grid_area: The CSS grid-area string.
            url: Optional URL to link to.
            url_transition: A CSS class name to apply to the body before navigating.
            fade_in: Whether to animate a fade-in on load.
            fade_start_time_ms: Delay in ms before starting the fade-in animation.
            fade_duration_ms: Duration in ms of the fade-in animation.
        """
        style = f"display: flex; align-items: center; justify-content: center; width: 100%; height: 100%; font-family: {font_family}; font-size: {font_size}; font-weight: {font_weight}; color: {text_color}; background-color: {background_color}; border: {border}; border-radius: {border_radius}; text-align: center; box-sizing: border-box;"

        inner_content = f'<div style="{style}">{text}</div>'

        if url:
            if url_transition:
                html_content = f'<a href="{url}" onclick="event.preventDefault(); document.body.classList.add(\'{url_transition}\'); setTimeout(() => window.location.href = \'{url}\', 600);" style="display: block; width: 100%; height: 100%; text-decoration: none; cursor: pointer;">{inner_content}</a>'
            else:
                html_content = f'<a href="{url}" style="display: block; width: 100%; height: 100%; text-decoration: none;">{inner_content}</a>'
        else:
            html_content = inner_content

        if fade_in:
            fade_style = f"opacity: 0; animation: sivo-fade-in-card {fade_duration_ms/1000.0}s ease-in-out forwards; animation-delay: {fade_start_time_ms/1000.0}s;"
            html_content = f'<div style="width: 100%; height: 100%; {fade_style}">{html_content}</div>'

        self.add_html_block(block_id, html_content, col_span=col_span, slot=slot, grid_area=grid_area, overflow_visible=overflow_visible, min_height=min_height)

    def add_details_panel(self, block_id: str, title: str = "Details", placeholder: str = "Select an item to view details.", col_span: int = 1, slot: str = "main", grid_area: Optional[str] = None, overflow_visible: bool = False, min_height: Optional[str] = None, background_color: Optional[str] = None, border_radius: Optional[str] = None, padding: Optional[str] = None):
        """
        Adds a pre-built panel that automatically listens to SIVO canvas clicks and renders
        the clicked element's `html` (tooltip content) mapping.
        """
        self.details_panels[block_id] = {
            "title": title,
            "placeholder": placeholder,
            "background_color": background_color,
            "border_radius": border_radius,
            "padding": padding
        }
        self.layout_order.append({"type": "details", "id": block_id, "col_span": col_span, "slot": slot, "grid_area": grid_area, "overflow_visible": overflow_visible, "min_height": min_height})

    def add_metrics_panel(self, block_id: str, title: str = "Metrics", metrics: List[str] = None, col_span: int = 1, slot: str = "main", grid_area: Optional[str] = None, overflow_visible: bool = False, min_height: Optional[str] = None):
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
        self.layout_order.append({"type": "metrics", "id": block_id, "col_span": col_span, "slot": slot, "grid_area": grid_area, "overflow_visible": overflow_visible, "min_height": min_height})


    def set_grid_layout(self, desktop: str, mobile: Optional[str] = None):
        """
        Defines the responsive CSS Grid layout using grid-template-areas.
        :param desktop: The CSS grid-template-areas string for desktop views.
        :param mobile: The CSS grid-template-areas string for mobile views.
        """
        self.desktop_grid = desktop
        self.mobile_grid = mobile

    def to_html(self, output_path: Optional[str] = None, custom_css: Optional[str] = None, custom_js: Optional[str] = None) -> str:
        """
        Generates a responsive HTML dashboard containing the assigned blocks.
        Optionally saves to a file.
        """
        if not self.blocks and not self.html_blocks:
            raise ValueError("No blocks added to the dashboard.")

        views_data = {}
        # We process each block as a "view" using the standard Sivo data extractor
        for block_id, app in self.blocks.items():
            view_data = app._get_view_data()
            if self.lock_canvas:
                view_data["lock_canvas"] = True
            views_data[block_id] = view_data

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
            background_image_opacity=self.background_image_opacity,
            background_image_size=self.background_image_size,
            gap=self.gap,
            mobile_gap=self.mobile_gap,
            width=self.width,
            mobile_width=self.mobile_width,
            theme=self.theme,
            navigation_menu=self.navigation_menu,
            navigation_menu_position=self.navigation_menu_position,
            output_path=output_path,
            custom_css=custom_css,
            custom_js=custom_js
        )
