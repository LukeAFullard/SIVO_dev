import os
import sys

# Optional: Add src to path if running directly without pip install
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from sivo import Sivo

def main():
    print("Building A4 Election News Infographic...")

    # Standard A4 proportions at high res: 1200x1700
    svg_content = """
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 1700" style="background-color: #f4f4f4;">
        <rect width="1200" height="1700" fill="#f4f4f4"/>

        <!-- Header News Banner -->
        <rect x="0" y="0" width="1200" height="180" fill="#1a1a1a"/>
        <text x="600" y="80" font-family="'Georgia', serif" font-size="64" font-weight="bold" fill="#ffffff" text-anchor="middle">THE DAILY HERALD</text>
        <line x1="100" y1="110" x2="1100" y2="110" stroke="#666" stroke-width="2"/>
        <text x="600" y="150" font-family="'Helvetica', sans-serif" font-size="28" fill="#cccccc" text-anchor="middle" letter-spacing="2">DECISIVE NIGHT: 2024 ELECTION RESULTS</text>

        <!-- Main Graphic: Map placeholder -->
        <rect x="100" y="250" width="1000" height="700" fill="#ffffff" stroke="#ddd" stroke-width="2" rx="10"/>

        <!-- Region 1: North -->
        <path id="region_north" d="M 150 280 L 500 280 L 550 500 L 250 600 Z" fill="#e2e8f0" stroke="#fff" stroke-width="4"/>
        <text x="350" y="450" font-family="sans-serif" font-size="24" font-weight="bold" fill="#1e293b" text-anchor="middle">North District</text>

        <!-- Region 2: South -->
        <path id="region_south" d="M 550 500 L 900 400 L 1050 800 L 400 900 Z" fill="#e2e8f0" stroke="#fff" stroke-width="4"/>
        <text x="750" y="650" font-family="sans-serif" font-size="24" font-weight="bold" fill="#1e293b" text-anchor="middle">South District</text>

        <!-- Region 3: West -->
        <path id="region_west" d="M 150 280 L 250 600 L 400 900 L 120 850 Z" fill="#e2e8f0" stroke="#fff" stroke-width="4"/>
        <text x="220" y="700" font-family="sans-serif" font-size="24" font-weight="bold" fill="#1e293b" text-anchor="middle">West District</text>

        <!-- Region 4: East -->
        <path id="region_east" d="M 500 280 L 950 280 L 900 400 L 550 500 Z" fill="#e2e8f0" stroke="#fff" stroke-width="4"/>
        <text x="750" y="380" font-family="sans-serif" font-size="24" font-weight="bold" fill="#1e293b" text-anchor="middle">East District</text>

        <text x="600" y="1000" font-family="'Helvetica', sans-serif" font-size="20" fill="#666" text-anchor="middle" font-style="italic">Click any district to view demographic breakdown and candidate vote share.</text>

        <!-- Key Takeaways Section -->
        <rect x="100" y="1050" width="480" height="500" fill="#ffffff" stroke="#ddd" stroke-width="2" rx="10"/>
        <text x="140" y="1110" font-family="'Georgia', serif" font-size="32" font-weight="bold" fill="#1a1a1a">Key Takeaways</text>
        <line x1="140" y1="1130" x2="540" y2="1130" stroke="#ee0000" stroke-width="4"/>

        <foreignObject x="140" y="1160" width="400" height="350">
            <div xmlns="http://www.w3.org/1999/xhtml" style="font-family: 'Helvetica', sans-serif; font-size: 18px; color: #333; line-height: 1.8;">
                <p><b>Turnout Surges:</b> Voter turnout reached a historic 78% in the South District, driven by youth engagement.</p>
                <p><b>Economic Focus:</b> Exit polls indicate inflation and housing costs were the primary concerns for 62% of suburban voters.</p>
                <p><b>Urban Shift:</b> Traditional voting blocks in the East saw unexpected margins of error, tightening the national race.</p>
            </div>
        </foreignObject>

        <!-- National Popular Vote Bar -->
        <rect x="620" y="1050" width="480" height="500" fill="#ffffff" stroke="#ddd" stroke-width="2" rx="10"/>
        <text x="660" y="1110" font-family="'Georgia', serif" font-size="32" font-weight="bold" fill="#1a1a1a">Popular Vote</text>
        <line x1="660" y1="1130" x2="1060" y2="1130" stroke="#0033cc" stroke-width="4"/>

        <rect x="660" y="1200" width="400" height="60" fill="#f4f4f4" rx="5"/>
        <rect x="660" y="1200" width="204" height="60" fill="#0052cc" rx="5"/> <!-- Candidate A 51% -->
        <rect x="864" y="1200" width="188" height="60" fill="#cc0000" rx="5"/> <!-- Candidate B 47% -->
        <rect x="1052" y="1200" width="8" height="60" fill="#eab308" rx="5"/> <!-- Third Party 2% -->

        <text x="660" y="1290" font-family="sans-serif" font-size="24" font-weight="bold" fill="#0052cc">Candidate A: 51%</text>
        <text x="660" y="1330" font-family="sans-serif" font-size="24" font-weight="bold" fill="#cc0000">Candidate B: 47%</text>
        <text x="660" y="1370" font-family="sans-serif" font-size="24" font-weight="bold" fill="#b45309">Other: 2%</text>

        <!-- Footer -->
        <text x="600" y="1650" font-family="'Helvetica', sans-serif" font-size="14" fill="#999" text-anchor="middle">Source: Daily Herald Polling Data | Interactive by SIVO</text>
    </svg>
    """

    # Custom CSS to frame the A4 poster securely in the center of the browser
    custom_css = """
    body {
        background-color: #d1d5db; /* Grey background like a desk */
    }
    #chart-container {
        display: flex;
        justify-content: center;
        padding: 40px 0;
        overflow-y: auto !important;
        align-items: flex-start !important;
    }
    .sivo-canvas-wrapper {
        min-height: 1700px;
        max-width: 1200px !important;
        margin: 0 auto;
        box-shadow: 0 10px 40px rgba(0,0,0,0.3);
        border: 1px solid #999;
    }
    #info-panel {
        background: #ffffff !important;
        color: #111 !important;
        box-shadow: -10px 0 20px rgba(0,0,0,0.1) !important;
        border-left: 2px solid #1a1a1a !important;
    }
    .info-panel-content h3 {
        color: #1a1a1a;
        border-bottom: 2px solid #ccc;
        font-family: 'Georgia', serif;
    }
    """

    # Initialize app with bounding_coords to maintain A4 aspect ratio logically
    sivo_app = Sivo.from_string(
        svg_content,
        title="2024 Election Results",
        panel_width="450px",
        disable_zoom_controls=True, # Prevent zooming to keep the one-pager intact
        bounding_coords=[[0, 1700], [1200, 0]]
    )

    # 1. District Map Interactions (Choropleth logic via simple coloring)
    # Using specific colors to simulate party wins
    blue_win = "#bfdbfe"
    blue_hover = "#93c5fd"
    red_win = "#fecaca"
    red_hover = "#fca5a5"

    sivo_app.map(
        element_id="region_north",
        tooltip="North District (Called for Cand. A)",
        color=blue_win, hover_color=blue_hover, glow=True,
        html="""
        <h3>North District</h3>
        <p>A traditional stronghold that held firm. Urban centers turned out in high numbers to secure the win.</p>
        """,
        echarts_option={
            "title": {"text": "Demographic Breakdown"},
            "tooltip": {"trigger": "item"},
            "series": [{"type": "pie", "radius": "60%", "data": [{"value": 60, "name": "Urban", "itemStyle": {"color":"#3b82f6"}}, {"value": 40, "name": "Suburban", "itemStyle": {"color":"#94a3b8"}}]}]
        }
    )

    sivo_app.map(
        element_id="region_south",
        tooltip="South District (Called for Cand. B)",
        color=red_win, hover_color=red_hover, glow=True,
        html="""
        <h3>South District</h3>
        <p>Swept by a significant margin. The agricultural communities heavily favored the incumbent's economic policies.</p>
        """,
        echarts_option={
            "title": {"text": "Demographic Breakdown"},
            "tooltip": {"trigger": "item"},
            "series": [{"type": "pie", "radius": "60%", "data": [{"value": 75, "name": "Rural", "itemStyle": {"color":"#ef4444"}}, {"value": 25, "name": "Suburban", "itemStyle": {"color":"#94a3b8"}}]}]
        }
    )

    sivo_app.map(
        element_id="region_west",
        tooltip="West District (Called for Cand. B)",
        color=red_win, hover_color=red_hover, glow=True,
        html="""
        <h3>West District</h3>
        <p>A highly contested battleground. It flipped red late into the night due to strong turnout in the industrial belt.</p>
        """,
        echarts_option={
            "title": {"text": "Vote Share Timeline"},
            "tooltip": {"trigger": "axis"},
            "xAxis": {"type": "category", "data": ["8pm", "10pm", "12am", "2am"]},
            "yAxis": {"type": "value"},
            "series": [
                {"name": "Cand A", "type": "line", "data": [52, 49, 48, 46], "itemStyle": {"color": "#3b82f6"}},
                {"name": "Cand B", "type": "line", "data": [48, 51, 52, 54], "itemStyle": {"color": "#ef4444"}}
            ]
        }
    )

    sivo_app.map(
        element_id="region_east",
        tooltip="East District (Called for Cand. A)",
        color=blue_win, hover_color=blue_hover, glow=True,
        html="""
        <h3>East District</h3>
        <p>Comfortable victory for the challenger. The coastal tech hubs provided a massive vote cushion.</p>
        """
    )

    # Export
    output_path = os.path.join(os.path.dirname(__file__), "election_a4.html")
    sivo_app.to_html(output_path, custom_css=custom_css)
    print(f"Generated at: {output_path}")

if __name__ == "__main__":
    main()
