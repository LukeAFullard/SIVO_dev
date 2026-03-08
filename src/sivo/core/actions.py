from typing import Optional, Literal, Union, Annotated
from pydantic import BaseModel, Field

class BaseAction(BaseModel):
    action_type: str

class TooltipAction(BaseAction):
    action_type: Literal["tooltip"] = "tooltip"
    content: str = Field(description="HTML content for the tooltip")
    title: Optional[str] = Field(default=None, description="Optional title for the tooltip")
    panel_position: Literal["right", "left", "bottom", "top"] = Field(default="right", description="Position of the info panel")

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


class GalleryAction(BaseAction):
    action_type: Literal["gallery"] = "gallery"
    images: list[str] = Field(description="List of image URLs to display in a lightbox gallery")

class AudioAction(BaseAction):
    action_type: Literal["audio"] = "audio"
    audio_url: str = Field(description="URL of the audio file to play")

class MarkdownAction(BaseAction):
    action_type: Literal["markdown"] = "markdown"
    markdown_text: str = Field(description="Markdown content to render in the info panel")
    panel_position: Literal["right", "left", "bottom", "top"] = Field(default="right", description="Position of the info panel")

class FetchAction(BaseAction):
    action_type: Literal["fetch"] = "fetch"
    fetch_url: str = Field(description="URL to fetch data from and display in the info panel")
    panel_position: Literal["right", "left", "bottom", "top"] = Field(default="right", description="Position of the info panel")

class FormAction(BaseAction):
    action_type: Literal["form"] = "form"
    form_fields: list[dict] = Field(description="List of fields (e.g., {'name': 'ticket', 'type': 'text'})")
    submit_event: str = Field(description="Event name to trigger on form submission")
    panel_position: Literal["right", "left", "bottom", "top"] = Field(default="right", description="Position of the info panel")

class SocialAction(BaseAction):
    action_type: Literal["social"] = "social"
    provider: Literal["instagram", "tiktok", "linkedin", "wikipedia", "website", "twitch", "pinterest", "apple_music", "reddit"] = Field(description="The platform provider or generic type")
    url: str = Field(description="The URL to the post or page")
    panel_position: Literal["right", "left", "bottom", "top"] = Field(default="right", description="Position of the info panel")

class DocumentAction(BaseAction):
    action_type: Literal["document"] = "document"
    document_url: str = Field(description="URL to the PDF, DOCX, PPTX, or XLSX file")
    panel_position: Literal["right", "left", "bottom", "top"] = Field(default="right", description="Position of the info panel")

class MapAction(BaseAction):
    action_type: Literal["map"] = "map"
    map_location: str = Field(description="Location query for Google Maps")
    panel_position: Literal["right", "left", "bottom", "top"] = Field(default="right", description="Position of the info panel")

class AnalyticsAction(BaseAction):
    action_type: Literal["analytics"] = "analytics"
    provider: Literal["google_analytics", "posthog", "plausible"] = Field(description="The analytics provider")
    event_name: str = Field(description="The event name to track")
    payload: Optional[dict] = Field(default=None, description="Optional payload/properties for the event")

class DataSourceAction(BaseAction):
    action_type: Literal["datasource"] = "datasource"
    provider: Literal["google_sheets", "airtable", "notion"] = Field(description="The data source provider")
    api_endpoint: str = Field(description="The API endpoint or URL to fetch data from")
    panel_position: Literal["right", "left", "bottom", "top"] = Field(default="right", description="Position of the info panel")

class ExternalFormAction(BaseAction):
    action_type: Literal["external_form"] = "external_form"
    provider: Literal["typeform", "jotform", "hubspot", "google_forms", "surveymonkey", "qualtrics", "calendly"] = Field(description="The external form provider")
    form_url: str = Field(description="The URL of the external form to embed")
    panel_position: Literal["right", "left", "bottom", "top"] = Field(default="right", description="Position of the info panel")

class EcommerceAction(BaseAction):
    action_type: Literal["ecommerce"] = "ecommerce"
    provider: Literal["stripe", "shopify"] = Field(description="The e-commerce provider")
    checkout_url: str = Field(description="The URL for the checkout or buy button")
    panel_position: Literal["right", "left", "bottom", "top"] = Field(default="right", description="Position of the info panel")

class RichMediaAction(BaseAction):
    action_type: Literal["rich_media"] = "rich_media"
    provider: Literal["vimeo", "wistia", "spotify", "soundcloud"] = Field(description="The rich media provider")
    media_url: str = Field(description="The URL of the media to embed")
    panel_position: Literal["right", "left", "bottom", "top"] = Field(default="right", description="Position of the info panel")

class BIAction(BaseAction):
    action_type: Literal["bi"] = "bi"
    provider: Literal["metabase", "tableau", "powerbi"] = Field(description="The Business Intelligence provider")
    dashboard_url: str = Field(description="The URL of the dashboard to embed")
    panel_position: Literal["right", "left", "bottom", "top"] = Field(default="right", description="Position of the info panel")



class ReplitAction(BaseAction):
    action_type: Literal["replit"] = "replit"
    repl_url: str = Field(description="The URL of the Repl to embed")
    panel_position: Literal["right", "left", "bottom", "top"] = Field(default="right", description="Position of the info panel")

class EchartsAction(BaseAction):
    action_type: Literal["echarts"] = "echarts"
    option: dict = Field(description="The Apache ECharts option dictionary to render")
    height: str = Field(default="400px", description="The CSS height for the ECharts container")
    panel_position: Literal["right", "left", "bottom", "top"] = Field(default="right", description="Position of the info panel")

class ThemeOverride(BaseModel):
    color: Optional[str] = None
    hover_color: Optional[str] = None
    border_width: Optional[float] = None
    border_color: Optional[str] = None
    glow: Optional[bool] = None
    animation: Optional[str] = None

ActionType = Annotated[Union[TooltipAction, URLAction, DrillDownAction, CallbackAction, HoverCallbackAction, VideoAction, GalleryAction, AudioAction, MarkdownAction, FetchAction, FormAction, SocialAction, DocumentAction, MapAction, AnalyticsAction, DataSourceAction, ExternalFormAction, EcommerceAction, RichMediaAction, BIAction, ReplitAction, EchartsAction], Field(discriminator='action_type')]

class InteractionMapping(BaseModel):
    id: str
    actions: list[ActionType] = Field(default_factory=list)
    open_by_default: bool = False
    theme: ThemeOverride = Field(default_factory=ThemeOverride)
