---
Last Updated: 2026-04-09
SIVO Version: 0.1.0
---

# H-10: Streamlit Integration Guide

How to use SIVO inside Streamlit applications.

## Table of Contents

1. [Introduction](#introduction)
2. [Setup](#setup)
3. [Usage](#usage)
   - [Basic Rendering](#basic-rendering)
   - [Handling Callbacks (Click & Hover)](#handling-callbacks-click--hover)
   - [Dynamic Colors](#dynamic-colors)
   - [Programmatic Zooming](#programmatic-zooming)

## Introduction

SIVO provides a custom component (`sivo_component`) that allows you to seamlessly embed interactive SIVO Infographics directly into your Streamlit applications. This integration uses a Streamlit V2 custom component with iframe message passing to enable bi-directional communication between your Python backend and the JavaScript frontend.

With `sivo_component`, you can:
- Render interactive SVG maps and infographics.
- Receive data back in Python when users click or hover over SVG elements.
- Update colors dynamically without triggering a full component re-render.
- Control the viewport programmatically (e.g., zoom to a specific element).

## Setup

The Streamlit component is included in the SIVO package under `sivo.streamlit.component`. Ensure you have both SIVO and Streamlit installed:

```bash
pip install sivo streamlit
```

Import the component in your Streamlit app:

```python
import streamlit as st
from sivo import Sivo
from sivo.streamlit.component import sivo_component
```

## Usage

### Basic Rendering

To display a SIVO object, you first initialize your `Sivo` application from an SVG file, then pass it to `sivo_component`.

```python
import streamlit as st
from sivo import Sivo
from sivo.streamlit.component import sivo_component

# Initialize SIVO from an SVG file
sivo_app = Sivo.from_svg("sample.svg")

# Map colors to elements
sivo_app.map(element_id="sun", color="gold", tooltip="This is the sun")
sivo_app.map(element_id="mountain", color="#a0a0a0")

# Render the SIVO component
sivo_component(
    sivo_app=sivo_app,
    key="sivo_basic_demo"
)
```

**Note:** The `sivo_component` expects a `Sivo` object.

### Handling Callbacks (Click & Hover)

You can capture user interactions (clicks and hovers) within the SIVO component and send that data back to Streamlit to update other parts of your UI.

Use the `callback_event` and `callback_payload` arguments in `sivo_app.map()` for clicks, and `hover_callback_event` / `hover_callback_payload` for hovers. The data returned by `sivo_component` will contain the payload.

```python
import streamlit as st
from sivo import Sivo
from sivo.streamlit.component import sivo_component

st.title("SIVO Callbacks")

sivo_app = Sivo.from_svg("sample.svg")

# Set up a click callback
sivo_app.map(
    element_id="sun",
    color="gold",
    hover_color="yellow",
    callback_event="sun_clicked",
    callback_payload={"name": "The Sun", "temp": "5778 K"}
)

# Set up a hover callback (Note: frequent hover callbacks can be expensive)
sivo_app.map(
    element_id="mountain1",
    color="#a0a0a0",
    hover_color="#c0c0c0",
    hover_callback_event="mountain_hovered",
    hover_callback_payload={"message": "Hovering over Mountain 1"}
)

col1, col2 = st.columns([2, 1])

with col1:
    # Render and capture the result
    result = sivo_component(sivo_app, key="sivo_callback_demo")

with col2:
    st.subheader("Callback Data")
    if result:
        st.json(result) # This will display the callback_payload
    else:
        st.info("Interact with the map...")
```

### Dynamic Colors

Normally, changing arguments in Streamlit triggers a full re-render of the component, which can cause flickering. To smoothly update colors in real-time (e.g., connected to a `st.color_picker`), use the `dynamic_colors` argument in `sivo_component`. This sends a message to the frontend to update colors via JavaScript instantly.

```python
import streamlit as st
from sivo import Sivo
from sivo.streamlit.component import sivo_component

sivo_app = Sivo.from_svg("sample.svg")

# Base maps
sivo_app.map(element_id="sun", color="yellow")
sivo_app.map(element_id="mountain1", color="#a0a0a0")

col1, col2 = st.columns([2, 1])

with col2:
    sun_color = st.color_picker("Pick Sun Color", "#FFD700")
    mountain_color = st.color_picker("Pick Mountain Color", "#A0A0A0")

    # Define the dynamic mapping
    dynamic_colors = {
        "sun": sun_color,
        "mountain1": mountain_color
    }

with col1:
    sivo_component(
        sivo_app,
        key="sivo_dynamic_colors_demo",
        dynamic_colors=dynamic_colors # Pass the dict here
    )
```

### Programmatic Zooming

You can control the map's viewport programmatically from Streamlit controls (like buttons or dropdowns). When the `zoom_to` argument is changed, the component sends a command to ECharts to smoothly zoom and pan to the specified element ID.

```python
import streamlit as st
from sivo import Sivo
from sivo.streamlit.component import sivo_component

sivo_app = Sivo.from_svg("sample.svg")

sivo_app.map(element_id="sun", color="gold")
sivo_app.map(element_id="mountain1", color="#a0a0a0")

target_element = st.selectbox("Zoom to:", ["None", "sun", "mountain1"])

# Only pass the string ID of the element you want to zoom to
zoom_target = target_element if target_element != "None" else None

sivo_component(
    sivo_app,
    key="sivo_zoom_demo",
    zoom_to=zoom_target
)
```

*(Under the hood, SIVO automatically calculates the center of the target element's bounding box and sends a postMessage to animate the zoom).*
