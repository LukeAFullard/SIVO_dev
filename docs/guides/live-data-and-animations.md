---
Last Updated: 2026-04-09
SIVO Version: 0.1.0
---

# H-15: Live Data and Animations Guide

Connecting SIVO to live API endpoints, WebSockets, and timeline animations.

## Table of Contents

1. **Introduction to Live Data in SIVO**
2. **Data Binding (`bind_data`)**
3. **Polling APIs (`bind_api`)**
4. **WebSockets (Live Streaming) (`bind_live`)**
5. **Timeline Animations (`bind_timeline`)**

## 1. Introduction to Live Data in SIVO

While SIVO excels at creating interactive static maps and dashboards, it also provides robust mechanisms for binding live and dynamic datasets. These capabilities transform static visuals into real-time operational dashboards or animated presentations. SIVO handles the complexity of polling, WebSocket connections, and timeline management on the frontend, allowing you to easily configure these behaviors in Python.

## 2. Data Binding (`bind_data`)

The `bind_data()` method binds quantitative data directly to SVG elements dynamically and applies a color scale. This is the foundation for creating choropleths or any visual where element colors represent data values.

### Example

```python
from sivo import Sivo

sivo = Sivo.from_svg("my_map.svg")

# Data format: Dict[element_id, Dict[metric_name, value]]
my_data = {
    "region_a": {"population": 15000},
    "region_b": {"population": 30000},
    "region_c": {"population": 5000}
}

sivo.bind_data(
    data=my_data,
    key="population",
    colors=["#e0f3f8", "#313695"], # Light blue to dark blue
    min_val=0,
    max_val=40000
)

sivo.to_html("data_bound_map.html")
```

The frontend will automatically interpolate the colors for each region based on its value relative to the `min_val` and `max_val` bounds.

## 3. Polling APIs (`bind_api`)

For data that updates periodically but doesn't require a constant live stream, you can use `bind_api()`. SIVO will generate the JavaScript required to poll the specified endpoint at regular intervals and update the mapped elements.

The API must return JSON. You can optionally use `data_path` (dot notation) to target a specific array or object within the response payload.

### Example

```python
from sivo import Sivo

sivo = Sivo.from_svg("dashboard.svg")

sivo.bind_api(
    url="https://api.example.com/sensors/latest",
    polling_interval_ms=10000, # Poll every 10 seconds
    method="GET",
    data_path="results.sensor_data"
)

sivo.to_html("polling_dashboard.html")
```

The frontend runtime expects the targeted data payload to contain an array of objects, where each object has properties that match elements defined in the SIVO map.

## 4. WebSockets (Live Streaming) (`bind_live`)

For true real-time telemetry, `bind_live()` connects the SIVO runtime to a WebSocket endpoint. This completely bypasses expensive full-page reloads (like in Streamlit) and mutates the ECharts canvas directly.

### Example

```python
from sivo import Sivo

sivo = Sivo.from_svg("factory_floor.svg")

sivo.bind_live(
    url="wss://live.example.com/telemetry",
    topic="machine_status",
    auth_token="optional-secure-token"
)

sivo.to_html("live_factory.html")
```

The WebSocket server should push messages in the following expected JSON format:
```json
{
  "element_id": "machine_01",
  "color": "#ff0000",
  "tooltip": "Temperature Critical: 95C"
}
```
SIVO will parse these messages and dynamically update the color and tooltip of the matching `element_id` on the fly.

## 5. Timeline Animations (`bind_timeline`)

To visualize data changes over time, use `bind_timeline()`. This method injects ECharts' native timeline controller, allowing users to play, pause, and scrub through data intervals.

### Example

```python
from sivo import Sivo

sivo = Sivo.from_svg("historical_map.svg")

# Data format: Dict[time_step, Dict[element_id, Dict[metric_name, value]]]
timeline_data = {
    "2020": {
        "region_a": {"metric": 10},
        "region_b": {"metric": 20}
    },
    "2021": {
        "region_a": {"metric": 15},
        "region_b": {"metric": 18}
    },
    "2022": {
        "region_a": {"metric": 25},
        "region_b": {"metric": 10}
    }
}

sivo.bind_timeline(
    data=timeline_data,
    key="metric",
    colors=["#fee5d9", "#a50f15"], # Light red to dark red
    min_val=0,
    max_val=30,
    auto_play=True,
    play_interval=2000, # 2 seconds per frame
    show_play_btn=True,
    loop=True
)

sivo.to_html("animated_map.html")
```
SIVO will automatically build the underlying ECharts `baseOption` and the array of `options` for each timestep, rendering a smooth animated transition between states.
