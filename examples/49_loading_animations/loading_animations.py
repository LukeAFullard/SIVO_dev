import os
import sys
# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from sivo import Sivo

def main():
    # Construct the path to the SVG template
    script_dir = os.path.dirname(os.path.abspath(__file__))
    svg_path = os.path.join(script_dir, "loading_template.svg")
    output_path = os.path.join(script_dir, "loading_animations.html")

    print(f"Loading SVG from: {svg_path}")

    # Initialize Sivo from the SVG
    app = Sivo.from_svg(svg_path)

    # Enable general features
    app.infographic.title = "Loading Animations Showcase"
    app.infographic.subtitle = "Click cards to trigger various CSS loading animations"

    # Map the different loading animations
    app.map("card-spinner", tooltip="Standard Spinner",
            loading={"trigger": "click", "duration_ms": 3000, "style": "spinner", "text": "Loading Data...",
                     "completion_html": "<h2 style='margin:0; color:#10b981;'>42%</h2><span style='font-size:12px; color:#64748b;'>Engagement</span>"})

    app.map("card-pulse", tooltip="Pulse Animation",
            loading={"trigger": "click", "duration_ms": 3000, "style": "pulse", "text": "Processing...",
                     "completion_html": "<h2 style='margin:0; color:#3b82f6;'>$4.2M</h2><span style='font-size:12px; color:#64748b;'>Revenue</span>",
                     "completion_color": "#dbeafe"})

    app.map("card-typewriter", tooltip="Typewriter Effect",
            loading={"trigger": "click", "duration_ms": 3000, "style": "typewriter", "text": "Initializing System...",
                     "completion_html": "<h2 style='margin:0; color:#8b5cf6;'>Active</h2><span style='font-size:12px; color:#64748b;'>Status</span>"})

    app.map("card-shimmer", tooltip="Shimmer Skeleton",
            loading={"trigger": "click", "duration_ms": 3000, "style": "shimmer",
                     "completion_html": "<h2 style='margin:0; color:#f59e0b;'>8.4K</h2><span style='font-size:12px; color:#64748b;'>Views</span>"})

    app.map("card-glitch", tooltip="Glitch Effect",
            loading={"trigger": "click", "duration_ms": 3000, "style": "glitch", "text": "HACKING...",
                     "completion_html": "<h2 style='margin:0; color:#ef4444;'>ACCESS</h2><span style='font-size:12px; color:#64748b;'>Granted</span>",
                     "completion_color": "#fee2e2"})

    app.map("card-matrix", tooltip="Matrix Effect",
            loading={"trigger": "click", "duration_ms": 3000, "style": "matrix", "text": "01001100...",
                     "completion_html": "<h2 style='margin:0; color:#14b8a6;'>Neo</h2><span style='font-size:12px; color:#64748b;'>Found</span>"})

    app.map("card-bouncing-dots", tooltip="Bouncing Dots",
            loading={"trigger": "click", "duration_ms": 3000, "style": "bouncing_dots", "text": "Saving...",
                     "completion_html": "<h2 style='margin:0; color:#38bdf8;'>Done</h2>"})

    app.map("card-ripple", tooltip="Ripple Effect",
            loading={"trigger": "click", "duration_ms": 3000, "style": "ripple", "text": "Pinging...",
                     "completion_html": "<h2 style='margin:0; color:#10b981;'>Alive</h2>"})

    app.map("card-radar", tooltip="Radar Effect",
            loading={"trigger": "click", "duration_ms": 3000, "style": "radar", "text": "Scanning...",
                     "completion_html": "<h2 style='margin:0; color:#8b5cf6;'>Clear</h2>"})

    app.map("card-neon", tooltip="Neon Effect",
            loading={"trigger": "click", "duration_ms": 3000, "style": "neon", "text": "Powering Up...",
                     "completion_html": "<h2 style='margin:0; color:#d946ef;'>Online</h2>"})

    app.map("card-typing", tooltip="Typing Indicator",
            loading={"trigger": "click", "duration_ms": 3000, "style": "typing_indicator", "text": "Jane is typing",
                     "completion_html": "<h2 style='margin:0; color:#f97316;'>Hello!</h2>"})

    app.map("card-progress", tooltip="Progress Bar",
            loading={"trigger": "click", "duration_ms": 3000, "style": "progress_bar", "text": "Downloading...",
                     "completion_html": "<h2 style='margin:0; color:#3b82f6;'>Complete</h2>"})

    app.map("card-heartbeat", tooltip="Heartbeat Effect",
            loading={"trigger": "click", "duration_ms": 3000, "style": "heartbeat", "text": "Monitoring...",
                     "completion_html": "<h2 style='margin:0; color:#ef4444;'>Stable</h2>"})

    app.map("card-slot", tooltip="Slot Machine Effect",
            loading={"trigger": "click", "duration_ms": 3000, "style": "slot_machine", "text": "Calculating...",
                     "completion_html": "<h2 style='margin:0; color:#eab308;'>777</h2>"})

    app.map("card-orbit", tooltip="Orbit Effect",
            loading={"trigger": "click", "duration_ms": 3000, "style": "orbit", "text": "Connecting...",
                     "completion_html": "<h2 style='margin:0; color:#10b981;'>Synced</h2>"})

    app.map("card-breathe", tooltip="Breathe Effect",
            loading={"trigger": "click", "duration_ms": 3000, "style": "breathe", "text": "Calibrating...",
                     "completion_html": "<h2 style='margin:0; color:#38bdf8;'>Ready</h2>"})

    # Map an "on load" animation
    app.map("card-onload", tooltip="This triggers as soon as the map loads",
            loading={"trigger": "load", "duration_ms": 4000, "style": "typewriter", "text": "Welcome to SIVO...",
                     "completion_html": "<h3 style='margin:0; color:#0f172a;'>System Ready</h3>"})

    # Save to an interactive HTML file
    print(f"Exporting to: {output_path}")
    app.to_html(output_path)
    print("Done! Open loading_animations.html in your browser.")

if __name__ == "__main__":
    main()
