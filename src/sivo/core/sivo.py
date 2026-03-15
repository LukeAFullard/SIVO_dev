from typing import Dict, Optional, Union, List, Any

from .config import ProjectConfig
from .infographic import Infographic

class Sivo:
    """
    SIVO (SVG Interactive Vector Objects) Orchestrator.
    This class serves as the primary declarative Python API for the framework,
    hiding JavaScript complexity and managing the Infographic lifecycle.
    """
    def __init__(self, infographic: Infographic, default_panel_position: str = "right", disable_panel: bool = False, panel_width: Optional[str] = None, panel_height: Optional[str] = None, disable_resizer: bool = False, disable_tooltips: bool = False, disable_zoom_controls: bool = False, lock_zoom_out: bool = False, lock_canvas: bool = False, enable_a11y: bool = False, render_mode: str = "canvas", enable_minimap: bool = False, enable_export: bool = False, fade_unselected: bool = False, theme: str = "light", enable_search: bool = False, watermark: Optional[str] = None, enable_brush_selection: bool = False, title: Optional[str] = None, subtitle: Optional[str] = None, attribution: Optional[str] = None, enable_fullscreen: bool = False, enable_share: bool = False, enable_data_download: bool = False, enable_drawing_tools: bool = False, ambient_effect: Optional[str] = None, bounding_coords: Optional[list[list[float]]] = None, graphic: Optional[list[dict]] = None):
        self.infographic = infographic
        self.infographic.default_panel_position = default_panel_position
        self.infographic.disable_panel = disable_panel
        self.infographic.panel_width = panel_width
        self.infographic.panel_height = panel_height
        self.infographic.disable_resizer = disable_resizer
        self.infographic.disable_tooltips = disable_tooltips
        self.infographic.disable_zoom_controls = disable_zoom_controls
        self.infographic.lock_zoom_out = lock_zoom_out
        self.infographic.enable_a11y = enable_a11y
        self.infographic.render_mode = render_mode
        self.infographic.enable_minimap = enable_minimap
        self.infographic.enable_export = enable_export
        self.infographic.lock_canvas = lock_canvas
        self.infographic.fade_unselected = fade_unselected
        self.infographic.theme = theme
        self.infographic.enable_search = enable_search
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
        self.infographic.bounding_coords = bounding_coords
        self.infographic.graphic = graphic

    @classmethod
    def from_svg(cls, filepath: str, default_panel_position: str = "right", disable_panel: bool = False, panel_width: Optional[str] = None, panel_height: Optional[str] = None, disable_resizer: bool = False, disable_tooltips: bool = False, disable_zoom_controls: bool = False, lock_zoom_out: bool = False, lock_canvas: bool = False, enable_a11y: bool = False, render_mode: str = "canvas", enable_minimap: bool = False, enable_export: bool = False, fade_unselected: bool = False, theme: str = "light", enable_search: bool = False, watermark: Optional[str] = None, enable_brush_selection: bool = False, title: Optional[str] = None, subtitle: Optional[str] = None, attribution: Optional[str] = None, enable_fullscreen: bool = False, enable_share: bool = False, enable_data_download: bool = False, enable_drawing_tools: bool = False, ambient_effect: Optional[str] = None, bounding_coords: Optional[list[list[float]]] = None, graphic: Optional[list[dict]] = None) -> "Sivo":
        """Initializes a Sivo instance from an SVG file path."""
        info = Infographic.from_svg(filepath)
        return cls(info, default_panel_position=default_panel_position, disable_panel=disable_panel, panel_width=panel_width, panel_height=panel_height, disable_resizer=disable_resizer, disable_tooltips=disable_tooltips, disable_zoom_controls=disable_zoom_controls, lock_zoom_out=lock_zoom_out, lock_canvas=lock_canvas, enable_a11y=enable_a11y, render_mode=render_mode, enable_minimap=enable_minimap, enable_export=enable_export, fade_unselected=fade_unselected, theme=theme, enable_search=enable_search, watermark=watermark, enable_brush_selection=enable_brush_selection, title=title, subtitle=subtitle, attribution=attribution, enable_fullscreen=enable_fullscreen, enable_share=enable_share, enable_data_download=enable_data_download, enable_drawing_tools=enable_drawing_tools, ambient_effect=ambient_effect, bounding_coords=bounding_coords, graphic=graphic)

    @classmethod
    def from_template(cls, template_name: str, default_panel_position: str = "right", disable_panel: bool = False, panel_width: Optional[str] = None, panel_height: Optional[str] = None, disable_resizer: bool = False, disable_tooltips: bool = False, disable_zoom_controls: bool = False, lock_zoom_out: bool = False, lock_canvas: bool = False, enable_a11y: bool = False, render_mode: str = "canvas", enable_minimap: bool = False, enable_export: bool = False, fade_unselected: bool = False, theme: str = "light", enable_search: bool = False, watermark: Optional[str] = None, enable_brush_selection: bool = False, title: Optional[str] = None, subtitle: Optional[str] = None, attribution: Optional[str] = None, enable_fullscreen: bool = False, enable_share: bool = False, enable_data_download: bool = False, enable_drawing_tools: bool = False, ambient_effect: Optional[str] = None, bounding_coords: Optional[list[list[float]]] = None, graphic: Optional[list[dict]] = None) -> "Sivo":
        """
        Initializes a Sivo instance from a bundled built-in template SVG.
        Available templates: 'dashboard', 'timeline'
        """
        import os
        template_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "templates")
        filepath = os.path.join(template_dir, f"{template_name}_template.svg")
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Template '{template_name}' not found. Looked in {template_dir}")
        return cls.from_svg(filepath, default_panel_position=default_panel_position, disable_panel=disable_panel, panel_width=panel_width, panel_height=panel_height, disable_resizer=disable_resizer, disable_tooltips=disable_tooltips, disable_zoom_controls=disable_zoom_controls, lock_zoom_out=lock_zoom_out, lock_canvas=lock_canvas, enable_a11y=enable_a11y, render_mode=render_mode, enable_minimap=enable_minimap, enable_export=enable_export, fade_unselected=fade_unselected, theme=theme, enable_search=enable_search, watermark=watermark, enable_brush_selection=enable_brush_selection, title=title, subtitle=subtitle, attribution=attribution, enable_fullscreen=enable_fullscreen, enable_share=enable_share, enable_data_download=enable_data_download, enable_drawing_tools=enable_drawing_tools, ambient_effect=ambient_effect, bounding_coords=bounding_coords, graphic=graphic)

    @classmethod
    def from_string(cls, svg_string: str, default_panel_position: str = "right", disable_panel: bool = False, panel_width: Optional[str] = None, panel_height: Optional[str] = None, disable_resizer: bool = False, disable_tooltips: bool = False, disable_zoom_controls: bool = False, lock_zoom_out: bool = False, lock_canvas: bool = False, enable_a11y: bool = False, render_mode: str = "canvas", enable_minimap: bool = False, enable_export: bool = False, fade_unselected: bool = False, theme: str = "light", enable_search: bool = False, watermark: Optional[str] = None, enable_brush_selection: bool = False, title: Optional[str] = None, subtitle: Optional[str] = None, attribution: Optional[str] = None, enable_fullscreen: bool = False, enable_share: bool = False, enable_data_download: bool = False, enable_drawing_tools: bool = False, ambient_effect: Optional[str] = None, bounding_coords: Optional[list[list[float]]] = None, graphic: Optional[list[dict]] = None) -> "Sivo":
        """Initializes a Sivo instance directly from an SVG string."""
        info = Infographic.from_string(svg_string)
        return cls(info, default_panel_position=default_panel_position, disable_panel=disable_panel, panel_width=panel_width, panel_height=panel_height, disable_resizer=disable_resizer, disable_tooltips=disable_tooltips, disable_zoom_controls=disable_zoom_controls, lock_zoom_out=lock_zoom_out, lock_canvas=lock_canvas, enable_a11y=enable_a11y, render_mode=render_mode, enable_minimap=enable_minimap, enable_export=enable_export, fade_unselected=fade_unselected, theme=theme, enable_search=enable_search, watermark=watermark, enable_brush_selection=enable_brush_selection, title=title, subtitle=subtitle, attribution=attribution, enable_fullscreen=enable_fullscreen, enable_share=enable_share, enable_data_download=enable_data_download, enable_drawing_tools=enable_drawing_tools, ambient_effect=ambient_effect, bounding_coords=bounding_coords, graphic=graphic)

    @classmethod
    def from_geodataframe(cls, gdf: Any, id_col: str, name_col: Optional[str] = None, default_panel_position: str = "right", disable_panel: bool = False, panel_width: Optional[str] = None, panel_height: Optional[str] = None, disable_resizer: bool = False, disable_tooltips: bool = False, disable_zoom_controls: bool = False, lock_zoom_out: bool = False, lock_canvas: bool = False, enable_a11y: bool = False, render_mode: str = "canvas", enable_minimap: bool = False, enable_export: bool = False, fade_unselected: bool = False, theme: str = "light", enable_search: bool = False, watermark: Optional[str] = None, enable_brush_selection: bool = False, title: Optional[str] = None, subtitle: Optional[str] = None, attribution: Optional[str] = None, enable_fullscreen: bool = False, enable_share: bool = False, enable_data_download: bool = False, enable_drawing_tools: bool = False, ambient_effect: Optional[str] = None, bounding_coords: Optional[list[list[float]]] = None) -> "Sivo":
        """
        Initializes a Sivo instance directly from a geopandas GeoDataFrame.
        Automatically converts geometries to SVG paths, assigns IDs and Names,
        and sets bounding coordinates for native geographical projection mapping.
        """
        if name_col is None:
            name_col = id_col

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

        return cls.from_string(svg_str, default_panel_position=default_panel_position, disable_panel=disable_panel, panel_width=panel_width, panel_height=panel_height, disable_resizer=disable_resizer, disable_tooltips=disable_tooltips, disable_zoom_controls=disable_zoom_controls, lock_zoom_out=lock_zoom_out, lock_canvas=lock_canvas, enable_a11y=enable_a11y, render_mode=render_mode, enable_minimap=enable_minimap, enable_export=enable_export, fade_unselected=fade_unselected, theme=theme, enable_search=enable_search, watermark=watermark, enable_brush_selection=enable_brush_selection, title=title, subtitle=subtitle, attribution=attribution, enable_fullscreen=enable_fullscreen, enable_share=enable_share, enable_data_download=enable_data_download, enable_drawing_tools=enable_drawing_tools, ambient_effect=ambient_effect, bounding_coords=bounding_coords)

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
            disable_resizer=getattr(info, "disable_resizer", False),
            disable_tooltips=getattr(info, "disable_tooltips", False),
            disable_zoom_controls=getattr(info, "disable_zoom_controls", False),
            lock_zoom_out=info.lock_zoom_out,
            enable_a11y=info.enable_a11y,
            render_mode=info.render_mode,
            enable_minimap=info.enable_minimap,
            enable_export=info.enable_export,
            lock_canvas=getattr(info, "lock_canvas", False),
            fade_unselected=info.fade_unselected,
            theme=info.theme,
            enable_search=info.enable_search,
            watermark=info.watermark,
            enable_brush_selection=info.enable_brush_selection,
            title=getattr(info, "title", None),
            subtitle=getattr(info, "subtitle", None),
            attribution=getattr(info, "attribution", None),
            enable_fullscreen=getattr(info, "enable_fullscreen", False),
            enable_share=getattr(info, "enable_share", False),
            enable_data_download=getattr(info, "enable_data_download", False),
            enable_drawing_tools=getattr(info, "enable_drawing_tools", False),
            ambient_effect=getattr(info, "ambient_effect", None),
            bounding_coords=getattr(info, "bounding_coords", None),
            graphic=getattr(info, "graphic", None)
        )

    def map(
        self,
        element_id: str,
        aria_label: Optional[str] = None,
        role: Optional[str] = None,
        tabindex: Optional[str] = None,
        tooltip: Optional[str] = None,
        html: Optional[str] = None,
        url: Optional[str] = None,
        drill_to: Optional[str] = None,
        drill_through: Optional[str] = None,
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
        replit: Optional[str] = None,
        echarts_option: Optional[dict] = None,
        map_name: Optional[str] = None,
        map_data: Optional[Union[str, dict]] = None,
        context_menu: Optional[list[dict]] = None,
        panel_position: Optional[str] = None,
        open_by_default: bool = False,
        zoom_on_click: bool = False,
        zoom_level: float = 2.0,
        draggable: bool = False,
        color: Optional[str] = None,
        hover_color: Optional[str] = None,
        fill_gradient: Optional[dict] = None,
        fill_pattern: Optional[dict] = None,
        border_width: Optional[float] = None,
        border_color: Optional[str] = None,
        glow: Optional[bool] = None,
        animation: Optional[str] = None,
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
            drill_to=drill_to,
            drill_through=drill_through,
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
            replit=replit,
            echarts_option=echarts_option,
            map_name=map_name,
            map_data=map_data,
            context_menu=context_menu,
            panel_position=panel_position,
            open_by_default=open_by_default,
            zoom_on_click=zoom_on_click,
            zoom_level=zoom_level,
            draggable=draggable,
            color=color,
            hover_color=hover_color,
            fill_gradient=fill_gradient,
            fill_pattern=fill_pattern,
            border_width=border_width,
            border_color=border_color,
            glow=glow,
            animation=animation,
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
        Available styles: 'dark_mode', 'minimalist', 'cyberpunk', 'glassmorphism', 'neon'.
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

        else:
            raise ValueError(f"Unknown template style: '{style_name}'. Supported styles: dark_mode, minimalist, cyberpunk, glassmorphism, neon.")

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

    def bind_api(self, url: str, polling_interval_ms: int = 5000, method: str = "GET", headers: Optional[Dict[str, str]] = None, payload: Optional[dict] = None, data_path: Optional[str] = None):
        """
        Binds an API endpoint for live UI updates via polling.
        """
        self.infographic.bind_api(url, polling_interval_ms, method, headers, payload, data_path)

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

    def map_bar_chart(self, element_id: str, title: str, data: list, categories: list, color: str | list[str] = "#43a2ca", tooltip: str = None, panel_position: str = None, title_color: str = None, title_size: int = None, axis_color: str = None, axis_size: int = None, tooltip_bg_color: str = None, grid_margin: list[int] = None, universal_transition: bool = True, datazoom: bool = False, extra_options: dict = None):
        """Helper to map a Bar Chart with extensive styling and morphing controls. 'color' can be a string or a list of strings (palette)."""
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
        """Helper to map a Scatter Chart with an overlaid trendline. trendline_type can be 'linear', 'exponential', 'logarithmic', 'polynomial'. data: [[x1, y1], [x2, y2]]"""

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

    def map_pictorial_bar_chart(self, element_id: str, title: str, data: list, categories: list, symbol: str, symbol_repeat: bool | str = True, symbol_size: list | int | str = ['100%', '100%'], color: str | list[str] = "#43a2ca", tooltip: str = None, panel_position: str = None, title_color: str = None, title_size: int = None, axis_color: str = None, axis_size: int = None, tooltip_bg_color: str = None, grid_margin: list[int] = None, universal_transition: bool = True, datazoom: bool = False, extra_options: dict = None):
        """Helper to map a Pictorial Bar Chart. 'symbol' can be 'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow', 'none', an image URL ('image://url'), or an SVG path ('path://...')."""
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
        """Helper to map a Line Chart with extensive styling and morphing controls. 'color' can be a string or a list of strings (palette)."""

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
        """Helper to map a Pie Chart. data format: [{"name": "A", "value": 10}, ...] 'color' can be a list of strings (palette)."""
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
        """Helper to map a Gauge Chart."""
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
        """Helper to map a Radar Chart. indicators: [{'name': 'A', 'max': 100}], data: [{'name': 'Series 1', 'value': [10, 20]}]"""
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
        """Helper to map a Scatter Chart. data: [[x1, y1], [x2, y2]]"""
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
        Helper to map a nested Map Chart inside the side panel.
        `map_data` can be an SVG string or a GeoJSON dictionary.
        `data`: [{'name': 'RegionA', 'value': 10}]
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
        """Helper to map a Treemap Chart. data: [{'name': 'node1', 'value': 10, 'children': [...]}]"""
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

    def map_polar_bar_chart(self, element_id: str, title: str, data: list[float], categories: list[str], color: str | list[str] = "#43a2ca", tooltip: str = None, panel_position: str = None, title_color: str = None, title_size: int = None, axis_color: str = None, axis_size: int = None, tooltip_bg_color: str = None, universal_transition: bool = True, datazoom: bool = False, extra_options: dict = None):
        """Helper to map a Polar Bar Chart. data: [10, 20, 30] corresponding to categories."""
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
        """Helper to map a Polar Line Chart (often used for math functions or cyclical data). data: list of values."""
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
        """Helper to map a Polar Scatter Chart. data: [[radius, angle], ...]"""
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
        """Helper to map a Liquid Fill Chart. data: [0.6, 0.5] (percentages as floats between 0 and 1).
        Note: Requires echarts-liquidfill plugin."""
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
        """Helper to map a Custom Series Chart.
        render_item_js must be a string containing a valid JavaScript function for the 'renderItem' property.
        Since JSON serialization cannot pass raw JS functions, we pass it as a special _sivo_render_item string
        which the HTML runtime will `eval()` during option generation.
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
        """Helper to map a Boxplot Chart. data is a 2D array of values for each category."""
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
        """Helper to map a Candlestick Chart (K-line). data: [[open, close, lowest, highest], ...]"""
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
        """Helper to map a Word Cloud Chart. data: [{'name': 'Word', 'value': 100}, ...]
        mask_image: Optional URL or base64 string to a silhouette image (black and white) to constrain the word cloud shape.
        Note: Requires echarts-wordcloud plugin (included by default in SIVO CDN templates)."""
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
        """Helper to map a Calendar Heatmap Chart. data: [['2017-01-01', 10], ['2017-01-02', 20], ...], calendar_range: '2017' or ['2017-01-01', '2017-12-31']"""
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
        """Helper to map a Cartesian Heatmap Chart. data: [[x_index, y_index, value], ...]"""
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
        """Helper to map a Graph Chart (Network). nodes: [{'name': 'Node1'}], links: [{'source': 'Node1', 'target': 'Node2'}]. layout can be 'none', 'circular', or 'force'."""
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
        """Helper to map a Sankey Diagram. nodes: [{'name': 'A'}], links: [{'source': 'A', 'target': 'B', 'value': 10}]"""
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
        """Helper to map a Sunburst Chart. data: [{'name': 'A', 'value': 10, 'children': [...]}]"""
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
        """Helper to map a Parallel Coordinates Chart. schema: [{'dim': 0, 'name': 'A'}, ...], data: [[val1, val2], ...]"""
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
        """Helper to map a ThemeRiver (Streamgraph) Chart. data: [[date, value, category_name], ...]"""
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
        """Helper to map an Effect Scatter Chart. data: [[x1, y1], [x2, y2]]"""
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
        """Helper to map a Lines Chart. data: [{'coords': [[lng1, lat1], [lng2, lat2]]}]"""
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
        """Helper to map a Funnel Chart. data: [{'value': 60, 'name': 'Visit'}]"""
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
        """Helper to map a Tree Chart. data: [{'name': 'Root', 'children': [...]}]"""
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
        import subprocess
        import os
        print(f"SIVO Build System: Bundling JS assets from {entry_point} -> {output_dir}")
        if not os.path.exists("package.json"):
            print("Warning: package.json not found. Generating default package.json for esbuild...")
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
            print("Running 'npm install'...")
            subprocess.run(["npm", "install"], check=True)
            print("Running 'npm run build'...")
            subprocess.run(["npm", "run", "build"], check=True)
            self.infographic.build_js = True
            print(f"Successfully bundled JS to {output_dir}/sivo.min.js")
        except FileNotFoundError:
            print("Error: npm or node not found in PATH. Please install Node.js to use JS bundling.")
        except subprocess.CalledProcessError as e:
            print(f"Build failed: {e}")

    def apply_choropleth(self, data_map: Dict[str, float], min_color: str = "#ffffff", max_color: str = "#ff0000", show_legend: bool = True):
        """
        Generates a choropleth map by interpolating colors based on a numeric data mapping.
        """
        self.infographic.apply_choropleth(data_map, min_color, max_color, show_legend)

    def add_connection(self, source_id: str, target_id: str, label: str = "", color: str = "#ff3333", width: float = 2.0, animation_speed: float = 3.0, type: str = "solid", opacity: float = 0.6, flow_effect: bool = False, effect_symbol: str = "circle", effect_size: float = 3.0):
        """
        Draws a visual connection line between the centers of two SVG elements.
        """
        self.infographic.add_connection(source_id, target_id, label, color, width, animation_speed, type, opacity, flow_effect, effect_symbol, effect_size)

    def fill_template_zone(self, element_id: str, text: str, font_size: int = 24, font_weight: str = "normal", font_family: str = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif", color: str = "#000000", align: str = "left", vertical_align: str = "middle"):
        """
        Replaces a placeholder SVG element (like a <rect>) with native, perfectly-scaled SVG text.
        This ensures text scales naturally with the viewBox on all devices (mobile/desktop)
        without relying on floating HTML overlays.

        Args:
            element_id: The ID of the placeholder shape.
            text: The text string to inject.
            font_size: The font size in SVG units.
            font_weight: The font weight (e.g., 'bold', '700').
            font_family: The font family.
            color: The fill color of the text.
            align: 'left', 'center', or 'right' alignment relative to the placeholder.
            vertical_align: 'top', 'middle', or 'bottom' alignment relative to the placeholder.
        """
        # Find the bounding box of the target placeholder
        bbox = None
        for elem in self.infographic.parser.process_elements():
            if elem['id'] == element_id or elem['name'] == element_id:
                bbox = elem.get('bbox')
                break

        if not bbox:
            print(f"Warning: Could not find template zone '{element_id}'. Skipping fill.")
            return

        min_x, min_y, max_x, max_y = bbox
        width = max_x - min_x
        height = max_y - min_y

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

        # Calculate vertical position based on alignment (SVG text is positioned by baseline)
        if vertical_align == "top":
            y = min_y + font_size
        elif vertical_align == "bottom":
            y = max_y
        else: # middle
            # Rough approximation to center the text baseline vertically in the box
            y = min_y + (height / 2) + (font_size / 3)

        import lxml.etree as etree

        # Hide the original placeholder shape and inject the text node exactly in the same DOM location
        # This ensures the text inherits any <g transform="..."> translation matrices naturally.
        ns = "http://www.w3.org/2000/svg"
        if None in self.infographic.parser.root.nsmap:
            ns = self.infographic.parser.root.nsmap[None]

        qname = f"{{{ns}}}text"

        for node in self.infographic.parser.root.iter():
            if node.get("id") == element_id or node.get("name") == element_id:
                # 1. Hide placeholder
                node.set("opacity", "0")
                node.set("pointer-events", "none")

                # 2. Construct text element
                text_elem = etree.Element(qname)
                text_elem.set("x", str(x))
                text_elem.set("y", str(y))
                text_elem.set("fill", color)
                text_elem.set("font-size", f"{font_size}px")
                text_elem.set("font-family", font_family)
                text_elem.set("font-weight", font_weight)
                text_elem.set("text-anchor", text_anchor)
                text_elem.set("class", "sivo-template-text")
                text_elem.text = text

                # 3. Append as an immediate sibling to inherit exact transform logic
                parent = node.getparent()
                if parent is not None:
                    # Insert right after the placeholder
                    idx = parent.index(node)
                    parent.insert(idx + 1, text_elem)
                else:
                    # Fallback to root
                    self.infographic.parser.root.append(text_elem)

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
            "connections": self.infographic.connections,
            "lock_zoom_out": getattr(self.infographic, "lock_zoom_out", False),
            "disable_panel": getattr(self.infographic, "disable_panel", False),
            "panel_width": getattr(self.infographic, "panel_width", None),
            "panel_height": getattr(self.infographic, "panel_height", None),
            "disable_resizer": getattr(self.infographic, "disable_resizer", False),
            "disable_tooltips": getattr(self.infographic, "disable_tooltips", False),
            "disable_zoom_controls": getattr(self.infographic, "disable_zoom_controls", False),
            "render_mode": getattr(self.infographic, "render_mode", "canvas"),
            "enable_minimap": getattr(self.infographic, "enable_minimap", False),
            "enable_export": getattr(self.infographic, "enable_export", False),
            "lock_canvas": getattr(self.infographic, "lock_canvas", False),
            "fade_unselected": getattr(self.infographic, "fade_unselected", False),
            "theme": getattr(self.infographic, "theme", "light"),
            "enable_search": getattr(self.infographic, "enable_search", False),
            "watermark": getattr(self.infographic, "watermark", None),
            "enable_brush_selection": getattr(self.infographic, "enable_brush_selection", False),
            "title": getattr(self.infographic, "title", None),
            "subtitle": getattr(self.infographic, "subtitle", None),
            "attribution": getattr(self.infographic, "attribution", None),
            "enable_fullscreen": getattr(self.infographic, "enable_fullscreen", False),
            "enable_share": getattr(self.infographic, "enable_share", False),
            "enable_data_download": getattr(self.infographic, "enable_data_download", False),
            "enable_drawing_tools": getattr(self.infographic, "enable_drawing_tools", False),
            "ambient_effect": getattr(self.infographic, "ambient_effect", None),
            "bounding_coords": getattr(self.infographic, "bounding_coords", None),
            "graphic": getattr(self.infographic, "graphic", None)
        }
        if self.infographic.data_binding:
            view_data["data_binding"] = self.infographic.data_binding.model_dump()
        if self.infographic.timeline_binding:
            view_data["timeline_binding"] = self.infographic.timeline_binding.model_dump()
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
        if hasattr(self.infographic, "hexbin") and self.infographic.hexbin:
            view_data["hexbin"] = self.infographic.hexbin
        if hasattr(self.infographic, "dot_density") and self.infographic.dot_density:
            view_data["dot_density"] = self.infographic.dot_density
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
