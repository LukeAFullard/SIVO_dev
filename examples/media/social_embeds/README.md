# Social Embeds Example

This example demonstrates how to integrate external social media platforms and generic website iframes into an interactive SIVO SVG canvas. It shows how static SVG graphical elements (like the Wikipedia, Instagram, TikTok logos, or a generic icon) can be turned into interactive buttons that fetch and display external content.

### Purpose and Features Tested
- **Social Media Integration**: Passing the `social` dictionary argument to `sivo_app.map()` to tell SIVO which provider's content to embed. Providers showcased here include `wikipedia`, `instagram`, `tiktok`, and a generic `website`.
- **Side Panel Overlay**: Using `panel_position="right"` to ensure the external content opens in a designated side panel, rather than replacing the current view or failing to appear (the default position is `'none'`). This is critical for keeping the user on the canvas while letting them view the content.
- **Styling and Tooltips**: Testing visual feedback parameters like `color` (default fill color), `hover_color` (fill color on mouse hover), and `tooltip` (text shown on hover).

### Setup and Steps
1. An SVG is defined containing four interactive `<g>` elements with unique IDs (`btn_wiki`, `btn_insta`, `btn_tiktok`, `btn_web`).
2. A `Sivo` instance is initialized from this SVG string.
3. The `map()` method is called for each ID to link it to a specific URL using the appropriate social provider.
4. The output is generated to `output.html`.

### Relevant Code Bits

Here is the code showing how the SVG elements are mapped to the social embeds and how the side panel is configured:

```python
# Embedding Wikipedia content. Notice panel_position="right".
sivo_app.map(
    "btn_wiki",
    social={"provider": "wikipedia", "url": "https://en.wikipedia.org/wiki/Python_(programming_language)"},
    tooltip="Wikipedia API Fetch",
    panel_position="right",
    hover_color="#eaecf0",
    color="#f8f9fa"
)

# Embedding Instagram content.
sivo_app.map(
    "btn_insta",
    social={"provider": "instagram", "url": "https://www.instagram.com/p/C0f9W5aIxtA/"},
    tooltip="Instagram Embed",
    panel_position="right",
    hover_color="#a0296e",
    color="#c13584"
)
```

By ensuring `panel_position` is explicitly set to `"right"` (or another valid panel position like `"left"`, `"bottom"`, etc.), the embeds will properly appear in an overlay container when the respective icon is clicked, allowing users to interact with the Wikipedia page, view an Instagram post, watch a TikTok, or explore an embedded webpage.
