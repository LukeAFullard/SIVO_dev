# SIVO Streamlit Integration Example

This example demonstrates how to integrate SIVO with Streamlit using the custom bi-directional Streamlit component (`sivo.streamlit.component.sivo_component`).

## What is being shown
- Setting up a SIVO app from an inline SVG string containing a simple floorplan.
- Mapping static visual properties and tooltips using `sivo_app.map()`.
- Passing `callback_event` and `callback_payload` parameters in `sivo_app.map()` to send data from the frontend click event directly back to the Python Streamlit backend.
- Rendering the component using `sivo_component(sivo_app, key="...")`.
- Printing the return value of the Streamlit component (which contains the callback data) to the Streamlit UI.

## Key Code Snippets

```python
# Mapping a shape to trigger a Streamlit callback with a JSON payload
sivo_app.map(
    "room2",
    tooltip="<b>Conference Room 2</b><br/>Status: 🔴 In Use",
    callback_event="book_room",
    callback_payload={"room_id": "room2", "action": "book"},
    color="#ffaaa5",
    hover_color="#ff7b72"
)

# Render the SIVO app in Streamlit
result = sivo_component(sivo_app, key="sivo_example")
st.write(result)
```

## Running the example
To run the example, you must have Streamlit installed (`pip install streamlit`). Then execute:
```bash
streamlit run streamlit_app.py
```
This will open a new browser tab with the Streamlit app. Click on the defined zones (Room 2, Zone 3) to see the `callback_event` data appear in the "Component Return Value" section at the bottom of the page.
