# Mixed Features & Background Image Dashboard Example

This example demonstrates how to use `SivoDashboard` with CSS grid to create a dashboard incorporating various media types—text, interactive Sivo graphs, external images, and video iframes—while demonstrating how to elegantly style a responsive background image behind the CSS grid.

## Purpose

The main goal of this example is to show how:
1. `add_html_block()` can be used not just for simple widgets, but for embedding standard web elements like images (`<img>`) and video iframes (`<iframe>`).
2. `SivoDashboard` supports a `background_image_url` parameter that automatically applies a background image and adds a translucent, blurred background to the grid cards, allowing the image to show through elegantly.
4. The background image behaves dynamically as the layout reshapes from desktop to mobile views based on the defined grid layout.

## Key Code Snippets

### Setting a Responsive CSS Grid
```python
dashboard.set_grid_layout(
    desktop='''
"header header header"
"text graph image"
"video graph image"
    ''',
    mobile='''
"header"
"text"
"graph"
"image"
"video"
    '''
)
```

### Setting a Background Image
You can pass the `background_image_url` parameter directly when initializing the `SivoDashboard`. The dashboard will automatically apply the necessary CSS styling to fix the image and apply a blur effect to the overlaying cards.

```python
dashboard = SivoDashboard(
    title="Mixed Features with Background",
    columns=3,
    background_image_url="https://images.unsplash.com/photo-1448375240586-882707db888b?q=80&w=2070&auto=format&fit=crop"
)
```

### Embedding a Video Iframe
A standard YouTube or Vimeo iframe can be easily embedded using `add_html_block()`.

```python
video_html = '''
<div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%;">
    <h3>Video Feature</h3>
    <iframe width="100%" height="250" src="..." title="YouTube video player" frameborder="0" allowfullscreen style="border-radius: 8px;"></iframe>
</div>
'''
dashboard.add_html_block("video_block", video_html, grid_area="video")
```

## Running the Example

Navigate to the root directory and execute:

```bash
python examples/dashboards/mixed_features_background/main.py
```

This will generate an `output.html` file in this directory. Open `output.html` in a web browser to view the generated dashboard. Try resizing the browser window to see how the grid components reflow and how the background image scales dynamically while remaining fixed during scrolling.
