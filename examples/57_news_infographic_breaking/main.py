import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from sivo import Sivo

def main():
    print("Building A4 Breaking News Infographic...")

    svg_content = """
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1414" style="background-color: #ffffff;">
        <!-- Breaking News Banner -->
        <rect x="0" y="0" width="1000" height="150" fill="#cc0000"/>
        <text x="50" y="70" font-family="'Helvetica', sans-serif" font-size="48" font-weight="900" fill="#ffffff">BREAKING NEWS</text>
        <text x="50" y="120" font-family="'Helvetica', sans-serif" font-size="24" fill="#ffcccc">MASSIVE INFRASTRUCTURE FAILURE AT PORT AUTHORITY</text>

        <!-- Main Graphic: Crane Collapse Diagram -->
        <rect x="50" y="200" width="900" height="600" fill="#f0f0f0" stroke="#ccc" stroke-width="2"/>
        <text x="500" y="250" font-family="'Helvetica', sans-serif" font-size="32" font-weight="bold" fill="#333" text-anchor="middle">INCIDENT DIAGRAM: PIER 42</text>

        <!-- Water -->
        <rect x="50" y="600" width="900" height="200" fill="#0066cc" opacity="0.3"/>
        <path d="M 50 600 Q 150 580 250 600 T 450 600 T 650 600 T 850 600 T 950 600 L 950 800 L 50 800 Z" fill="#0066cc" opacity="0.5"/>

        <!-- Pier Structure -->
        <rect x="50" y="550" width="300" height="50" fill="#666"/>
        <rect x="80" y="600" width="20" height="200" fill="#444"/>
        <rect x="250" y="600" width="20" height="200" fill="#444"/>

        <!-- Ship -->
        <path d="M 400 550 L 800 550 L 750 650 L 450 650 Z" fill="#333"/>
        <rect x="500" y="500" width="100" height="50" fill="#999"/>
        <rect x="530" y="450" width="20" height="50" fill="#cc0000"/>

        <!-- Collapsed Crane -->
        <g id="hotspot_crane">
            <line x1="150" y1="550" x2="550" y2="450" stroke="#f59e0b" stroke-width="15" stroke-linecap="round"/>
            <line x1="200" y1="550" x2="300" y2="250" stroke="#f59e0b" stroke-width="10" stroke-linecap="round" stroke-dasharray="5,5"/> <!-- Broken wire -->
            <circle cx="450" cy="475" r="30" fill="#ef4444" opacity="0.5"/> <!-- Impact point -->
            <text x="450" y="482" font-family="sans-serif" font-size="20" font-weight="bold" fill="#fff" text-anchor="middle">!</text>
        </g>

        <!-- Container Stack -->
        <g id="hotspot_cargo">
            <rect x="650" y="450" width="100" height="100" fill="#10b981" stroke="#047857" stroke-width="2"/>
            <rect x="650" y="350" width="100" height="100" fill="#3b82f6" stroke="#1d4ed8" stroke-width="2"/>
            <line x1="600" y1="350" x2="800" y2="550" stroke="#ef4444" stroke-width="5" stroke-dasharray="10,10"/> <!-- Damage radius -->
        </g>

        <text x="500" y="850" font-family="sans-serif" font-size="18" fill="#666" text-anchor="middle">Click the highlighted hotspots on the diagram for live updates and details.</text>

        <!-- Timeline Section -->
        <rect x="50" y="900" width="900" height="400" fill="#fafafa" stroke="#ddd" stroke-width="2"/>
        <text x="100" y="960" font-family="'Helvetica', sans-serif" font-size="32" font-weight="bold" fill="#333">Incident Timeline</text>
        <line x1="100" y1="980" x2="900" y2="980" stroke="#cc0000" stroke-width="3"/>

        <!-- Timeline nodes -->
        <circle cx="150" cy="1100" r="15" fill="#cc0000"/>
        <text x="150" y="1060" font-family="sans-serif" font-size="20" font-weight="bold" fill="#333" text-anchor="middle">04:15 AM</text>
        <foreignObject x="100" y="1130" width="200" height="150">
            <div xmlns="http://www.w3.org/1999/xhtml" style="font-family: sans-serif; font-size: 16px; color: #555;">Cargo ship docks at Pier 42. Unloading commences.</div>
        </foreignObject>

        <line x1="150" y1="1100" x2="450" y2="1100" stroke="#ccc" stroke-width="4"/>
        <circle cx="450" cy="1100" r="15" fill="#cc0000"/>
        <text x="450" y="1060" font-family="sans-serif" font-size="20" font-weight="bold" fill="#333" text-anchor="middle">06:30 AM</text>
        <foreignObject x="400" y="1130" width="200" height="150">
            <div xmlns="http://www.w3.org/1999/xhtml" style="font-family: sans-serif; font-size: 16px; color: #555;">Structural failure in Crane A's primary cable system.</div>
        </foreignObject>

        <line x1="450" y1="1100" x2="750" y2="1100" stroke="#ccc" stroke-width="4"/>
        <circle cx="750" cy="1100" r="15" fill="#f59e0b"/>
        <text x="750" y="1060" font-family="sans-serif" font-size="20" font-weight="bold" fill="#333" text-anchor="middle">06:35 AM</text>
        <foreignObject x="700" y="1130" width="200" height="150">
            <div xmlns="http://www.w3.org/1999/xhtml" style="font-family: sans-serif; font-size: 16px; color: #555;">Crane collapses onto ship deck. Emergency services dispatched.</div>
        </foreignObject>

        <!-- Footer -->
        <text x="500" y="1380" font-family="'Helvetica', sans-serif" font-size="14" fill="#999" text-anchor="middle">Graphics Desk | Updated: 10 mins ago</text>
    </svg>
    """

    custom_css = """
    body { background-color: #e5e7eb; }
    #chart-container { display: flex; justify-content: center; padding: 40px 0; overflow-y: auto !important; align-items: flex-start !important; }
    .sivo-canvas-wrapper { min-height: 1414px; max-width: 1000px !important; margin: 0 auto; box-shadow: 0 10px 40px rgba(0,0,0,0.3); }
    #info-panel { border-top: 5px solid #cc0000 !important; }
    .info-panel-content h3 { color: #cc0000; font-family: 'Helvetica', sans-serif; font-weight: 900; }
    """

    sivo_app = Sivo.from_string(
        svg_content, title="Breaking News: Pier 42", panel_width="400px", disable_zoom_controls=True,
        bounding_coords=[[0, 1414], [1000, 0]]
    )

    # Interactions
    sivo_app.map(
        element_id="hotspot_crane",
        tooltip="Crane A Failure Point",
        hover_color="#fca5a5", glow=True,
        html="""
        <h3>Structural Failure</h3>
        <p>Engineers report that the primary tension cable snapped under heavy load. The crane was last inspected 6 months ago.</p>
        <p><b>Casualties:</b> 0 reported</p>
        <p><b>Injuries:</b> 2 (Minor)</p>
        """
    )

    sivo_app.map(
        element_id="hotspot_cargo",
        tooltip="Damaged Cargo Manifest",
        hover_color="#fca5a5", glow=True,
        html="""
        <h3>Cargo Impact</h3>
        <p>The collapsing structure struck two shipping containers holding electronics and textiles.</p>
        """,
        echarts_option={
            "title": {"text": "Estimated Financial Loss"},
            "tooltip": {"trigger": "item"},
            "series": [{"type": "pie", "radius": "50%", "data": [{"value": 1.2, "name": "Electronics ($1.2M)", "itemStyle": {"color":"#3b82f6"}}, {"value": 0.5, "name": "Textiles ($0.5M)", "itemStyle": {"color":"#10b981"}}, {"value": 2.8, "name": "Infrastructure ($2.8M)", "itemStyle": {"color":"#ef4444"}}]}]
        }
    )

    output_path = os.path.join(os.path.dirname(__file__), "breaking_a4.html")
    sivo_app.to_html(output_path, custom_css=custom_css)
    print(f"Generated at: {output_path}")

if __name__ == "__main__":
    main()
