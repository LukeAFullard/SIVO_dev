import os
import json
from typing import Dict, Optional, Union, List
from pydantic import BaseModel

from ..svg.parser import SVGParser
from .actions import InteractionMapping, TooltipAction, URLAction, DrillDownAction, CallbackAction, ThemeOverride, HoverCallbackAction, VideoAction, GalleryAction, AudioAction, MarkdownAction, FetchAction, FormAction, SocialAction, DocumentAction, MapAction, AnalyticsAction, DataSourceAction, ExternalFormAction, EcommerceAction, RichMediaAction, BIAction, ReplitAction, EchartsAction, ZoomAction, LottieAction, CompareAction, ProgressBarAction, A11yAction, ConfettiAction
from .config import ProjectConfig, ElementConfig, DataBindingConfig, TimelineBindingConfig
from ..runtime.bundle_generator import generate_echarts_html

class Infographic:
    def __init__(self, parser: SVGParser, default_panel_position: str = "right", disable_panel: bool = False, panel_width: Optional[str] = None, panel_height: Optional[str] = None, disable_resizer: bool = False, disable_tooltips: bool = False, disable_zoom_controls: bool = False, lock_zoom_out: bool = False, lock_canvas: bool = False, enable_a11y: bool = False, render_mode: str = "canvas", enable_minimap: bool = False, enable_export: bool = False, fade_unselected: bool = False, theme: str = "light", enable_search: bool = False, watermark: Optional[str] = None, enable_brush_selection: bool = False, title: Optional[str] = None, subtitle: Optional[str] = None, attribution: Optional[str] = None, enable_fullscreen: bool = False, enable_share: bool = False, enable_data_download: bool = False, enable_drawing_tools: bool = False, ambient_effect: Optional[str] = None, bounding_coords: Optional[list[list[float]]] = None):
        self.parser = parser
        self.elements = self.parser.process_elements()
        self.mappings: Dict[str, InteractionMapping] = {}
        self._element_lookup: Dict[str, dict] = {}
        self.overlays: Dict[str, dict] = {}
        self.connections: list[dict] = []
        self.default_panel_position = default_panel_position
        self.disable_panel = disable_panel
        self.panel_width = panel_width
        self.panel_height = panel_height
        self.disable_resizer = disable_resizer
        self.disable_tooltips = disable_tooltips
        self.disable_zoom_controls = disable_zoom_controls
        self.lock_zoom_out = lock_zoom_out
        self.lock_canvas = lock_canvas
        self.enable_a11y = enable_a11y
        self.render_mode = render_mode
        self.enable_minimap = enable_minimap
        self.enable_export = enable_export
        self.fade_unselected = fade_unselected
        self.theme = theme
        self.enable_search = enable_search
        self.watermark = watermark
        self.enable_brush_selection = enable_brush_selection
        self.title = title
        self.subtitle = subtitle
        self.attribution = attribution
        self.enable_fullscreen = enable_fullscreen
        self.enable_share = enable_share
        self.enable_data_download = enable_data_download
        self.enable_drawing_tools = enable_drawing_tools
        self.ambient_effect = ambient_effect
        self.bounding_coords = bounding_coords
        self.data_binding: Optional[DataBindingConfig] = None
        self.timeline_binding: Optional[TimelineBindingConfig] = None
        self.scrollytelling: Optional[list] = None
        self.tour: Optional[list] = None
        self.layer_toggles: Optional[list] = None
        self.scratchoff: Optional[dict] = None
        self.proportional_symbols: Optional[dict] = None

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
        infographic.default_panel_position = getattr(cfg, "default_panel_position", "right")
        infographic.disable_panel = getattr(cfg, "disable_panel", False)
        infographic.panel_width = getattr(cfg, "panel_width", None)
        infographic.panel_height = getattr(cfg, "panel_height", None)
        infographic.disable_resizer = getattr(cfg, "disable_resizer", False)
        infographic.disable_tooltips = getattr(cfg, "disable_tooltips", False)
        infographic.disable_zoom_controls = getattr(cfg, "disable_zoom_controls", False)
        infographic.lock_zoom_out = getattr(cfg, "lock_zoom_out", False)

        infographic.enable_a11y = getattr(cfg, "enable_a11y", False)
        infographic.render_mode = getattr(cfg, "render_mode", "canvas")
        infographic.enable_minimap = getattr(cfg, "enable_minimap", False)
        infographic.enable_export = getattr(cfg, "enable_export", False)
        infographic.lock_canvas = getattr(cfg, "lock_canvas", False)
        infographic.fade_unselected = getattr(cfg, "fade_unselected", False)
        infographic.theme = getattr(cfg, "theme", "light")
        infographic.enable_search = getattr(cfg, "enable_search", False)
        infographic.watermark = getattr(cfg, "watermark", None)
        infographic.enable_brush_selection = getattr(cfg, "enable_brush_selection", False)
        infographic.title = getattr(cfg, "title", None)
        infographic.subtitle = getattr(cfg, "subtitle", None)
        infographic.attribution = getattr(cfg, "attribution", None)
        infographic.enable_fullscreen = getattr(cfg, "enable_fullscreen", False)
        infographic.enable_share = getattr(cfg, "enable_share", False)
        infographic.enable_data_download = getattr(cfg, "enable_data_download", False)
        infographic.enable_drawing_tools = getattr(cfg, "enable_drawing_tools", False)
        infographic.ambient_effect = getattr(cfg, "ambient_effect", None)
        infographic.bounding_coords = getattr(cfg, "bounding_coords", None)
        infographic.data_binding = getattr(cfg, "data_binding", None)
        infographic.timeline_binding = getattr(cfg, "timeline_binding", None)
        infographic.scrollytelling = getattr(cfg, "scrollytelling", None)
        infographic.tour = getattr(cfg, "tour", None)
        infographic.layer_toggles = getattr(cfg, "layer_toggles", None)
        infographic.scratchoff = getattr(cfg, "scratchoff", None)
        infographic.proportional_symbols = getattr(cfg, "proportional_symbols", None)

        if getattr(cfg, "connections", None):
            for conn in cfg.connections:
                infographic.add_connection(
                    source_id=conn.source_id,
                    target_id=conn.target_id,
                    label=conn.label,
                    color=conn.color,
                    width=conn.width,
                    animation_speed=conn.animation_speed,
                    type=conn.type,
                    opacity=conn.opacity,
                    flow_effect=conn.flow_effect,
                    effect_symbol=conn.effect_symbol,
                    effect_size=conn.effect_size
                )

        for element_id, elem_config in cfg.mappings.items():
            try:
                infographic.map(
                    element_id,
                    aria_label=elem_config.aria_label,
                    role=elem_config.role,
                    tabindex=elem_config.tabindex,
                    tooltip=elem_config.tooltip,
                    html=elem_config.html,
                    url=elem_config.url,
                    drill_to=elem_config.drill_to,
                    callback_event=elem_config.callback_event,
                    callback_payload=elem_config.callback_payload,
                    hover_callback_event=elem_config.hover_callback_event,
                    hover_callback_payload=elem_config.hover_callback_payload,
                    social=elem_config.social,
                    document=getattr(elem_config, 'document', None),
                    map_location=getattr(elem_config, 'map_location', None),
                    analytics=getattr(elem_config, 'analytics', None),
                    datasource=getattr(elem_config, 'datasource', None),
                    external_form=getattr(elem_config, 'external_form', None),
                    ecommerce=getattr(elem_config, 'ecommerce', None),
                    rich_media=getattr(elem_config, 'rich_media', None),
                    bi=getattr(elem_config, 'bi', None),
                    lottie=getattr(elem_config, 'lottie', None),
                    compare=getattr(elem_config, 'compare', None),
                    progress_bar=getattr(elem_config, 'progress_bar', None),
                    confetti=getattr(elem_config, 'confetti', None),
                    echarts_option=getattr(elem_config, 'echarts_option', None),
                    context_menu=getattr(elem_config, 'context_menu', None),
                    panel_position=elem_config.panel_position,
                    open_by_default=elem_config.open_by_default,
                    zoom_on_click=elem_config.zoom_on_click,
                    zoom_level=elem_config.zoom_level,
                    draggable=elem_config.draggable,
                    color=elem_config.color,
                    hover_color=elem_config.hover_color,
                    fill_gradient=elem_config.fill_gradient,
                    fill_pattern=elem_config.fill_pattern,
                    border_width=elem_config.border_width,
                    border_color=elem_config.border_color,
                    glow=elem_config.glow,
                    morph_to_path=elem_config.morph_to_path,
                    morph_duration_ms=elem_config.morph_duration_ms,
                    morph_delay_ms=elem_config.morph_delay_ms,
                    morph_easing=elem_config.morph_easing,
                    morph_iterations=elem_config.morph_iterations,
                    filter=elem_config.filter,
                    clip_path=elem_config.clip_path,
                    mask=elem_config.mask,
                    transform=elem_config.transform
                )
            except ValueError as e:
                # Log or handle missing elements gracefully, perhaps a warning
                print(f"Warning mapping {element_id}: {e}")

        return infographic

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
        """
        target_elem = self._element_lookup.get(element_id)
        if not target_elem:
            raise ValueError(f"Element with id/name '{element_id}' not found in SVG.")

        elem_name = target_elem['name']
        mapping = self.mappings[elem_name]

        # Handle Accessibility (A11y) Actions
        if aria_label or role or tabindex or self.enable_a11y:
            a11y_action = next((a for a in mapping.actions if a.action_type == "a11y"), None)
            if not a11y_action:
                # Generate default aria_label from tooltip or element_id if enable_a11y is True but aria_label wasn't provided
                default_label = tooltip if tooltip else element_id

                # Check if it was provided, else fallback to generated
                final_label = aria_label if aria_label is not None else default_label
                final_role = role if role is not None else "button"
                final_tabindex = tabindex if tabindex is not None else "0"

                mapping.actions.append(A11yAction(aria_label=final_label, role=final_role, tabindex=final_tabindex))
            else:
                if aria_label is not None:
                    a11y_action.aria_label = aria_label
                if role is not None:
                    a11y_action.role = role
                if tabindex is not None:
                    a11y_action.tabindex = tabindex


        if open_by_default:
            mapping.open_by_default = True

        if context_menu:
            mapping.context_menu = context_menu

        if draggable:
            mapping.draggable = True

        if zoom_on_click:
            center = self.get_element_center(element_id)
            if center:
                mapping.actions.append(ZoomAction(center=center, zoom_level=zoom_level))

        if html or tooltip:
            mapping.actions.append(TooltipAction(
                title=tooltip,
                content=html if html else f"<h3>{tooltip}</h3>" if tooltip else "",
                panel_position=panel_position or self.default_panel_position
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
            mapping.actions.append(MarkdownAction(markdown_text=markdown, panel_position=panel_position or self.default_panel_position))

        if fetch_url:
            mapping.actions.append(FetchAction(fetch_url=fetch_url, panel_position=panel_position or self.default_panel_position))

        if form_fields and form_submit_event:
            mapping.actions.append(FormAction(form_fields=form_fields, submit_event=form_submit_event, panel_position=panel_position or self.default_panel_position))

        if social and 'provider' in social and 'url' in social:
            mapping.actions.append(SocialAction(provider=social['provider'], url=social['url'], panel_position=panel_position or self.default_panel_position))

        if document:
            mapping.actions.append(DocumentAction(document_url=document, panel_position=panel_position or self.default_panel_position))

        if map_location:
            mapping.actions.append(MapAction(map_location=map_location, panel_position=panel_position or self.default_panel_position))

        if analytics and 'provider' in analytics and 'event_name' in analytics:
            mapping.actions.append(AnalyticsAction(provider=analytics['provider'], event_name=analytics['event_name'], payload=analytics.get('payload')))

        if datasource and 'provider' in datasource and 'api_endpoint' in datasource:
            mapping.actions.append(DataSourceAction(provider=datasource['provider'], api_endpoint=datasource['api_endpoint'], panel_position=panel_position or self.default_panel_position))

        if external_form and 'provider' in external_form and 'form_url' in external_form:
            mapping.actions.append(ExternalFormAction(provider=external_form['provider'], form_url=external_form['form_url'], panel_position=panel_position or self.default_panel_position))

        if ecommerce and 'provider' in ecommerce and 'checkout_url' in ecommerce:
            mapping.actions.append(EcommerceAction(provider=ecommerce['provider'], checkout_url=ecommerce['checkout_url'], panel_position=panel_position or self.default_panel_position))

        if rich_media and 'provider' in rich_media and 'media_url' in rich_media:
            mapping.actions.append(RichMediaAction(provider=rich_media['provider'], media_url=rich_media['media_url'], panel_position=panel_position or self.default_panel_position))

        if bi and 'provider' in bi and 'dashboard_url' in bi:
            mapping.actions.append(BIAction(provider=bi['provider'], dashboard_url=bi['dashboard_url'], panel_position=panel_position or self.default_panel_position))

        if lottie and 'lottie_url' in lottie:
            mapping.actions.append(LottieAction(lottie_url=lottie['lottie_url'], loop=lottie.get('loop', True), autoplay=lottie.get('autoplay', True), panel_position=panel_position or self.default_panel_position))

        if compare and 'before_image' in compare and 'after_image' in compare:
            mapping.actions.append(CompareAction(before_image=compare['before_image'], after_image=compare['after_image'], label_before=compare.get('label_before', 'Before'), label_after=compare.get('label_after', 'After'), panel_position=panel_position or self.default_panel_position))

        if progress_bar and 'title' in progress_bar and 'progress' in progress_bar:
            mapping.actions.append(ProgressBarAction(title=progress_bar['title'], progress=progress_bar['progress'], color=progress_bar.get('color', '#38bdf8'), panel_position=panel_position or self.default_panel_position))

        if confetti:
            mapping.actions.append(ConfettiAction(particle_count=confetti.get('particle_count', 100), spread=confetti.get('spread', 70)))

        if replit:
            mapping.actions.append(ReplitAction(repl_url=replit, panel_position=panel_position or self.default_panel_position))

        if echarts_option:
            mapping.actions.append(EchartsAction(option=echarts_option, panel_position=panel_position or self.default_panel_position, map_name=map_name, map_data=map_data))

        if color:
            mapping.theme.color = color

        if hover_color:
            mapping.theme.hover_color = hover_color

        if fill_gradient:
            mapping.theme.fill_gradient = fill_gradient

        if fill_pattern:
            mapping.theme.fill_pattern = fill_pattern

        if border_width is not None:
            mapping.theme.border_width = border_width

        if border_color:
            mapping.theme.border_color = border_color

        if glow is not None:
            mapping.theme.glow = glow

        if animation:
            mapping.theme.animation = animation

        if morph_to_path:
            mapping.theme.morph_to_path = morph_to_path

        if morph_duration_ms is not None:
            mapping.theme.morph_duration_ms = morph_duration_ms

        if morph_delay_ms is not None:
            mapping.theme.morph_delay_ms = morph_delay_ms

        if morph_easing:
            mapping.theme.morph_easing = morph_easing

        if morph_iterations is not None:
            mapping.theme.morph_iterations = morph_iterations

        if filter:
            mapping.theme.filter = filter

        if clip_path:
            mapping.theme.clip_path = clip_path

        if mask:
            mapping.theme.mask = mask

        if transform:
            mapping.theme.transform = transform

        if odometer_value is not None:
            mapping.theme.odometer_value = odometer_value
            mapping.theme.odometer_duration_ms = odometer_duration_ms
            mapping.theme.odometer_format = odometer_format

    def add_shape(self, tag: str, attributes: Dict[str, str]):
        """
        Programmatically adds a simple vector shape to the SVG and registers it
        in the internal elements lookup so it can be mapped to actions.
        """
        self.parser.add_shape(tag, attributes)

        # After adding, re-process elements to find the new one and register it
        # We only need to add the newest element to our mappings/lookup
        elem_id = attributes.get('id')
        if elem_id:
            # We construct the element data exactly like process_elements does
            elem_name = attributes.get('name', elem_id)
            element_data = {
                'id': elem_id,
                'name': elem_name,
                'tag': tag
            }
            # Add to elements list
            self.elements.append(element_data)

            # Register in internal lookup and default mapping
            if elem_name not in self.mappings:
                self.mappings[elem_name] = InteractionMapping(id=elem_id)
            self._element_lookup[elem_id] = element_data
            self._element_lookup[elem_name] = element_data

    def bind_data(self, data: Dict[str, Dict[str, float]], key: str, colors: list, min_val: float, max_val: float):
        """
        Binds quantitative data to SVG IDs dynamically and applies a color scale.
        """
        self.data_binding = DataBindingConfig(
            data=data,
            key=key,
            colors=colors,
            min_val=min_val,
            max_val=max_val
        )

    def bind_timeline(self, data: Dict[str, Dict[str, Dict[str, float]]], key: str, colors: list, min_val: float, max_val: float, auto_play: bool = True, play_interval: int = 1000, show_play_btn: bool = True, loop: bool = True, control_position: str = "left", symbol: str = "emptyCircle", symbol_size: Union[int, List[int]] = 10, bottom: Union[int, str] = 20):
        """
        Binds quantitative time-series data to SVG IDs dynamically and applies a color scale over an animated timeline.
        data format: { "2020": { "RegionA": { "value": 10 }, "RegionB": { "value": 20 } }, "2021": ... }
        """
        self.timeline_binding = TimelineBindingConfig(
            data=data,
            key=key,
            colors=colors,
            min_val=min_val,
            max_val=max_val,
            auto_play=auto_play,
            play_interval=play_interval,
            show_play_btn=show_play_btn,
            loop=loop,
            control_position=control_position,
            symbol=symbol,
            symbol_size=symbol_size,
            bottom=bottom
        )

    def bind_live(self, url: str, topic: str, auth_token: Optional[str] = None):
        """Binds a WebSocket connection for live UI updates via the frontend runtime."""
        from .config import LiveBindingConfig
        self.live_binding = LiveBindingConfig(
            url=url,
            topic=topic,
            auth_token=auth_token
        )

    def bind_scrollytelling(self, steps: list[Dict]):
        from .config import ScrollytellingStepConfig
        self.scrollytelling = []
        for step in steps:
            self.scrollytelling.append(ScrollytellingStepConfig(**step))

    def bind_tour(self, steps: list[Dict]):
        from .config import TourStepConfig
        self.tour = []
        for step in steps:
            self.tour.append(TourStepConfig(**step))

    def add_layer_toggle(self, label: str, element_ids: list[str], default_visible: bool = True):
        from .config import LayerToggleConfig
        if not self.layer_toggles:
            self.layer_toggles = []
        self.layer_toggles.append(LayerToggleConfig(label=label, element_ids=element_ids, default_visible=default_visible))

    def enable_scratchoff(self, color: str = "#cccccc", image_url: Optional[str] = None, brush_size: int = 40):
        """Enables a scratch-off reveal layer over the map."""
        from .config import ScratchoffConfig
        self.scratchoff = ScratchoffConfig(color=color, image_url=image_url, brush_size=brush_size).model_dump()

    def apply_proportional_symbols(self, data_map: Dict[str, Union[float, Dict]], min_size: float = 10.0, max_size: float = 50.0, color: str = "rgba(255, 0, 0, 0.6)", is_pulse: bool = False):
        """
        Creates a proportional symbol map (e.g., bubble map) by calculating the center of each
        mapped element and passing the parameters to the frontend to render an ECharts scatter series.
        data_map can be a dict of {id: value} or {id: {"value": 10, "color": "#00ff00"}} for custom per-marker colors.
        """
        from .config import ProportionalSymbolConfig

        processed_data = {}
        for elem_id, val in data_map.items():
            center = self.get_element_center(elem_id)
            if center:
                coord = center
            else:
                # If we have bounding_coords, users can pass raw coordinates instead of SVG IDs.
                # Check if the dictionary contains a "coord" value explicitly.
                if isinstance(val, dict) and "coord" in val:
                    coord = val["coord"]
                else:
                    coord = None

            if coord:
                if isinstance(val, dict):
                    processed_data[elem_id] = {
                        "value": val.get("value", 0),
                        "coord": coord,
                        "color": val.get("color")
                    }
                else:
                    processed_data[elem_id] = {
                        "value": val,
                        "coord": coord
                    }
                # Ensure it exists in mappings so it renders an ECharts hit area if needed
                if elem_id not in self.mappings:
                    # Register an empty mapping so tooltip binding can work for these dynamically added points
                    self.mappings[elem_id] = InteractionMapping(id=elem_id)
                    # And add to lookup to prevent crashes on subsequent mappings
                    self._element_lookup[elem_id] = {"id": elem_id, "name": elem_id, "tag": "virtual_scatter"}

        self.proportional_symbols = ProportionalSymbolConfig(
            data=processed_data,
            min_size=min_size,
            max_size=max_size,
            color=color,
            is_pulse=is_pulse
        ).model_dump()

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

    def add_connection(self, source_id: str, target_id: str, label: str = "", color: str = "#ff3333", width: float = 2.0, animation_speed: float = 3.0, type: str = 'solid', opacity: float = 0.6, flow_effect: bool = False, effect_symbol: str = "circle", effect_size: float = 3.0):
        """
        Adds a visual connection (line) between the centers of two SVG elements.
        Optionally animated as a flow arrow with `flow_effect=True` and an `effect_symbol` like "arrow".
        """
        source_elem = self._element_lookup.get(source_id)
        target_elem = self._element_lookup.get(target_id)

        if not source_elem:
            raise ValueError(f"Source element '{source_id}' not found in SVG.")
        if not target_elem:
            raise ValueError(f"Target element '{target_id}' not found in SVG.")

        source_center = self.get_element_center(source_id)
        target_center = self.get_element_center(target_id)

        if not source_center or not target_center:
            raise ValueError("Could not calculate bounding box centers for one or both elements.")

        self.connections.append({
            "source_id": source_id,
            "target_id": target_id,
            "coords": [source_center, target_center],
            "label": label,
            "color": color,
            "width": width,
            "animation_speed": animation_speed,
            "type": type,
            "opacity": opacity,
            "flow_effect": flow_effect,
            "effect_symbol": effect_symbol,
            "effect_size": effect_size
        })

    def add_overlay(self, element_id: str, html: str, offset_x: int = 0, offset_y: int = 0, scale_with_zoom: bool = False):
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
            "offset": [offset_x, offset_y],
            "scale_with_zoom": scale_with_zoom
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

        view_data = {
            "svg_string": self.parser.to_string(),
            "mappings": mappings_dict,
            "overlays": self.overlays,
            "connections": self.connections,
            "disable_panel": self.disable_panel,
            "panel_width": self.panel_width,
            "panel_height": self.panel_height,
            "disable_resizer": self.disable_resizer,
            "disable_tooltips": self.disable_tooltips,
            "disable_zoom_controls": self.disable_zoom_controls,
            "lock_zoom_out": self.lock_zoom_out,
            "render_mode": self.render_mode,
            "enable_minimap": self.enable_minimap,
            "enable_export": self.enable_export,
            "lock_canvas": self.lock_canvas,
            "fade_unselected": self.fade_unselected,
            "theme": self.theme,
            "enable_search": self.enable_search,
            "watermark": self.watermark,
            "enable_brush_selection": self.enable_brush_selection,
            "title": self.title,
            "subtitle": self.subtitle,
            "attribution": self.attribution,
            "enable_fullscreen": self.enable_fullscreen,
            "enable_share": self.enable_share,
            "enable_data_download": self.enable_data_download,
            "enable_drawing_tools": self.enable_drawing_tools,
            "ambient_effect": self.ambient_effect,
            "bounding_coords": self.bounding_coords
        }
        if self.data_binding:
            view_data["data_binding"] = self.data_binding.model_dump()
        if self.timeline_binding:
            view_data["timeline_binding"] = self.timeline_binding.model_dump()
        if self.scrollytelling:
            view_data["scrollytelling"] = [s.model_dump() for s in self.scrollytelling]
        if self.tour:
            view_data["tour"] = [s.model_dump() for s in self.tour]
        if self.layer_toggles:
            view_data["layer_toggles"] = [s.model_dump() for s in self.layer_toggles]
        if self.scratchoff:
            view_data["scratchoff"] = self.scratchoff
        if self.proportional_symbols:
            view_data["proportional_symbols"] = self.proportional_symbols

        views_data = {
            "default_view": view_data
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
