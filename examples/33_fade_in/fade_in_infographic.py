import os
from sivo.core.sivo import Sivo

def create_fade_in_example():
    """
    Demonstrates using the 'fade_in' and 'fade_pulse' feature to slowly reveal
    or pulse mapped elements in a SIVO infographic.
    """

    # 1. Provide an SVG string
    # We will draw a simple grid of rectangles.
    svg_content = """<?xml version="1.0" encoding="utf-8"?>
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500">
        <rect id="rect1" name="rect1" x="50" y="50" width="150" height="150" fill="#cbd5e1" stroke="#334155" stroke-width="2"/>
        <rect id="rect2" name="rect2" x="250" y="50" width="150" height="150" fill="#cbd5e1" stroke="#334155" stroke-width="2"/>
        <rect id="rect3" name="rect3" x="50" y="250" width="150" height="150" fill="#cbd5e1" stroke="#334155" stroke-width="2"/>
        <rect id="rect4" name="rect4" x="250" y="250" width="150" height="150" fill="#cbd5e1" stroke="#334155" stroke-width="2"/>
    </svg>
    """

    # 2. Initialize SIVO with the SVG string
    app = Sivo.from_string(svg_content, title="Fade-In Features", subtitle="Demonstrating fade_in and fade_pulse")

    # 3. Map the elements with fade logic
    # Element 1: Fades in starting immediately (default), taking 5 seconds (default)
    app.map("rect1",
            tooltip="Fades in immediately",
            color="#3b82f6",
            fade_in=True)

    # Element 2: Fades in after a 5 second delay, takes 5 seconds
    app.map("rect2",
            tooltip="Fades in after 5 seconds",
            color="#10b981",
            fade_in=True,
            fade_start_time_ms=5000)

    # Element 3: Fades in after a 10 second delay, takes 5 seconds
    app.map("rect3",
            tooltip="Fades in after 10 seconds",
            color="#f59e0b",
            fade_in=True,
            fade_start_time_ms=10000)

    # Element 4: Pulses continuously, starting after 15 seconds
    app.map("rect4",
            tooltip="Pulses continuously",
            color="#ef4444",
            fade_in=True,
            fade_pulse=True,
            fade_start_time_ms=15000)

    # 4. Generate the HTML bundle
    output_filename = "fade_in_infographic.html"
    app.to_html(output_filename)
    print(f"Generated {output_filename}. Open this file in your browser to see the fade effects.")

if __name__ == "__main__":
    create_fade_in_example()