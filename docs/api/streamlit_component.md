---
Last Updated: 2026-04-09
SIVO Version: 0.1.0
---

# Streamlit Component API Reference

The `sivo_component` function allows you to render a SIVO Infographic inside a Streamlit application using a custom V2 component.

## `sivo_component`

**Location:** `src/sivo/streamlit/component.py`

Renders an interactive SIVO map or infographic directly within your Streamlit layout. It uses Streamlit's custom component API (V2) to embed the compiled SIVO HTML bundle via an iframe and supports bidirectional communication.

### Signature

```python
def sivo_component(
    sivo_app: Sivo,
    key: Optional[str] = None,
    custom_css: Optional[str] = None,
    custom_js: Optional[str] = None,
    zoom_to: Optional[str] = None,
    dynamic_colors: Optional[Dict[str, str]] = None
) -> Any
```

### Parameters

* **`sivo_app`** (`Sivo`): The SIVO orchestrator instance to render. This instance must be fully configured before passing it to the component.
* **`key`** (`str`, optional): An optional string that uniquely identifies this component. If you have multiple SIVO components on the same page, or if you need to maintain state across re-renders, provide a unique key for each.
* **`custom_css`** (`str`, optional): An optional CSS string to inject into the component's HTML bundle.
* **`custom_js`** (`str`, optional): An optional JavaScript string to inject into the component's HTML bundle.
* **`zoom_to`** (`str`, optional): An SVG element ID to zoom to programmatically. This uses JavaScript messaging to instruct the embedded SIVO app to zoom into the specified element's bounding box without performing a full component re-render.
* **`dynamic_colors`** (`dict`, optional): A dictionary mapping `element_id` to color hex codes (e.g., `{"US-CA": "#ff0000"}`). This updates the fill colors of the specified elements dynamically via postMessage without re-rendering the iframe.

### Returns

* **`Any`**: The value returned by the Streamlit component. This typically contains the payload from any interactive events triggered inside the SIVO map, such as `sivo_click` or `sivo_hover` events sent from the frontend.

### Usage Example

```python
import streamlit as st
from sivo.core.sivo import Sivo
from sivo.streamlit.component import sivo_component

st.title("SIVO Streamlit Integration")

# Load and configure SIVO
sivo = Sivo.from_svg("map.svg")
sivo.map("region-1", tooltip="Region 1", fill_color="#blue")

# Render component
event_data = sivo_component(
    sivo_app=sivo,
    key="my_map",
    zoom_to=st.session_state.get("zoom_target"),
    dynamic_colors={"region-1": "#ff0000"}
)

if event_data:
    st.write("You interacted with:", event_data)
```

## Features

- **Bidirectional Communication:** Interaction events in the SIVO map (e.g., clicks and hovers) are sent back to the Streamlit backend and returned by the `sivo_component` call.
- **Dynamic Updates:** Features like `zoom_to` and `dynamic_colors` utilize `postMessage` to update the SIVO state on the client side without needing to re-generate the entire HTML bundle or reload the iframe.
