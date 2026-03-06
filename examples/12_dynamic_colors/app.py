import os
import streamlit as st
from sivo import Sivo
from sivo.streamlit.component import sivo_component

def main():
    st.set_page_config(layout="wide")
    st.title("SIVO Dynamic Colors")
    st.write("Updates colors without triggering a full re-render of the component.")

    svg_path = os.path.join(os.path.dirname(__file__), "sample.svg")
    sivo_app = Sivo.from_svg(svg_path)

    # Base colors
    sivo_app.map(element_id="sun", color="yellow")
    sivo_app.map(element_id="mountain1", color="#a0a0a0")

    col1, col2 = st.columns([2, 1])

    with col2:
        st.subheader("Control Panel")
        sun_color = st.color_picker("Pick Sun Color", "#FFD700")
        mountain_color = st.color_picker("Pick Mountain Color", "#A0A0A0")

        dynamic_colors = {
            "sun": sun_color,
            "mountain1": mountain_color
        }

    with col1:
        # Pass dynamic_colors to instantly apply colors via frontend JS postMessage
        sivo_component(
            sivo_app.infographic,
            key="sivo_dynamic_colors_demo",
            dynamic_colors=dynamic_colors,
            height=500
        )

if __name__ == "__main__":
    main()
