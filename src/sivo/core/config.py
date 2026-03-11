from typing import Dict, Optional, Any, List, Union
from pydantic import BaseModel, Field

class ElementConfig(BaseModel):
    """Configuration for a single SVG element's interactions and theme."""
    aria_label: Optional[str] = None
    role: Optional[str] = None
    tabindex: Optional[str] = None
    tooltip: Optional[str] = None
    html: Optional[str] = None
    url: Optional[str] = None
    drill_to: Optional[str] = None
    callback_event: Optional[str] = None
    callback_payload: Optional[Dict[str, Any]] = None
    hover_callback_event: Optional[str] = None
    hover_callback_payload: Optional[Dict[str, Any]] = None
    social: Optional[Dict[str, str]] = None
    document: Optional[str] = None
    map_location: Optional[str] = None
    analytics: Optional[Dict[str, Any]] = None
    datasource: Optional[Dict[str, str]] = None
    external_form: Optional[Dict[str, str]] = None
    ecommerce: Optional[Dict[str, str]] = None
    rich_media: Optional[Dict[str, str]] = None
    bi: Optional[Dict[str, str]] = None
    lottie: Optional[Dict[str, Any]] = None
    compare: Optional[Dict[str, str]] = None
    progress_bar: Optional[Dict[str, Any]] = None
    confetti: Optional[Dict[str, int]] = None
    echarts_option: Optional[Dict[str, Any]] = None
    map_name: Optional[str] = None
    map_data: Optional[Union[str, dict]] = None
    context_menu: Optional[List[Dict[str, Any]]] = None
    panel_position: Optional[str] = None
    open_by_default: bool = False
    zoom_on_click: bool = False
    zoom_level: float = 2.0
    draggable: bool = False
    color: Optional[str] = None
    hover_color: Optional[str] = None
    fill_gradient: Optional[Dict[str, Any]] = None
    fill_pattern: Optional[Dict[str, Any]] = None
    border_width: Optional[float] = None
    border_color: Optional[str] = None
    glow: Optional[bool] = None
    morph_to_path: Optional[str] = None
    morph_duration_ms: Optional[int] = 1000
    morph_delay_ms: Optional[int] = 0
    morph_easing: Optional[str] = "ease-in-out"
    morph_iterations: Optional[float] = 1.0
    filter: Optional[str] = None
    clip_path: Optional[str] = None
    mask: Optional[str] = None
    transform: Optional[str] = None
    odometer_value: Optional[float] = None
    odometer_duration_ms: Optional[int] = 2000
    odometer_format: Optional[str] = None

class DataBindingConfig(BaseModel):
    data: Dict[str, Dict[str, float]]
    key: str
    colors: List[str]
    min_val: float
    max_val: float

class TimelineBindingConfig(BaseModel):
    data: Dict[str, Dict[str, Dict[str, float]]]
    key: str
    colors: List[str]
    min_val: float
    max_val: float
    auto_play: bool = True
    play_interval: int = 1000

class ConnectionConfig(BaseModel):
    source_id: str
    target_id: str
    label: str = ""
    color: str = "#ff3333"
    width: float = 2.0
    animation_speed: float = 3.0
    type: str = "solid"
    opacity: float = 0.6

class LiveBindingConfig(BaseModel):
    """Configuration for native WebSocket/PubSub real-time data updates without Streamlit re-renders."""
    url: str
    topic: str
    auth_token: Optional[str] = None
    reconnect_attempts: int = 5
    fallback_polling_interval: int = 0

class ScrollytellingStepConfig(BaseModel):
    """Configuration for a single scrollytelling step."""
    content: str = Field(description="HTML content for the step text")
    zoom_to: Optional[str] = Field(default=None, description="Element ID to zoom to")
    zoom_level: float = Field(default=2.0, description="Zoom level")
    colors: Optional[Dict[str, str]] = Field(default=None, description="Mapping of Element IDs to colors")
    show_tooltips: Optional[List[str]] = Field(default=None, description="List of Element IDs to show tooltips for")
    audio_url: Optional[str] = Field(default=None, description="Optional audio file URL to play automatically when this step is reached")

class TourStepConfig(BaseModel):
    """Configuration for a single guided tour step."""
    content: str = Field(description="HTML content for the tour step tooltip/modal")
    zoom_to: Optional[str] = Field(default=None, description="Element ID to zoom to")
    zoom_level: float = Field(default=2.0, description="Zoom level")
    show_tooltips: Optional[List[str]] = Field(default=None, description="List of Element IDs to show tooltips for")
    audio_url: Optional[str] = Field(default=None, description="Optional audio file URL to play automatically when this step is reached")

class ScratchoffConfig(BaseModel):
    """Configuration for a scratch-off reveal layer."""
    image_url: Optional[str] = Field(default=None, description="URL to an image to use as the scratch-off layer. If None, color is used.")
    color: str = Field(default="#cccccc", description="Solid color to use as the scratch-off layer if image_url is not provided.")
    brush_size: int = Field(default=40, description="Size of the scratch-off brush.")

class ProportionalSymbolConfig(BaseModel):
    """Configuration for a proportional symbol map."""
    data: Dict[str, Dict[str, Any]] = Field(description="Mapping of Element IDs to dicts containing 'value' and 'coord'.")
    min_size: float = Field(default=10.0, description="Minimum symbol size")
    max_size: float = Field(default=50.0, description="Maximum symbol size")
    color: str = Field(default="rgba(255, 0, 0, 0.6)", description="Color of the symbols")
    is_pulse: bool = Field(default=False, description="If True, renders the symbols as animated, rippling markers.")

class LayerToggleConfig(BaseModel):
    """Configuration for an interactive layer toggle legend."""
    label: str = Field(description="Display label for the legend item")
    element_ids: List[str] = Field(description="List of SVG Element IDs to toggle visibility for")
    default_visible: bool = Field(default=True, description="Initial visibility state")

class ProjectConfig(BaseModel):
    """Configuration for a complete SIVO project."""
    svg_file: str = Field(description="Path to the source SVG file.")
    default_panel_position: str = Field(
        default="right",
        description="Global default position for the info panel ('right', 'left', 'top', 'bottom')."
    )
    disable_panel: bool = Field(
        default=False,
        description="If True, completely suppresses the info panel from opening."
    )
    panel_width: Optional[str] = Field(
        default=None,
        description="Optional width (or height on mobile) for the info panel as a percentage or valid CSS unit (e.g., '50%', '30vw')."
    )
    lock_zoom_out: bool = Field(
        default=False,
        description="If True, prevents the user from zooming out further than the initial zoom level (1.0)."
    )
    enable_a11y: bool = Field(
        default=False,
        description="If True, automatically generates accessibility actions (A11yAction) for interactive elements."
    )
    render_mode: str = Field(
        default="canvas",
        description="Rendering mode: 'canvas' (default ECharts) or 'svg' (enables native SVG features like morphing and filters)."
    )
    theme: str = Field(
        default="light",
        description="The visual theme for the infographic UI. Options: 'light', 'dark'."
    )
    mappings: Dict[str, ElementConfig] = Field(
        default_factory=dict,
        description="Dictionary mapping element IDs to their configuration."
    )
    connections: List[ConnectionConfig] = Field(
        default_factory=list,
        description="List of connections to draw between elements."
    )
    data_binding: Optional[DataBindingConfig] = Field(
        default=None,
        description="Optional data binding for generating choropleth maps dynamically."
    )
    timeline_binding: Optional[TimelineBindingConfig] = Field(
        default=None,
        description="Optional timeline binding for animating choropleth maps over time."
    )
    live_binding: Optional[LiveBindingConfig] = Field(
        default=None,
        description="Optional WebSocket connection for live telemetry."
    )
    scrollytelling: Optional[List[ScrollytellingStepConfig]] = Field(
        default=None,
        description="Optional list of scrollytelling steps."
    )
    tour: Optional[List[TourStepConfig]] = Field(
        default=None,
        description="Optional list of tour steps."
    )
    layer_toggles: Optional[List[LayerToggleConfig]] = Field(
        default=None,
        description="Optional list of layer visibility toggles."
    )
    scratchoff: Optional[ScratchoffConfig] = Field(
        default=None,
        description="Optional configuration for a scratch-off layer."
    )
    proportional_symbols: Optional[ProportionalSymbolConfig] = Field(
        default=None,
        description="Optional configuration for proportional symbol overlays."
    )
    enable_minimap: bool = Field(
        default=False,
        description="If True, renders a small minimap in the corner to show global viewport context."
    )
    enable_export: bool = Field(
        default=False,
        description="If True, renders an export button that allows snapshotting the canvas."
    )
    lock_canvas: bool = Field(
        default=False,
        description="Disable panning and zooming on the map canvas"
    )
    build_js: bool = Field(
        default=False,
        description="If True, runs an optional JavaScript bundler (e.g., Vite/Webpack) to minify frontend assets."
    )
    enable_e2e_testing: bool = Field(
        default=False,
        description="If True, provisions scaffolding for End-to-End (E2E) Browser Testing via Playwright."
    )
    fade_unselected: bool = Field(
        default=False,
        description="If True, clicking on an interactive element will automatically fade out all other elements on the canvas to emphasize the selection."
    )
    enable_search: bool = Field(
        default=False,
        description="If True, renders a search bar overlay that allows users to quickly locate SVG elements by ID or tooltip content."
    )
    watermark: Optional[str] = Field(
        default=None,
        description="Optional HTML string to render a fixed watermark overlay (e.g., enterprise logo) in the bottom right corner."
    )
    enable_brush_selection: bool = Field(
        default=False,
        description="If True, enables a lasso/box selection tool to select multiple SVG elements at once."
    )
    title: Optional[str] = Field(
        default=None,
        description="Main title to display at the top of the infographic."
    )
    subtitle: Optional[str] = Field(
        default=None,
        description="Subtitle to display below the main title."
    )
    attribution: Optional[str] = Field(
        default=None,
        description="Attribution text (e.g. 'Data: WHO | Created by SIVO') to display at the bottom."
    )
    enable_fullscreen: bool = Field(
        default=False,
        description="If True, adds a fullscreen toggle button to the zoom controls."
    )
    enable_share: bool = Field(
        default=False,
        description="If True, adds a share button that uses the Web Share API if available."
    )
    enable_data_download: bool = Field(
        default=False,
        description="If True, adds a download button to export the bound data as a CSV."
    )
    bounding_coords: Optional[List[List[float]]] = Field(
        default=None,
        description="Optional bounding coordinates [[minLng, minLat], [maxLng, maxLat]] to map the SVG to a geographic coordinate system."
    )
