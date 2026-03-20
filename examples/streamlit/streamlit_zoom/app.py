import os
import streamlit as st
from sivo import Sivo
from sivo.streamlit.component import sivo_component

def main():
    st.set_page_config(layout="wide")
    st.title("SIVO Programmatic Zooming")
    st.write("Control the map viewport programmatically.")

    svg_path = os.path.join(os.path.dirname(__file__), "sample.svg")
    sivo_app = Sivo.from_svg(svg_path)

    # Some basic styles
    sivo_app.map(element_id="sun", color="gold")
    sivo_app.map(element_id="mountain1", color="#a0a0a0")
    sivo_app.map(element_id="house", color="brown")

    col1, col2 = st.columns([2, 1])

    with col2:
        st.subheader("Controls")
        target_element = st.selectbox("Zoom to:", ["None", "sun", "mountain1", "house"])
        zoom_level = st.slider("Zoom Level", 1.0, 5.0, 2.0)

        zoom_config = None
        if target_element != "None":
            zoom_config = {
                "element_id": target_element,
                "zoom": zoom_level,
                "zoom_center": sivo_app.get_element_center(target_element)
            }

    with col1:
        sivo_component(
            sivo_app.infographic,
            key="sivo_zoom_demo",
            zoom_to=zoom_config,
            height=500
        )

if __name__ == "__main__":
    main()
