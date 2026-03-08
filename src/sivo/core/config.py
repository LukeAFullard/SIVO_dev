from typing import Dict, Optional, Any, List
from pydantic import BaseModel, Field

class ElementConfig(BaseModel):
    """Configuration for a single SVG element's interactions and theme."""
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
    color: Optional[str] = None
    hover_color: Optional[str] = None
    border_width: Optional[float] = None
    border_color: Optional[str] = None
    glow: Optional[bool] = None

class DataBindingConfig(BaseModel):
    data: Dict[str, Dict[str, float]]
    key: str
    colors: List[str]
    min_val: float
    max_val: float

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
    mappings: Dict[str, ElementConfig] = Field(
        default_factory=dict,
        description="Dictionary mapping element IDs to their configuration."
    )
    data_binding: Optional[DataBindingConfig] = Field(
        default=None,
        description="Optional data binding for generating choropleth maps dynamically."
    )
