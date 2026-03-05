from typing import Dict, Optional, Any
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
    color: Optional[str] = None
    hover_color: Optional[str] = None
    border_width: Optional[float] = None
    border_color: Optional[str] = None
    glow: Optional[bool] = None

class ProjectConfig(BaseModel):
    """Configuration for a complete SIVO project."""
    svg_file: str = Field(description="Path to the source SVG file.")
    mappings: Dict[str, ElementConfig] = Field(
        default_factory=dict,
        description="Dictionary mapping element IDs to their configuration."
    )
