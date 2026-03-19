import os
from sivo import Sivo

def main():
    # 1. Provide a simple static SVG string representing a few blocks
    svg_data = """<svg width="400" height="200" xmlns="http://www.w3.org/2000/svg">
      <rect id="block_a" x="50" y="50" width="100" height="100" fill="#e2e8f0" stroke="#94a3b8" stroke-width="2"/>
      <rect id="block_b" x="250" y="50" width="100" height="100" fill="#e2e8f0" stroke="#94a3b8" stroke-width="2"/>
      <text x="100" y="105" text-anchor="middle" font-family="sans-serif" font-size="14" fill="#333">Block A</text>
      <text x="300" y="105" text-anchor="middle" font-family="sans-serif" font-size="14" fill="#333">Block B</text>
    </svg>"""

    # 2. Initialize SIVO
    app = Sivo.from_string(svg_data, title="Native Timeline Playback UI", subtitle="Demonstrating programmatic control over the ECharts timeline component.")

    # 3. Create temporal data to drive the map
    # The structure is: { "TimeStep": { "ElementID": { "DataKey": Value } } }
    timeline_data = {
        "2020": {
            "block_a": {"metric": 10},
            "block_b": {"metric": 20}
        },
        "2021": {
            "block_a": {"metric": 40},
            "block_b": {"metric": 10}
        },
        "2022": {
            "block_a": {"metric": 60},
            "block_b": {"metric": 50}
        },
        "2023": {
            "block_a": {"metric": 90},
            "block_b": {"metric": 100}
        }
    }

    # 4. Bind the timeline to the UI
    # We apply custom Timeline UI styling, enabling the play button, looping, and setting custom sizing
    app.bind_timeline(
        data=timeline_data,
        key="metric",
        colors=["#bae6fd", "#0284c7"], # Light blue to dark blue gradient
        min_val=0,
        max_val=100,
        auto_play=True,
        play_interval=1500, # 1.5 seconds per step
        show_play_btn=True, # Show the native play/pause button
        loop=True,          # Loop continuously
        control_position="left", # Position controls on the left side of the axis
        symbol="diamond",   # Change the step symbol to a diamond
        symbol_size=16,     # Increase symbol size
        bottom=40           # Lift the timeline up slightly from the bottom edge
    )

    # 5. Output to HTML
    output_path = os.path.join(os.path.dirname(__file__), 'output.html')
    app.to_html(output_path)
    print(f"Generated Example: {output_path}")

if __name__ == "__main__":
    main()
