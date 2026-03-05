import sys
import os
import streamlit as st

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from sivo.core.infographic import Infographic
from sivo.streamlit.component import sivo_component

st.set_page_config(page_title="SIVO Streamlit V2 Component Example", layout="wide")

st.title("SIVO Streamlit V2 Component Example")
st.markdown("This example demonstrates rendering an interactive SVG infographic using the `st.components.v2.component` API.")

svg_content = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300" width="100%" height="100%">
    <!-- Base styling -->
    <style>
        .shape { fill: #e0e0e0; stroke: #999; stroke-width: 2; transition: all 0.3s; }
        .shape:hover { fill: #c0c0c0; cursor: pointer; }
    </style>

    <!-- Room 1 -->
    <path id="room1" class="shape" d="M50 50 L150 50 L150 150 L50 150 Z" />
    <text x="100" y="105" text-anchor="middle" font-family="Arial" font-size="14">Room 1</text>

    <!-- Room 2 -->
    <path id="room2" class="shape" d="M160 50 L260 50 L260 150 L160 150 Z" />
    <text x="210" y="105" text-anchor="middle" font-family="Arial" font-size="14">Room 2</text>

    <!-- Circle Zone -->
    <circle id="zone3" class="shape" cx="155" cy="220" r="50" />
    <text x="155" y="225" text-anchor="middle" font-family="Arial" font-size="14">Zone 3</text>
</svg>
"""

# 1. Create Infographic from SVG string
infographic = Infographic.from_string(svg_content)

# 2. Map interactions
infographic.map(
    "room1",
    tooltip="<b>Conference Room 1</b><br/>Status: 🟢 Available",
    color="#a8e6cf",
    hover_color="#56c596",
    border_width=3,
    border_color="#2e8c61"
)

infographic.map(
    "room2",
    tooltip="<b>Conference Room 2</b><br/>Status: 🔴 In Use",
    color="#ffaaa5",
    hover_color="#ff7b72",
    border_width=3,
    border_color="#c94c4c"
)

infographic.map(
    "zone3",
    tooltip="<b>Break Area</b><br/>Status: 🟡 Needs Cleaning",
    color="#ffd3b6",
    hover_color="#ffb385",
    border_width=3,
    border_color="#d68c45"
)

st.subheader("Interactive Graphic")
st.markdown("Hover over the rooms and zones to see tooltips and custom styles mapped from Python!")

# Render using the custom V2 component
result = sivo_component(infographic, key="sivo_example")

st.markdown("---")
st.subheader("Component Return Value")
st.write(result)
