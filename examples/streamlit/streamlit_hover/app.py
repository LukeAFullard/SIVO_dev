import os
import streamlit as st
from sivo import Sivo
from sivo.streamlit.component import sivo_component

def main():
    st.set_page_config(layout="wide")
    st.title("SIVO Hover Callbacks")
    st.write("Hover over SVG elements to instantly update Streamlit state.")

    svg_path = os.path.join(os.path.dirname(__file__), "sample.svg")
    sivo_app = Sivo.from_svg(svg_path)

    # Note: frequent hover callbacks can be expensive. Use them deliberately.
    sivo_app.map(
        element_id="sun",
        hover_color="yellow",
        hover_callback_event="sun_hovered",
        hover_callback_payload={"message": "You are hovering over the Sun!"}
    )

    sivo_app.map(
        element_id="mountain1",
        hover_color="#c0c0c0",
        hover_callback_event="mountain_hovered",
        hover_callback_payload={"message": "You are hovering over Mountain 1!"}
    )

    col1, col2 = st.columns([2, 1])

    with col1:
        result = sivo_component(sivo_app.infographic, key="sivo_hover_demo", height=500)

    with col2:
        st.subheader("Live Hover Data")
        if result:
            st.json(result)
        else:
            st.info("Hover over the sun or mountains...")

if __name__ == "__main__":
    main()
