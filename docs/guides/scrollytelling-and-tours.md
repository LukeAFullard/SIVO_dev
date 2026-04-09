---
Last Updated: 2026-04-09
SIVO Version: 0.1.0
---

# H-17: Scrollytelling and Tours Guide

Building narrative-driven data presentations using `bind_scrollytelling` and `bind_tour`.

## Table of Contents

1. **Introduction to Narrative Visualizations**
   - Guiding the user through your interactive SIVO map.
2. **Scrollytelling**
   - Using `bind_scrollytelling()` to change views as the user scrolls.
   - Example configuration and steps.
3. **Interactive Tours**
   - Using `bind_tour()` to create a step-by-step guided walkthrough.
   - Triggering tooltips, zooms, and highlights automatically.
4. **Best Practices**
   - Designing effective step transitions and maintaining context.

## 1. Introduction to Narrative Visualizations

SIVO is not just for creating static or purely exploratory maps. You can use it to guide your users through a narrative, explaining different parts of the map or visualization sequentially. SIVO provides two primary methods for this:

- **Scrollytelling (`bind_scrollytelling`)**: As the user scrolls down the page, the text content updates, and the map simultaneously pans, zooms, highlights, and plays audio based on the active "step."
- **Guided Tours (`bind_tour`)**: A more explicit, modal-based walkthrough where the user clicks "Next" or "Previous" to advance through steps.

These features are powered by SIVO's declarative API, where you define an array of steps, and SIVO handles the complex scroll-event or click-event logic, view transitions, and state management on the frontend.

## 2. Scrollytelling

Scrollytelling keeps your map "sticky" on one side of the screen while a panel of text scrolls on the other side. As different text sections enter the viewport, the map reacts.

To enable scrollytelling, use the `bind_scrollytelling` method on your `Sivo` instance.

### The `ScrollytellingStepConfig` Schema

Each step is defined by a dictionary (parsed as a `ScrollytellingStepConfig` Pydantic model) that dictates what should happen:

*   `content` (str): The HTML content for the step text that the user reads.
*   `zoom_to` (Optional[str]): The SVG Element ID to zoom and pan to when this step becomes active.
*   `zoom_to_size` (str): The percentage of the viewport the target bounding box should fill (default: "90%").
*   `zoom_level` (float): A generic zoom multiplier (default: 2.0).
*   `colors` (Optional[Dict[str, str]]): A mapping of SVG Element IDs to CSS colors to apply during this step. This is useful for highlighting specific elements or fading others out.
*   `show_tooltips` (Optional[List[str]]): A list of SVG Element IDs whose tooltips should be programmatically forced open during this step.
*   `audio_url` (Optional[str]): Optional audio file URL to play automatically when this step is reached.

### Scrollytelling Example

Here's an example of setting up a scrollytelling narrative:

```python
from sivo import Sivo
import os

svg_content = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 600">
  <rect id="section1" x="100" y="100" width="200" height="200" fill="#f0f0f0" stroke="#ccc"/>
  <text x="200" y="200" font-size="24" text-anchor="middle">Data Center</text>

  <circle id="section2" cx="700" cy="200" r="100" fill="#f0f0f0" stroke="#ccc"/>
  <text x="700" y="200" font-size="24" text-anchor="middle">Logistics</text>

  <path id="section3" d="M 300 400 L 700 400 L 500 550 Z" fill="#f0f0f0" stroke="#ccc"/>
  <text x="500" y="470" font-size="24" text-anchor="middle">HQ</text>
</svg>
"""

# Initialize Sivo App
sivo_app = Sivo.from_string(svg_content)

# Map standard tooltips
sivo_app.map("section1", tooltip="Data Center (Active)")
sivo_app.map("section2", tooltip="Logistics Hub (Active)")
sivo_app.map("section3", tooltip="Headquarters (Active)")

# Define Scrollytelling narrative
steps = [
    {
        "content": "<h1>1. The Global Network</h1><p>Our operations span across three main hubs. Scroll down to take a closer look.</p>",
        "colors": {
            "section1": "#f0f0f0",
            "section2": "#f0f0f0",
            "section3": "#f0f0f0"
        }
    },
    {
        "content": "<h2>2. The Data Center</h2><p>This is where all our processing happens. It handles over 10TB of data per second.</p>",
        "zoom_to": "section1",
        "zoom_level": 2.5,
        "colors": {
            "section1": "#3b82f6",  # Highlight blue
            "section2": "#f0f0f0",
            "section3": "#f0f0f0"
        },
        "show_tooltips": ["section1"]
    },
    {
        "content": "<h2>3. The Logistics Hub</h2><p>Physical goods are routed through this circular zone, ensuring 24-hour delivery.</p>",
        "zoom_to": "section2",
        "zoom_level": 2.5,
        "colors": {
            "section1": "#f0f0f0",
            "section2": "#10b981",  # Highlight green
            "section3": "#f0f0f0"
        },
        "show_tooltips": ["section2"]
    },
    {
        "content": "<h2>4. Headquarters</h2><p>The central triangle coordinates both data and physical routing.</p>",
        "zoom_to": "section3",
        "zoom_level": 2.0,
        "colors": {
            "section1": "#f0f0f0",
            "section2": "#f0f0f0",
            "section3": "#8b5cf6"  # Highlight purple
        },
        "show_tooltips": ["section3"]
    }
]

# Bind the scrollytelling steps
sivo_app.bind_scrollytelling(steps)

# Export
sivo_app.to_html("scrollytelling.html")
```

## 3. Interactive Tours

Guided tours are similar to scrollytelling, but instead of scrolling, the user progresses via a "Next/Previous" UI (often rendered as a modal or a floating box over the map).

To enable a tour, use the `bind_tour` method.

### The `TourStepConfig` Schema

The tour step configuration is very similar to scrollytelling:

*   `content` (str): The HTML content for the tour step tooltip/modal.
*   `zoom_to` (Optional[str]): Element ID to zoom to.
*   `zoom_to_size` (str): The percentage of the viewport the target bounding box should fill (default: "90%").
*   `zoom_level` (float): Zoom level multiplier.
*   `show_tooltips` (Optional[List[str]]): List of Element IDs to show tooltips for automatically.
*   `audio_url` (Optional[str]): Optional audio file URL to play automatically.

### Guided Tour Example

```python
from sivo import Sivo

svg_content = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 600">
  <rect id="gallery" x="100" y="100" width="200" height="200" fill="#e5e7eb" stroke="#94a3b8" stroke-width="2"/>
  <text x="200" y="200" font-size="24" text-anchor="middle">Art Gallery</text>

  <rect id="cafe" x="700" y="100" width="200" height="200" fill="#e5e7eb" stroke="#94a3b8" stroke-width="2"/>
  <text x="800" y="200" font-size="24" text-anchor="middle">Cafe</text>

  <rect id="giftshop" x="400" y="400" width="200" height="150" fill="#e5e7eb" stroke="#94a3b8" stroke-width="2"/>
  <text x="500" y="480" font-size="24" text-anchor="middle">Gift Shop</text>
</svg>
"""

sivo_app = Sivo.from_string(svg_content)

# Map standard tooltips for the tour to trigger
sivo_app.map("gallery", tooltip="Main Art Gallery", html="<p>Featuring modern artists.</p>")
sivo_app.map("cafe", tooltip="Museum Cafe", html="<p>Coffee and pastries.</p>")
sivo_app.map("giftshop", tooltip="Gift Shop", html="<p>Souvenirs and books.</p>")

# Define Guided Tour Steps
steps = [
    {
        "content": "<h3>Welcome to the Museum Tour</h3><p>We'll guide you through the main exhibits. Click <b>Next</b> to begin.</p>",
    },
    {
        "content": "<h3>1. Art Gallery</h3><p>First stop: the main exhibition hall.</p>",
        "zoom_to": "gallery",
        "zoom_level": 2.5,
        "show_tooltips": ["gallery"]
    },
    {
        "content": "<h3>2. Museum Cafe</h3><p>Take a break and grab a coffee.</p>",
        "zoom_to": "cafe",
        "zoom_level": 2.5,
        "show_tooltips": ["cafe"]
    },
    {
        "content": "<h3>3. Gift Shop</h3><p>Don't forget to exit through the gift shop!</p>",
        "zoom_to": "giftshop",
        "zoom_level": 2.5,
        "show_tooltips": ["giftshop"]
    },
    {
        "content": "<h3>End of Tour</h3><p>Enjoy the rest of your visit!</p>"
    }
]

# Bind the tour to the app
sivo_app.bind_tour(steps)

sivo_app.to_html("guided_tour.html")
```

## 4. Best Practices

*   **Meaningful Highlights**: Use the `colors` property (in scrollytelling) to grey-out irrelevant parts of the map while highlighting the active element. This dramatically improves focus.
*   **Audio Triggers**: If using `audio_url`, ensure the audio clips are short. Note that strict browser autoplay policies may block the very first audio playback if the user hasn't interacted with the page yet, so consider adding a "Start Tour" or "Start Scrollytelling" button or instruction at the top.
*   **Provide Exits**: If the user wants to break out of the scrollytelling or tour, make sure your map allows regular interaction if that's desired, or use `lock_canvas=True` during initialization if you want to force them to stick to the narrative path.
