from typing import Dict, Optional, Union

from .config import ProjectConfig
from .infographic import Infographic

class Sivo:
    """
    SIVO (SVG Interactive Vector Objects) Orchestrator.
    This class serves as the primary declarative Python API for the framework,
    hiding JavaScript complexity and managing the Infographic lifecycle.
    """
    def __init__(self, infographic: Infographic, default_panel_position: str = "right", lock_zoom_out: bool = False, enable_a11y: bool = False, render_mode: str = "canvas", enable_minimap: bool = False, enable_export: bool = False, fade_unselected: bool = False, theme: str = "light", enable_search: bool = False, watermark: Optional[str] = None, enable_brush_selection: bool = False):
        self.infographic = infographic
        self.infographic.default_panel_position = default_panel_position
        self.infographic.lock_zoom_out = lock_zoom_out
        self.infographic.enable_a11y = enable_a11y
        self.infographic.render_mode = render_mode
        self.infographic.enable_minimap = enable_minimap
        self.infographic.enable_export = enable_export
        self.infographic.fade_unselected = fade_unselected
        self.infographic.theme = theme
        self.infographic.enable_search = enable_search
        self.infographic.watermark = watermark
        self.infographic.enable_brush_selection = enable_brush_selection

    @classmethod
    def from_svg(cls, filepath: str, default_panel_position: str = "right", lock_zoom_out: bool = False, enable_a11y: bool = False, render_mode: str = "canvas", enable_minimap: bool = False, enable_export: bool = False, fade_unselected: bool = False, theme: str = "light", enable_search: bool = False, watermark: Optional[str] = None, enable_brush_selection: bool = False) -> "Sivo":
        """Initializes a Sivo instance from an SVG file path."""
        info = Infographic.from_svg(filepath)
        return cls(info, default_panel_position=default_panel_position, lock_zoom_out=lock_zoom_out, enable_a11y=enable_a11y, render_mode=render_mode, enable_minimap=enable_minimap, enable_export=enable_export, fade_unselected=fade_unselected, theme=theme, enable_search=enable_search, watermark=watermark, enable_brush_selection=enable_brush_selection)

    @classmethod
    def from_string(cls, svg_string: str, default_panel_position: str = "right", lock_zoom_out: bool = False, enable_a11y: bool = False, render_mode: str = "canvas", enable_minimap: bool = False, enable_export: bool = False, fade_unselected: bool = False, theme: str = "light", enable_search: bool = False, watermark: Optional[str] = None, enable_brush_selection: bool = False) -> "Sivo":
        """Initializes a Sivo instance directly from an SVG string."""
        info = Infographic.from_string(svg_string)
        return cls(info, default_panel_position=default_panel_position, lock_zoom_out=lock_zoom_out, enable_a11y=enable_a11y, render_mode=render_mode, enable_minimap=enable_minimap, enable_export=enable_export, fade_unselected=fade_unselected, theme=theme, enable_search=enable_search, watermark=watermark, enable_brush_selection=enable_brush_selection)

    @classmethod
    def from_config(cls, config: Union[str, dict, ProjectConfig], base_dir: str = ".") -> "Sivo":
        """
        Creates a Sivo instance from a configuration file, dictionary, or ProjectConfig object.
        """
        info = Infographic.from_config(config, base_dir=base_dir)
        return cls(
            info,
            default_panel_position=info.default_panel_position,
            lock_zoom_out=info.lock_zoom_out,
            enable_a11y=info.enable_a11y,
            render_mode=info.render_mode,
            enable_minimap=info.enable_minimap,
            enable_export=info.enable_export,
            fade_unselected=info.fade_unselected,
            theme=info.theme,
            enable_search=info.enable_search,
            watermark=info.watermark,
            enable_brush_selection=info.enable_brush_selection
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

    def bind_timeline(self, data: Dict[str, Dict[str, Dict[str, float]]], key: str, colors: list, min_val: float, max_val: float, auto_play: bool = True, play_interval: int = 1000):
        """
        Binds quantitative time-series data to SVG IDs dynamically and animates a color scale over time.
        """
        self.infographic.bind_timeline(data, key, colors, min_val, max_val, auto_play, play_interval)

    def bind_live(self, url: str, topic: str, auth_token: Optional[str] = None):
        """
        Binds a WebSocket/PubSub connection to dynamically mutate the ECharts canvas based on live
        telemetry data, completely bypassing Streamlit re-renders.
        """
        self.infographic.bind_live(url, topic, auth_token)

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

    def add_connection(self, source_id: str, target_id: str, label: str = "", color: str = "#ff3333", width: float = 2.0, animation_speed: float = 3.0, type: str = "solid", opacity: float = 0.6):
        """
        Draws a visual connection line between the centers of two SVG elements.
        """
        self.infographic.add_connection(source_id, target_id, label, color, width, animation_speed, type, opacity)

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
            "render_mode": getattr(self.infographic, "render_mode", "canvas"),
            "enable_minimap": getattr(self.infographic, "enable_minimap", False),
            "enable_export": getattr(self.infographic, "enable_export", False),
            "fade_unselected": getattr(self.infographic, "fade_unselected", False),
            "theme": getattr(self.infographic, "theme", "light"),
            "enable_search": getattr(self.infographic, "enable_search", False),
            "watermark": getattr(self.infographic, "watermark", None),
            "enable_brush_selection": getattr(self.infographic, "enable_brush_selection", False)
        }
        if self.infographic.data_binding:
            view_data["data_binding"] = self.infographic.data_binding.model_dump()
        if self.infographic.timeline_binding:
            view_data["timeline_binding"] = self.infographic.timeline_binding.model_dump()
        if hasattr(self.infographic, "live_binding") and self.infographic.live_binding:
            view_data["live_binding"] = self.infographic.live_binding.model_dump()
        if hasattr(self.infographic, "scrollytelling") and self.infographic.scrollytelling:
            view_data["scrollytelling"] = [s.model_dump() for s in self.infographic.scrollytelling]
        if hasattr(self.infographic, "tour") and self.infographic.tour:
            view_data["tour"] = [s.model_dump() for s in self.infographic.tour]
        if hasattr(self.infographic, "layer_toggles") and self.infographic.layer_toggles:
            view_data["layer_toggles"] = [s.model_dump() for s in self.infographic.layer_toggles]
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
