import os
from sivo import SivoDashboard, Sivo

def create_fade_in_dashboard():
    """
    Demonstrates using the 'fade_in' feature in a multi-block SIVO dashboard layout.
    """

    # 1. Create Dashboard
    dashboard = SivoDashboard(
        title="Fade-In Dashboard",
        theme="light",
        columns=2
    )

    # 2. Add some simple SVG blocks
    svg_box = """<?xml version="1.0" encoding="utf-8"?>
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
        <rect id="bg" x="0" y="0" width="100" height="100" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2"/>
        <text id="label" x="50" y="50" font-family="sans-serif" font-size="12" text-anchor="middle" dominant-baseline="middle" fill="#334155">Block</text>
    </svg>
    """

    # Block 1: Fades in immediately
    block1 = Sivo.from_string(svg_box)
    block1.map("bg", tooltip="Immediate Fade", color="#bae6fd", fade_in=True)
    dashboard.add_sivo_block(block_id="b1", sivo_app=block1)

    # Block 2: Fades in after 5s
    block2 = Sivo.from_string(svg_box)
    block2.map("bg", tooltip="5s Delay", color="#bbf7d0", fade_in=True, fade_start_time_ms=5000)
    dashboard.add_sivo_block(block_id="b2", sivo_app=block2)

    # Block 3: Fades in after 10s
    block3 = Sivo.from_string(svg_box)
    block3.map("bg", tooltip="10s Delay", color="#fef08a", fade_in=True, fade_start_time_ms=10000)
    dashboard.add_sivo_block(block_id="b3", sivo_app=block3)

    # Block 4: Pulses continuously after 15s
    block4 = Sivo.from_string(svg_box)
    block4.map("bg", tooltip="15s Delay + Pulse", color="#fecaca", fade_in=True, fade_pulse=True, fade_start_time_ms=15000)
    dashboard.add_sivo_block(block_id="b4", sivo_app=block4)

    # 3. Export HTML
    output_filename = "fade_in_dashboard.html"
    dashboard.to_html(output_filename)
    print(f"Generated {output_filename}. Open this file in your browser to see the dashboard fade effects.")

if __name__ == "__main__":
    create_fade_in_dashboard()