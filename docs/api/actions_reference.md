---
Last Updated: 2026-04-09
SIVO Version: 0.1.0
---

# Actions API Reference

This document provides a comprehensive reference for all Action models available in the SIVO framework. These actions are used within `InteractionMapping`s to dictate the behavior of interactive SVG elements.

All action models inherit from `BaseAction` and define a specific `action_type`.

## Base Models

### `BaseAction`
The foundation for all action models.
- **`action_type`** (`str`): The string identifier of the action.

### `InteractionMapping`
Defines a set of actions and configurations mapped to a specific SVG element ID.
- **`id`** (`str`): The ID of the mapped SVG element.
- **`actions`** (`list[ActionType]`): A list of actions to apply to the element. Defaults to `[]`.
- **`context_menu`** (`Optional[list[dict]]`): List of dictionaries defining context menu items: `[{'label': 'Action', 'event': 'my_event'}]`.
- **`open_by_default`** (`bool`): If True, panels/modals associated with actions open on load. Defaults to `False`.
- **`panel_position`** (`Optional[str]`): Position override for the element's panel.
- **`panel_css`** (`Optional[str]`): Custom CSS to apply to the panel.
- **`draggable`** (`bool`): Whether the element is draggable. Defaults to `False`.
- **`theme`** (`ThemeOverride`): Thematic overrides for the element (colors, borders, morphing, etc.).

---

## Tooltips and Overlays

### `TooltipAction`
Displays a hover or click tooltip/panel with HTML content.
- **`action_type`**: `"tooltip"`
- **`content`** (`str`): HTML content for the tooltip.
- **`title`** (`Optional[str]`): Optional title for the tooltip.
- **`panel_position`** (`Literal["right", "left", "bottom", "top", "overlay", "none"]`): Position of the info panel. Defaults to `"none"`.

### `FootnoteAction`
Displays a footnote or provenance popover.
- **`action_type`**: `"footnote"`
- **`content`** (`str`): HTML content explaining provenance or footnotes.
- **`title`** (`Optional[str]`): Optional title for the footnote popover. Defaults to `"Data Note"`.

### `MarkdownAction`
Renders markdown content in the info panel.
- **`action_type`**: `"markdown"`
- **`markdown_text`** (`str`): Markdown content to render.
- **`panel_position`** (`Literal["right", "left", "bottom", "top", "overlay", "none"]`): Position of the info panel. Defaults to `"none"`.

---

## Navigation and Drilldowns

### `URLAction`
Navigates to an external URL.
- **`action_type`**: `"url"`
- **`url`** (`str`): External URL to navigate to.
- **`target`** (`Literal["_blank", "_self"]`): Target frame. Defaults to `"_blank"`.

### `DrillDownAction`
Loads a secondary SIVO view into the current viewport (multi-level dashboards).
- **`action_type`**: `"drilldown"`
- **`target_svg`** (`str`): Registered `view_id` from `SivoProject` OR path to an external secondary SVG file.
- **`transition`** (`Optional[str]`): Optional transition animation name (e.g., `'fade'`, `'slide-left'`, `'slide-right'`, `'page-turn'`).

### `DrillThroughAction`
Navigates to a deeply detailed sub-dashboard or external page.
- **`action_type`**: `"drill_through"`
- **`url`** (`str`): URL to navigate to.
- **`target`** (`Literal["_blank", "_self"]`): Target frame. Defaults to `"_self"`.
- **`transition`** (`Optional[str]`): Optional transition animation name.

---

## Callbacks and Events

### `CallbackAction`
Triggers an event back to Streamlit or the backend on click.
- **`action_type`**: `"callback"`
- **`event_name`** (`str`): Event name to send.
- **`payload`** (`Optional[dict]`): Optional data payload to send.

### `HoverCallbackAction`
Triggers an event back to Streamlit or the backend on hover.
- **`action_type`**: `"hover_callback"`
- **`event_name`** (`str`): Event name to send.
- **`payload`** (`Optional[dict]`): Optional data payload to send.

---

## Multimedia and Rich Content

### `VideoAction`
Embeds a video (e.g., YouTube/Vimeo) in the panel.
- **`action_type`**: `"video"`
- **`video_url`** (`str`): Embed URL for the video.

### `AudioAction`
Plays an audio file.
- **`action_type`**: `"audio"`
- **`audio_url`** (`str`): URL of the audio file to play.

### `GalleryAction`
Displays a lightbox gallery of images.
- **`action_type`**: `"gallery"`
- **`images`** (`list[str]`): List of image URLs to display.

### `ToggleImageAction`
Cycles through images applied to an element's background.
- **`action_type`**: `"toggle_image"`
- **`target_id`** (`Optional[str]`): The ID of the target element. Defaults to the mapped element.
- **`image_urls`** (`list[str]`): List of image URLs to cycle through.

### `DocumentAction`
Embeds or links to a document (PDF, DOCX, etc.).
- **`action_type`**: `"document"`
- **`document_url`** (`str`): URL to the document file.
- **`panel_position`** (`Literal["right", "left", "bottom", "top", "overlay", "none"]`): Position of the info panel. Defaults to `"none"`.

### `MapAction`
Embeds a location query map (e.g., Google Maps).
- **`action_type`**: `"map"`
- **`map_location`** (`str`): Location query.
- **`panel_position`** (`Literal["right", "left", "bottom", "top", "overlay", "none"]`): Position of the info panel. Defaults to `"none"`.

### `EchartsAction`
Renders a native Apache ECharts visualization.
- **`action_type`**: `"echarts"`
- **`option`** (`dict`): The Apache ECharts option dictionary to render.
- **`height`** (`str`): The CSS height for the container. Defaults to `"400px"`.
- **`panel_position`** (`Literal["right", "left", "bottom", "top", "overlay", "none"]`): Position of the info panel. Defaults to `"none"`.
- **`map_name`** (`Optional[str]`): Optional map name to register before rendering.
- **`map_data`** (`Optional[Union[str, dict]]`): Optional map data (SVG string or GeoJSON dict) to register.

---

## Forms and Data

### `FormAction`
Renders an internal data entry form.
- **`action_type`**: `"form"`
- **`form_fields`** (`list[dict]`): List of fields (e.g., `[{'name': 'ticket', 'type': 'text'}]`).
- **`submit_event`** (`str`): Event name to trigger on form submission.
- **`panel_position`** (`Literal["right", "left", "bottom", "top", "overlay", "none"]`): Position of the info panel. Defaults to `"none"`.

### `FetchAction`
Fetches external data and displays it in the panel.
- **`action_type`**: `"fetch"`
- **`fetch_url`** (`str`): URL to fetch data from.
- **`panel_position`** (`Literal["right", "left", "bottom", "top", "overlay", "none"]`): Position of the info panel. Defaults to `"none"`.

---

## External Integrations

### `SocialAction`
Embeds a social media post or profile.
- **`action_type`**: `"social"`
- **`provider`** (`Literal["instagram", "tiktok", "linkedin", "wikipedia", "website", "twitch", "pinterest", "apple_music", "reddit"]`): The platform provider.
- **`url`** (`str`): The URL to the post or page.
- **`panel_position`** (`Literal["right", "left", "bottom", "top", "overlay", "none"]`): Position of the info panel. Defaults to `"none"`.

### `AnalyticsAction`
Fires an analytics tracking event.
- **`action_type`**: `"analytics"`
- **`provider`** (`Literal["google_analytics", "posthog", "plausible"]`): The analytics provider.
- **`event_name`** (`str`): The event name to track.
- **`payload`** (`Optional[dict]`): Optional payload/properties for the event.

### `DataSourceAction`
Connects to an external data source provider.
- **`action_type`**: `"datasource"`
- **`provider`** (`Literal["google_sheets", "airtable", "notion"]`): The data source provider.
- **`api_endpoint`** (`str`): The API endpoint or URL.
- **`panel_position`** (`Literal["right", "left", "bottom", "top", "overlay", "none"]`): Position of the info panel. Defaults to `"none"`.

### `ExternalFormAction`
Embeds an external form provider.
- **`action_type`**: `"external_form"`
- **`provider`** (`Literal["typeform", "jotform", "hubspot", "google_forms", "surveymonkey", "qualtrics", "calendly"]`): The external form provider.
- **`form_url`** (`str`): The URL of the external form to embed.
- **`panel_position`** (`Literal["right", "left", "bottom", "top", "overlay", "none"]`): Position of the info panel. Defaults to `"none"`.

### `EcommerceAction`
Embeds a checkout or buy button.
- **`action_type`**: `"ecommerce"`
- **`provider`** (`Literal["stripe", "shopify"]`): The e-commerce provider.
- **`checkout_url`** (`str`): The URL for the checkout.
- **`panel_position`** (`Literal["right", "left", "bottom", "top", "overlay", "none"]`): Position of the info panel. Defaults to `"none"`.

### `RichMediaAction`
Embeds rich media players.
- **`action_type`**: `"rich_media"`
- **`provider`** (`Literal["vimeo", "wistia", "spotify", "soundcloud"]`): The rich media provider.
- **`media_url`** (`str`): The URL of the media to embed.
- **`panel_position`** (`Literal["right", "left", "bottom", "top", "overlay", "none"]`): Position of the info panel. Defaults to `"none"`.

### `BIAction`
Embeds Business Intelligence dashboards.
- **`action_type`**: `"bi"`
- **`provider`** (`Literal["metabase", "tableau", "powerbi"]`): The BI provider.
- **`dashboard_url`** (`str`): The URL of the dashboard.
- **`panel_position`** (`Literal["right", "left", "bottom", "top", "overlay", "none"]`): Position of the info panel. Defaults to `"none"`.

### `ReplitAction`
Embeds a Repl workspace.
- **`action_type`**: `"replit"`
- **`repl_url`** (`str`): The URL of the Repl.
- **`panel_position`** (`Literal["right", "left", "bottom", "top", "overlay", "none"]`): Position of the info panel. Defaults to `"none"`.

---

## Visual Animations & Effects

### `ExplodeAction`
Triggers an explosion animation onto a target SVG grid/hex layout.
- **`action_type`**: `"explode"`
- **`target_svg`** (`str`): The path or content of the stylized hex/grid SVG to explode into.
- **`duration_ms`** (`int`): Animation duration in milliseconds. Defaults to `1000`.

### `ZoomAction`
Programmatically zooms into an element or coordinate.
- **`action_type`**: `"zoom"`
- **`center`** (`list[float]`): The `[x, y]` center coordinate to zoom to.
- **`zoom_level`** (`float`): The ECharts zoom magnification level. Defaults to `2.0`.
- **`duration_ms`** (`int`): The duration of the zoom animation in milliseconds. Defaults to `500`.
- **`target_bbox`** (`Optional[list[float]]`): The `[min_x, min_y, max_x, max_y]` bounding box of the target element.
- **`zoom_to_size`** (`Optional[str]`): The percentage of the viewport the target bounding box should fill when zoomed. Defaults to `"90%"`.

### `LottieAction`
Renders a Lottie JSON animation.
- **`action_type`**: `"lottie"`
- **`lottie_url`** (`str`): URL to the Lottie JSON animation file.
- **`loop`** (`bool`): Whether the animation should loop. Defaults to `True`.
- **`autoplay`** (`bool`): Whether the animation should play automatically. Defaults to `True`.
- **`panel_position`** (`Literal["right", "left", "bottom", "top", "overlay", "none"]`): Position of the info panel. Defaults to `"none"`.

### `ConfettiAction`
Fires a confetti particle burst on the screen.
- **`action_type`**: `"confetti"`
- **`particle_count`** (`int`): Number of confetti particles. Defaults to `100`.
- **`spread`** (`int`): Spread of the confetti burst in degrees. Defaults to `70`.

### `LoadingAction`
Displays a loading animation effect.
- **`action_type`**: `"loading"`
- **`trigger`** (`Literal["load", "click"]`): When to trigger the loading animation. Defaults to `"click"`.
- **`duration_ms`** (`int`): Duration of the loading animation in milliseconds. Defaults to `2000`.
- **`text`** (`str`): Text to display during loading. Defaults to `"Loading..."`.
- **`style`** (`str`): Visual style of the loading animation (e.g. `"spinner"`, `"glitch"`, `"matrix"`, `"neon"`). Defaults to `"spinner"`.
- **`completion_html`** (`Optional[str]`): HTML content to display permanently in the overlay after loading completes.
- **`completion_color`** (`Optional[str]`): Color to apply to the SVG element after loading completes.
- **`panel_position`** (`Literal["right", "left", "bottom", "top", "overlay", "none"]`): Position of the info panel. Defaults to `"none"`.

---

## Utility UI Components

### `CompareAction`
Displays a before/after image slider.
- **`action_type`**: `"compare"`
- **`before_image`** (`str`): URL of the 'before' image.
- **`after_image`** (`str`): URL of the 'after' image.
- **`label_before`** (`str`): Label for the before image. Defaults to `"Before"`.
- **`label_after`** (`str`): Label for the after image. Defaults to `"After"`.
- **`panel_position`** (`Literal["right", "left", "bottom", "top", "overlay", "none"]`): Position of the info panel. Defaults to `"none"`.

### `ProgressBarAction`
Renders a progress bar.
- **`action_type`**: `"progress_bar"`
- **`title`** (`str`): Title of the progress bar.
- **`progress`** (`float`): Progress value between 0 and 100.
- **`color`** (`str`): Color of the progress bar. Defaults to `"#38bdf8"`.
- **`panel_position`** (`Literal["right", "left", "bottom", "top", "overlay", "none"]`): Position of the info panel. Defaults to `"none"`.

---

## Accessibility

### `A11yAction`
Injects ARIA labels and keyboard navigability attributes.
- **`action_type`**: `"a11y"`
- **`role`** (`str`): The ARIA role for the interactive element. Defaults to `"button"`.
- **`tabindex`** (`str`): The tabindex for keyboard navigation. Defaults to `"0"`.
- **`aria_label`** (`str`): The screen reader accessible label for the element.
