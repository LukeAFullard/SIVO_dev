from typing import Optional, Literal, Union, Annotated
from pydantic import BaseModel, Field

class BaseAction(BaseModel):
    action_type: str

class TooltipAction(BaseAction):
    action_type: Literal["tooltip"] = "tooltip"
    content: str = Field(description="HTML content for the tooltip")
    title: Optional[str] = Field(default=None, description="Optional title for the tooltip")

class URLAction(BaseAction):
    action_type: Literal["url"] = "url"
    url: str = Field(description="External URL to navigate to")
    target: Literal["_blank", "_self"] = Field(default="_blank")

class DrillDownAction(BaseAction):
    action_type: Literal["drilldown"] = "drilldown"
    target_svg: str = Field(description="Registered view_id from SivoProject OR path to an external secondary SVG file")

class CallbackAction(BaseAction):
    action_type: Literal["callback"] = "callback"
    event_name: str = Field(description="Event name to send back to Streamlit or backend")
    payload: Optional[dict] = Field(default=None, description="Optional data payload to send")

class HoverCallbackAction(BaseAction):
    action_type: Literal["hover_callback"] = "hover_callback"
    event_name: str = Field(description="Event name to send back to Streamlit or backend on hover")
    payload: Optional[dict] = Field(default=None, description="Optional data payload to send")

class VideoAction(BaseAction):
    action_type: Literal["video"] = "video"
    video_url: str = Field(description="Embed URL for the video (e.g., YouTube embed URL)")

class ThemeOverride(BaseModel):
    color: Optional[str] = None
    hover_color: Optional[str] = None
    border_width: Optional[float] = None
    border_color: Optional[str] = None
    glow: Optional[bool] = None
    animation: Optional[str] = None

ActionType = Annotated[Union[TooltipAction, URLAction, DrillDownAction, CallbackAction, HoverCallbackAction, VideoAction], Field(discriminator='action_type')]

class InteractionMapping(BaseModel):
    id: str
    actions: list[ActionType] = Field(default_factory=list)
    theme: ThemeOverride = Field(default_factory=ThemeOverride)
