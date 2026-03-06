import os
import streamlit as st
from sivo import Sivo
from sivo.streamlit.component import sivo_component

def main():
    st.set_page_config(layout="wide")
    st.title("SIVO Comprehensive Dashboard")

    svg_path = os.path.join(os.path.dirname(__file__), "sample.svg")
    sivo_app = Sivo.from_svg(svg_path)

    # 1. Advanced interactions
    sivo_app.map(
        element_id="sun",
        tooltip="Main Star",
        color="gold",
        animation="pulse",
        callback_event="select_sun"
    )

    # 2. Add overlays
    sivo_app.add_marker("mountain1", icon="🏔️", label="Base Camp")

    col1, col2 = st.columns([3, 1])

    with col2:
        st.subheader("Controls")
        dynamic_color = st.color_picker("Live Sun Color", "#FFD700")
        do_zoom = st.button("Zoom to Mountain")

        zoom_cfg = None
        if do_zoom:
            zoom_cfg = {
                "element_id": "mountain1",
                "zoom": 3,
                "zoom_center": sivo_app.get_element_center("mountain1")
            }

    with col1:
        result = sivo_component(
            sivo_app.infographic,
            key="sivo_dashboard",
            dynamic_colors={"sun": dynamic_color},
            zoom_to=zoom_cfg,
            height=600
        )

    if result:
        st.success(f"Dashboard Event Received: {result}")

if __name__ == "__main__":
    main()
