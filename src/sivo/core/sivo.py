# Copyright (c) 2024 SIVO. All rights reserved.
# Licensed under the MIT License. See LICENSE file in the project root for full license information.

import logging
from typing import Dict, Optional, Union, List, Any

logger = logging.getLogger(__name__)

from .config import ProjectConfig
from .infographic import Infographic
from .a11y_audit import audit_tap_target, audit_contrast

class Sivo:
    """
    SIVO (SVG Interactive Vector Objects) Orchestrator.
    This class serves as the primary declarative Python API for the framework,
    hiding JavaScript complexity and managing the Infographic lifecycle.
    """


    @staticmethod
    def get_theme_css(theme_name: str) -> str:
        """
        Reads a custom theme CSS file from src/sivo/themes based on the theme name.
        Prevents path traversal attacks.
        Returns empty string if theme doesn't exist or on error.
        """
        import os

        if not theme_name or theme_name in ['light', 'dark']:
            return ""

        try:
            # Prevent path traversal
            safe_theme_name = os.path.basename(theme_name)
            if not safe_theme_name.endswith('.css'):
                safe_theme_name += '.css'

            current_dir = os.path.dirname(os.path.abspath(__file__))
            themes_dir = os.path.abspath(os.path.join(current_dir, '..', 'themes'))

            target_path = os.path.abspath(os.path.join(themes_dir, safe_theme_name))

            # Additional safety check
            if os.path.commonpath([themes_dir, target_path]) != themes_dir:
                logger.warning(f"Path traversal attempt detected for theme: {theme_name}")
                return ""

            if os.path.exists(target_path):
                with open(target_path, 'r', encoding='utf-8') as f:
                    return f.read()
            return ""
        except Exception as e:
            logger.error(f"Error loading custom theme CSS '{theme_name}': {e}")
            return ""

    @staticmethod
    def fetch_image_base64(url: str) -> str:
        """
        Fetches an image from a URL and returns it as a base64 data URI.
        Useful for ensuring ECharts renders images immediately without async loading issues.
        """
        import base64
        import mimetypes
        import sys
        import urllib.request
        from urllib.parse import urlparse

        # SSRF Protection: Block known internal/local IP spaces and localhost
        parsed_url = urlparse(url)
        if parsed_url.scheme not in ['http', 'https']:
            raise ValueError(f"SSRF Protection: Invalid URL scheme '{parsed_url.scheme}'. Only http and https are allowed.")

        hostname = parsed_url.hostname
        if hostname:
            hostname = hostname.lower()
            # Blocklist for common SSRF targets
            if hostname in ['localhost', '127.0.0.1', '0.0.0.0'] or hostname.startswith('10.') or hostname.startswith('192.168.'):
                raise ValueError(f"SSRF Protection: Fetching images from local/internal network ({hostname}) is forbidden.")

            # More careful check for 172.16.x.x - 172.31.x.x
            if hostname.startswith('172.'):
                parts = hostname.split('.')
                if len(parts) >= 2 and parts[1].isdigit():
                    octet = int(parts[1])
                    if 16 <= octet <= 31:
                        raise ValueError(f"SSRF Protection: Fetching images from local/internal network ({hostname}) is forbidden.")

        # Try to guess mime type from URL, default to jpeg
        mime_type, _ = mimetypes.guess_type(url)
        if not mime_type:
            mime_type = "image/jpeg"

        if "pyodide" in sys.modules:
            # In Pyodide, use synchronous XMLHttpRequest or js fetch if available.
            # However, pyodide.http.open_url returns a StringIO. For binary data, we use pyodide.http.pyfetch synchronously using async/await if possible,
            # but since this is a synchronous method, pyodide.http.open_url is our best fallback if we want to avoid asyncio.
            try:
                # pyodide.http.open_url doesn't support binary easily before 0.21, but in modern pyodide we can just use urllib as it's patched.
                # However, it will fail if CORS is missing.
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
                with urllib.request.urlopen(req, timeout=10) as response:
                    img_data = response.read()
            except Exception as e:
                import logging
                logging.getLogger(__name__).warning(f"Failed to fetch image synchronously in Pyodide/WASM. CORS or network issues may block this. Error: {e}")
                return ""
        else:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
            with urllib.request.urlopen(req, timeout=10) as response:
                img_data = response.read()

        b64_str = base64.b64encode(img_data).decode('utf-8')

        return f"data:{mime_type};base64,{b64_str}"
    def __init__(self, infographic: Infographic, default_panel_position: str = "none", disable_panel: bool = False, panel_width: Optional[str] = "90%", panel_height: Optional[str] = "90%", panel_css: Optional[str] = None, disable_resizer: bool = False, disable_tooltips: bool = False, disable_zoom_controls: bool = False, lock_scroll_bounds: bool = True, lock_zoom_out: bool = True, layout_size: Optional[str] = "95%", mobile_layout_size: Optional[str] = None, starting_zoom: float = 1.0, lock_canvas: bool = False, enable_a11y: bool = True, render_mode: str = "canvas", enable_minimap: bool = False, enable_export: bool = False, fade_unselected: bool = False, theme: str = "light", enable_search: bool = False, enable_geocoder: bool = False, geocode_provider: str = "nominatim", geocode_api_key: Optional[str] = None, geocode_country_codes: Optional[Union[str, List[str]]] = None, geocoder_position: str = "top-center", watermark: Optional[str] = None, enable_brush_selection: bool = False, title: Optional[str] = None, subtitle: Optional[str] = None, attribution: Optional[str] = None, enable_fullscreen: bool = False, enable_share: bool = False, enable_data_download: bool = False, enable_drawing_tools: bool = False, ambient_effect: Optional[str] = None, ambient_speed: float = 1.0, bounding_coords: Optional[list[list[float]]] = None, graphic: Optional[list[dict]] = None, background_image_url: Optional[str] = None, border_image_url: Optional[str] = None, border_image_position: str = 'all', border_image_width: str = '10%', border_image_opacity: float = 1.0, border_image_grayscale: bool = False, background_image_opacity: float = 1.0, background_image_grayscale: bool = False, svg_background_image_url: Optional[str] = None, svg_background_image_opacity: float = 1.0, svg_background_image_grayscale: bool = False, svg_background_image_insert_after: Optional[str] = None, transparent_template_lines: bool = False, presentation_order: Optional[list[str]] = None, navigation_menu: Optional[list[dict]] = None, navigation_menu_position: str = 'top-right'):
        self.infographic = infographic
        self.infographic.presentation_order = presentation_order
        if navigation_menu is not None:
            self.infographic.navigation_menu = navigation_menu
        self.infographic.navigation_menu_position = navigation_menu_position
        self.infographic.transparent_template_lines = transparent_template_lines
        self.infographic.default_panel_position = default_panel_position
        self.infographic.disable_panel = disable_panel
        self.infographic.panel_width = panel_width
        self.infographic.panel_height = panel_height
        self.infographic.panel_css = panel_css
        self.infographic.disable_resizer = disable_resizer
        self.infographic.disable_tooltips = disable_tooltips
        self.infographic.disable_zoom_controls = disable_zoom_controls
        self.infographic.lock_scroll_bounds = lock_scroll_bounds
        self.infographic.lock_zoom_out = lock_zoom_out
        self.infographic.layout_size = layout_size
        self.infographic.mobile_layout_size = mobile_layout_size
        self.infographic.starting_zoom = starting_zoom
        self.infographic.enable_a11y = enable_a11y
        self.infographic.render_mode = render_mode
        self.infographic.enable_minimap = enable_minimap
        self.infographic.enable_export = enable_export
        self.infographic.lock_canvas = lock_canvas
        self.infographic.fade_unselected = fade_unselected
        self.infographic.theme = theme
        self.infographic.enable_search = enable_search
        self.infographic.enable_geocoder = enable_geocoder
        self.infographic.geocode_provider = geocode_provider
        self.infographic.geocode_api_key = geocode_api_key
        self.infographic.geocode_country_codes = geocode_country_codes
        self.infographic.watermark = watermark
        self.infographic.enable_brush_selection = enable_brush_selection
        self.infographic.title = title
        self.infographic.subtitle = subtitle
        self.infographic.attribution = attribution
        self.infographic.enable_fullscreen = enable_fullscreen
        self.infographic.enable_share = enable_share
        self.infographic.enable_data_download = enable_data_download
        self.infographic.enable_drawing_tools = enable_drawing_tools
        self.infographic.ambient_effect = ambient_effect
        self.infographic.ambient_speed = ambient_speed
        self.infographic.bounding_coords = bounding_coords
        self.infographic.graphic = graphic
        if background_image_url is not None:
            self.infographic.background_image_url = background_image_url
            self.infographic.background_image_opacity = background_image_opacity
            self.infographic.background_image_grayscale = background_image_grayscale
        if svg_background_image_url is not None:
            self.infographic.svg_background_image_url = svg_background_image_url
            self.infographic.svg_background_image_opacity = svg_background_image_opacity
            self.infographic.svg_background_image_grayscale = svg_background_image_grayscale
            self.infographic.svg_background_image_insert_after = svg_background_image_insert_after

    @classmethod
    def from_svg(cls, filepath: str, default_panel_position: str = "none", disable_panel: bool = False, panel_width: Optional[str] = "90%", panel_height: Optional[str] = "90%", panel_css: Optional[str] = None, disable_resizer: bool = False, disable_tooltips: bool = False, disable_zoom_controls: bool = False, lock_scroll_bounds: bool = True, lock_zoom_out: bool = True, layout_size: Optional[str] = "95%", mobile_layout_size: Optional[str] = None, starting_zoom: float = 1.0, lock_canvas: bool = False, enable_a11y: bool = True, render_mode: str = "canvas", enable_minimap: bool = False, enable_export: bool = False, fade_unselected: bool = False, theme: str = "light", enable_search: bool = False, enable_geocoder: bool = False, geocode_provider: str = "nominatim", geocode_api_key: Optional[str] = None, geocode_country_codes: Optional[Union[str, List[str]]] = None, geocoder_position: str = "top-center", watermark: Optional[str] = None, enable_brush_selection: bool = False, title: Optional[str] = None, subtitle: Optional[str] = None, attribution: Optional[str] = None, enable_fullscreen: bool = False, enable_share: bool = False, enable_data_download: bool = False, enable_drawing_tools: bool = False, ambient_effect: Optional[str] = None, ambient_speed: float = 1.0, bounding_coords: Optional[list[list[float]]] = None, graphic: Optional[list[dict]] = None, background_image_url: Optional[str] = None, border_image_url: Optional[str] = None, border_image_position: str = 'all', border_image_width: str = '10%', border_image_opacity: float = 1.0, border_image_grayscale: bool = False, background_image_opacity: float = 1.0, background_image_grayscale: bool = False, svg_background_image_url: Optional[str] = None, svg_background_image_opacity: float = 1.0, svg_background_image_grayscale: bool = False, svg_background_image_insert_after: Optional[str] = None, transparent_template_lines: bool = False, presentation_order: Optional[list[str]] = None, navigation_menu: Optional[list[dict]] = None, navigation_menu_position: str = 'top-right', simplify_tolerance: Optional[float] = None) -> "Sivo":
        """
        Initializes a Sivo instance from an SVG file path.
        default_panel_position can be 'right', 'left', 'top', 'bottom', or 'overlay'.
        """
        # Path validation is explicitly handled in Infographic.from_svg
        info = Infographic.from_svg(filepath, simplify_tolerance=simplify_tolerance)

        if bounding_coords is None:
            viewbox = info.parser.get_viewbox()
            if viewbox:
                parts = viewbox.split()
                if len(parts) >= 4:
                    try:
                        x = float(parts[0])
                        y = float(parts[1])
                        w = float(parts[2])
                        h = float(parts[3])
                        bounding_coords = [[x, y], [x + w, y + h]]
                    except:
                        pass
        return cls(info, default_panel_position=default_panel_position, disable_panel=disable_panel, panel_width=panel_width, panel_height=panel_height, panel_css=panel_css, disable_resizer=disable_resizer, disable_tooltips=disable_tooltips, disable_zoom_controls=disable_zoom_controls, lock_scroll_bounds=lock_scroll_bounds, lock_zoom_out=lock_zoom_out, layout_size=layout_size, mobile_layout_size=mobile_layout_size, starting_zoom=starting_zoom, lock_canvas=lock_canvas, enable_a11y=enable_a11y, render_mode=render_mode, enable_minimap=enable_minimap, enable_export=enable_export, fade_unselected=fade_unselected, theme=theme, enable_search=enable_search, enable_geocoder=enable_geocoder, geocode_provider=geocode_provider, geocode_api_key=geocode_api_key, geocode_country_codes=geocode_country_codes, geocoder_position=geocoder_position, watermark=watermark, enable_brush_selection=enable_brush_selection, title=title, subtitle=subtitle, attribution=attribution, enable_fullscreen=enable_fullscreen, enable_share=enable_share, enable_data_download=enable_data_download, enable_drawing_tools=enable_drawing_tools, ambient_effect=ambient_effect, ambient_speed=ambient_speed, bounding_coords=bounding_coords, graphic=graphic, background_image_url=background_image_url, border_image_url=border_image_url, border_image_position=border_image_position, border_image_width=border_image_width, border_image_opacity=border_image_opacity, border_image_grayscale=border_image_grayscale, background_image_opacity=background_image_opacity, background_image_grayscale=background_image_grayscale, svg_background_image_url=svg_background_image_url, svg_background_image_opacity=svg_background_image_opacity, svg_background_image_grayscale=svg_background_image_grayscale, svg_background_image_insert_after=svg_background_image_insert_after, transparent_template_lines=transparent_template_lines, presentation_order=presentation_order, navigation_menu=navigation_menu, navigation_menu_position=navigation_menu_position)

    @classmethod
    def from_template(cls, template_name: str, default_panel_position: str = "none", disable_panel: bool = False, panel_width: Optional[str] = "90%", panel_height: Optional[str] = "90%", panel_css: Optional[str] = None, disable_resizer: bool = False, disable_tooltips: bool = False, disable_zoom_controls: bool = False, lock_scroll_bounds: bool = True, lock_zoom_out: bool = True, layout_size: Optional[str] = "95%", mobile_layout_size: Optional[str] = None, starting_zoom: float = 1.0, lock_canvas: bool = False, enable_a11y: bool = True, render_mode: str = "canvas", enable_minimap: bool = False, enable_export: bool = False, fade_unselected: bool = False, theme: str = "light", enable_search: bool = False, enable_geocoder: bool = False, geocode_provider: str = "nominatim", geocode_api_key: Optional[str] = None, geocode_country_codes: Optional[Union[str, List[str]]] = None, geocoder_position: str = "top-center", watermark: Optional[str] = None, enable_brush_selection: bool = False, title: Optional[str] = None, subtitle: Optional[str] = None, attribution: Optional[str] = None, enable_fullscreen: bool = False, enable_share: bool = False, enable_data_download: bool = False, enable_drawing_tools: bool = False, ambient_effect: Optional[str] = None, ambient_speed: float = 1.0, bounding_coords: Optional[list[list[float]]] = None, graphic: Optional[list[dict]] = None, background_image_url: Optional[str] = None, border_image_url: Optional[str] = None, border_image_position: str = 'all', border_image_width: str = '10%', border_image_opacity: float = 1.0, border_image_grayscale: bool = False, background_image_opacity: float = 1.0, background_image_grayscale: bool = False, svg_background_image_url: Optional[str] = None, svg_background_image_opacity: float = 1.0, svg_background_image_grayscale: bool = False, svg_background_image_insert_after: Optional[str] = None, transparent_template_lines: bool = False, presentation_order: Optional[list[str]] = None, navigation_menu: Optional[list[dict]] = None, navigation_menu_position: str = 'top-right', simplify_tolerance: Optional[float] = None) -> "Sivo":
        """
        Initializes a Sivo instance from a bundled built-in template SVG.
        Available templates: 'dashboard', 'timeline'
        """
        import os
        template_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "templates")

        # Determine the subdirectory if template_name contains it
        if "/" in template_name:
            # Try plain .svg first, then fallback to _template.svg
            filepath = os.path.join(template_dir, f"{template_name}.svg")
            if not os.path.exists(filepath):
                filepath = os.path.join(template_dir, f"{template_name}_template.svg")
        else:
            # Fallback for old template names without subdirectory
            filepath = None
            for root, dirs, files in os.walk(template_dir):
                if f"{template_name}.svg" in files:
                    filepath = os.path.join(root, f"{template_name}.svg")
                    break
                elif f"{template_name}_template.svg" in files:
                    filepath = os.path.join(root, f"{template_name}_template.svg")
                    break
            if not filepath:
                filepath = os.path.join(template_dir, f"{template_name}.svg") # trigger FileNotFoundError

        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Template '{template_name}' not found. Looked in {template_dir}")
        return cls.from_svg(filepath, default_panel_position=default_panel_position, disable_panel=disable_panel, panel_width=panel_width, panel_height=panel_height, panel_css=panel_css, disable_resizer=disable_resizer, disable_tooltips=disable_tooltips, disable_zoom_controls=disable_zoom_controls, lock_scroll_bounds=lock_scroll_bounds, lock_zoom_out=lock_zoom_out, layout_size=layout_size, mobile_layout_size=mobile_layout_size, starting_zoom=starting_zoom, lock_canvas=lock_canvas, enable_a11y=enable_a11y, render_mode=render_mode, enable_minimap=enable_minimap, enable_export=enable_export, fade_unselected=fade_unselected, theme=theme, enable_search=enable_search, enable_geocoder=enable_geocoder, geocode_provider=geocode_provider, geocode_api_key=geocode_api_key, geocode_country_codes=geocode_country_codes, geocoder_position=geocoder_position, watermark=watermark, enable_brush_selection=enable_brush_selection, title=title, subtitle=subtitle, attribution=attribution, enable_fullscreen=enable_fullscreen, enable_share=enable_share, enable_data_download=enable_data_download, enable_drawing_tools=enable_drawing_tools, ambient_effect=ambient_effect, ambient_speed=ambient_speed, bounding_coords=bounding_coords, graphic=graphic, background_image_url=background_image_url, border_image_url=border_image_url, border_image_position=border_image_position, border_image_width=border_image_width, border_image_opacity=border_image_opacity, border_image_grayscale=border_image_grayscale, background_image_opacity=background_image_opacity, background_image_grayscale=background_image_grayscale, svg_background_image_url=svg_background_image_url, svg_background_image_opacity=svg_background_image_opacity, svg_background_image_grayscale=svg_background_image_grayscale, svg_background_image_insert_after=svg_background_image_insert_after, transparent_template_lines=transparent_template_lines, presentation_order=presentation_order, navigation_menu=navigation_menu, navigation_menu_position=navigation_menu_position)

    @classmethod
    def from_string(cls, svg_string: str, default_panel_position: str = "none", disable_panel: bool = False, panel_width: Optional[str] = "90%", panel_height: Optional[str] = "90%", panel_css: Optional[str] = None, disable_resizer: bool = False, disable_tooltips: bool = False, disable_zoom_controls: bool = False, lock_scroll_bounds: bool = True, lock_zoom_out: bool = True, layout_size: Optional[str] = "95%", mobile_layout_size: Optional[str] = None, starting_zoom: float = 1.0, lock_canvas: bool = False, enable_a11y: bool = True, render_mode: str = "canvas", enable_minimap: bool = False, enable_export: bool = False, fade_unselected: bool = False, theme: str = "light", enable_search: bool = False, enable_geocoder: bool = False, geocode_provider: str = "nominatim", geocode_api_key: Optional[str] = None, geocode_country_codes: Optional[Union[str, List[str]]] = None, geocoder_position: str = "top-center", watermark: Optional[str] = None, enable_brush_selection: bool = False, title: Optional[str] = None, subtitle: Optional[str] = None, attribution: Optional[str] = None, enable_fullscreen: bool = False, enable_share: bool = False, enable_data_download: bool = False, enable_drawing_tools: bool = False, ambient_effect: Optional[str] = None, ambient_speed: float = 1.0, bounding_coords: Optional[list[list[float]]] = None, graphic: Optional[list[dict]] = None, background_image_url: Optional[str] = None, border_image_url: Optional[str] = None, border_image_position: str = 'all', border_image_width: str = '10%', border_image_opacity: float = 1.0, border_image_grayscale: bool = False, background_image_opacity: float = 1.0, background_image_grayscale: bool = False, svg_background_image_url: Optional[str] = None, svg_background_image_opacity: float = 1.0, svg_background_image_grayscale: bool = False, svg_background_image_insert_after: Optional[str] = None, transparent_template_lines: bool = False, presentation_order: Optional[list[str]] = None, navigation_menu: Optional[list[dict]] = None, navigation_menu_position: str = 'top-right', simplify_tolerance: Optional[float] = None) -> "Sivo":
        """Initializes a Sivo instance directly from an SVG string."""
        if not svg_string or not isinstance(svg_string, str) or '<svg' not in svg_string.lower():
            raise ValueError("Invalid SVG string provided.")
        info = Infographic.from_string(svg_string, simplify_tolerance=simplify_tolerance)

        if bounding_coords is None:
            viewbox = info.parser.get_viewbox()
            if viewbox:
                parts = viewbox.split()
                if len(parts) >= 4:
                    try:
                        x = float(parts[0])
                        y = float(parts[1])
                        w = float(parts[2])
                        h = float(parts[3])
                        bounding_coords = [[x, y], [x + w, y + h]]
                    except:
                        pass
        return cls(info, default_panel_position=default_panel_position, disable_panel=disable_panel, panel_width=panel_width, panel_height=panel_height, panel_css=panel_css, disable_resizer=disable_resizer, disable_tooltips=disable_tooltips, disable_zoom_controls=disable_zoom_controls, lock_scroll_bounds=lock_scroll_bounds, lock_zoom_out=lock_zoom_out, layout_size=layout_size, mobile_layout_size=mobile_layout_size, starting_zoom=starting_zoom, lock_canvas=lock_canvas, enable_a11y=enable_a11y, render_mode=render_mode, enable_minimap=enable_minimap, enable_export=enable_export, fade_unselected=fade_unselected, theme=theme, enable_search=enable_search, enable_geocoder=enable_geocoder, geocode_provider=geocode_provider, geocode_api_key=geocode_api_key, geocode_country_codes=geocode_country_codes, geocoder_position=geocoder_position, watermark=watermark, enable_brush_selection=enable_brush_selection, title=title, subtitle=subtitle, attribution=attribution, enable_fullscreen=enable_fullscreen, enable_share=enable_share, enable_data_download=enable_data_download, enable_drawing_tools=enable_drawing_tools, ambient_effect=ambient_effect, ambient_speed=ambient_speed, bounding_coords=bounding_coords, graphic=graphic, background_image_url=background_image_url, border_image_url=border_image_url, border_image_position=border_image_position, border_image_width=border_image_width, border_image_opacity=border_image_opacity, border_image_grayscale=border_image_grayscale, background_image_opacity=background_image_opacity, background_image_grayscale=background_image_grayscale, svg_background_image_url=svg_background_image_url, svg_background_image_opacity=svg_background_image_opacity, svg_background_image_grayscale=svg_background_image_grayscale, svg_background_image_insert_after=svg_background_image_insert_after, transparent_template_lines=transparent_template_lines, presentation_order=presentation_order, navigation_menu=navigation_menu, navigation_menu_position=navigation_menu_position)

    @classmethod
    def from_geodataframe(cls, gdf: Any, id_col: str, name_col: Optional[str] = None, simplify_tolerance: Optional[float] = None, default_panel_position: str = "none", disable_panel: bool = False, panel_width: Optional[str] = "90%", panel_height: Optional[str] = "90%", panel_css: Optional[str] = None, disable_resizer: bool = False, disable_tooltips: bool = False, disable_zoom_controls: bool = False, lock_scroll_bounds: bool = True, lock_zoom_out: bool = True, layout_size: Optional[str] = "95%", mobile_layout_size: Optional[str] = None, starting_zoom: float = 1.0, lock_canvas: bool = False, enable_a11y: bool = True, render_mode: str = "canvas", enable_minimap: bool = False, enable_export: bool = False, fade_unselected: bool = False, theme: str = "light", enable_search: bool = False, enable_geocoder: bool = False, geocode_provider: str = "nominatim", geocode_api_key: Optional[str] = None, geocode_country_codes: Optional[Union[str, List[str]]] = None, geocoder_position: str = "top-center", watermark: Optional[str] = None, enable_brush_selection: bool = False, title: Optional[str] = None, subtitle: Optional[str] = None, attribution: Optional[str] = None, enable_fullscreen: bool = False, enable_share: bool = False, enable_data_download: bool = False, enable_drawing_tools: bool = False, ambient_effect: Optional[str] = None, ambient_speed: float = 1.0, bounding_coords: Optional[list[list[float]]] = None, background_image_url: Optional[str] = None, border_image_url: Optional[str] = None, border_image_position: str = 'all', border_image_width: str = '10%', border_image_opacity: float = 1.0, border_image_grayscale: bool = False, background_image_opacity: float = 1.0, background_image_grayscale: bool = False, svg_background_image_url: Optional[str] = None, svg_background_image_opacity: float = 1.0, svg_background_image_grayscale: bool = False, svg_background_image_insert_after: Optional[str] = None, transparent_template_lines: bool = False, presentation_order: Optional[list[str]] = None, navigation_menu: Optional[list[dict]] = None, navigation_menu_position: str = 'top-right') -> "Sivo":
        """
        Initializes a Sivo instance directly from a geopandas GeoDataFrame.
        Automatically converts geometries to SVG paths, assigns IDs and Names,
        and sets bounding coordinates for native geographical projection mapping.
        If `simplify_tolerance` is provided, it simplifies the geometries.
        """
        if name_col is None:
            name_col = id_col

        if simplify_tolerance is not None:
            gdf = gdf.copy()
            gdf.geometry = gdf.geometry.simplify(simplify_tolerance)

        svg_parts = []
        minx, miny, maxx, maxy = gdf.total_bounds
        width = maxx - minx
        height = maxy - miny

        import xml.etree.ElementTree as ET
        import re

        for idx, row in gdf.iterrows():
            geom_svg = row.geometry.svg()
            elem_id = str(row[id_col])
            elem_name = str(row[name_col])

            # ECharts requires the `name` attribute directly on the shape tag (<path>, <polygon>, etc.)
            # in order to apply dynamic visualMap/timeline colors. A wrapper <g> is insufficient because
            # ECharts SVG renderer does not cascade fill colors to child paths.
            # We parse the geometry SVG, strip Shapely's hardcoded inline styles, and inject the Name directly into the shapes,
            # then wrap the whole thing in a <g id="..."> so SIVO's Python mapping lookup can still find the root ID.
            try:
                root = ET.fromstring(f"<root>{geom_svg}</root>")

                path_idx = 0
                for elem in root.iter():
                    # ET parses namespaces if present, though shapely usually outputs raw tags.
                    tag = elem.tag.split('}')[-1] if '}' in elem.tag else elem.tag
                    if tag in ['path', 'polygon', 'rect', 'circle', 'polyline']:
                        # Inject SIVO attributes directly onto the path
                        # Multiple paths can share the same name, ECharts will group them into one region
                        elem.set('id', f"{elem_id}_{path_idx}")
                        elem.set('name', elem_name)
                        path_idx += 1

                        # Strip inline styles so ECharts can inject dynamic styles
                        for attr in ['fill', 'stroke', 'stroke-width', 'opacity']:
                            if attr in elem.attrib:
                                del elem.attrib[attr]

                # Re-serialize the children
                cleaned_svg = ''.join([ET.tostring(child, encoding='unicode') for child in root])

                safe_id = elem_id.replace('"', '&quot;')
                safe_name = elem_name.replace('"', '&quot;')
                g_tag = f'<g id="{safe_id}" name="{safe_name}">{cleaned_svg}</g>'
                svg_parts.append(g_tag)

            except Exception:
                # Fallback if parsing fails, though ET should handle shapely output perfectly
                safe_id = elem_id.replace('"', '&quot;')
                safe_name = elem_name.replace('"', '&quot;')
                clean = re.sub(r'\s*(fill|stroke|stroke-width|opacity)="[^"]*"', '', geom_svg)
                svg_parts.append(f'<g id="{safe_id}" name="{safe_name}">{clean}</g>')

        # Invert the Y-axis using an SVG transform since geographic coordinates (Y points North)
        # are inverted relative to standard screen coordinates (Y points South).
        newline = '\n'
        svg_str = f'''<?xml version="1.0" encoding="utf-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="{minx} {miny} {width} {height}">
  <g transform="matrix(1, 0, 0, -1, 0, {maxy + miny})">
    {newline.join(svg_parts)}
  </g>
</svg>'''

        if bounding_coords is None:
            bounding_coords = [[minx, miny], [maxx, maxy]]

        return cls.from_string(svg_str, default_panel_position=default_panel_position, disable_panel=disable_panel, panel_width=panel_width, panel_height=panel_height, panel_css=panel_css, disable_resizer=disable_resizer, disable_tooltips=disable_tooltips, disable_zoom_controls=disable_zoom_controls, lock_scroll_bounds=lock_scroll_bounds, lock_zoom_out=lock_zoom_out, layout_size=layout_size, mobile_layout_size=mobile_layout_size, starting_zoom=starting_zoom, lock_canvas=lock_canvas, enable_a11y=enable_a11y, render_mode=render_mode, enable_minimap=enable_minimap, enable_export=enable_export, fade_unselected=fade_unselected, theme=theme, enable_search=enable_search, enable_geocoder=enable_geocoder, geocode_provider=geocode_provider, geocode_api_key=geocode_api_key, geocode_country_codes=geocode_country_codes, geocoder_position=geocoder_position, watermark=watermark, enable_brush_selection=enable_brush_selection, title=title, subtitle=subtitle, attribution=attribution, enable_fullscreen=enable_fullscreen, enable_share=enable_share, enable_data_download=enable_data_download, enable_drawing_tools=enable_drawing_tools, ambient_effect=ambient_effect, ambient_speed=ambient_speed, bounding_coords=bounding_coords, background_image_url=background_image_url, border_image_url=border_image_url, border_image_position=border_image_position, border_image_width=border_image_width, border_image_opacity=border_image_opacity, border_image_grayscale=border_image_grayscale, background_image_opacity=background_image_opacity, background_image_grayscale=background_image_grayscale, svg_background_image_url=svg_background_image_url, svg_background_image_opacity=svg_background_image_opacity, svg_background_image_grayscale=svg_background_image_grayscale, svg_background_image_insert_after=svg_background_image_insert_after, transparent_template_lines=transparent_template_lines, presentation_order=presentation_order, navigation_menu=navigation_menu, navigation_menu_position=navigation_menu_position)

    @classmethod
    def from_config(cls, config: Union[str, dict, ProjectConfig], base_dir: str = ".") -> "Sivo":
        """
        Creates a Sivo instance from a configuration file, dictionary, or ProjectConfig object.
        """
        info = Infographic.from_config(config, base_dir=base_dir)
        return cls(
            info,
            default_panel_position=info.default_panel_position,
            disable_panel=getattr(info, "disable_panel", False),
            panel_width=getattr(info, "panel_width", None),
            panel_height=getattr(info, "panel_height", None),
            panel_css=getattr(info, "panel_css", None),
            disable_resizer=getattr(info, "disable_resizer", False),
            disable_tooltips=getattr(info, "disable_tooltips", False),
            disable_zoom_controls=getattr(info, "disable_zoom_controls", False),
            lock_scroll_bounds=getattr(info, "lock_scroll_bounds", True),
            lock_zoom_out=info.lock_zoom_out,
            starting_zoom=getattr(info, "starting_zoom", 1.0),
            enable_a11y=info.enable_a11y,
            render_mode=info.render_mode,
            enable_minimap=info.enable_minimap,
            enable_export=info.enable_export,
            lock_canvas=getattr(info, "lock_canvas", False),
            fade_unselected=info.fade_unselected,
            theme=info.theme,
            enable_search=info.enable_search,
            enable_geocoder=getattr(info, "enable_geocoder", False),
            geocode_provider=getattr(info, "geocode_provider", "nominatim"),
            geocode_api_key=getattr(info, "geocode_api_key", None),
            geocode_country_codes=getattr(info, "geocode_country_codes", None),
            watermark=info.watermark,
            enable_brush_selection=info.enable_brush_selection,
            title=getattr(info, "title", None),
            subtitle=getattr(info, "subtitle", None),
            attribution=getattr(info, "attribution", None),
            enable_fullscreen=getattr(info, "enable_fullscreen", False),
            navigation_menu=getattr(info, "navigation_menu", None),
            navigation_menu_position=getattr(info, "navigation_menu_position", "top-right"),
            enable_share=getattr(info, "enable_share", False),
            enable_data_download=getattr(info, "enable_data_download", False),
            enable_drawing_tools=getattr(info, "enable_drawing_tools", False),
            ambient_effect=getattr(info, "ambient_effect", None),
            bounding_coords=getattr(info, "bounding_coords", None),
            graphic=getattr(info, "graphic", None),
            background_image_url=getattr(info, "background_image_url", None),
            border_image_url=getattr(info, "border_image_url", None),
            border_image_position=getattr(info, "border_image_position", "all"),
            border_image_width=getattr(info, "border_image_width", "10%"),
            border_image_opacity=getattr(info, "border_image_opacity", 1.0),
            border_image_grayscale=getattr(info, "border_image_grayscale", False),
            background_image_opacity=getattr(info, "background_image_opacity", 1.0),
            background_image_grayscale=getattr(info, "background_image_grayscale", False),
            svg_background_image_url=getattr(info, "svg_background_image_url", None),
            svg_background_image_opacity=getattr(info, "svg_background_image_opacity", 1.0),
            svg_background_image_grayscale=getattr(info, "svg_background_image_grayscale", False),
            svg_background_image_insert_after=getattr(info, "svg_background_image_insert_after", None),
            transparent_template_lines=getattr(info, "transparent_template_lines", False)
        )


    def add_border_image(self, url: str, position: str = 'all', width: str = '10%', opacity: float = 1.0, grayscale: bool = False):
        """
        Adds an image overlay to the UI along a specific border.

        Args:
            url (str): The URL or relative path to the image.
            position (str): 'left', 'right', 'top', 'bottom', or 'all'.
            width (str): The width or thickness of the border (e.g. '10%').
            opacity (float): 0.0 to 1.0
            grayscale (bool): If True, makes the image black and white.
        """
        self.infographic.border_image_url = url
        self.infographic.border_image_position = position
        self.infographic.border_image_width = width
        self.infographic.border_image_opacity = opacity
        self.infographic.border_image_grayscale = grayscale

    def add_background_image(self, url: str, opacity: float = 1.0, grayscale: bool = False, fade_in: bool = False, fade_pulse: bool = False, fade_start_time_ms: int = 0, fade_duration_ms: int = 5000):
        """
        Adds a background image to the SVG canvas.
        The image will be rendered beneath all SVG elements.
        """
        self.infographic.background_image_url = url
        self.infographic.background_image_opacity = opacity
        self.infographic.background_image_grayscale = grayscale
        self.infographic.background_image_fade_in = fade_in
        self.infographic.background_image_fade_pulse = fade_pulse
        self.infographic.background_image_fade_start_time_ms = fade_start_time_ms
        self.infographic.background_image_fade_duration_ms = fade_duration_ms

    def add_svg_background_image(self, url: str, opacity: float = 1.0, grayscale: bool = False, insert_after: Optional[str] = None, encode_base64: bool = False, fade_in: bool = False, fade_pulse: bool = False, fade_start_time_ms: int = 0, fade_duration_ms: int = 5000):
        """
        Adds a background image specifically to the SVG, which pans and zooms with the SVG elements.
        The image is injected into the SVG at the lowest z-index level, or directly after the node with ID `insert_after`.
        """
        if encode_base64 and url.startswith('http'):
            url = self.fetch_image_base64(url)
        self.infographic.svg_background_image_url = url
        self.infographic.svg_background_image_opacity = opacity
        self.infographic.svg_background_image_grayscale = grayscale
        self.infographic.svg_background_image_insert_after = insert_after
        self.infographic._inject_svg_background_image()

        if fade_in or fade_pulse:
            self.map("sivo-svg-bg-image", fade_in=fade_in, fade_pulse=fade_pulse, fade_start_time_ms=fade_start_time_ms, fade_duration_ms=fade_duration_ms)

    def map(
        self,
        element_id: str,
        aria_label: Optional[str] = None,
        role: Optional[str] = None,
        tabindex: Optional[str] = None,
        tooltip: Optional[str] = None,
        html: Optional[str] = None,
        url: Optional[str] = None,
        url_target: str = "_blank",
        url_transition: Optional[str] = None,
        drill_to: Optional[str] = None,
        drill_through: Optional[str] = None,
        drill_transition: Optional[str] = None,
        explode_to: Optional[str] = None,
        explode_duration_ms: int = 1000,
        footnote: Optional[str] = None,
        footnote_title: Optional[str] = None,
        callback_event: Optional[str] = None,
        callback_payload: Optional[dict] = None,
        hover_callback_event: Optional[str] = None,
        hover_callback_payload: Optional[dict] = None,
        video: Optional[str] = None,
        gallery: Optional[list[str]] = None,
        audio: Optional[str] = None,
        markdown: Optional[str] = None,
        fetch_url: Optional[str] = None,
        fetch_data_path: Optional[str] = None,
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
        lottie: Optional[dict] = None,
        compare: Optional[dict] = None,
        progress_bar: Optional[dict] = None,
        confetti: Optional[dict] = None,
        loading: Optional[dict] = None,
        replit: Optional[str] = None,
        echarts_option: Optional[dict] = None,
        toggle_image: Optional[dict] = None,
        map_name: Optional[str] = None,
        map_data: Optional[Union[str, dict]] = None,
        context_menu: Optional[list[dict]] = None,
        panel_position: Optional[str] = None,
        panel_css: Optional[str] = None,
        open_by_default: bool = False,
        zoom_on_click: bool = False,
        zoom_level: float = 2.0,
        zoom_duration_ms: int = 500,
        zoom_to: Optional[str] = None,
        zoom_to_size: str = "90%",
        draggable: bool = False,
        color: Optional[str] = "transparent",
        hover_color: Optional[str] = None,
        hover_image: Optional[str] = None,
        fill_gradient: Optional[dict] = None,
        fill_pattern: Optional[dict] = None,
        border_width: Optional[float] = None,
        border_color: Optional[str] = "transparent",
        transparent_lines: Optional[bool] = None,
        glow: Optional[bool] = None,
        animation: Optional[str] = None,
        animation_duration_ms: Optional[int] = 1000,
        fade_in: bool = False,
        fade_pulse: bool = False,
        fade_start_time_ms: int = 0,
        fade_duration_ms: int = 5000,
        morph_to_path: Optional[str] = None,
        morph_duration_ms: Optional[int] = 1000,
        morph_delay_ms: Optional[int] = 0,
        morph_easing: Optional[str] = "ease-in-out",
        morph_iterations: Optional[float] = 1.0,
        filter: Optional[str] = None,
        clip_path: Optional[str] = None,
        mask: Optional[str] = None,
        transform: Optional[str] = None,
        odometer_value: Optional[float] = None,
        odometer_duration_ms: Optional[int] = 2000,
        odometer_format: Optional[str] = None
    ):
        """
        Maps an SVG element id (or name) to actions or visual themes.
        This provides a seamless, declarative API.
        """
        self.infographic.map(
            element_id=element_id,
            aria_label=aria_label,
            role=role,
            tabindex=tabindex,
            tooltip=tooltip,
            html=html,
            url=url,
            url_target=url_target,
            url_transition=url_transition,
            drill_to=drill_to,
            drill_through=drill_through,
            drill_transition=drill_transition,
            explode_to=explode_to,
            explode_duration_ms=explode_duration_ms,
            footnote=footnote,
            footnote_title=footnote_title,
            callback_event=callback_event,
            callback_payload=callback_payload,
            hover_callback_event=hover_callback_event,
            hover_callback_payload=hover_callback_payload,
            video=video,
            gallery=gallery,
            audio=audio,
            markdown=markdown,
            fetch_url=fetch_url,
            fetch_data_path=fetch_data_path,
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
            lottie=lottie,
            compare=compare,
            progress_bar=progress_bar,
            confetti=confetti,
            loading=loading,
            replit=replit,
            echarts_option=echarts_option,
            toggle_image=toggle_image,
            map_name=map_name,
            map_data=map_data,
            context_menu=context_menu,
            panel_position=panel_position,
            panel_css=panel_css,
            open_by_default=open_by_default,
            zoom_on_click=zoom_on_click,
            zoom_level=zoom_level,
            zoom_duration_ms=zoom_duration_ms,
            zoom_to=zoom_to,
            zoom_to_size=zoom_to_size,
            draggable=draggable,
            color=color,
            hover_color=hover_color,
            hover_image=hover_image,
            fill_gradient=fill_gradient,
            fill_pattern=fill_pattern,
            border_width=border_width,
            border_color=border_color,
            transparent_lines=transparent_lines,
            glow=glow,
            animation=animation,
            animation_duration_ms=animation_duration_ms,
            fade_in=fade_in,
            fade_pulse=fade_pulse,
            fade_start_time_ms=fade_start_time_ms,
            fade_duration_ms=fade_duration_ms,
            morph_to_path=morph_to_path,
            morph_duration_ms=morph_duration_ms,
            morph_delay_ms=morph_delay_ms,
            morph_easing=morph_easing,
            morph_iterations=morph_iterations,
            filter=filter,
            clip_path=clip_path,
            mask=mask,
            transform=transform,
            odometer_value=odometer_value,
            odometer_duration_ms=odometer_duration_ms,
            odometer_format=odometer_format
        )

    def apply_template_style(self, style_name: str):
        """
        Applies a pre-defined set of global styles and themes to the infographic.
        Available styles: 'dark_mode', 'minimalist', 'cyberpunk', 'glassmorphism', 'neon', 'monochrome', 'ocean', 'forest', 'sunset', 'pastel'.
        This method will iterate through the SVG DOM and inject inline styles directly onto
        the nodes based on their class names, ensuring 100% compatibility with ECharts ZRender.
        """
        style_name = style_name.lower()

        # Define style mappings for various classes based on the selected theme
        style_map = {}

        if style_name == "dark_mode":
            self.infographic.theme = "dark"
            style_map = {
                "bg": {"fill": "#0f172a"},
                "bento-card": {"fill": "#1e293b", "stroke": "#334155"},
                "soft-card": {"fill": "#1e293b", "stroke": "#334155"},
                "glass-panel": {"fill": "rgba(30, 41, 59, 0.7)", "stroke": "rgba(148, 163, 184, 0.2)"},
                "card-header-line": {"stroke": "#334155"},
                "connecting-line": {"stroke": "#334155"},
                "placeholder-title": {"fill": "#f8fafc"},
                "placeholder-text-title": {"fill": "#f8fafc"},
                "placeholder-text": {"fill": "#94a3b8"},
                "placeholder-text-subtitle": {"fill": "#94a3b8"},
                "placeholder-text-large": {"fill": "#cbd5e1"},
                "placeholder-text-card-title": {"fill": "#cbd5e1"},
                "placeholder-text-card-value": {"fill": "#94a3b8"},
                "node-circle": {"fill": "#1e293b", "stroke": "#3b82f6"}
            }

        elif style_name == "minimalist":
            self.infographic.theme = "light"
            style_map = {
                "bg": {"fill": "#ffffff"},
                "bento-card": {"fill": "#ffffff", "stroke": "#e2e8f0", "stroke-width": "1px", "filter": "none"},
                "soft-card": {"fill": "#ffffff", "stroke": "#e2e8f0", "stroke-width": "1px", "filter": "none"},
                "glass-panel": {"fill": "#ffffff", "stroke": "#e2e8f0", "filter": "none"},
                "card-header-line": {"stroke": "#e2e8f0"},
                "connecting-line": {"stroke": "#e2e8f0"},
                "placeholder-title": {"fill": "#0f172a", "font-weight": "500"},
                "placeholder-text-title": {"fill": "#0f172a", "font-weight": "500"},
                "placeholder-text": {"fill": "#64748b"},
                "placeholder-text-subtitle": {"fill": "#64748b"},
                "placeholder-text-large": {"fill": "#cbd5e1"},
                "placeholder-text-card-title": {"fill": "#cbd5e1"},
                "placeholder-text-card-value": {"fill": "#94a3b8"},
                "node-circle": {"fill": "#ffffff", "stroke": "#0f172a"},
                "node-circle-active": {"fill": "#0f172a", "stroke": "#ffffff"}
            }

        elif style_name == "cyberpunk":
            self.infographic.theme = "dark"
            style_map = {
                "bg": {"fill": "#0a0a0c"},
                "bento-card": {"fill": "#111116", "stroke": "#00ffcc", "stroke-width": "1.5px", "rx": "0", "ry": "0"},
                "soft-card": {"fill": "#111116", "stroke": "#00ffcc", "stroke-width": "1.5px", "rx": "0", "ry": "0"},
                "glass-panel": {"fill": "rgba(10,10,12,0.8)", "stroke": "#ff00ff", "rx": "0", "ry": "0"},
                "card-header-line": {"stroke": "#00ffcc"},
                "connecting-line": {"stroke": "#00ffcc"},
                "placeholder-title": {"fill": "#ffffff"},
                "placeholder-text-title": {"fill": "#ffffff"},
                "placeholder-text": {"fill": "#ff00ff"},
                "placeholder-text-subtitle": {"fill": "#ff00ff"},
                "placeholder-text-large": {"fill": "#00ffcc"},
                "placeholder-text-card-title": {"fill": "#00ffcc"},
                "placeholder-text-card-value": {"fill": "#ff00ff"},
                "node-circle": {"fill": "#111116", "stroke": "#00ffcc", "rx": "0", "ry": "0"},
                "node-circle-active": {"fill": "#ff00ff", "stroke": "#111116", "rx": "0", "ry": "0"}
            }

        elif style_name == "glassmorphism":
            self.infographic.theme = "light"
            style_map = {
                "bg": {"fill": "#f8fafc"},
                "bento-card": {"fill": "rgba(255, 255, 255, 0.4)", "stroke": "rgba(255, 255, 255, 0.8)"},
                "soft-card": {"fill": "rgba(255, 255, 255, 0.4)", "stroke": "rgba(255, 255, 255, 0.8)"},
                "glass-panel": {"fill": "rgba(255, 255, 255, 0.4)", "stroke": "rgba(255, 255, 255, 0.8)"},
                "card-header-line": {"stroke": "rgba(148, 163, 184, 0.5)"},
                "connecting-line": {"stroke": "rgba(148, 163, 184, 0.5)"},
                "placeholder-title": {"fill": "rgba(30,41,59,0.5)"},
                "placeholder-text-title": {"fill": "rgba(30,41,59,0.5)"},
                "placeholder-text": {"fill": "rgba(100,116,139,0.3)"},
                "placeholder-text-subtitle": {"fill": "rgba(100,116,139,0.3)"},
                "placeholder-text-large": {"fill": "rgba(203, 213, 225, 0.5)"},
                "placeholder-text-card-title": {"fill": "rgba(203, 213, 225, 0.5)"},
                "placeholder-text-card-value": {"fill": "rgba(148, 163, 184, 0.3)"},
                "node-circle": {"fill": "rgba(255,255,255,0.5)", "stroke": "#3b82f6"}
            }

        elif style_name == "neon":
            self.infographic.theme = "dark"
            style_map = {
                "bg": {"fill": "#050505"},
                "bento-card": {"fill": "#0a0a0a", "stroke": "#ff00ff", "stroke-width": "2px"},
                "soft-card": {"fill": "#0a0a0a", "stroke": "#ff00ff", "stroke-width": "2px"},
                "glass-panel": {"fill": "rgba(5,5,5,0.8)", "stroke": "#00ffff"},
                "card-header-line": {"stroke": "#00ffff", "stroke-width": "3px"},
                "connecting-line": {"stroke": "#00ffff", "stroke-width": "3px"},
                "placeholder-title": {"fill": "#ffffff", "font-weight": "900"},
                "placeholder-text-title": {"fill": "#ffffff", "font-weight": "900"},
                "placeholder-text": {"fill": "#ff00ff"},
                "placeholder-text-subtitle": {"fill": "#ff00ff"},
                "placeholder-text-large": {"fill": "rgba(255,0,255,0.3)", "stroke": "#ff00ff", "stroke-width": "1px"},
                "placeholder-text-card-title": {"fill": "rgba(255,0,255,0.3)", "stroke": "#ff00ff", "stroke-width": "1px"},
                "placeholder-text-card-value": {"fill": "rgba(0,255,255,0.3)", "stroke": "#00ffff", "stroke-width": "1px"},
                "node-circle": {"fill": "#0a0a0a", "stroke": "#00ffff"},
                "node-circle-active": {"fill": "#ff00ff", "stroke": "#ffffff"}
            }

        elif style_name == "monochrome":
            self.infographic.theme = "light"
            style_map = {
                "bg": {"fill": "#ffffff"},
                "bento-card": {"fill": "#ffffff", "stroke": "#000000", "stroke-width": "2px", "filter": "none", "rx": "0", "ry": "0"},
                "soft-card": {"fill": "#ffffff", "stroke": "#000000", "stroke-width": "2px", "filter": "none", "rx": "0", "ry": "0"},
                "glass-panel": {"fill": "#f8f8f8", "stroke": "#000000", "stroke-width": "1px", "rx": "0", "ry": "0"},
                "card-header-line": {"stroke": "#000000"},
                "connecting-line": {"stroke": "#000000"},
                "placeholder-title": {"fill": "#000000", "font-weight": "bold"},
                "placeholder-text-title": {"fill": "#000000", "font-weight": "bold"},
                "placeholder-text": {"fill": "#333333"},
                "placeholder-text-subtitle": {"fill": "#333333"},
                "placeholder-text-large": {"fill": "#666666"},
                "placeholder-text-card-title": {"fill": "#000000"},
                "placeholder-text-card-value": {"fill": "#000000"},
                "node-circle": {"fill": "#ffffff", "stroke": "#000000", "stroke-width": "2px"},
                "node-circle-active": {"fill": "#000000", "stroke": "#ffffff", "stroke-width": "2px"}
            }

        elif style_name == "ocean":
            self.infographic.theme = "light"
            style_map = {
                "bg": {"fill": "#e0f2fe"},
                "bento-card": {"fill": "#ffffff", "stroke": "#0284c7"},
                "soft-card": {"fill": "#ffffff", "stroke": "#0284c7"},
                "glass-panel": {"fill": "rgba(255, 255, 255, 0.7)", "stroke": "#38bdf8"},
                "card-header-line": {"stroke": "#7dd3fc"},
                "connecting-line": {"stroke": "#7dd3fc"},
                "placeholder-title": {"fill": "#0c4a6e"},
                "placeholder-text-title": {"fill": "#0c4a6e"},
                "placeholder-text": {"fill": "#0284c7"},
                "placeholder-text-subtitle": {"fill": "#0284c7"},
                "placeholder-text-large": {"fill": "#7dd3fc"},
                "placeholder-text-card-title": {"fill": "#0ea5e9"},
                "placeholder-text-card-value": {"fill": "#0369a1"},
                "node-circle": {"fill": "#ffffff", "stroke": "#0284c7"},
                "node-circle-active": {"fill": "#0284c7", "stroke": "#ffffff"}
            }

        elif style_name == "forest":
            self.infographic.theme = "light"
            style_map = {
                "bg": {"fill": "#f0fdf4"},
                "bento-card": {"fill": "#ffffff", "stroke": "#16a34a"},
                "soft-card": {"fill": "#ffffff", "stroke": "#16a34a"},
                "glass-panel": {"fill": "rgba(255, 255, 255, 0.7)", "stroke": "#4ade80"},
                "card-header-line": {"stroke": "#86efac"},
                "connecting-line": {"stroke": "#86efac"},
                "placeholder-title": {"fill": "#14532d"},
                "placeholder-text-title": {"fill": "#14532d"},
                "placeholder-text": {"fill": "#16a34a"},
                "placeholder-text-subtitle": {"fill": "#16a34a"},
                "placeholder-text-large": {"fill": "#86efac"},
                "placeholder-text-card-title": {"fill": "#22c55e"},
                "placeholder-text-card-value": {"fill": "#15803d"},
                "node-circle": {"fill": "#ffffff", "stroke": "#16a34a"},
                "node-circle-active": {"fill": "#16a34a", "stroke": "#ffffff"}
            }

        elif style_name == "sunset":
            self.infographic.theme = "light"
            style_map = {
                "bg": {"fill": "#fff7ed"},
                "bento-card": {"fill": "#ffffff", "stroke": "#ea580c"},
                "soft-card": {"fill": "#ffffff", "stroke": "#ea580c"},
                "glass-panel": {"fill": "rgba(255, 255, 255, 0.7)", "stroke": "#fb923c"},
                "card-header-line": {"stroke": "#fdba74"},
                "connecting-line": {"stroke": "#fdba74"},
                "placeholder-title": {"fill": "#7c2d12"},
                "placeholder-text-title": {"fill": "#7c2d12"},
                "placeholder-text": {"fill": "#ea580c"},
                "placeholder-text-subtitle": {"fill": "#ea580c"},
                "placeholder-text-large": {"fill": "#fdba74"},
                "placeholder-text-card-title": {"fill": "#f97316"},
                "placeholder-text-card-value": {"fill": "#c2410c"},
                "node-circle": {"fill": "#ffffff", "stroke": "#ea580c"},
                "node-circle-active": {"fill": "#ea580c", "stroke": "#ffffff"}
            }

        elif style_name == "pastel":
            self.infographic.theme = "light"
            style_map = {
                "bg": {"fill": "#faf5ff"},
                "bento-card": {"fill": "#ffffff", "stroke": "#d8b4fe"},
                "soft-card": {"fill": "#ffffff", "stroke": "#d8b4fe"},
                "glass-panel": {"fill": "rgba(255, 255, 255, 0.7)", "stroke": "#e9d5ff"},
                "card-header-line": {"stroke": "#f3e8ff"},
                "connecting-line": {"stroke": "#f3e8ff"},
                "placeholder-title": {"fill": "#4c1d95"},
                "placeholder-text-title": {"fill": "#4c1d95"},
                "placeholder-text": {"fill": "#9333ea"},
                "placeholder-text-subtitle": {"fill": "#9333ea"},
                "placeholder-text-large": {"fill": "#d8b4fe"},
                "placeholder-text-card-title": {"fill": "#a855f7"},
                "placeholder-text-card-value": {"fill": "#7e22ce"},
                "node-circle": {"fill": "#ffffff", "stroke": "#9333ea"},
                "node-circle-active": {"fill": "#9333ea", "stroke": "#ffffff"}
            }

        else:
            raise ValueError(f"Unknown template style: '{style_name}'. Supported styles: dark_mode, minimalist, cyberpunk, glassmorphism, neon, monochrome, ocean, forest, sunset, pastel.")

        # Directly mutate the SVG DOM to ensure ECharts parses these properties flawlessly natively
        for elem in self.infographic.parser.root.iter():
            cls_attr = elem.get("class")
            if cls_attr:
                classes = cls_attr.split()
                for c in classes:
                    if c in style_map:
                        # Apply new styles directly to inline attributes
                        for k, v in style_map[c].items():
                            # Note: ECharts strongly prefers native attributes over inline style="fill:..."
                            if k == "style":
                                elem.set("style", v)
                            else:
                                elem.set(k, v)

    def add_graphic(self, graphic_element: dict):
        """
        Adds an ECharts graphic element (image, text, shape) directly to the map overlay.
        """
        if not hasattr(self.infographic, "graphic") or self.infographic.graphic is None:
            self.infographic.graphic = []
        self.infographic.graphic.append(graphic_element)


    def embed_svg(self, element_id: str, filepath_or_string: str, is_file: bool = False, preserve_aspect_ratio: bool = True, keep_target: bool = False, scale_multiplier: float = 1.0):
        """
        Embeds an external SVG graphic directly into the bounding box of a specific element in the main SVG canvas.
        The embedded SVG's paths and shapes will be injected into the main SVG structure and become fully interactive natively.

        Args:
            element_id: The ID or name of the target shape to embed the SVG into.
            filepath_or_string: The file path to the SVG or the raw SVG string content.
            is_file: Whether filepath_or_string is a file path (True) or raw string (False).
            preserve_aspect_ratio: Whether to uniformly scale the embedded SVG to fit within the target bounding box (True), or stretch it to fill the exact dimensions (False).
            keep_target: Whether to keep the target bounding box element visible in the background (True) or remove it (False).
        """
        self.infographic.embed_svg(element_id, filepath_or_string, is_file, preserve_aspect_ratio, keep_target, scale_multiplier)

    def add_shape(self, tag: str, attributes: Dict[str, str]):
        """
        Programmatically adds a simple vector shape to the SVG directly from Python.

        Args:
            tag (str): The SVG tag name (e.g., "rect", "circle", "path").
            attributes (Dict[str, str]): Dictionary of SVG attributes (e.g., {'id': 'myRect', 'x': '10', 'y': '10', 'width': '50', 'height': '50', 'fill': 'red'}).
        """
        self.infographic.add_shape(tag, attributes)

    def bind_data(self, data: Dict[str, Dict[str, float]], key: str, colors: list, min_val: float, max_val: float):
        """
        Binds quantitative data to SVG IDs dynamically and applies a color scale.
        """
        self.infographic.bind_data(data, key, colors, min_val, max_val)

    def bind_timeline(self, data: Dict[str, Dict[str, Dict[str, float]]], key: str, colors: list, min_val: float, max_val: float, auto_play: bool = True, play_interval: int = 1000, show_play_btn: bool = True, loop: bool = True, control_position: str = "left", symbol: str = "emptyCircle", symbol_size: Union[int, List[int]] = 10, bottom: Union[int, str] = 20):
        """
        Binds quantitative time-series data to SVG IDs dynamically and animates a color scale over time.
        """
        self.infographic.bind_timeline(data, key, colors, min_val, max_val, auto_play, play_interval, show_play_btn, loop, control_position, symbol, symbol_size, bottom)

    def bind_live(self, url: str, topic: str, auth_token: Optional[str] = None):
        """
        Binds a WebSocket/PubSub connection to dynamically mutate the ECharts canvas based on live
        telemetry data, completely bypassing Streamlit re-renders.
        """
        self.infographic.bind_live(url, topic, auth_token)

    def bind_api(self, url: str, polling_interval_ms: int = 5000, method: str = "GET", headers: Optional[Dict[str, str]] = None, payload: Optional[dict] = None, data_path: Optional[str] = None, max_retries: Optional[int] = None):
        """
        Binds an API endpoint for live UI updates via polling.
        """
        self.infographic.bind_api(url, polling_interval_ms, method, headers, payload, data_path, max_retries)



    def bind_geocoder_intersection(self, geojson_url: str, display_element_id: str, property_name: str, no_result_text: str = "No zone found"):
        """
        Binds the geocoder search result to perform a client-side Point-in-Polygon
        intersection against a remote GeoJSON file, updating an element's text with the result.
        """
        self.infographic.bind_geocoder_intersection(geojson_url, display_element_id, property_name, no_result_text)

    def bind_scrollytelling(self, steps: list[Dict]):
        """
        Binds a scrollytelling configuration. The infographic will stay sticky while scrolling
        through the text content, and trigger zooms or style changes.
        """
        self.infographic.bind_scrollytelling(steps)

    def bind_tour(self, steps: list[Dict]):
        """
        Binds a guided tour configuration. A next/prev UI will walk the user through the steps.
        """
        self.infographic.bind_tour(steps)

    def add_layer_toggle(self, label: str, element_ids: list[str], default_visible: bool = True):
        """
        Adds a layer toggle legend item for the specified element IDs.
        """
        self.infographic.add_layer_toggle(label, element_ids, default_visible)

    def enable_scratchoff(self, color: str = "#cccccc", image_url: Optional[str] = None, brush_size: int = 40):
        """
        Enables a scratch-off reveal layer over the infographic.
        """
        self.infographic.enable_scratchoff(color, image_url, brush_size)

    def apply_hexbin(self, points: List[List[float]], hex_size: float = 15.0, color_palette: list[str] = ["#e0f3f8", "#014636"], min_opacity: float = 0.3, max_opacity: float = 0.9, stroke_color: str = "#ffffff", stroke_width: float = 1.0):
        """
        Creates a hexagonal binning overlay map by aggregating raw coordinates.
        """
        self.infographic.apply_hexbin(points, hex_size, color_palette, min_opacity, max_opacity, stroke_color, stroke_width)

    def apply_dot_density(self, data_map: Dict[str, Union[int, Dict]], dot_size: float = 3.0, dot_color: str = "rgba(255, 0, 0, 0.8)", dots_per_value: float = 1.0):
        """
        Creates a dot density map by specifying the number of dots per region.
        """
        self.infographic.apply_dot_density(data_map, dot_size, dot_color, dots_per_value)

    def apply_proportional_symbols(self, data_map: Dict[str, Union[float, Dict]], min_size: float = 10.0, max_size: float = 50.0, color: str = "rgba(255, 0, 0, 0.6)", is_pulse: bool = False):
        """
        Creates a proportional symbol overlay (scatter/bubble map).
        """
        self.infographic.apply_proportional_symbols(data_map, min_size, max_size, color, is_pulse=is_pulse)

    def apply_spike_map(self, data_map: Dict[str, float], max_height: float = 100.0, base_width: float = 10.0, color: str = "rgba(255, 0, 0, 0.8)"):
        """
        Creates a spike map overlay where the height of a triangular spike from the region's center is proportional to the value.
        """
        self.infographic.apply_spike_map(data_map, max_height, base_width, color)

    def apply_flow_map(self, data_list: list[dict], min_width: float = 1.0, max_width: float = 5.0, color: str = "rgba(255, 51, 51, 0.6)", flow_effect: bool = True, effect_symbol: str = "arrow", effect_size: float = 5.0, animation_speed: float = 3.0):
        """
        Creates a flow map by drawing scaled arrows/lines between origins and destinations.
        data_list format: [{"origin": "id1", "destination": "id2", "value": 100, "source_coord": [x,y], "target_coord": [x,y]}, ...]
        """
        self.infographic.apply_flow_map(data_list, min_width, max_width, color, flow_effect, effect_symbol, effect_size, animation_speed)




    def _apply_chart_styling(self, option: dict, color: str | list[str] = None, title_color: str = None, title_size: int = None, axis_color: str = None, axis_size: int = None, tooltip_bg_color: str = None, grid_margin: list[int] = None, universal_transition: bool = True, datazoom: bool = False, extra_options: dict = None):
        if color:
            if isinstance(color, list):
                option["color"] = color
                if "series" in option and isinstance(option["series"], list):
                    for s in option["series"]:
                        if s.get("type") in ["bar", "scatter"]:
                            s["colorBy"] = "data"
                        elif "itemStyle" in s and "color" in s["itemStyle"]:
                            del s["itemStyle"]["color"]
            else:
                if "series" in option and isinstance(option["series"], list):
                    for s in option["series"]:
                        if "itemStyle" not in s: s["itemStyle"] = {}
                        s["itemStyle"]["color"] = color

        if title_color or title_size:
            if "title" not in option: option["title"] = {}
            if "textStyle" not in option["title"]: option["title"]["textStyle"] = {}
            if title_color: option["title"]["textStyle"]["color"] = title_color
            if title_size: option["title"]["textStyle"]["fontSize"] = title_size

        if axis_color or axis_size:
            for axis_type in ["xAxis", "yAxis"]:
                if axis_type in option and isinstance(option[axis_type], dict):
                    if "axisLabel" not in option[axis_type]: option[axis_type]["axisLabel"] = {}
                    if axis_color: option[axis_type]["axisLabel"]["color"] = axis_color
                    if axis_size: option[axis_type]["axisLabel"]["fontSize"] = axis_size
                    if "nameTextStyle" not in option[axis_type]: option[axis_type]["nameTextStyle"] = {}
                    if axis_color: option[axis_type]["nameTextStyle"]["color"] = axis_color
                    if axis_size: option[axis_type]["nameTextStyle"]["fontSize"] = axis_size

        if tooltip_bg_color:
            if "tooltip" not in option: option["tooltip"] = {}
            option["tooltip"]["backgroundColor"] = tooltip_bg_color

        if grid_margin and len(grid_margin) == 4:
            if "grid" not in option: option["grid"] = {}
            option["grid"]["top"] = grid_margin[0]
            option["grid"]["right"] = grid_margin[1]
            option["grid"]["bottom"] = grid_margin[2]
            option["grid"]["left"] = grid_margin[3]

        if universal_transition:
            if "series" in option and isinstance(option["series"], list):
                for s in option["series"]:
                    s["universalTransition"] = True

        if datazoom:
            option["dataZoom"] = [
                {
                    "type": "slider",
                    "xAxisIndex": 0,
                    "filterMode": "filter"
                },
                {
                    "type": "slider",
                    "yAxisIndex": 0,
                    "filterMode": "filter"
                },
                {
                    "type": "inside",
                    "xAxisIndex": 0,
                    "filterMode": "filter"
                },
                {
                    "type": "inside",
                    "yAxisIndex": 0,
                    "filterMode": "filter"
                }
            ]

        if extra_options:
            def merge_dicts(d1, d2):
                for k, v in d2.items():
                    if isinstance(v, dict) and k in d1 and isinstance(d1[k], dict):
                        merge_dicts(d1[k], v)
                    elif isinstance(v, list) and k in d1 and isinstance(d1[k], list):
                        for i in range(min(len(d1[k]), len(v))):
                            if isinstance(v[i], dict) and isinstance(d1[k][i], dict):
                                merge_dicts(d1[k][i], v[i])
                            else:
                                d1[k][i] = v[i]
                        if len(v) > len(d1[k]):
                            d1[k].extend(v[len(d1[k]):])
                    else:
                        d1[k] = v
            merge_dicts(option, extra_options)

        return option

    def map_bar_chart(self, element_id: str, title: str, data: list, categories: list, color: str | list[str] = "#3b82f6", tooltip: str = None, panel_position: str = None, title_color: str = None, title_size: int = None, axis_color: str = None, axis_size: int = None, tooltip_bg_color: str = None, grid_margin: list[int] = None, universal_transition: bool = True, datazoom: bool = False, extra_options: dict = None):
        """
        Maps a standard Bar Chart to an element.

        Args:
            element_id (str): The SVG element ID to map to.
            title (str): The chart title.
            data (list): A list of data values corresponding to the categories.
            categories (list): A list of category labels for the X-axis.
            color (str | list[str]): A single color string or a list of color strings (palette). Defaults to "#3b82f6".
            tooltip (str, optional): The tooltip text to display on hover. Defaults to None.
            panel_position (str, optional): The position of the panel where the chart will be rendered. Defaults to None.
            title_color (str, optional): The color of the chart title. Defaults to None.
            title_size (int, optional): The font size of the chart title. Defaults to None.
            axis_color (str, optional): The color of the axis lines and labels. Defaults to None.
            axis_size (int, optional): The font size of the axis labels. Defaults to None.
            tooltip_bg_color (str, optional): The background color of the tooltip. Defaults to None.
            grid_margin (list[int], optional): The margins for the chart grid [top, right, bottom, left]. Defaults to None.
            universal_transition (bool, optional): Whether to enable universal transitions. Defaults to True.
            datazoom (bool, optional): Whether to enable data zooming. Defaults to False.
            extra_options (dict, optional): Additional ECharts options to merge. Defaults to None.
        """
        option = {
            "title": {"text": title},
            "tooltip": {},
            "xAxis": {"data": categories},
            "yAxis": {},
            "series": [{
                "name": title,
                "type": "bar",
                "data": data
            }]
        }
        option = self._apply_chart_styling(option, color, title_color, title_size, axis_color, axis_size, tooltip_bg_color, grid_margin, universal_transition, datazoom, extra_options)
        self.map(element_id=element_id, tooltip=tooltip, echarts_option=option, panel_position=panel_position)

    def map_trendline_chart(self, element_id: str, title: str, data: list[list[float]], trendline_type: str = "linear", trendline_color: str = "#ff0000", trendline_width: int = 2, trendline_arrow: bool = False, trendline_arrow_size: int = 10, trendline_label: str = None, color: str | list[str] = None, tooltip: str = None, panel_position: str = None, title_color: str = None, title_size: int = None, axis_color: str = None, axis_size: int = None, tooltip_bg_color: str = None, grid_margin: list[int] = None, universal_transition: bool = True, datazoom: bool = False, extra_options: dict = None):
        """
        Maps a Scatter Chart with an overlaid trendline to an element.

        Args:
            element_id (str): The SVG element ID to map to.
            title (str): The chart title.
            data (list[list[float]]): The scatter plot data, formatted as a list of [x, y] coordinates.
            trendline_type (str): The type of trendline to overlay ('linear', 'exponential', 'logarithmic', 'polynomial'). Defaults to 'linear'.
            color (str | list[str]): A single color string or a list of color strings (palette) for the scatter points. Defaults to "#3b82f6".
            trendline_color (str): The color of the trendline. Defaults to "#ef4444".
            tooltip (str, optional): The tooltip text to display on hover. Defaults to None.
            panel_position (str, optional): The position of the panel where the chart will be rendered. Defaults to None.
            title_color (str, optional): The color of the chart title. Defaults to None.
            title_size (int, optional): The font size of the chart title. Defaults to None.
            axis_color (str, optional): The color of the axis lines and labels. Defaults to None.
            axis_size (int, optional): The font size of the axis labels. Defaults to None.
            tooltip_bg_color (str, optional): The background color of the tooltip. Defaults to None.
            grid_margin (list[int], optional): The margins for the chart grid [top, right, bottom, left]. Defaults to None.
            universal_transition (bool, optional): Whether to enable universal transitions. Defaults to True.
            datazoom (bool, optional): Whether to enable data zooming. Defaults to False.
            extra_options (dict, optional): Additional ECharts options to merge. Defaults to None.
        """

        symbol = "none"

        option = {
            "title": {"text": title},
            "tooltip": {"trigger": "item"},
            "xAxis": {},
            "yAxis": {},
            "dataset": [
                {
                    "source": data
                },
                {
                    "transform": {
                        "type": "ecStat:regression",
                        "config": {"method": trendline_type}
                    }
                }
            ],
            "series": [
                {
                    "name": title,
                    "type": "scatter",
                    "datasetIndex": 0
                },
                {
                    "name": "Trendline",
                    "type": "line",
                    "datasetIndex": 1,
                    "symbol": symbol,
                    "symbolSize": 0,
                    "lineStyle": {
                        "color": trendline_color,
                        "width": trendline_width
                    }
                }
            ]
        }

        # In ECharts, dataset-driven line series cannot dynamically calculate arrow angles via markPoint
        # To make arrows point perfectly along the path of the slope, we overlay a custom series that evaluates
        # the angle between the last two points of the generated dataset on render.
        if trendline_arrow or trendline_label:
            js_str = f"""
                var currPos = api.coord([api.value(0), api.value(1)]);
                var sid = params.seriesIndex;
                if (!window._sivo_prev_pos) window._sivo_prev_pos = {{}};
                if (!window._sivo_start_pos) window._sivo_start_pos = {{}};

                if (params.dataIndex === 0) {{
                    window._sivo_start_pos[sid] = currPos;
                }}

                if (params.dataIndex === params.dataInsideLength - 2) {{
                    window._sivo_prev_pos[sid] = currPos;
                }}

                if (params.dataIndex !== params.dataInsideLength - 1) return;

                var start = window._sivo_start_pos[sid] || currPos;
                var prev = window._sivo_prev_pos[sid] || [currPos[0] - 1, currPos[1]];
                var dx = currPos[0] - prev[0];
                var dy = currPos[1] - prev[1];
                var angle = -Math.atan2(dy, dx);

                var size = {trendline_arrow_size};
                var color = '{trendline_color}';
                var labelText = {f"'{trendline_label}'" if trendline_label else "null"};
                var showArrow = {'true' if trendline_arrow else 'false'};

                var half = size / 2;

                var returnObj = {{
                    type: 'group',
                    children: []
                }};

                if (showArrow) {{
                    returnObj.children.push({{
                        type: 'path',
                        shape: {{
                            // Base is precisely at (0,0) so the line connects to the base and the tip extends to +size
                            pathData: 'M0,' + (-half) + ' L' + size + ',0 L0,' + half + ' Z',
                        }},
                        position: currPos,
                        rotation: angle,
                        origin: [0, 0], // Pivot exactly around the base to maintain correct trajectory angle
                        style: {{ fill: color }},
                        enterFrom: {{ position: start }},
                        transition: 'position'
                    }});
                }}

                if (labelText) {{
                    // Offset text further right to prevent overlapping with the new extended arrow
                    var textOffsetX = showArrow ? size + 10 : 10;
                    returnObj.children.push({{
                        type: 'text',
                        position: [currPos[0] + textOffsetX, currPos[1]],
                        style: {{
                            text: labelText,
                            fill: color,
                            fontSize: 14,
                            fontWeight: 'bold',
                            textVerticalAlign: 'middle'
                        }},
                        enterFrom: {{ position: [start[0] + textOffsetX, start[1]], style: {{ opacity: 0 }} }},
                        transition: ['position', 'style']
                    }});
                }}

                return returnObj;
            """

            option["series"].append({
                "type": "custom",
                "datasetIndex": 1,
                "_sivo_render_item": js_str
            })

        option = self._apply_chart_styling(option, color, title_color, title_size, axis_color, axis_size, tooltip_bg_color, grid_margin, universal_transition, datazoom, extra_options)
        self.map(element_id=element_id, tooltip=tooltip, echarts_option=option, panel_position=panel_position)

    def map_pictorial_bar_chart(self, element_id: str, title: str, data: list, categories: list, symbol: str, symbol_repeat: bool | str = True, symbol_size: list | int | str = ['100%', '100%'], color: str | list[str] = "#3b82f6", tooltip: str = None, panel_position: str = None, title_color: str = None, title_size: int = None, axis_color: str = None, axis_size: int = None, tooltip_bg_color: str = None, grid_margin: list[int] = None, universal_transition: bool = True, datazoom: bool = False, extra_options: dict = None):
        """
        Maps a Pictorial Bar Chart to an element.

        Args:
            element_id (str): The SVG element ID to map to.
            title (str): The chart title.
            data (list): A list of data values corresponding to the categories.
            categories (list): A list of category labels for the X-axis.
            symbol (str): The symbol type to use ('circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow', 'none', 'image://url', 'path://...'). Defaults to 'circle'.
            symbol_repeat (bool | str): Whether to repeat the symbol. Defaults to False.
            symbol_size (list[str | int] | str | int): The size of the symbol. Defaults to ['100%', '100%'].
            color (str | list[str]): A single color string or a list of color strings (palette). Defaults to "#3b82f6".
            tooltip (str, optional): The tooltip text to display on hover. Defaults to None.
            panel_position (str, optional): The position of the panel where the chart will be rendered. Defaults to None.
            title_color (str, optional): The color of the chart title. Defaults to None.
            title_size (int, optional): The font size of the chart title. Defaults to None.
            axis_color (str, optional): The color of the axis lines and labels. Defaults to None.
            axis_size (int, optional): The font size of the axis labels. Defaults to None.
            tooltip_bg_color (str, optional): The background color of the tooltip. Defaults to None.
            grid_margin (list[int], optional): The margins for the chart grid [top, right, bottom, left]. Defaults to None.
            universal_transition (bool, optional): Whether to enable universal transitions. Defaults to True.
            datazoom (bool, optional): Whether to enable data zooming. Defaults to False.
            extra_options (dict, optional): Additional ECharts options to merge. Defaults to None.
        """
        option = {
            "title": {"text": title},
            "tooltip": {},
            "xAxis": {"data": categories},
            "yAxis": {},
            "series": [{
                "name": title,
                "type": "pictorialBar",
                "symbol": symbol,
                "symbolRepeat": symbol_repeat,
                "symbolSize": symbol_size,
                "data": data
            }]
        }
        option = self._apply_chart_styling(option, color, title_color, title_size, axis_color, axis_size, tooltip_bg_color, grid_margin, universal_transition, datazoom, extra_options)
        self.map(element_id=element_id, tooltip=tooltip, echarts_option=option, panel_position=panel_position)

    def map_line_chart(self, element_id: str, title: str, data: list, categories: list, color: str | list[str] = "#ff7f50", smooth: bool = True, tooltip: str = None, panel_position: str = None, title_color: str = None, title_size: int = None, axis_color: str = None, axis_size: int = None, tooltip_bg_color: str = None, grid_margin: list[int] = None, universal_transition: bool = True, uncertainty_lower: list = None, uncertainty_upper: list = None, uncertainty_color: str = 'rgba(204, 204, 204, 0.5)', datazoom: bool = False, extra_options: dict = None):
        """
        Maps a Line Chart to an element.

        Args:
            element_id (str): The SVG element ID to map to.
            title (str): The chart title.
            data (list): A list of data values corresponding to the categories.
            categories (list): A list of category labels for the X-axis.
            color (str | list[str]): A single color string or a list of color strings (palette). Defaults to "#ff7f50".
            smooth (bool): Whether the line should be smoothed. Defaults to True.
            tooltip (str, optional): The tooltip text to display on hover. Defaults to None.
            panel_position (str, optional): The position of the panel where the chart will be rendered. Defaults to None.
            title_color (str, optional): The color of the chart title. Defaults to None.
            title_size (int, optional): The font size of the chart title. Defaults to None.
            axis_color (str, optional): The color of the axis lines and labels. Defaults to None.
            axis_size (int, optional): The font size of the axis labels. Defaults to None.
            tooltip_bg_color (str, optional): The background color of the tooltip. Defaults to None.
            grid_margin (list[int], optional): The margins for the chart grid [top, right, bottom, left]. Defaults to None.
            universal_transition (bool, optional): Whether to enable universal transitions. Defaults to True.
            uncertainty_lower (list, optional): A list of lower bound uncertainty values. Defaults to None.
            uncertainty_upper (list, optional): A list of upper bound uncertainty values. Defaults to None.
            uncertainty_color (str, optional): The color of the uncertainty band. Defaults to 'rgba(204, 204, 204, 0.5)'.
            datazoom (bool, optional): Whether to enable data zooming. Defaults to False.
            extra_options (dict, optional): Additional ECharts options to merge. Defaults to None.
        """

        series_data = []

        if uncertainty_lower and uncertainty_upper:
            # Add the lower invisible boundary
            series_data.append({
                "name": f"{title} (Lower)",
                "type": "line",
                "data": uncertainty_lower,
                "lineStyle": {"opacity": 0},
                "stack": "uncertainty_band",
                "symbol": "none",
                "tooltip": {"show": False}
            })

            # Add the upper colored band (difference between upper and lower)
            diff_data = [u - l for u, l in zip(uncertainty_upper, uncertainty_lower)]
            series_data.append({
                "name": f"{title} (Upper)",
                "type": "line",
                "data": diff_data,
                "lineStyle": {"opacity": 0},
                "areaStyle": {"color": uncertainty_color},
                "stack": "uncertainty_band",
                "symbol": "none",
                "tooltip": {"show": False}
            })

        series_data.append({
            "name": title,
            "data": data,
            "type": "line",
            "smooth": smooth,
            "z": 10
        })

        option = {
            "title": {"text": title},
            "tooltip": {"trigger": "axis"},
            "xAxis": {"type": "category", "data": categories},
            "yAxis": {"type": "value"},
            "series": series_data
        }
        option = self._apply_chart_styling(option, color, title_color, title_size, axis_color, axis_size, tooltip_bg_color, grid_margin, universal_transition, datazoom, extra_options)
        self.map(element_id=element_id, tooltip=tooltip, echarts_option=option, panel_position=panel_position)

    def map_pie_chart(self, element_id: str, title: str, data: list[dict], color: str | list[str] = None, tooltip: str = None, panel_position: str = None, title_color: str = None, title_size: int = None, tooltip_bg_color: str = None, universal_transition: bool = True, datazoom: bool = False, extra_options: dict = None):
        """
        Maps a Pie Chart to an element.

        Args:
            element_id (str): The SVG element ID to map to.
            title (str): The chart title.
            data (list[dict]): A list of data dictionaries formatted as `[{"name": "A", "value": 10}, ...]`.
            color (str | list[str], optional): A single color string or a list of color strings (palette). Defaults to None.
            tooltip (str, optional): The tooltip text to display on hover. Defaults to None.
            panel_position (str, optional): The position of the panel where the chart will be rendered. Defaults to None.
            title_color (str, optional): The color of the chart title. Defaults to None.
            title_size (int, optional): The font size of the chart title. Defaults to None.
            tooltip_bg_color (str, optional): The background color of the tooltip. Defaults to None.
            universal_transition (bool, optional): Whether to enable universal transitions. Defaults to True.
            datazoom (bool, optional): Whether to enable data zooming. Defaults to False.
            extra_options (dict, optional): Additional ECharts options to merge. Defaults to None.
        """
        option = {
            "title": {"text": title, "left": "center"},
            "tooltip": {"trigger": "item"},
            "legend": {"orient": "vertical", "left": "left"},
            "series": [{
                "name": title,
                "type": "pie",
                "radius": "50%",
                "data": data,
                "emphasis": {
                    "itemStyle": {
                        "shadowBlur": 10,
                        "shadowOffsetX": 0,
                        "shadowColor": "rgba(0, 0, 0, 0.5)"
                    }
                }
            }]
        }
        option = self._apply_chart_styling(option, color, title_color, title_size, None, None, tooltip_bg_color, None, universal_transition, datazoom, extra_options)
        self.map(element_id=element_id, tooltip=tooltip, echarts_option=option, panel_position=panel_position)

    def map_gauge_chart(self, element_id: str, title: str, value: float, max_value: float = 100, color: str | list[str] = None, tooltip: str = None, panel_position: str = None, title_color: str = None, title_size: int = None, tooltip_bg_color: str = None, universal_transition: bool = True, datazoom: bool = False, extra_options: dict = None):
        """
        Maps a Gauge Chart to an element.

        Args:
            element_id (str): The SVG element ID to map to.
            title (str): The chart title.
            value (float): The current value to display on the gauge.
            max_value (float, optional): The maximum value of the gauge. Defaults to 100.
            color (str, optional): The color of the gauge progress. Defaults to "#10b981".
            tooltip (str, optional): The tooltip text to display on hover. Defaults to None.
            panel_position (str, optional): The position of the panel where the chart will be rendered. Defaults to None.
            title_color (str, optional): The color of the chart title. Defaults to None.
            title_size (int, optional): The font size of the chart title. Defaults to None.
            tooltip_bg_color (str, optional): The background color of the tooltip. Defaults to None.
            universal_transition (bool, optional): Whether to enable universal transitions. Defaults to True.
            extra_options (dict, optional): Additional ECharts options to merge. Defaults to None.
        """
        option = {
            "title": {"text": title, "left": "center"},
            "tooltip": {"formatter": "{a} <br/>{b} : {c}"},
            "series": [{
                "name": title,
                "type": "gauge",
                "max": max_value,
                "detail": {"formatter": "{value}"},
                "data": [{"value": value, "name": title}]
            }]
        }
        option = self._apply_chart_styling(option, color, title_color, title_size, None, None, tooltip_bg_color, None, universal_transition, datazoom, extra_options)
        self.map(element_id=element_id, tooltip=tooltip, echarts_option=option, panel_position=panel_position)

    def map_radar_chart(self, element_id: str, title: str, indicators: list[dict], data: list[dict], color: str | list[str] = None, tooltip: str = None, panel_position: str = None, title_color: str = None, title_size: int = None, tooltip_bg_color: str = None, universal_transition: bool = True, datazoom: bool = False, extra_options: dict = None):
        """
        Maps a Radar Chart to an element.

        Args:
            element_id (str): The SVG element ID to map to.
            title (str): The chart title.
            indicators (list[dict]): A list of indicator definitions (e.g., `[{'name': 'A', 'max': 100}]`).
            data (list[dict]): A list of data series (e.g., `[{'name': 'Series 1', 'value': [10, 20]}]`).
            color (str | list[str], optional): A single color string or a list of color strings (palette). Defaults to None.
            tooltip (str, optional): The tooltip text to display on hover. Defaults to None.
            panel_position (str, optional): The position of the panel where the chart will be rendered. Defaults to None.
            title_color (str, optional): The color of the chart title. Defaults to None.
            title_size (int, optional): The font size of the chart title. Defaults to None.
            tooltip_bg_color (str, optional): The background color of the tooltip. Defaults to None.
            universal_transition (bool, optional): Whether to enable universal transitions. Defaults to True.
            datazoom (bool, optional): Whether to enable data zooming. Defaults to False.
            extra_options (dict, optional): Additional ECharts options to merge. Defaults to None.
        """
        option = {
            "title": {"text": title},
            "tooltip": {},
            "radar": {
                "indicator": indicators
            },
            "series": [{
                "name": title,
                "type": "radar",
                "data": data
            }]
        }
        option = self._apply_chart_styling(option, color, title_color, title_size, None, None, tooltip_bg_color, None, universal_transition, datazoom, extra_options)
        self.map(element_id=element_id, tooltip=tooltip, echarts_option=option, panel_position=panel_position)

    def map_scatter_chart(self, element_id: str, title: str, data: list[list[float]], color: str | list[str] = None, tooltip: str = None, panel_position: str = None, title_color: str = None, title_size: int = None, axis_color: str = None, axis_size: int = None, tooltip_bg_color: str = None, grid_margin: list[int] = None, universal_transition: bool = True, datazoom: bool = False, extra_options: dict = None):
        """
        Maps a Scatter Chart to an element.

        Args:
            element_id (str): The SVG element ID to map to.
            title (str): The chart title.
            data (list[list[float]]): The scatter plot data, formatted as a list of [x, y] coordinates.
            color (str | list[str], optional): A single color string or a list of color strings (palette). Defaults to "#3b82f6".
            tooltip (str, optional): The tooltip text to display on hover. Defaults to None.
            panel_position (str, optional): The position of the panel where the chart will be rendered. Defaults to None.
            title_color (str, optional): The color of the chart title. Defaults to None.
            title_size (int, optional): The font size of the chart title. Defaults to None.
            axis_color (str, optional): The color of the axis lines and labels. Defaults to None.
            axis_size (int, optional): The font size of the axis labels. Defaults to None.
            tooltip_bg_color (str, optional): The background color of the tooltip. Defaults to None.
            grid_margin (list[int], optional): The margins for the chart grid [top, right, bottom, left]. Defaults to None.
            universal_transition (bool, optional): Whether to enable universal transitions. Defaults to True.
            datazoom (bool, optional): Whether to enable data zooming. Defaults to False.
            extra_options (dict, optional): Additional ECharts options to merge. Defaults to None.
        """
        option = {
            "title": {"text": title},
            "tooltip": {"trigger": "item"},
            "xAxis": {},
            "yAxis": {},
            "series": [{
                "name": title,
                "type": "scatter",
                "data": data
            }]
        }
        option = self._apply_chart_styling(option, color, title_color, title_size, axis_color, axis_size, tooltip_bg_color, grid_margin, universal_transition, datazoom, extra_options)
        self.map(element_id=element_id, tooltip=tooltip, echarts_option=option, panel_position=panel_position)

    def map_nested_map_chart(self, element_id: str, title: str, map_name: str, map_data: Union[str, dict], data: list[dict], color: str | list[str] = None, min_val: float = 0, max_val: float = 100, tooltip: str = None, panel_position: str = None, title_color: str = None, title_size: int = None, tooltip_bg_color: str = None, universal_transition: bool = True, datazoom: bool = False, extra_options: dict = None):
        """
        Maps a nested Map Chart inside the side panel.

        Args:
            element_id (str): The SVG element ID to map to.
            title (str): The chart title.
            map_name (str): The name of the map to register in ECharts.
            map_data (Union[str, dict]): An SVG string or a GeoJSON dictionary.
            data (list[dict]): The data values for the regions on the map, formatted as `[{'name': 'RegionA', 'value': 10}]`.
            color (str | list[str], optional): A single color string or a list of color strings (palette). Defaults to None.
            min_val (float, optional): The minimum value for the visual map scale. Defaults to 0.
            max_val (float, optional): The maximum value for the visual map scale. Defaults to 100.
            tooltip (str, optional): The tooltip text to display on hover. Defaults to None.
            panel_position (str, optional): The position of the panel where the chart will be rendered. Defaults to None.
            title_color (str, optional): The color of the chart title. Defaults to None.
            title_size (int, optional): The font size of the chart title. Defaults to None.
            tooltip_bg_color (str, optional): The background color of the tooltip. Defaults to None.
            universal_transition (bool, optional): Whether to enable universal transitions. Defaults to True.
            datazoom (bool, optional): Whether to enable data zooming. Defaults to False.
            extra_options (dict, optional): Additional ECharts options to merge. Defaults to None.
        """
        option = {
            "title": {"text": title},
            "tooltip": {"trigger": "item"},
            "visualMap": {
                "min": min_val,
                "max": max_val,
                "left": "left",
                "bottom": "bottom",
                "calculable": True,
                "inRange": {
                    "color": color if color else ["#e0f3f8", "#014636"]
                }
            },
            "series": [{
                "name": title,
                "type": "map",
                "map": map_name,
                "roam": True,
                "data": data
            }]
        }
        option = self._apply_chart_styling(option, None, title_color, title_size, None, None, tooltip_bg_color, None, universal_transition, datazoom, extra_options)
        self.map(element_id=element_id, tooltip=tooltip, echarts_option=option, panel_position=panel_position, map_name=map_name, map_data=map_data)

    def map_treemap_chart(self, element_id: str, title: str, data: list[dict], color: str | list[str] = None, tooltip: str = None, panel_position: str = None, title_color: str = None, title_size: int = None, tooltip_bg_color: str = None, universal_transition: bool = True, datazoom: bool = False, extra_options: dict = None):
        """
        Maps a Treemap Chart to an element.

        Args:
            element_id (str): The SVG element ID to map to.
            title (str): The chart title.
            data (list[dict]): A list of hierarchical data node dictionaries formatted as `[{'name': 'node1', 'value': 10, 'children': [...]}]`.
            color (str | list[str], optional): A single color string or a list of color strings (palette). Defaults to None.
            tooltip (str, optional): The tooltip text to display on hover. Defaults to None.
            panel_position (str, optional): The position of the panel where the chart will be rendered. Defaults to None.
            title_color (str, optional): The color of the chart title. Defaults to None.
            title_size (int, optional): The font size of the chart title. Defaults to None.
            tooltip_bg_color (str, optional): The background color of the tooltip. Defaults to None.
            universal_transition (bool, optional): Whether to enable universal transitions. Defaults to True.
            datazoom (bool, optional): Whether to enable data zooming. Defaults to False.
            extra_options (dict, optional): Additional ECharts options to merge. Defaults to None.
        """
        option = {
            "title": {"text": title},
            "tooltip": {"formatter": "{b}: {c}"},
            "series": [{
                "type": "treemap",
                "data": data
            }]
        }
        option = self._apply_chart_styling(option, color, title_color, title_size, None, None, tooltip_bg_color, None, universal_transition, datazoom, extra_options)
        self.map(element_id=element_id, tooltip=tooltip, echarts_option=option, panel_position=panel_position)

    def map_polar_bar_chart(self, element_id: str, title: str, data: list[float], categories: list[str], color: str | list[str] = "#3b82f6", tooltip: str = None, panel_position: str = None, title_color: str = None, title_size: int = None, axis_color: str = None, axis_size: int = None, tooltip_bg_color: str = None, universal_transition: bool = True, datazoom: bool = False, extra_options: dict = None):
        """
        Maps a Polar Bar Chart to an element.

        Args:
            element_id (str): The SVG element ID to map to.
            title (str): The chart title.
            data (list[float]): A list of data values corresponding to the categories.
            categories (list[str]): A list of category labels for the angular axis.
            color (str | list[str], optional): A single color string or a list of color strings (palette). Defaults to "#3b82f6".
            tooltip (str, optional): The tooltip text to display on hover. Defaults to None.
            panel_position (str, optional): The position of the panel where the chart will be rendered. Defaults to None.
            title_color (str, optional): The color of the chart title. Defaults to None.
            title_size (int, optional): The font size of the chart title. Defaults to None.
            axis_color (str, optional): The color of the axis lines and labels. Defaults to None.
            axis_size (int, optional): The font size of the axis labels. Defaults to None.
            tooltip_bg_color (str, optional): The background color of the tooltip. Defaults to None.
            universal_transition (bool, optional): Whether to enable universal transitions. Defaults to True.
            datazoom (bool, optional): Whether to enable data zooming. Defaults to False.
            extra_options (dict, optional): Additional ECharts options to merge. Defaults to None.
        """
        option = {
            "title": {"text": title},
            "tooltip": {},
            "polar": {"radius": ["10%", "80%"]},
            "angleAxis": {"max": max(data) if data else 100, "startAngle": 90},
            "radiusAxis": {"type": "category", "data": categories},
            "series": [{
                "name": title,
                "type": "bar",
                "data": data,
                "coordinateSystem": "polar",
                "label": {"show": True, "position": "middle", "formatter": "{b}: {c}"}
            }]
        }
        option = self._apply_chart_styling(option, color, title_color, title_size, axis_color, axis_size, tooltip_bg_color, None, universal_transition, datazoom, extra_options)
        self.map(element_id=element_id, tooltip=tooltip, echarts_option=option, panel_position=panel_position)

    def map_polar_line_chart(self, element_id: str, title: str, data: list[float], color: str | list[str] = "#ff7f50", tooltip: str = None, panel_position: str = None, title_color: str = None, title_size: int = None, axis_color: str = None, axis_size: int = None, tooltip_bg_color: str = None, universal_transition: bool = True, datazoom: bool = False, extra_options: dict = None):
        """
        Maps a Polar Line Chart to an element (often used for math functions or cyclical data).

        Args:
            element_id (str): The SVG element ID to map to.
            title (str): The chart title.
            data (list[float]): A list of data values.
            color (str | list[str], optional): A single color string or a list of color strings (palette). Defaults to "#ff7f50".
            tooltip (str, optional): The tooltip text to display on hover. Defaults to None.
            panel_position (str, optional): The position of the panel where the chart will be rendered. Defaults to None.
            title_color (str, optional): The color of the chart title. Defaults to None.
            title_size (int, optional): The font size of the chart title. Defaults to None.
            axis_color (str, optional): The color of the axis lines and labels. Defaults to None.
            axis_size (int, optional): The font size of the axis labels. Defaults to None.
            tooltip_bg_color (str, optional): The background color of the tooltip. Defaults to None.
            universal_transition (bool, optional): Whether to enable universal transitions. Defaults to True.
            datazoom (bool, optional): Whether to enable data zooming. Defaults to False.
            extra_options (dict, optional): Additional ECharts options to merge. Defaults to None.
        """
        # Typically, a simple polar line chart maps values to angles.
        # We can map the index to the angle.
        option = {
            "title": {"text": title},
            "tooltip": {"trigger": "axis", "axisPointer": {"type": "cross"}},
            "polar": {},
            "angleAxis": {"type": "value", "startAngle": 0},
            "radiusAxis": {"min": 0},
            "series": [{
                "name": title,
                "type": "line",
                "coordinateSystem": "polar",
                "showSymbol": False,
                "data": [[d, i * (360 / len(data))] for i, d in enumerate(data)] if data else []
            }]
        }
        option = self._apply_chart_styling(option, color, title_color, title_size, axis_color, axis_size, tooltip_bg_color, None, universal_transition, datazoom, extra_options)
        self.map(element_id=element_id, tooltip=tooltip, echarts_option=option, panel_position=panel_position)

    def map_polar_scatter_chart(self, element_id: str, title: str, data: list[list[float]], color: str | list[str] = None, tooltip: str = None, panel_position: str = None, title_color: str = None, title_size: int = None, axis_color: str = None, axis_size: int = None, tooltip_bg_color: str = None, universal_transition: bool = True, datazoom: bool = False, extra_options: dict = None):
        """
        Maps a Polar Scatter Chart to an element.

        Args:
            element_id (str): The SVG element ID to map to.
            title (str): The chart title.
            data (list[list[float]]): A list of data coordinates formatted as `[[radius, angle], ...]`.
            color (str | list[str], optional): A single color string or a list of color strings (palette). Defaults to "#3b82f6".
            tooltip (str, optional): The tooltip text to display on hover. Defaults to None.
            panel_position (str, optional): The position of the panel where the chart will be rendered. Defaults to None.
            title_color (str, optional): The color of the chart title. Defaults to None.
            title_size (int, optional): The font size of the chart title. Defaults to None.
            axis_color (str, optional): The color of the axis lines and labels. Defaults to None.
            axis_size (int, optional): The font size of the axis labels. Defaults to None.
            tooltip_bg_color (str, optional): The background color of the tooltip. Defaults to None.
            universal_transition (bool, optional): Whether to enable universal transitions. Defaults to True.
            datazoom (bool, optional): Whether to enable data zooming. Defaults to False.
            extra_options (dict, optional): Additional ECharts options to merge. Defaults to None.
        """
        option = {
            "title": {"text": title},
            "tooltip": {"trigger": "item"},
            "polar": {},
            "angleAxis": {"type": "value", "startAngle": 0},
            "radiusAxis": {"type": "value"},
            "series": [{
                "name": title,
                "type": "scatter",
                "coordinateSystem": "polar",
                "data": data
            }]
        }
        option = self._apply_chart_styling(option, color, title_color, title_size, axis_color, axis_size, tooltip_bg_color, None, universal_transition, datazoom, extra_options)
        self.map(element_id=element_id, tooltip=tooltip, echarts_option=option, panel_position=panel_position)

    def map_liquidfill_chart(self, element_id: str, title: str, data: list[float], color: str | list[str] = None, tooltip: str = None, panel_position: str = None, title_color: str = None, title_size: int = None, tooltip_bg_color: str = None, universal_transition: bool = True, datazoom: bool = False, extra_options: dict = None):
        """
        Maps a Liquid Fill Chart to an element. Note: Requires echarts-liquidfill plugin.

        Args:
            element_id (str): The SVG element ID to map to.
            title (str): The chart title.
            data (list[float]): A list of data float percentages formatted as `[0.6, 0.5]`.
            color (str | list[str], optional): A single color string or a list of color strings (palette). Defaults to None.
            tooltip (str, optional): The tooltip text to display on hover. Defaults to None.
            panel_position (str, optional): The position of the panel where the chart will be rendered. Defaults to None.
            title_color (str, optional): The color of the chart title. Defaults to None.
            title_size (int, optional): The font size of the chart title. Defaults to None.
            tooltip_bg_color (str, optional): The background color of the tooltip. Defaults to None.
            universal_transition (bool, optional): Whether to enable universal transitions. Defaults to True.
            datazoom (bool, optional): Whether to enable data zooming. Defaults to False.
            extra_options (dict, optional): Additional ECharts options to merge. Defaults to None.
        """
        option = {
            "title": {"text": title},
            "tooltip": {"show": True},
            "series": [{
                "name": title,
                "type": "liquidFill",
                "data": data,
                "radius": "80%"
            }]
        }
        # echarts-liquidfill has specific coloring parameters
        if color:
            if isinstance(color, list):
                option["series"][0]["color"] = color
            else:
                option["series"][0]["color"] = [color]

        option = self._apply_chart_styling(option, None, title_color, title_size, None, None, tooltip_bg_color, None, universal_transition, datazoom, extra_options)
        self.map(element_id=element_id, tooltip=tooltip, echarts_option=option, panel_position=panel_position)

    def map_custom_chart(self, element_id: str, title: str, render_item_js: str, data: list, tooltip: str = None, panel_position: str = None, datazoom: bool = False, extra_options: dict = None):
        """
        Maps a Custom Series Chart to an element.

        Args:
            element_id (str): The SVG element ID to map to.
            title (str): The chart title.
            render_item_js (str): A string containing a valid JavaScript function for the 'renderItem' property. Since JSON serialization cannot pass raw JS functions, we pass it as a special `_sivo_render_item` string which the HTML runtime will `eval()` during option generation.
            data (list): A list of data values.
            tooltip (str, optional): The tooltip text to display on hover. Defaults to None.
            panel_position (str, optional): The position of the panel where the chart will be rendered. Defaults to None.
            datazoom (bool, optional): Whether to enable data zooming. Defaults to False.
            extra_options (dict, optional): Additional ECharts options to merge. Defaults to None.
        """
        option = {
            "title": {"text": title},
            "tooltip": {},
            "xAxis": {},
            "yAxis": {},
            "series": [{
                "name": title,
                "type": "custom",
                "_sivo_render_item": render_item_js,
                "data": data
            }]
        }
        if datazoom:
            option["dataZoom"] = [
                {
                    "type": "slider",
                    "xAxisIndex": 0,
                    "filterMode": "filter"
                },
                {
                    "type": "slider",
                    "yAxisIndex": 0,
                    "filterMode": "filter"
                },
                {
                    "type": "inside",
                    "xAxisIndex": 0,
                    "filterMode": "filter"
                },
                {
                    "type": "inside",
                    "yAxisIndex": 0,
                    "filterMode": "filter"
                }
            ]

        if extra_options:
            option = self._apply_chart_styling(option, None, None, None, None, None, None, None, True, datazoom, extra_options)
        self.map(element_id=element_id, tooltip=tooltip, echarts_option=option, panel_position=panel_position)

    def map_boxplot_chart(self, element_id: str, title: str, data: list[list[float]], categories: list[str], color: str | list[str] = None, tooltip: str = None, panel_position: str = None, title_color: str = None, title_size: int = None, axis_color: str = None, axis_size: int = None, tooltip_bg_color: str = None, grid_margin: list[int] = None, universal_transition: bool = True, datazoom: bool = False, extra_options: dict = None):
        """
        Maps a Boxplot Chart to an element.

        Args:
            element_id (str): The SVG element ID to map to.
            title (str): The chart title.
            data (list[list[float]]): A 2D array of values for each category.
            categories (list[str]): A list of category labels for the axis.
            color (str | list[str], optional): A single color string or a list of color strings (palette). Defaults to None.
            tooltip (str, optional): The tooltip text to display on hover. Defaults to None.
            panel_position (str, optional): The position of the panel where the chart will be rendered. Defaults to None.
            title_color (str, optional): The color of the chart title. Defaults to None.
            title_size (int, optional): The font size of the chart title. Defaults to None.
            axis_color (str, optional): The color of the axis lines and labels. Defaults to None.
            axis_size (int, optional): The font size of the axis labels. Defaults to None.
            tooltip_bg_color (str, optional): The background color of the tooltip. Defaults to None.
            grid_margin (list[int], optional): The margins for the chart grid [top, right, bottom, left]. Defaults to None.
            universal_transition (bool, optional): Whether to enable universal transitions. Defaults to True.
            datazoom (bool, optional): Whether to enable data zooming. Defaults to False.
            extra_options (dict, optional): Additional ECharts options to merge. Defaults to None.
        """
        option = {
            "title": {"text": title},
            "tooltip": {"trigger": "item", "axisPointer": {"type": "shadow"}},
            "xAxis": {"type": "category", "data": categories},
            "yAxis": {"type": "value"},
            "series": [{
                "name": title,
                "type": "boxplot",
                "data": data
            }]
        }
        option = self._apply_chart_styling(option, color, title_color, title_size, axis_color, axis_size, tooltip_bg_color, grid_margin, universal_transition, datazoom, extra_options)
        self.map(element_id=element_id, tooltip=tooltip, echarts_option=option, panel_position=panel_position)

    def map_candlestick_chart(self, element_id: str, title: str, data: list[list[float]], categories: list[str], item_color: str = '#eb5454', item_color0: str = '#47b262', tooltip: str = None, panel_position: str = None, title_color: str = None, title_size: int = None, axis_color: str = None, axis_size: int = None, tooltip_bg_color: str = None, grid_margin: list[int] = None, universal_transition: bool = True, datazoom: bool = False, extra_options: dict = None):
        """
        Maps a Candlestick Chart (K-line) to an element.

        Args:
            element_id (str): The SVG element ID to map to.
            title (str): The chart title.
            data (list[list[float]]): A list of data arrays formatted as `[[open, close, lowest, highest], ...]`.
            categories (list[str]): A list of category labels for the axis.
            item_color (str, optional): The color of bullish candles. Defaults to '#eb5454'.
            item_color0 (str, optional): The color of bearish candles. Defaults to '#47b262'.
            tooltip (str, optional): The tooltip text to display on hover. Defaults to None.
            panel_position (str, optional): The position of the panel where the chart will be rendered. Defaults to None.
            title_color (str, optional): The color of the chart title. Defaults to None.
            title_size (int, optional): The font size of the chart title. Defaults to None.
            axis_color (str, optional): The color of the axis lines and labels. Defaults to None.
            axis_size (int, optional): The font size of the axis labels. Defaults to None.
            tooltip_bg_color (str, optional): The background color of the tooltip. Defaults to None.
            grid_margin (list[int], optional): The margins for the chart grid [top, right, bottom, left]. Defaults to None.
            universal_transition (bool, optional): Whether to enable universal transitions. Defaults to True.
            datazoom (bool, optional): Whether to enable data zooming. Defaults to False.
            extra_options (dict, optional): Additional ECharts options to merge. Defaults to None.
        """
        option = {
            "title": {"text": title},
            "tooltip": {"trigger": "axis", "axisPointer": {"type": "cross"}},
            "xAxis": {"data": categories},
            "yAxis": {"scale": True},
            "series": [{
                "name": title,
                "type": "candlestick",
                "data": data,
                "itemStyle": {
                    "color": item_color,
                    "color0": item_color0,
                    "borderColor": item_color,
                    "borderColor0": item_color0
                }
            }]
        }
        option = self._apply_chart_styling(option, None, title_color, title_size, axis_color, axis_size, tooltip_bg_color, grid_margin, universal_transition, datazoom, extra_options)
        self.map(element_id=element_id, tooltip=tooltip, echarts_option=option, panel_position=panel_position)

    def map_word_cloud_chart(self, element_id: str, title: str, data: list[dict], mask_image: str = None, color: Union[str, list[str]] = None, tooltip: str = None, panel_position: str = None, title_color: str = None, title_size: int = None, tooltip_bg_color: str = None, universal_transition: bool = True, datazoom: bool = False, extra_options: dict = None):
        """
        Maps a Word Cloud Chart to an element. Note: Requires echarts-wordcloud plugin (included by default in SIVO CDN templates).

        Args:
            element_id (str): The SVG element ID to map to.
            title (str): The chart title.
            data (list[dict]): A list of word definitions formatted as `[{'name': 'Word', 'value': 100}, ...]`.
            mask_image (str, optional): Optional URL or base64 string to a silhouette image (black and white) to constrain the word cloud shape.
            color (Union[str, list[str]], optional): A single color string or a list of color strings (palette). Defaults to None.
            tooltip (str, optional): The tooltip text to display on hover. Defaults to None.
            panel_position (str, optional): The position of the panel where the chart will be rendered. Defaults to None.
            title_color (str, optional): The color of the chart title. Defaults to None.
            title_size (int, optional): The font size of the chart title. Defaults to None.
            tooltip_bg_color (str, optional): The background color of the tooltip. Defaults to None.
            universal_transition (bool, optional): Whether to enable universal transitions. Defaults to True.
            datazoom (bool, optional): Whether to enable data zooming. Defaults to False.
            extra_options (dict, optional): Additional ECharts options to merge. Defaults to None.
        """
        option = {
            "title": {"text": title},
            "tooltip": {"show": True},
            "series": [{
                "name": title,
                "type": "wordCloud",
                "shape": "circle",
                "left": "center",
                "top": "center",
                "width": "90%",
                "height": "90%",
                "right": None,
                "bottom": None,
                "sizeRange": [12, 60],
                "rotationRange": [-90, 90],
                "rotationStep": 45,
                "gridSize": 8,
                "drawOutOfBound": False,
                "layoutAnimation": True,
                "textStyle": {
                    "fontFamily": "sans-serif",
                    "fontWeight": "bold"
                },
                "emphasis": {
                    "focus": "self",
                    "textStyle": {
                        "textShadowBlur": 10,
                        "textShadowColor": "#333"
                    }
                },
                "data": data
            }]
        }

        if mask_image:
            # We pass this as a custom property. The JS runtime will intercept it, load the image, and attach the DOM object to maskImage
            option["series"][0]["_sivo_mask_image_url"] = mask_image

        option = self._apply_chart_styling(option, color, title_color, title_size, None, None, tooltip_bg_color, None, universal_transition, datazoom, extra_options)
        self.map(element_id=element_id, tooltip=tooltip, echarts_option=option, panel_position=panel_position)

    def map_calendar_heatmap_chart(self, element_id: str, title: str, data: list[list[Union[str, float]]], calendar_range: Union[str, list[str]], color: list[str] = None, tooltip: str = None, panel_position: str = None, title_color: str = None, title_size: int = None, tooltip_bg_color: str = None, universal_transition: bool = True, datazoom: bool = False, extra_options: dict = None):
        """
        Maps a Calendar Heatmap Chart to an element.

        Args:
            element_id (str): The SVG element ID to map to.
            title (str): The chart title.
            data (list[list[Union[str, float]]]): A list of data coordinates formatted as `[['2017-01-01', 10], ['2017-01-02', 20], ...]`.
            calendar_range (Union[str, list[str]]): The range of the calendar, formatted as `'2017'` or `['2017-01-01', '2017-12-31']`.
            color (list[str], optional): A list of color strings for the gradient scale. Defaults to None.
            tooltip (str, optional): The tooltip text to display on hover. Defaults to None.
            panel_position (str, optional): The position of the panel where the chart will be rendered. Defaults to None.
            title_color (str, optional): The color of the chart title. Defaults to None.
            title_size (int, optional): The font size of the chart title. Defaults to None.
            tooltip_bg_color (str, optional): The background color of the tooltip. Defaults to None.
            universal_transition (bool, optional): Whether to enable universal transitions. Defaults to True.
            datazoom (bool, optional): Whether to enable data zooming. Defaults to False.
            extra_options (dict, optional): Additional ECharts options to merge. Defaults to None.
        """
        option = {
            "title": {"text": title},
            "tooltip": {"position": "top"},
            "visualMap": {
                "min": 0,
                "max": max([d[1] for d in data]) if data else 100,
                "calculable": True,
                "orient": "horizontal",
                "left": "center",
                "top": "top",
                "inRange": {"color": color if color else ["#ebedf0", "#c6e48b", "#7bc96f", "#239a3b", "#196127"]}
            },
            "calendar": [{
                "range": calendar_range,
                "cellSize": ["auto", 20],
                "yearLabel": {"show": True, "margin": 40}
            }],
            "series": [{
                "name": title,
                "type": "heatmap",
                "coordinateSystem": "calendar",
                "data": data
            }]
        }
        option = self._apply_chart_styling(option, None, title_color, title_size, None, None, tooltip_bg_color, None, universal_transition, datazoom, extra_options)
        self.map(element_id=element_id, tooltip=tooltip, echarts_option=option, panel_position=panel_position)

    def map_heatmap_chart(self, element_id: str, title: str, data: list[list[float]], x_categories: list[str], y_categories: list[str], color: list[str] = None, tooltip: str = None, panel_position: str = None, title_color: str = None, title_size: int = None, axis_color: str = None, axis_size: int = None, tooltip_bg_color: str = None, grid_margin: list[int] = None, universal_transition: bool = True, datazoom: bool = False, extra_options: dict = None):
        """
        Maps a Cartesian Heatmap Chart to an element.

        Args:
            element_id (str): The SVG element ID to map to.
            title (str): The chart title.
            data (list[list[float]]): A list of data coordinates formatted as `[[x_index, y_index, value], ...]`.
            x_categories (list[str]): A list of categories for the X axis.
            y_categories (list[str]): A list of categories for the Y axis.
            color (list[str], optional): A list of color strings for the gradient scale. Defaults to None.
            tooltip (str, optional): The tooltip text to display on hover. Defaults to None.
            panel_position (str, optional): The position of the panel where the chart will be rendered. Defaults to None.
            title_color (str, optional): The color of the chart title. Defaults to None.
            title_size (int, optional): The font size of the chart title. Defaults to None.
            axis_color (str, optional): The color of the axis lines and labels. Defaults to None.
            axis_size (int, optional): The font size of the axis labels. Defaults to None.
            tooltip_bg_color (str, optional): The background color of the tooltip. Defaults to None.
            grid_margin (list[int], optional): The margins for the chart grid [top, right, bottom, left]. Defaults to None.
            universal_transition (bool, optional): Whether to enable universal transitions. Defaults to True.
            datazoom (bool, optional): Whether to enable data zooming. Defaults to False.
            extra_options (dict, optional): Additional ECharts options to merge. Defaults to None.
        """
        option = {
            "title": {"text": title},
            "tooltip": {"position": "top"},
            "xAxis": {"type": "category", "data": x_categories, "splitArea": {"show": True}},
            "yAxis": {"type": "category", "data": y_categories, "splitArea": {"show": True}},
            "visualMap": {
                "min": 0,
                "max": max([d[2] for d in data]) if data else 100,
                "calculable": True,
                "orient": "horizontal",
                "left": "center",
                "bottom": "0%",
                "inRange": {"color": color if color else ["#ebedf0", "#c6e48b", "#7bc96f", "#239a3b", "#196127"]}
            },
            "series": [{
                "name": title,
                "type": "heatmap",
                "data": data,
                "label": {"show": True},
                "emphasis": {
                    "itemStyle": {
                        "shadowBlur": 10,
                        "shadowColor": "rgba(0, 0, 0, 0.5)"
                    }
                }
            }]
        }
        option = self._apply_chart_styling(option, None, title_color, title_size, axis_color, axis_size, tooltip_bg_color, grid_margin, universal_transition, datazoom, extra_options)
        self.map(element_id=element_id, tooltip=tooltip, echarts_option=option, panel_position=panel_position)

    def map_graph_chart(self, element_id: str, title: str, nodes: list[dict], links: list[dict], categories: list[dict] = None, color: str | list[str] = None, layout: str = "force", tooltip: str = None, panel_position: str = None, title_color: str = None, title_size: int = None, tooltip_bg_color: str = None, universal_transition: bool = True, datazoom: bool = False, extra_options: dict = None):
        """
        Maps a Graph Chart (Network) to an element.

        Args:
            element_id (str): The SVG element ID to map to.
            title (str): The chart title.
            nodes (list[dict]): A list of nodes formatted as `[{'name': 'Node1'}]`.
            links (list[dict]): A list of links formatted as `[{'source': 'Node1', 'target': 'Node2'}]`.
            categories (list[dict], optional): A list of categories to assign nodes to. Defaults to None.
            color (str | list[str], optional): A single color string or a list of color strings (palette). Defaults to None.
            layout (str, optional): The layout strategy to use ('none', 'circular', 'force'). Defaults to "force".
            tooltip (str, optional): The tooltip text to display on hover. Defaults to None.
            panel_position (str, optional): The position of the panel where the chart will be rendered. Defaults to None.
            title_color (str, optional): The color of the chart title. Defaults to None.
            title_size (int, optional): The font size of the chart title. Defaults to None.
            tooltip_bg_color (str, optional): The background color of the tooltip. Defaults to None.
            universal_transition (bool, optional): Whether to enable universal transitions. Defaults to True.
            datazoom (bool, optional): Whether to enable data zooming. Defaults to False.
            extra_options (dict, optional): Additional ECharts options to merge. Defaults to None.
        """
        option = {
            "title": {"text": title},
            "tooltip": {},
            "legend": {"data": [c.get("name") for c in categories]} if categories else None,
            "series": [{
                "name": title,
                "type": "graph",
                "layout": layout,
                "data": nodes,
                "links": links,
                "categories": categories,
                "roam": True,
                "label": {"position": "right", "formatter": "{b}"},
                "lineStyle": {"color": "source", "curveness": 0.3},
                "emphasis": {
                    "focus": "adjacency",
                    "lineStyle": {"width": 10}
                }
            }]
        }
        if layout == "force":
            option["series"][0]["force"] = {"repulsion": 100}

        option = self._apply_chart_styling(option, color, title_color, title_size, None, None, tooltip_bg_color, None, universal_transition, datazoom, extra_options)
        self.map(element_id=element_id, tooltip=tooltip, echarts_option=option, panel_position=panel_position)

    def map_sankey_chart(self, element_id: str, title: str, nodes: list[dict], links: list[dict], color: str | list[str] = None, tooltip: str = None, panel_position: str = None, title_color: str = None, title_size: int = None, tooltip_bg_color: str = None, universal_transition: bool = True, datazoom: bool = False, extra_options: dict = None):
        """
        Maps a Sankey Diagram to an element.

        Args:
            element_id (str): The SVG element ID to map to.
            title (str): The chart title.
            nodes (list[dict]): A list of nodes formatted as `[{'name': 'A'}]`.
            links (list[dict]): A list of links formatted as `[{'source': 'A', 'target': 'B', 'value': 10}]`.
            color (str | list[str], optional): A single color string or a list of color strings (palette). Defaults to None.
            tooltip (str, optional): The tooltip text to display on hover. Defaults to None.
            panel_position (str, optional): The position of the panel where the chart will be rendered. Defaults to None.
            title_color (str, optional): The color of the chart title. Defaults to None.
            title_size (int, optional): The font size of the chart title. Defaults to None.
            tooltip_bg_color (str, optional): The background color of the tooltip. Defaults to None.
            universal_transition (bool, optional): Whether to enable universal transitions. Defaults to True.
            datazoom (bool, optional): Whether to enable data zooming. Defaults to False.
            extra_options (dict, optional): Additional ECharts options to merge. Defaults to None.
        """
        option = {
            "title": {"text": title},
            "tooltip": {"trigger": "item", "triggerOn": "mousemove"},
            "series": [{
                "type": "sankey",
                "data": nodes,
                "links": links,
                "emphasis": {"focus": "adjacency"},
                "lineStyle": {"color": "gradient", "curveness": 0.5}
            }]
        }
        option = self._apply_chart_styling(option, color, title_color, title_size, None, None, tooltip_bg_color, None, universal_transition, datazoom, extra_options)
        self.map(element_id=element_id, tooltip=tooltip, echarts_option=option, panel_position=panel_position)

    def map_sunburst_chart(self, element_id: str, title: str, data: list[dict], color: str | list[str] = None, tooltip: str = None, panel_position: str = None, title_color: str = None, title_size: int = None, tooltip_bg_color: str = None, universal_transition: bool = True, datazoom: bool = False, extra_options: dict = None):
        """
        Maps a Sunburst Chart to an element.

        Args:
            element_id (str): The SVG element ID to map to.
            title (str): The chart title.
            data (list[dict]): A list of hierarchical nodes formatted as `[{'name': 'A', 'value': 10, 'children': [...]}]`.
            color (str | list[str], optional): A single color string or a list of color strings (palette). Defaults to None.
            tooltip (str, optional): The tooltip text to display on hover. Defaults to None.
            panel_position (str, optional): The position of the panel where the chart will be rendered. Defaults to None.
            title_color (str, optional): The color of the chart title. Defaults to None.
            title_size (int, optional): The font size of the chart title. Defaults to None.
            tooltip_bg_color (str, optional): The background color of the tooltip. Defaults to None.
            universal_transition (bool, optional): Whether to enable universal transitions. Defaults to True.
            datazoom (bool, optional): Whether to enable data zooming. Defaults to False.
            extra_options (dict, optional): Additional ECharts options to merge. Defaults to None.
        """
        option = {
            "title": {"text": title},
            "tooltip": {},
            "series": [{
                "type": "sunburst",
                "data": data,
                "radius": [0, "90%"],
                "label": {"rotate": "radial"}
            }]
        }
        option = self._apply_chart_styling(option, color, title_color, title_size, None, None, tooltip_bg_color, None, universal_transition, datazoom, extra_options)
        self.map(element_id=element_id, tooltip=tooltip, echarts_option=option, panel_position=panel_position)

    def map_parallel_chart(self, element_id: str, title: str, schema: list[dict], data: list[list[float]], color: str | list[str] = None, tooltip: str = None, panel_position: str = None, title_color: str = None, title_size: int = None, tooltip_bg_color: str = None, universal_transition: bool = True, datazoom: bool = False, extra_options: dict = None):
        """
        Maps a Parallel Coordinates Chart to an element.

        Args:
            element_id (str): The SVG element ID to map to.
            title (str): The chart title.
            schema (list[dict]): A list of dimensions formatted as `[{'dim': 0, 'name': 'A'}, ...]`.
            data (list[list[float]]): A list of data arrays formatted as `[[val1, val2], ...]`.
            color (str | list[str], optional): A single color string or a list of color strings (palette). Defaults to None.
            tooltip (str, optional): The tooltip text to display on hover. Defaults to None.
            panel_position (str, optional): The position of the panel where the chart will be rendered. Defaults to None.
            title_color (str, optional): The color of the chart title. Defaults to None.
            title_size (int, optional): The font size of the chart title. Defaults to None.
            tooltip_bg_color (str, optional): The background color of the tooltip. Defaults to None.
            universal_transition (bool, optional): Whether to enable universal transitions. Defaults to True.
            datazoom (bool, optional): Whether to enable data zooming. Defaults to False.
            extra_options (dict, optional): Additional ECharts options to merge. Defaults to None.
        """
        option = {
            "title": {"text": title},
            "tooltip": {"padding": 10, "backgroundColor": "#222", "borderColor": "#777", "borderWidth": 1},
            "parallelAxis": schema,
            "parallel": {
                "left": "5%", "right": "18%", "bottom": "10%", "top": "20%",
                "parallelAxisDefault": {"type": "value", "nameLocation": "end", "nameGap": 20}
            },
            "series": [{
                "name": title,
                "type": "parallel",
                "lineStyle": {"width": 1, "opacity": 0.5},
                "data": data
            }]
        }
        option = self._apply_chart_styling(option, color, title_color, title_size, None, None, tooltip_bg_color, None, universal_transition, datazoom, extra_options)
        self.map(element_id=element_id, tooltip=tooltip, echarts_option=option, panel_position=panel_position)

    def map_theme_river_chart(self, element_id: str, title: str, data: list[list[Union[str, float]]], legend_data: list[str], color: str | list[str] = None, tooltip: str = None, panel_position: str = None, title_color: str = None, title_size: int = None, tooltip_bg_color: str = None, universal_transition: bool = True, datazoom: bool = False, extra_options: dict = None):
        """
        Maps a ThemeRiver (Streamgraph) Chart to an element.

        Args:
            element_id (str): The SVG element ID to map to.
            title (str): The chart title.
            data (list[list[Union[str, float]]]): A list of data arrays formatted as `[[date, value, category_name], ...]`.
            legend_data (list[str]): A list of legend category names.
            color (str | list[str], optional): A single color string or a list of color strings (palette). Defaults to None.
            tooltip (str, optional): The tooltip text to display on hover. Defaults to None.
            panel_position (str, optional): The position of the panel where the chart will be rendered. Defaults to None.
            title_color (str, optional): The color of the chart title. Defaults to None.
            title_size (int, optional): The font size of the chart title. Defaults to None.
            tooltip_bg_color (str, optional): The background color of the tooltip. Defaults to None.
            universal_transition (bool, optional): Whether to enable universal transitions. Defaults to True.
            datazoom (bool, optional): Whether to enable data zooming. Defaults to False.
            extra_options (dict, optional): Additional ECharts options to merge. Defaults to None.
        """
        option = {
            "title": {"text": title},
            "tooltip": {"trigger": "axis", "axisPointer": {"type": "line", "lineStyle": {"color": "rgba(0,0,0,0.2)", "width": 1, "type": "solid"}}},
            "legend": {"data": legend_data},
            "singleAxis": {
                "top": 50, "bottom": 50,
                "axisTick": {}, "axisLabel": {}, "type": "time",
                "axisPointer": {"animation": True, "label": {"show": True}},
                "splitLine": {"show": True, "lineStyle": {"type": "dashed", "opacity": 0.2}}
            },
            "series": [{
                "type": "themeRiver",
                "emphasis": {"itemStyle": {"shadowBlur": 20, "shadowColor": "rgba(0, 0, 0, 0.8)"}},
                "data": data
            }]
        }
        option = self._apply_chart_styling(option, color, title_color, title_size, None, None, tooltip_bg_color, None, universal_transition, datazoom, extra_options)
        self.map(element_id=element_id, tooltip=tooltip, echarts_option=option, panel_position=panel_position)


    def map_effect_scatter_chart(self, element_id: str, title: str, data: list[list[float]], color: str | list[str] = None, tooltip: str = None, panel_position: str = None, title_color: str = None, title_size: int = None, axis_color: str = None, axis_size: int = None, tooltip_bg_color: str = None, grid_margin: list[int] = None, universal_transition: bool = True, datazoom: bool = False, extra_options: dict = None):
        """
        Maps an Effect Scatter Chart to an element.

        Args:
            element_id (str): The SVG element ID to map to.
            title (str): The chart title.
            data (list[list[float]]): A list of data coordinates formatted as `[[x1, y1], [x2, y2]]`.
            color (str | list[str], optional): A single color string or a list of color strings (palette). Defaults to None.
            tooltip (str, optional): The tooltip text to display on hover. Defaults to None.
            panel_position (str, optional): The position of the panel where the chart will be rendered. Defaults to None.
            title_color (str, optional): The color of the chart title. Defaults to None.
            title_size (int, optional): The font size of the chart title. Defaults to None.
            axis_color (str, optional): The color of the axis lines and labels. Defaults to None.
            axis_size (int, optional): The font size of the axis labels. Defaults to None.
            tooltip_bg_color (str, optional): The background color of the tooltip. Defaults to None.
            grid_margin (list[int], optional): The margins for the chart grid [top, right, bottom, left]. Defaults to None.
            universal_transition (bool, optional): Whether to enable universal transitions. Defaults to True.
            datazoom (bool, optional): Whether to enable data zooming. Defaults to False.
            extra_options (dict, optional): Additional ECharts options to merge. Defaults to None.
        """
        option = {
            "title": {"text": title},
            "tooltip": {"trigger": "item"},
            "xAxis": {},
            "yAxis": {},
            "series": [{
                "name": title,
                "type": "effectScatter",
                "data": data,
                "showEffectOn": "render",
                "rippleEffect": {
                    "brushType": "stroke"
                }
            }]
        }
        option = self._apply_chart_styling(option, color, title_color, title_size, axis_color, axis_size, tooltip_bg_color, grid_margin, universal_transition, datazoom, extra_options)
        self.map(element_id=element_id, tooltip=tooltip, echarts_option=option, panel_position=panel_position)

    def map_lines_chart(self, element_id: str, title: str, data: list[dict], color: str | list[str] = None, tooltip: str = None, panel_position: str = None, title_color: str = None, title_size: int = None, tooltip_bg_color: str = None, universal_transition: bool = True, datazoom: bool = False, extra_options: dict = None):
        """
        Maps a Lines Chart to an element.

        Args:
            element_id (str): The SVG element ID to map to.
            title (str): The chart title.
            data (list[dict]): A list of data lines formatted as `[{'coords': [[lng1, lat1], [lng2, lat2]]}]`.
            color (str | list[str], optional): A single color string or a list of color strings (palette). Defaults to None.
            tooltip (str, optional): The tooltip text to display on hover. Defaults to None.
            panel_position (str, optional): The position of the panel where the chart will be rendered. Defaults to None.
            title_color (str, optional): The color of the chart title. Defaults to None.
            title_size (int, optional): The font size of the chart title. Defaults to None.
            tooltip_bg_color (str, optional): The background color of the tooltip. Defaults to None.
            universal_transition (bool, optional): Whether to enable universal transitions. Defaults to True.
            datazoom (bool, optional): Whether to enable data zooming. Defaults to False.
            extra_options (dict, optional): Additional ECharts options to merge. Defaults to None.
        """
        option = {
            "title": {"text": title},
            "tooltip": {"trigger": "item"},
            "xAxis": {"show": False},
            "yAxis": {"show": False},
            "series": [{
                "name": title,
                "type": "lines",
                "data": data,
                "coordinateSystem": "cartesian2d",
                "polyline": True,
                "lineStyle": {
                    "width": 2
                }
            }]
        }
        option = self._apply_chart_styling(option, color, title_color, title_size, None, None, tooltip_bg_color, None, universal_transition, datazoom, extra_options)
        self.map(element_id=element_id, tooltip=tooltip, echarts_option=option, panel_position=panel_position)

    def map_funnel_chart(self, element_id: str, title: str, data: list[dict], color: str | list[str] = None, tooltip: str = None, panel_position: str = None, title_color: str = None, title_size: int = None, tooltip_bg_color: str = None, universal_transition: bool = True, datazoom: bool = False, extra_options: dict = None):
        """
        Maps a Funnel Chart to an element.

        Args:
            element_id (str): The SVG element ID to map to.
            title (str): The chart title.
            data (list[dict]): A list of data series formatted as `[{'value': 60, 'name': 'Visit'}]`.
            color (str | list[str], optional): A single color string or a list of color strings (palette). Defaults to None.
            tooltip (str, optional): The tooltip text to display on hover. Defaults to None.
            panel_position (str, optional): The position of the panel where the chart will be rendered. Defaults to None.
            title_color (str, optional): The color of the chart title. Defaults to None.
            title_size (int, optional): The font size of the chart title. Defaults to None.
            tooltip_bg_color (str, optional): The background color of the tooltip. Defaults to None.
            universal_transition (bool, optional): Whether to enable universal transitions. Defaults to True.
            datazoom (bool, optional): Whether to enable data zooming. Defaults to False.
            extra_options (dict, optional): Additional ECharts options to merge. Defaults to None.
        """
        option = {
            "title": {"text": title},
            "tooltip": {"trigger": "item"},
            "series": [{
                "name": title,
                "type": "funnel",
                "data": data,
                "left": "10%",
                "top": 60,
                "bottom": 60,
                "width": "80%",
                "min": 0,
                "max": 100,
                "minSize": "0%",
                "maxSize": "100%",
                "sort": "descending",
                "gap": 2,
                "label": {
                    "show": True,
                    "position": "inside"
                },
                "labelLine": {
                    "length": 10,
                    "lineStyle": {
                        "width": 1,
                        "type": "solid"
                    }
                },
                "itemStyle": {
                    "borderColor": "#fff",
                    "borderWidth": 1
                }
            }]
        }
        option = self._apply_chart_styling(option, color, title_color, title_size, None, None, tooltip_bg_color, None, universal_transition, datazoom, extra_options)
        self.map(element_id=element_id, tooltip=tooltip, echarts_option=option, panel_position=panel_position)

    def map_tree_chart(self, element_id: str, title: str, data: list[dict], color: str | list[str] = None, tooltip: str = None, panel_position: str = None, title_color: str = None, title_size: int = None, tooltip_bg_color: str = None, universal_transition: bool = True, datazoom: bool = False, extra_options: dict = None):
        """
        Maps a Tree Chart to an element.

        Args:
            element_id (str): The SVG element ID to map to.
            title (str): The chart title.
            data (list[dict]): A list of hierarchical nodes formatted as `[{'name': 'Root', 'children': [...]}]`.
            color (str | list[str], optional): A single color string or a list of color strings (palette). Defaults to None.
            tooltip (str, optional): The tooltip text to display on hover. Defaults to None.
            panel_position (str, optional): The position of the panel where the chart will be rendered. Defaults to None.
            title_color (str, optional): The color of the chart title. Defaults to None.
            title_size (int, optional): The font size of the chart title. Defaults to None.
            tooltip_bg_color (str, optional): The background color of the tooltip. Defaults to None.
            universal_transition (bool, optional): Whether to enable universal transitions. Defaults to True.
            datazoom (bool, optional): Whether to enable data zooming. Defaults to False.
            extra_options (dict, optional): Additional ECharts options to merge. Defaults to None.
        """
        option = {
            "title": {"text": title},
            "tooltip": {"trigger": "item", "triggerOn": "mousemove"},
            "series": [{
                "name": title,
                "type": "tree",
                "data": data,
                "top": "10%",
                "left": "20%",
                "bottom": "10%",
                "right": "20%",
                "symbolSize": 7,
                "label": {
                    "position": "left",
                    "verticalAlign": "middle",
                    "align": "right",
                    "fontSize": 9
                },
                "leaves": {
                    "label": {
                        "position": "right",
                        "verticalAlign": "middle",
                        "align": "left"
                    }
                },
                "emphasis": {
                    "focus": "descendant"
                },
                "expandAndCollapse": True,
                "animationDuration": 550,
                "animationDurationUpdate": 750
            }]
        }
        option = self._apply_chart_styling(option, color, title_color, title_size, None, None, tooltip_bg_color, None, universal_transition, datazoom, extra_options)
        self.map(element_id=element_id, tooltip=tooltip, echarts_option=option, panel_position=panel_position)

    def build_javascript(self, entry_point: str = "src/sivo/runtime/templates/sivo_bundle.js", output_dir: str = "dist"):
        """
        Non-default option: Triggers a JavaScript bundler (e.g., esbuild) to minify and
        bundle frontend assets instead of relying on CDN links.
        Requires Node.js and 'npm install' to have been run.
        """
        import sys
        if "pyodide" in sys.modules:
            logger.error("Error: JavaScript bundling is not supported in WebAssembly/Pyodide because the subprocess module is not available.")
            return

        import subprocess
        import os
        logger.info(f"SIVO Build System: Bundling JS assets from {entry_point} -> {output_dir}")
        if not os.path.exists("package.json"):
            logger.warning("Warning: package.json not found. Generating default package.json for esbuild...")
            import json
            pkg_data = {
                "name": "sivo",
                "scripts": {
                    "build": f"esbuild {entry_point} --bundle --minify --outfile={output_dir}/sivo.min.js"
                },
                "dependencies": {
                    "echarts": "^5.5.0",
                    "dompurify": "^3.0.6",
                    "marked": "^12.0.0"
                },
                "devDependencies": {
                    "esbuild": "^0.20.0"
                }
            }
            with open("package.json", "w") as f:
                json.dump(pkg_data, f, indent=2)
        try:
            logger.info("Running 'npm install'...")
            subprocess.run(["npm", "install"], check=True)
            logger.info("Running 'npm run build'...")
            subprocess.run(["npm", "run", "build"], check=True)
            self.infographic.build_js = True
            logger.info(f"Successfully bundled JS to {output_dir}/sivo.min.js")
        except FileNotFoundError:
            logger.error("Error: npm or node not found in PATH. Please install Node.js to use JS bundling.")
        except subprocess.CalledProcessError as e:
            logger.error(f"Build failed: {e}")

    def apply_choropleth(self, data_map: Dict[str, float], min_color: str = "#ffffff", max_color: str = "#ff0000", show_legend: bool = True, legend_draggable: bool = True):
        """
        Generates a choropleth map by interpolating colors based on a numeric data mapping.
        """
        self.infographic.apply_choropleth(data_map, min_color, max_color, show_legend, legend_draggable)

    def apply_value_by_alpha(self, base_data_map: Dict[str, float], alpha_data_map: Dict[str, float], min_color: str = "#ffffff", max_color: str = "#ff0000", min_alpha: float = 0.2, max_alpha: float = 1.0, show_legend: bool = True, legend_draggable: bool = True):
        """
        Generates a Value-by-Alpha choropleth map where the base color is determined by one variable,
        and the transparency (alpha) is determined by a second absolute variable (e.g., population density).
        """
        self.infographic.apply_value_by_alpha(base_data_map, alpha_data_map, min_color, max_color, min_alpha, max_alpha, show_legend, legend_draggable)

    def apply_categorical_map(self, data_map: Dict[str, str], color_palette: Dict[str, str] = None, show_legend: bool = True, legend_draggable: bool = True, item_opacity: float = 1.0, border_color: str = "rgba(0,0,0,0.1)", border_width: float = 0.5):
        """
        Generates a categorical map mapping discrete categories (strings) to specific colors.
        """
        self.infographic.apply_categorical_map(data_map, color_palette, show_legend, legend_draggable, item_opacity, border_color, border_width)

    def add_connection(self, source_id: str, target_id: str, label: str = "", color: str = "#ff3333", width: float = 2.0, animation_speed: float = 3.0, type: str = "solid", opacity: float = 0.6, flow_effect: bool = False, effect_symbol: str = "circle", effect_size: float = 3.0, source_coord: list[float] = None, target_coord: list[float] = None):
        """
        Draws a visual connection line between the centers of two SVG elements.
        Optionally override the coordinates using source_coord and target_coord.
        """
        self.infographic.add_connection(source_id, target_id, label, color, width, animation_speed, type, opacity, flow_effect, effect_symbol, effect_size, source_coord, target_coord)


    def add_card(self, element_id: str, title: str, value: str = "", subtitle: str = "", body: str = "",
                 left: str = "0%", top: str = "0%", width: str = "100%", height: str = "100%",
                 shape: str = "rect", bg_color: str = "#ffffff", border_color: str = "#e2e8f0", border_width: str = "1px", rx: str = "8",
                 title_color: str = "#64748b", value_color: str = "#0f172a", subtitle_color: str = "#94a3b8", body_color: str = "#475569",
                 auto_fit_text: bool = True, url: Optional[str] = None, url_target: str = "_blank",
                 url_transition: Optional[str] = None, glow: Optional[bool] = None, fade_in: bool = False,
                 fade_pulse: bool = False, fade_start_time_ms: int = 0, fade_duration_ms: int = 5000,
                 shadow: bool = False, glass: bool = False, dasharray: str = "", gradient_bg: str = "", html_body: bool = False):
        """
        Automatically generates a perfectly scaled, native SVG card relative to the bounding box
        of a target element, displaying a title, main value, and optional subtitle.

        Args:
            element_id: The ID or name of the target SVG element (e.g., a card or region) to anchor to.
            title: The title text of the card.
            value: The main value text of the card.
            subtitle: Optional subtitle text.
            left: The left offset relative to the bounding box (e.g., "0%").
            top: The top offset relative to the bounding box (e.g., "0%").
            width: The total width of the card relative to the bounding box (e.g., "100%").
            height: The height of the card relative to the bounding box (e.g., "100%").
            bg_color: Background color of the card.
            border_color: Border color of the card.
            border_width: Border width of the card.
            rx: The border radius of the card (in absolute pixels).
            title_color: The text color for the title.
            value_color: The text color for the main value.
            subtitle_color: The text color for the subtitle.
            url: Optional URL to navigate to when the card is clicked.
            url_target: Target window for the URL (e.g. "_blank").
            url_transition: Optional CSS transition class to add to body when navigating.
            glow: Applies a CSS glow effect on hover if true.
            fade_in: Applies a fade in animation.
            fade_pulse: Applies a continuous pulsing fade animation.
            fade_start_time_ms: Delay in milliseconds before animation starts.
            fade_duration_ms: Duration of the animation in milliseconds.
            shadow: Applies a drop shadow to the card.
            glass: Applies a glassmorphism effect to the card.
            dasharray: Applies a dashed border style (e.g., "5,5").
            gradient_bg: Applies a linear gradient background (comma-separated colors).
        """
        card_id = self.infographic.add_card(element_id, title, value, subtitle, body, left, top, width, height, shape, bg_color, border_color, border_width, rx, title_color, value_color, subtitle_color, body_color, auto_fit_text, url, url_target, url_transition, glow, fade_in, fade_pulse, fade_start_time_ms, fade_duration_ms, shadow, glass, dasharray, gradient_bg, html_body)
        if card_id and (url or glow is not None or fade_in or fade_pulse):
            self.map(card_id, url=url, url_target=url_target, url_transition=url_transition, glow=glow, fade_in=fade_in, fade_pulse=fade_pulse, fade_start_time_ms=fade_start_time_ms, fade_duration_ms=fade_duration_ms)

    def add_scalable_progress_bar(self, element_id: str, progress: float, left: str = "0%", top: str = "0%", width: str = "100%", height: str = "10%", bg_color: str = "#f1f5f9", fill_color: str = "#10b981", rx: str = "4"):
        """
        Automatically generates a perfectly scaled, native SVG progress bar relative to the bounding box
        of a target element.

        Args:
            element_id: The ID or name of the target SVG element (e.g., a card or region) to anchor to.
            progress: The progress value as a float (0.0 to 1.0) or percentage string (e.g., "75%").
            left: The left offset relative to the bounding box (e.g., "10%" or "10").
            top: The top offset relative to the bounding box (e.g., "10%" or "10").
            width: The total width of the progress bar relative to the bounding box (e.g., "80%" or "80").
            height: The height of the progress bar relative to the bounding box (e.g., "10%" or "10").
            bg_color: The color of the background track.
            fill_color: The color of the active progress fill.
            rx: The border radius of the progress bar (in absolute pixels).
        """
        self.infographic.add_scalable_progress_bar(element_id, progress, left, top, width, height, bg_color, fill_color, rx)

    def add_image_overlay(self, element_id: str, image_url: str, object_fit: str = "cover", border_radius: str = "0px", box_shadow: str = "none", offset_x: int = 0, offset_y: int = 0, scale_with_zoom: bool = False):
        """
        A helper method to easily embed responsive images within an SVG element's bounding box without writing custom HTML.

        Args:
            element_id: The ID of the target SVG element.
            image_url: The URL or path to the image.
            object_fit: The CSS object-fit property (e.g., 'cover', 'contain', 'fill'). Default 'cover'.
            border_radius: The CSS border-radius for the image. Default '0px'.
            box_shadow: The CSS box-shadow for the image. Default 'none'.
            offset_x: Pixel offset from the center X.
            offset_y: Pixel offset from the center Y.
            scale_with_zoom: Whether the overlay scales with ECharts zooming.
        """
        self.infographic.add_image_overlay(element_id, image_url, object_fit, border_radius, box_shadow, offset_x, offset_y, scale_with_zoom)

    def clip_html_to_shape(self, element_id: str, html: str, pointer_events: str = "auto", offset_x: float = 0.0, offset_y: float = 0.0):
        """
        Clips raw HTML (such as an iframe or a Folium map) directly to the exact shape of a target SVG element.
        It creates a perfectly-sized HTML overlay that uses the exact SVG path as a CSS mask.
        If `html` is provided and does not begin with an iframe, it will automatically be wrapped in an iframe
        and base64-encoded to prevent CSS/JS clashes with the SIVO DOM environment.

        Args:
            element_id: The ID or name of the target SVG element.
            html: The HTML string to inject.
            pointer_events: CSS pointer-events (e.g., 'auto' to allow interaction, 'none' to pass clicks to SVG).
            offset_x: Additional X offset for the HTML position (in pixels relative to bounding box).
            offset_y: Additional Y offset for the HTML position (in pixels relative to bounding box).
        """
        self.infographic.clip_html_to_shape(element_id, html, pointer_events, offset_x, offset_y)

    def add_image_rect(self, element_id: str, image_url: str, x: str = "0", y: str = "0", width: str = "100", height: str = "100", preserve_aspect_ratio: str = "xMidYMid slice", opacity: float = 1.0):
        """
        Dynamically adds a rectangular `<image>` tag to the SVG canvas. This allows the user to easily inject an image
        at a specific coordinate or size without needing an existing path in the template.

        Args:
            element_id: The ID to assign to the new image element.
            image_url: URL or path to the image.
            x: X coordinate (can be string like '10%' or absolute pixels like '100').
            y: Y coordinate.
            width: Width of the image.
            height: Height of the image.
            preserve_aspect_ratio: SVG preserveAspectRatio attribute (default "xMidYMid slice" for cover).
            opacity: Opacity of the image (0.0 to 1.0).
        """
        attributes = {
            "id": element_id,
            "href": image_url,
            "x": str(x),
            "y": str(y),
            "width": str(width),
            "height": str(height),
            "preserveAspectRatio": preserve_aspect_ratio,
            "opacity": str(opacity)
        }
        self.add_shape("image", attributes)

    def clip_image_to_shape(self, element_id: str, image_url: str, scale: float = 1.0, rotate: float = 0.0, opacity: float = 1.0, preserve_aspect_ratio: str = "xMidYMid slice", offset_x: float = 0.0, offset_y: float = 0.0, translate_x: float = 0.0, translate_y: float = 0.0, use_html_overlay: bool = True, encode_base64: bool = False, fade_in: bool = False, fade_pulse: bool = False, fade_start_time_ms: int = 0, fade_duration_ms: int = 5000):
        """
        Clips an image directly to the exact shape of a target SVG element (e.g., a circle, complex path).
        The image perfectly scales and pans natively with the ECharts vector renderer.

        Args:
            element_id: The ID or name of the target SVG element.
            image_url: The URL or path to the image.
            scale: Scale multiplier for the image (default 1.0).
            rotate: Rotation angle in degrees (default 0.0).
            opacity: Opacity of the image (0.0 to 1.0).
            preserve_aspect_ratio: SVG preserveAspectRatio attribute (default "xMidYMid slice" for cover).
            offset_x: Additional X offset for the mask position over the canvas.
            offset_y: Additional Y offset for the mask position over the canvas.
            translate_x: Panning X offset for the image inside the clipped region (in pixels).
            translate_y: Panning Y offset for the image inside the clipped region (in pixels).
            use_html_overlay: Whether to use an HTML mask overlay (True) or a native SVG `<image>` bounding box injection (False). Use False for microscopic shapes that zoom extremely. Note: Setting this to False does not apply a true SVG `<clipPath>`, it injects a rectangular `<image>` matching the bounding box of the target path.
            encode_base64: Fetches the image and base64 encodes it so it renders immediately.
        """
        if encode_base64 and image_url.startswith('http'):
            image_url = self.fetch_image_base64(image_url)
        base_id = self.infographic.clip_image_to_shape(element_id, image_url, scale, rotate, opacity, preserve_aspect_ratio, offset_x, offset_y, translate_x, translate_y, use_html_overlay, fade_in=fade_in, fade_pulse=fade_pulse, fade_start_time_ms=fade_start_time_ms, fade_duration_ms=fade_duration_ms)
        if base_id and (fade_in or fade_pulse):
            self.map(base_id, fade_in=fade_in, fade_pulse=fade_pulse, fade_start_time_ms=fade_start_time_ms, fade_duration_ms=fade_duration_ms)

    def add_scalable_text(self, target_id: str, text: str, left: str = "0%", top: str = "0%", width: str = "100%", height: str = "20%", font_size: str = "10%", font_weight: str = "normal", font_family: str = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif", color: str = "#000000", align: str = "left", vertical_align: str = "middle", auto_shrink: bool = True, interactive: bool = False, fade_in: bool = False, fade_pulse: bool = False, fade_start_time_ms: int = 0, fade_duration_ms: int = 5000):
        """
        Automatically generates a perfectly scaled, native SVG text element relative to the bounding box
        of a target element, eliminating the need to manually compute absolute x, y, and font sizes.

        Args:
            target_id: The ID or name of the target SVG element (e.g., a card or region) to anchor to.
            text: The text string to inject.
            left: The left offset relative to the bounding box (e.g., "10%" or "10").
            top: The top offset relative to the bounding box (e.g., "10%" or "10").
            width: The width of the text container relative to the bounding box (e.g., "80%" or "80").
            height: The height of the text container relative to the bounding box (e.g., "20%" or "20").
            font_size: The font size relative to the bounding box height (e.g., "10%") or absolute pixels (e.g., "16").
            font_weight: The font weight (e.g., "normal", "bold", "800").
            font_family: The font family.
            color: The text color.
            align: Horizontal alignment ('left', 'center', 'right').
            vertical_align: Vertical alignment ('top', 'middle', 'bottom').
            auto_shrink: Whether to automatically reduce font size if the wrapped text overflows the bottom of the bounding box.
            interactive: Whether the injected text itself should be interactive in ECharts. If False, the ID is stripped from the DOM to prevent hit-testing occlusion.
        """
        import uuid

        target_elem = self.infographic._element_lookup.get(target_id)
        if not target_elem or 'bbox' not in target_elem or not target_elem['bbox']:
            raise ValueError(f"Cannot add scalable text: Element '{target_id}' not found or has no bounding box.")

        bbox = target_elem['bbox']
        bbox_min_x, bbox_min_y, bbox_max_x, bbox_max_y = bbox
        bbox_width = bbox_max_x - bbox_min_x
        bbox_height = bbox_max_y - bbox_min_y

        def _parse_val(val_str, relative_to):
            if isinstance(val_str, (int, float)):
                return float(val_str)
            val_str = str(val_str)
            if val_str.endswith('%'):
                return (float(val_str[:-1]) / 100.0) * relative_to
            return float(val_str)

        abs_left = bbox_min_x + _parse_val(left, bbox_width)
        abs_top = bbox_min_y + _parse_val(top, bbox_height)
        abs_width = _parse_val(width, bbox_width)
        abs_height = _parse_val(height, bbox_height)

        # If font_size is a string ending with %, calculate it against the target's height.
        # Otherwise treat it as a raw number.
        abs_font_size = _parse_val(font_size, bbox_height)

        placeholder_id = f"sivo-native-text-{uuid.uuid4().hex[:8]}"

        shape_opts = {
            "id": placeholder_id,
            "x": str(abs_left),
            "y": str(abs_top),
            "width": str(abs_width),
            "height": str(abs_height),
            "fill": "none",
            "pointer-events": "none",
            "silent": "true"
        }

        self.add_shape("rect", shape_opts)

        self.fill_template_zone(
            element_id=placeholder_id,
            text=text,
            font_size=abs_font_size,
            font_weight=font_weight,
            font_family=font_family,
            color=color,
            align=align,
            vertical_align=vertical_align,
            auto_shrink=auto_shrink,
            interactive=interactive,
            fade_in=fade_in,
            fade_pulse=fade_pulse,
            fade_start_time_ms=fade_start_time_ms,
            fade_duration_ms=fade_duration_ms
        )

    def fill_template_zone(self, element_id: str, text: str, font_size: str | float | int = 24.0, font_weight: str = "normal", font_family: str = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif", color: str = "#000000", align: str = "left", vertical_align: str = "middle", auto_shrink: bool = True, interactive: bool = False, fade_in: bool = False, fade_pulse: bool = False, fade_start_time_ms: int = 0, fade_duration_ms: int = 5000):
        """
        Replaces a placeholder SVG element (like a <rect>) with native, perfectly-scaled SVG text.
        This ensures text scales naturally with the viewBox on all devices (mobile/desktop)
        without relying on floating HTML overlays.

        Args:
            element_id: The ID of the placeholder shape.
            text: The text string to inject.
            font_size: The font size in SVG units or percentage string relative to bounding box height.
            font_weight: The font weight (e.g., 'bold', '700').
            font_family: The font family.
            color: The fill color of the text.
            align: 'left', 'center', or 'right' alignment relative to the placeholder.
            vertical_align: 'top', 'middle', or 'bottom' alignment relative to the placeholder.
            interactive: Whether the injected text itself should be interactive in ECharts. If False, the ID is stripped from the DOM to prevent hit-testing occlusion.
        """
        import lxml.etree as etree

        ns = "http://www.w3.org/2000/svg"
        if None in self.infographic.parser.root.nsmap:
            ns = self.infographic.parser.root.nsmap[None]
        qname = f"{{{ns}}}text"

        # Find the bounding box of the target placeholder
        bbox = None
        target_node = None
        for node in self.infographic.parser.root.iter():
            if node.get("id") == element_id or node.get("name") == element_id:
                target_node = node
                break

        if target_node is None:
            logger.warning(f"Warning: Could not find template zone '{element_id}'. Skipping fill.")
            return

        for elem in self.infographic.parser.process_elements():
            if elem['id'] == element_id or elem['name'] == element_id:
                bbox = elem.get('bbox')
                break

        parsed_font_size = font_size

        if not bbox:
            # Fallback for text nodes or groups without parsed bounding boxes
            try:
                x = float(target_node.get("x", 0))
                y = float(target_node.get("y", 0))
            except (ValueError, TypeError):
                x, y = 0, 0
            text_anchor = target_node.get("text-anchor", "start")

            # Simple override alignment if passed explicitly
            if align == "center": text_anchor = "middle"
            elif align == "right": text_anchor = "end"
            elif align == "left": text_anchor = "start"

            # Parse font size if string. Without a bounding box, a percentage like "100%"
            # has nothing to scale against. Let's default to a sane baseline (e.g., 24.0)
            # or try to extract the original font-size if it's replacing an existing text node.
            if isinstance(parsed_font_size, str) and parsed_font_size.endswith('%'):
                try:
                    # Attempt to read existing font-size attribute
                    existing_fs = target_node.get("font-size", "24px").replace("px", "").replace("pt", "")
                    base_fs = float(existing_fs)
                    pct = float(parsed_font_size[:-1]) / 100.0
                    parsed_font_size = base_fs * pct
                except ValueError:
                    parsed_font_size = 24.0
            else:
                try:
                    parsed_font_size = float(parsed_font_size)
                except ValueError:
                    parsed_font_size = 24.0

            lines = [str(text)]
            start_y = y
            line_height = parsed_font_size * 1.2
        else:
            min_x, min_y, max_x, max_y = bbox
            width = max_x - min_x
            height = max_y - min_y

            # Parse font size with relative scaling if percentage
            if isinstance(parsed_font_size, str) and parsed_font_size.endswith('%'):
                try:
                    parsed_font_size = (float(parsed_font_size[:-1]) / 100.0) * height
                except ValueError:
                    parsed_font_size = 24.0
            else:
                try:
                    parsed_font_size = float(parsed_font_size)
                except ValueError:
                    parsed_font_size = 24.0

            # Calculate horizontal position based on alignment
            text_anchor = "start"
            if align == "center":
                x = min_x + (width / 2)
                text_anchor = "middle"
            elif align == "right":
                x = max_x
                text_anchor = "end"
            else: # left
                x = min_x

            # Text wrapping logic with auto-shrink
            words = str(text).split()
            lines = []
            total_text_height = 0
            line_height = 0

            # Try progressively smaller font sizes until it fits the height, or hits a minimum
            min_font_size = 8.0 # Minimum legible fallback

            while True:
                lines = []
                current_line = []
                max_chars = int(width / (0.6 * parsed_font_size)) if parsed_font_size > 0 else len(str(text))
                if max_chars < 1: max_chars = 1

                for word in words:
                    # If a single word is longer than max_chars, it's going to be tricky.
                    # We'll just append it to its own line.
                    if len(word) > max_chars:
                        if current_line:
                            lines.append(" ".join(current_line))
                            current_line = []
                        lines.append(word)
                    elif len(" ".join(current_line + [word])) <= max_chars:
                        current_line.append(word)
                    else:
                        if current_line:
                            lines.append(" ".join(current_line))
                            current_line = [word]
                        else:
                            lines.append(word)
                            current_line = []

                if current_line:
                    lines.append(" ".join(current_line))

                line_height = parsed_font_size * 1.2
                total_text_height = len(lines) * line_height

                # Break early if we shouldn't shrink, or if text fits, or if font is too small
                if not auto_shrink or total_text_height <= height or parsed_font_size <= min_font_size:
                    break

                # Decrease font size by 5% and retry
                parsed_font_size *= 0.95
                if parsed_font_size < min_font_size:
                    parsed_font_size = min_font_size

            # Calculate vertical position based on alignment and total text height
            if vertical_align == "top":
                start_y = min_y + parsed_font_size
            elif vertical_align == "bottom":
                start_y = max_y - total_text_height + parsed_font_size
            else: # middle
                start_y = min_y + (height / 2) - (total_text_height / 2) + parsed_font_size

        for node in self.infographic.parser.root.iter():
            if node.get("id") == element_id or node.get("name") == element_id:
                # Determine if the target is already a <text> element
                tag = node.tag.split("}")[-1] if "}" in node.tag else node.tag
                if tag == "text":
                    # Directly inject into the existing text element to preserve styles
                    # but override position and text properties
                    node.set("x", str(x))
                    node.set("y", str(start_y))
                    node.set("fill", color)
                    node.set("font-size", f"{parsed_font_size}px")
                    node.set("font-family", font_family)
                    node.set("font-weight", font_weight)
                    node.set("text-anchor", text_anchor)
                    node.set("pointer-events", "none")
                    node.set("silent", "true")

                    # Clear existing text and children
                    node.text = ""
                    for child in list(node):
                        node.remove(child)

                    # Create tspans for each line
                    tspan_qname = f"{{{ns}}}tspan"
                    for i, line_text in enumerate(lines):
                        tspan = etree.Element(tspan_qname)
                        tspan.set("x", str(x))
                        tspan.set("y", str(start_y + i * line_height))
                        tspan.set("pointer-events", "none")
                        tspan.set("silent", "true")
                        tspan.text = line_text
                        node.append(tspan)
                else:
                    # 1. Hide placeholder shape
                    node.set("opacity", "0")
                    node.set("pointer-events", "none")
                    node.set("silent", "true")
                    # Remove ID from placeholder so the text element is the only one
                    if "id" in node.attrib:
                        del node.attrib["id"]
                    if "name" in node.attrib:
                        del node.attrib["name"]

                    # 2. Construct wrapper group and text element
                    g_qname = f"{{{ns}}}g"
                    wrapper_elem = etree.Element(g_qname)
                    wrapper_elem.set("name", element_id)
                    wrapper_elem.set("id", element_id)
                    wrapper_elem.set("class", "sivo-template-text-group")

                    if fade_in or fade_pulse:
                        wrapper_elem.set("opacity", "0")

                    text_elem = etree.Element(qname)
                    text_elem.set("x", str(x))
                    text_elem.set("y", str(start_y))
                    text_elem.set("fill", color)
                    text_elem.set("font-size", f"{parsed_font_size}px")
                    text_elem.set("font-family", font_family)
                    text_elem.set("font-weight", font_weight)
                    text_elem.set("text-anchor", text_anchor)
                    text_elem.set("class", "sivo-template-text")
                    text_elem.set("pointer-events", "none")
                    text_elem.set("silent", "true")

                    # Create tspans for each line
                    tspan_qname = f"{{{ns}}}tspan"
                    for i, line_text in enumerate(lines):
                        tspan = etree.Element(tspan_qname)
                        tspan.set("x", str(x))
                        tspan.set("y", str(start_y + i * line_height))
                        tspan.set("pointer-events", "none")
                        tspan.set("silent", "true")
                        tspan.text = line_text
                        text_elem.append(tspan)

                    wrapper_elem.append(text_elem)

                    # 3. Append as an immediate sibling to inherit exact transform logic
                    parent = node.getparent()
                    if parent is not None:
                        # Insert right after the placeholder
                        idx = parent.index(node)
                        parent.insert(idx + 1, wrapper_elem)
                    else:
                        # Fallback to root
                        self.infographic.parser.root.append(wrapper_elem)

        if not interactive and not fade_in and not fade_pulse:
            # Remove from mappings so it does not become an interactive ECharts region
            self.infographic.mappings.pop(element_id, None)

            # Remove the generated ID from the underlying SVG node so ECharts ignores it entirely for hit-testing
            for node in self.infographic.parser.root.iter():
                if node.get("id") == element_id or node.get("name") == element_id:
                    if "id" in node.attrib:
                        del node.attrib["id"]
                    if "name" in node.attrib:
                        del node.attrib["name"]

        if fade_in or fade_pulse:
            self.map(element_id, fade_in=fade_in, fade_pulse=fade_pulse, fade_start_time_ms=fade_start_time_ms, fade_duration_ms=fade_duration_ms, color=color, hover_color="transparent" if not interactive else None)

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
            "metadata": self.get_metadata(),
            "connections": self.infographic.connections,
            "lock_zoom_out": getattr(self.infographic, "lock_zoom_out", False),
            "default_panel_position": getattr(self.infographic, "default_panel_position", "none"),
            "disable_panel": getattr(self.infographic, "disable_panel", False),
            "panel_width": getattr(self.infographic, "panel_width", None),
            "panel_height": getattr(self.infographic, "panel_height", None),
            "panel_css": getattr(self.infographic, "panel_css", None),
            "disable_resizer": getattr(self.infographic, "disable_resizer", False),
            "disable_tooltips": getattr(self.infographic, "disable_tooltips", False),
            "disable_zoom_controls": getattr(self.infographic, "disable_zoom_controls", False),
            "lock_scroll_bounds": getattr(self.infographic, "lock_scroll_bounds", True),
            "presentation_order": getattr(self.infographic, "presentation_order", None),
            "layout_size": getattr(self.infographic, "layout_size", None),
            "starting_zoom": getattr(self.infographic, "starting_zoom", 1.0),
            "render_mode": getattr(self.infographic, "render_mode", "canvas"),
            "enable_minimap": getattr(self.infographic, "enable_minimap", False),
            "enable_export": getattr(self.infographic, "enable_export", False),
            "lock_canvas": getattr(self.infographic, "lock_canvas", False),
            "fade_unselected": getattr(self.infographic, "fade_unselected", False),
            "theme": getattr(self.infographic, "theme", "light"),
            "enable_search": getattr(self.infographic, "enable_search", False),
            "enable_geocoder": getattr(self.infographic, "enable_geocoder", False),
            "geocode_provider": getattr(self.infographic, "geocode_provider", "nominatim"),
            "geocode_api_key": getattr(self.infographic, "geocode_api_key", None),
            "geocode_country_codes": getattr(self.infographic, "geocode_country_codes", None),
            "geocoder_position": getattr(self.infographic, "geocoder_position", "top-center"),
            "watermark": getattr(self.infographic, "watermark", None),
            "enable_brush_selection": getattr(self.infographic, "enable_brush_selection", False),
            "title": getattr(self.infographic, "title", None),
            "subtitle": getattr(self.infographic, "subtitle", None),
            "attribution": getattr(self.infographic, "attribution", None),
            "enable_fullscreen": getattr(self.infographic, "enable_fullscreen", False),
            "navigation_menu": getattr(self.infographic, "navigation_menu", None),
            "navigation_menu_position": getattr(self.infographic, "navigation_menu_position", "top-right"),
            "enable_share": getattr(self.infographic, "enable_share", False),
            "enable_data_download": getattr(self.infographic, "enable_data_download", False),
            "enable_drawing_tools": getattr(self.infographic, "enable_drawing_tools", False),
            "ambient_effect": getattr(self.infographic, "ambient_effect", None),
            "ambient_speed": getattr(self.infographic, "ambient_speed", 1.0),
            "bounding_coords": getattr(self.infographic, "bounding_coords", None),
            "graphic": getattr(self.infographic, "graphic", None),
            "background_image_url": getattr(self.infographic, "background_image_url", None),
            "border_image_url": getattr(self.infographic, "border_image_url", None),
            "border_image_position": getattr(self.infographic, "border_image_position", "all"),
            "border_image_width": getattr(self.infographic, "border_image_width", "10%"),
            "border_image_opacity": getattr(self.infographic, "border_image_opacity", 1.0),
            "border_image_grayscale": getattr(self.infographic, "border_image_grayscale", False),
            "background_image_opacity": getattr(self.infographic, "background_image_opacity", 1.0),
            "background_image_grayscale": getattr(self.infographic, "background_image_grayscale", False),
            "background_image_fade_in": getattr(self.infographic, "background_image_fade_in", False),
            "background_image_fade_pulse": getattr(self.infographic, "background_image_fade_pulse", False),
            "background_image_fade_start_time_ms": getattr(self.infographic, "background_image_fade_start_time_ms", 0),
            "background_image_fade_duration_ms": getattr(self.infographic, "background_image_fade_duration_ms", 5000),
            "svg_background_image_url": getattr(self.infographic, "svg_background_image_url", None),
            "svg_background_image_opacity": getattr(self.infographic, "svg_background_image_opacity", 1.0),
            "svg_background_image_grayscale": getattr(self.infographic, "svg_background_image_grayscale", False),
            "svg_background_image_insert_after": getattr(self.infographic, "svg_background_image_insert_after", None),
            "transparent_template_lines": getattr(self.infographic, "transparent_template_lines", False)
        }
        if self.infographic.data_binding:
            view_data["data_binding"] = self.infographic.data_binding.model_dump()
        if self.infographic.timeline_binding:
            view_data["timeline_binding"] = self.infographic.timeline_binding.model_dump()
        if hasattr(self.infographic, "geocoder_intersection") and self.infographic.geocoder_intersection:
            view_data["geocoder_intersection"] = self.infographic.geocoder_intersection
        if hasattr(self.infographic, "live_binding") and self.infographic.live_binding:
            view_data["live_binding"] = self.infographic.live_binding.model_dump()
        if hasattr(self.infographic, "api_binding") and self.infographic.api_binding:
            if hasattr(self.infographic.api_binding, "model_dump"):
                view_data["api_binding"] = self.infographic.api_binding.model_dump()
            elif hasattr(self.infographic.api_binding, "dict"):
                view_data["api_binding"] = self.infographic.api_binding.dict()
            else:
                view_data["api_binding"] = self.infographic.api_binding
        if hasattr(self.infographic, "scrollytelling") and self.infographic.scrollytelling:
            view_data["scrollytelling"] = [s.model_dump() for s in self.infographic.scrollytelling]
        if hasattr(self.infographic, "tour") and self.infographic.tour:
            view_data["tour"] = [s.model_dump() for s in self.infographic.tour]
        if hasattr(self.infographic, "layer_toggles") and self.infographic.layer_toggles:
            view_data["layer_toggles"] = [s.model_dump() for s in self.infographic.layer_toggles]
        if hasattr(self.infographic, "scratchoff") and self.infographic.scratchoff:
            view_data["scratchoff"] = self.infographic.scratchoff
        if hasattr(self.infographic, "proportional_symbols") and self.infographic.proportional_symbols:
            view_data["proportional_symbols"] = self.infographic.proportional_symbols
        if hasattr(self.infographic, "spike_map") and self.infographic.spike_map:
            view_data["spike_map"] = self.infographic.spike_map
        if hasattr(self.infographic, "hexbin") and self.infographic.hexbin:
            view_data["hexbin"] = self.infographic.hexbin
        if hasattr(self.infographic, "dot_density") and self.infographic.dot_density:
            view_data["dot_density"] = self.infographic.dot_density
        return view_data

    def audit_a11y(self) -> None:
        """
        Runs an accessibility audit on the mapped elements of this SIVO instance,
        checking for tap target sizes and color contrast against WCAG 2.2 guidelines.
        Warnings are logged to the console.
        """
        if not self.infographic or not self.infographic.parser:
            return

        # Attempt to determine a base background color from the layout
        bg_color = "#ffffff"  # Default to white
        if self.infographic.theme == "dark":
            bg_color = "#121212" # Echarts dark theme default background

        logger.info("Running SIVO Accessibility (A11y) Audit...")
        warnings_found = 0

        # We need the parsed SVG elements to get bounding boxes and colors
        # The parser tree should already be built
        parser = self.infographic.parser

        for elem in parser.root.iter():
            elem_id = elem.get('id')
            elem_name = elem.get('name')

            # Check if this element is mapped and interactive
            target_id = elem_name if elem_name else elem_id

            if target_id and target_id in self.infographic.mappings:
                mapping = self.infographic.mappings[target_id]

                # Check if it has any interactive actions (clicks, hovers, etc)
                is_interactive = len([a for a in mapping.actions if a.action_type not in ('a11y', 'tooltip')]) > 0

                if is_interactive:
                    from ..svg.metadata import get_bounding_box
                    bbox = get_bounding_box(elem)

                    # 1. Check Tap Target Size
                    tap_warnings = audit_tap_target(target_id, bbox)
                    for w in tap_warnings:
                        logger.warning(w)
                        warnings_found += 1

                    # 2. Check Color Contrast
                    contrast_warnings = audit_contrast(target_id, elem, bg_color)
                    for w in contrast_warnings:
                        logger.warning(w)
                        warnings_found += 1

        if warnings_found == 0:
            logger.info("✅ A11y Audit Passed: No WCAG 2.2 violations detected for interactive elements.")
        else:
            logger.warning(f"⚠️ A11y Audit Completed: {warnings_found} warning(s) found.")

    def to_html(self, output_path: Optional[str] = None, custom_css: Optional[str] = None, custom_js: Optional[str] = None) -> str:
        """
        Generates the interactive HTML string (bundle) containing the ECharts map,
        Jinja2 template, and mapped behaviors. Optionally saves to a file.
        """
        if getattr(self.infographic, 'enable_a11y', False):
            self.audit_a11y()

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

    def to_svg(self, output_path: Optional[str] = None) -> str:
        """
        Returns the processed SVG as a string.
        Optionally saves it directly to a file if output_path is provided.
        """
        svg_str = self.infographic.parser.to_string()
        if output_path:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(svg_str)
        return svg_str

    def to_html_compare(self, other_sivo: 'Sivo', output_path: Optional[str] = None, custom_css: Optional[str] = None, custom_js: Optional[str] = None) -> str:
        """
        Generates a specialized interactive HTML string that renders TWO Sivo canvases
        with a native before/after drag slider separating them natively.
        """
        from ..runtime.bundle_generator import generate_echarts_html

        view1_data = self._get_view_data()
        view2_data = other_sivo._get_view_data()

        # We flag this specifically for the template to know we are in comparison mode
        views_data = {
            "compare_left": view1_data,
            "compare_right": view2_data
        }

        return generate_echarts_html(
            views_data=views_data,
            initial_view="compare_mode", # Special keyword for the template
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
