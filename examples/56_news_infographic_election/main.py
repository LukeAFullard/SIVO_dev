import os
import sys

# Optional: Add src to path if running directly without pip install
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from sivo import Sivo

def main():
    print("Building Professional Election Infographic...")

    # Professional Newspaper Aesthetic (e.g. NYT / WSJ)
    svg_content = """
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1414" style="background-color: #fcfcfc;">
        <rect width="1000" height="1414" fill="#fcfcfc"/>

        <!-- Header -->
        <rect x="0" y="0" width="1000" height="15" fill="#0f172a"/>
        <text x="500" y="80" font-family="'Times New Roman', Times, serif" font-size="64" font-weight="bold" fill="#0f172a" text-anchor="middle">The National Review</text>
        <line x1="50" y1="110" x2="950" y2="110" stroke="#cbd5e1" stroke-width="1"/>
        <line x1="50" y1="114" x2="950" y2="114" stroke="#0f172a" stroke-width="2"/>

        <text x="50" y="160" font-family="'Helvetica Neue', Helvetica, Arial, sans-serif" font-size="32" font-weight="800" fill="#0f172a">ELECTION 2024: THE FINAL TALLY</text>
        <text x="50" y="195" font-family="'Helvetica Neue', Helvetica, Arial, sans-serif" font-size="18" fill="#475569">A decisive victory hinges on key swing districts. Explore the geographic breakdown of the national vote.</text>

        <!-- Main Graphic: Map Area -->
        <rect x="50" y="240" width="900" height="600" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/>
        <!-- Grid background for the map -->
        <pattern id="dot-grid" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse">
            <circle cx="2" cy="2" r="1" fill="#cbd5e1" />
        </pattern>
        <rect x="50" y="240" width="900" height="600" fill="url(#dot-grid)"/>

        <!-- Abstracted Map Regions (More precise, geometric paths) -->
        <!-- North -->
        <path id="region_north" d="M 150 280 L 450 280 L 500 500 L 250 550 Z" fill="#e2e8f0" stroke="#ffffff" stroke-width="3" filter="drop-shadow(0 4px 6px rgba(0,0,0,0.05))"/>
        <text x="330" y="420" font-family="'Helvetica Neue', sans-serif" font-size="20" font-weight="bold" fill="#334155" text-anchor="middle">North</text>
        <text x="330" y="445" font-family="'Helvetica Neue', sans-serif" font-size="14" fill="#64748b" text-anchor="middle">54% Turnout</text>

        <!-- South -->
        <path id="region_south" d="M 500 500 L 850 420 L 900 750 L 400 800 Z" fill="#e2e8f0" stroke="#ffffff" stroke-width="3" filter="drop-shadow(0 4px 6px rgba(0,0,0,0.05))"/>
        <text x="680" y="620" font-family="'Helvetica Neue', sans-serif" font-size="20" font-weight="bold" fill="#334155" text-anchor="middle">South</text>
        <text x="680" y="645" font-family="'Helvetica Neue', sans-serif" font-size="14" fill="#64748b" text-anchor="middle">71% Turnout</text>

        <!-- West -->
        <path id="region_west" d="M 150 280 L 250 550 L 400 800 L 100 750 Z" fill="#e2e8f0" stroke="#ffffff" stroke-width="3" filter="drop-shadow(0 4px 6px rgba(0,0,0,0.05))"/>
        <text x="210" y="620" font-family="'Helvetica Neue', sans-serif" font-size="20" font-weight="bold" fill="#334155" text-anchor="middle">West</text>
        <text x="210" y="645" font-family="'Helvetica Neue', sans-serif" font-size="14" fill="#64748b" text-anchor="middle">62% Turnout</text>

        <!-- East -->
        <path id="region_east" d="M 450 280 L 850 300 L 850 420 L 500 500 Z" fill="#e2e8f0" stroke="#ffffff" stroke-width="3" filter="drop-shadow(0 4px 6px rgba(0,0,0,0.05))"/>
        <text x="650" y="380" font-family="'Helvetica Neue', sans-serif" font-size="20" font-weight="bold" fill="#334155" text-anchor="middle">East</text>
        <text x="650" y="405" font-family="'Helvetica Neue', sans-serif" font-size="14" fill="#64748b" text-anchor="middle">48% Turnout</text>

        <text x="500" y="875" font-family="'Helvetica Neue', sans-serif" font-size="14" font-weight="bold" fill="#2563eb" text-anchor="middle" letter-spacing="1">INTERACTIVE: CLICK ANY REGION TO VIEW DEMOGRAPHIC SHIFT</text>

        <!-- Analysis Section -->
        <rect x="50" y="920" width="430" height="420" fill="#ffffff" stroke="#e2e8f0" stroke-width="1"/>
        <text x="80" y="970" font-family="'Helvetica Neue', sans-serif" font-size="20" font-weight="bold" fill="#0f172a">Editorial Takeaways</text>
        <line x1="80" y1="985" x2="450" y2="985" stroke="#0f172a" stroke-width="2"/>

        <foreignObject x="80" y="1010" width="370" height="300">
            <div xmlns="http://www.w3.org/1999/xhtml" style="font-family: 'Times New Roman', serif; font-size: 18px; color: #334155; line-height: 1.7;">
                <p><b>The Suburban Shift:</b> Exit polls confirmed that suburban voters, historically a reliable bloc for the incumbent, swung dramatically toward the challenger, citing economic instability.</p>
                <p><b>Youth Turnout Disappoints:</b> Despite significant polling enthusiasm, youth voter turnout in the East District fell by 4 points compared to the last cycle, tightening margins unexpectedly.</p>
                <p><b>The Rural Wall:</b> The South held an impenetrable firewall, maintaining its deep partisan lean and driving record-breaking turnout.</p>
            </div>
        </foreignObject>

        <!-- National Popular Vote -->
        <rect x="520" y="920" width="430" height="420" fill="#ffffff" stroke="#e2e8f0" stroke-width="1"/>
        <text x="550" y="970" font-family="'Helvetica Neue', sans-serif" font-size="20" font-weight="bold" fill="#0f172a">National Popular Vote</text>
        <line x1="550" y1="985" x2="920" y2="985" stroke="#0f172a" stroke-width="2"/>

        <g transform="translate(550, 1050)">
            <rect x="0" y="0" width="370" height="40" fill="#f1f5f9"/>
            <rect x="0" y="0" width="188" height="40" fill="#1d4ed8"/> <!-- Dem: 51% -->
            <rect x="188" y="0" width="177" height="40" fill="#b91c1c"/> <!-- Rep: 48% -->
            <rect x="365" y="0" width="5" height="40" fill="#fbbf24"/> <!-- Third: 1% -->

            <text x="0" y="-10" font-family="'Helvetica Neue', sans-serif" font-size="16" font-weight="bold" fill="#1d4ed8">Candidate A (51.0%)</text>
            <text x="370" y="-10" font-family="'Helvetica Neue', sans-serif" font-size="16" font-weight="bold" fill="#b91c1c" text-anchor="end">Candidate B (47.8%)</text>
            <text x="370" y="65" font-family="'Helvetica Neue', sans-serif" font-size="12" fill="#64748b" text-anchor="end">Other (1.2%)</text>

            <!-- 270 Line -->
            <line x1="185" y1="-5" x2="185" y2="45" stroke="#0f172a" stroke-width="2" stroke-dasharray="4,4"/>
            <text x="185" y="-10" font-family="'Helvetica Neue', sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">MAJORITY</text>
        </g>

        <!-- Footer -->
        <line x1="50" y1="1370" x2="950" y2="1370" stroke="#cbd5e1" stroke-width="1"/>
        <text x="50" y="1395" font-family="'Helvetica Neue', sans-serif" font-size="12" fill="#94a3b8">Source: The National Review Polling Desk &amp; Associated Press. Data updated 03:00 EST.</text>
        <text x="950" y="1395" font-family="'Helvetica Neue', sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="end">INTERACTIVE GRAPHIC</text>
    </svg>
    """

    # Clean, editorial CSS
    custom_css = """
    body {
        background-color: #e2e8f0; /* Soft studio background */
    }
    #chart-container {
        display: flex;
        justify-content: center;
        padding: 40px 0;
        overflow-y: auto !important;
        align-items: flex-start !important;
    }
    .sivo-canvas-wrapper {
        min-height: 1414px;
        max-width: 1000px !important;
        margin: 0 auto;
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        border: 1px solid #cbd5e1;
    }
    /* Elegant Info Panel for Newspaper Style */
    #info-panel {
        background: rgba(255, 255, 255, 0.98) !important;
        color: #1e293b !important;
        box-shadow: -10px 0 25px rgba(0,0,0,0.05) !important;
        border-left: 3px solid #0f172a !important;
        font-family: 'Helvetica Neue', Arial, sans-serif !important;
    }
    .info-panel-content h3 {
        color: #0f172a;
        font-weight: 800;
        font-size: 1.6rem;
        margin-bottom: 0.5rem;
        border-bottom: 1px solid #e2e8f0;
        padding-bottom: 0.5rem;
    }
    .info-panel-content p {
        font-family: 'Times New Roman', serif;
        font-size: 1.1rem;
        line-height: 1.6;
        color: #334155;
    }
    .close-btn { color: #64748b !important; }
    .close-btn:hover { color: #0f172a !important; background: #f1f5f9 !important; }
    """

    sivo_app = Sivo.from_string(
        svg_content,
        title="Election 2024 Final Tally",
        panel_width="450px",
        disable_zoom_controls=True,
        bounding_coords=[[0, 1414], [1000, 0]]
    )

    # Polished ECharts styling
    dem_color = "#3b82f6" # Professional blue
    gop_color = "#ef4444" # Professional red
    muted_color = "#cbd5e1"

    sivo_app.map(
        element_id="region_north",
        tooltip="North (Cand. A)",
        color="#bfdbfe", hover_color="#93c5fd", glow=True,
        html="""
        <h3>North District</h3>
        <p>A narrow victory for Candidate A, driven entirely by high margins in the metropolitan center offsetting rural deficits.</p>
        """,
        echarts_option={
            "title": {"text": "Vote Share Margin", "textStyle": {"fontSize": 14, "fontFamily": "Helvetica Neue"}},
            "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
            "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
            "xAxis": {"type": "value", "show": False},
            "yAxis": {"type": "category", "data": ["Rural", "Suburban", "Urban"], "axisLine": {"show": False}, "axisTick": {"show": False}},
            "series": [
                {"name": "Cand. A", "type": "bar", "stack": "total", "data": [35, 52, 68], "itemStyle": {"color": dem_color}},
                {"name": "Cand. B", "type": "bar", "stack": "total", "data": [65, 48, 32], "itemStyle": {"color": gop_color}}
            ]
        }
    )

    sivo_app.map(
        element_id="region_south",
        tooltip="South (Cand. B)",
        color="#fecaca", hover_color="#fca5a5", glow=True,
        html="""
        <h3>South District</h3>
        <p>Candidate B expanded their margin here by 4 points compared to the last election, capitalizing on economic messaging.</p>
        """,
        echarts_option={
            "title": {"text": "Vote Share Margin", "textStyle": {"fontSize": 14, "fontFamily": "Helvetica Neue"}},
            "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
            "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
            "xAxis": {"type": "value", "show": False},
            "yAxis": {"type": "category", "data": ["Rural", "Suburban", "Urban"], "axisLine": {"show": False}, "axisTick": {"show": False}},
            "series": [
                {"name": "Cand. A", "type": "bar", "stack": "total", "data": [25, 45, 55], "itemStyle": {"color": dem_color}},
                {"name": "Cand. B", "type": "bar", "stack": "total", "data": [75, 55, 45], "itemStyle": {"color": gop_color}}
            ]
        }
    )

    sivo_app.map(
        element_id="region_west",
        tooltip="West (Cand. B)",
        color="#fecaca", hover_color="#fca5a5", glow=True,
        html="""
        <h3>West District</h3>
        <p>The ultimate battleground. A late surge in mail-in ballots tightened the race, but Candidate B held on by 0.8%.</p>
        """,
        echarts_option={
            "title": {"text": "Hourly Vote Count (Millions)", "textStyle": {"fontSize": 14, "fontFamily": "Helvetica Neue"}},
            "tooltip": {"trigger": "axis"},
            "xAxis": {"type": "category", "data": ["8 PM", "10 PM", "12 AM", "2 AM", "4 AM"], "boundaryGap": False, "axisLine": {"lineStyle": {"color": muted_color}}},
            "yAxis": {"type": "value", "splitLine": {"lineStyle": {"color": "#f1f5f9"}}},
            "series": [
                {"name": "Cand. A", "type": "line", "smooth": True, "data": [1.2, 1.8, 2.4, 2.9, 3.1], "itemStyle": {"color": dem_color}, "areaStyle": {"opacity": 0.1}},
                {"name": "Cand. B", "type": "line", "smooth": True, "data": [1.5, 2.2, 2.5, 2.8, 3.15], "itemStyle": {"color": gop_color}, "areaStyle": {"opacity": 0.1}}
            ]
        }
    )

    sivo_app.map(
        element_id="region_east",
        tooltip="East (Cand. A)",
        color="#bfdbfe", hover_color="#93c5fd", glow=True,
        html="""
        <h3>East District</h3>
        <p>A solid wall for Candidate A. Despite lower overall turnout, the raw vote advantage was insurmountable.</p>
        """
    )

    output_path = os.path.join(os.path.dirname(__file__), "election_a4.html")
    sivo_app.to_html(output_path, custom_css=custom_css)
    print(f"Generated at: {output_path}")

if __name__ == "__main__":
    main()
