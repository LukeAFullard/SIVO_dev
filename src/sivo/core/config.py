from typing import Dict, Optional, Any, List
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
    echarts_option: Optional[Dict[str, Any]] = None
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
    filter: Optional[str] = None
    clip_path: Optional[str] = None
    mask: Optional[str] = None
    transform: Optional[str] = None

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

class ProjectConfig(BaseModel):
    """Configuration for a complete SIVO project."""
    svg_file: str = Field(description="Path to the source SVG file.")
    default_panel_position: str = Field(
        default="right",
        description="Global default position for the info panel ('right', 'left', 'top', 'bottom')."
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
    build_js: bool = Field(
        default=False,
        description="If True, runs an optional JavaScript bundler (e.g., Vite/Webpack) to minify frontend assets."
    )
    enable_e2e_testing: bool = Field(
        default=False,
        description="If True, provisions scaffolding for End-to-End (E2E) Browser Testing via Playwright."
    )
