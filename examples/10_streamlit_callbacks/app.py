import os
import streamlit as st
from sivo import Sivo
from sivo.streamlit.component import sivo_component

def main():
    st.set_page_config(layout="wide")
    st.title("SIVO Basic Callbacks")
    st.write("Click on an SVG element to trigger a callback in Streamlit.")

    svg_path = os.path.join(os.path.dirname(__file__), "sample.svg")
    sivo_app = Sivo.from_svg(svg_path)

    sivo_app.map(
        element_id="sun",
        tooltip="Click me to trigger a sun event",
        color="gold",
        hover_color="yellow",
        callback_event="sun_clicked",
        callback_payload={"name": "The Sun", "temp": "5778 K"}
    )

    sivo_app.map(
        element_id="mountain1",
        tooltip="Click me to trigger a mountain event",
        color="#a0a0a0",
        hover_color="#c0c0c0",
        callback_event="mountain_clicked",
        callback_payload={"height": "8848 m"}
    )

    col1, col2 = st.columns([2, 1])

    with col1:
        # Render the SIVO component
        result = sivo_component(sivo_app.infographic, key="sivo_callback_demo", height=500)

    with col2:
        st.subheader("Event Callback Output")
        if result:
            st.json(result)
        else:
            st.info("Awaiting user click interaction...")

if __name__ == "__main__":
    main()
