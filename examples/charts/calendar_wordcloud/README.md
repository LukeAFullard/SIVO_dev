# Calendar Heatmap and Word Cloud Example

This example demonstrates how to integrate rich interactive charts within SIVO, specifically a Calendar Heatmap and a Word Cloud.

## Purpose

The main goal of this example is to show how data visualizations can be mapped directly to elements on an SVG canvas and presented within an interactive panel. It highlights two types of charts:

1.  **Calendar Heatmap:** Maps a time-series dataset to an activity calendar (e.g., GitHub commit history).
2.  **Word Cloud:** Displays text data scaled by frequency or importance, shaped by a custom image mask.

Additionally, this example covers an important UI configuration setting: overriding the default panel position.

## Key Features Displayed

### 1. The Panel Position Default
In newer versions of SIVO, the `default_panel_position` has been updated to `"none"`. In this script, it has been manually set to `"bottom"` during initialization to ensure charts pop up at the bottom of the screen when clicked.

```python
sivo_app = Sivo.from_string(svg_string, default_panel_position="bottom")
```

### 2. Calendar Heatmap Mapping
The script uses `sivo_app.map_calendar_heatmap_chart()` to map an element ID (`calendar_box`) to a generated dataset of daily activity values over a defined range.

```python
sivo_app.map_calendar_heatmap_chart(
    element_id="calendar_box",
    title="2017 Commit History",
    data=calendar_data,
    calendar_range="2017",
    tooltip="View full calendar heatmap"
)
```

### 3. Word Cloud Custom Masks
To make a word cloud conform to a specific shape, a base64 encoded image string is read from `mask_b64.txt`. This defines a solid silhouette area into which the words are rendered using `map_word_cloud_chart`.

```python
mask_path = os.path.join(os.path.dirname(__file__), "mask_b64.txt")
large_mask_b64 = open(mask_path).read().strip()

sivo_app.map_word_cloud_chart(
    element_id="wordcloud_box",
    title="Topic Relevance (Circle Mask)",
    data=wordcloud_data,
    mask_image=large_mask_b64,
    tooltip="View full word cloud",
    # ...
)
```

## Running the Example

Run this file directly via python, ensuring you have SIVO installed or available via your `PYTHONPATH`:

```bash
PYTHONPATH=src python examples/charts/calendar_wordcloud/main.py
```

This generates `output.html`. Open `output.html` in your web browser. Click on the rectangles to view the respective interactive charts opening up in the bottom panel.