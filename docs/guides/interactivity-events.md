---
Last Updated: 2026-04-09
SIVO Version: 0.1.0
---

# H-05: Interactivity & Events Guide

This guide covers how to use Python callbacks, tooltips, click events, dynamic state transitions, and audio playback in SIVO.

## Table of Contents

1. [Tooltips and Hover Effects](#1-tooltips-and-hover-effects)
2. [Click Events & The Sidebar Panel](#2-click-events--the-sidebar-panel)
3. [Dynamic State Transitions (`toggle_image`)](#3-dynamic-state-transitions)
4. [Audio Playback on Event](#4-audio-playback-on-event)
5. [Form Events and External Callbacks](#5-form-events-and-external-callbacks)

---

## 1. Tooltips and Hover Effects

SIVO provides built-in interactivity simply by mapping the `tooltip` property to an SVG element.

### Basic Tooltip Usage

When you map a `tooltip`, SIVO automatically binds mouse hover events to that SVG element.

```python
from sivo.core.sivo import Sivo

sivo = Sivo.from_svg("map.svg")

# Basic text tooltip
sivo.map("region_1", tooltip="Northern District")
```

### Advanced Tooltip Formatting

You can inject rich HTML into tooltips, which allows you to include images, formatted text, and data points.

```python
html_content = """
<div style="padding: 5px;">
    <h4>Northern District</h4>
    <p>Population: <strong>1.2M</strong></p>
</div>
"""
sivo.map("region_1", tooltip="Northern District", html=html_content)
```

You can also use custom `hover_color` or `hover_image` to style an element visually while hovered:

```python
sivo.map("region_1", hover_color="#ffcc00")
sivo.map("region_2", hover_image="https://example.com/hover.png")
```

---

## 2. Click Events & The Sidebar Panel

SIVO supports creating rich informative sidebars triggered when an element is clicked. By default, the sidebar is hidden.

### Enabling the Sidebar

To display the HTML content associated with an element in a panel upon click, define the `panel_position`. Available positions are `right`, `left`, `bottom`, `top`, `overlay`, or `none`.

```python
sivo.map(
    "region_1",
    tooltip="Click for more info",
    html="<h2>Northern District Details</h2><p>Here is some expanded information.</p>",
    panel_position="right"
)
```

When clicked, the SIVO runtime will slide open a sidebar on the right and render the `html` content.

---

## 3. Dynamic State Transitions

Dynamic visual states can be tied to interactive elements.

*Note: The highly requested `cycle_state` parameter to dynamically update multiple CSS properties across sequential clicks is currently planned as a future enhancement.*

### The `toggle_image` Action

Currently, you can dynamically transition element states using the `toggle_image` action. This will cycle an element's background image fill through a specified list of URLs each time it is clicked.

```python
sivo.map(
    "interactive_button",
    toggle_image={
        "target_id": "interactive_button",
        "image_urls": [
            "https://example.com/state_off.png",
            "https://example.com/state_on.png"
        ]
    }
)
```

---

## 4. Audio Playback on Event

SIVO can trigger audio playback when a user clicks on an element.

```python
sivo.map(
    "play_button",
    audio="https://example.com/sound_clip.mp3"
)
```

### Handling Browser Autoplay Policies

Modern web browsers enforce strict autoplay policies, requiring a user gesture before audio can play. Because SIVO triggers audio explicitly on user interaction (`click` events), these policies are generally satisfied automatically.

Internal JS Snippet reference handling the audio playback safely:

```javascript
// Internal SIVO runtime handling audio
var audio = new Audio(action.audio_url);
audio.play().catch(e => console.error("Audio playback failed:", e));
```

---

## 5. Form Events and External Callbacks

SIVO makes it easy to integrate your frontend application logic with external systems via standard Javascript `postMessage` calls from the iframe.

### Callback Events

When a `callback_event` is mapped to an element, the SIVO frontend dispatches a `sivo_click` message to the parent window containing the element ID, event name, and optional payload.

```python
sivo.map(
    "submit_btn",
    callback_event="process_data",
    callback_payload={"status": "approved", "id": 123}
)
```

**JavaScript Parent Window Listener:**
```javascript
window.addEventListener("message", function(event) {
    if (event.data.type === "sivo_click" && event.data.payload.event_name === "process_data") {
        console.log("Processing data:", event.data.payload.data);
    }
});
```

### Hover Callbacks

You can also hook into `mouseover` events by defining a `hover_callback_event`:

```python
sivo.map("region_1", hover_callback_event="user_hovered_region_1")
```

This sends a `sivo_hover` event type to the parent window.

### Built-in Form Action

SIVO can dynamically render a form in the panel. When submitted, it fires a `sivo_click` message containing the form data.

```python
sivo.map(
    "contact_us",
    form_fields=[
        {"name": "email", "type": "email", "label": "Your Email"},
        {"name": "message", "type": "text", "label": "Message"}
    ],
    form_submit_event="contact_form_submit",
    panel_position="right"
)
```
