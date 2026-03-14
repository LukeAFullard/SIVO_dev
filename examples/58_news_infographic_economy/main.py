import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from sivo import Sivo

def main():
    print("Building A4 Global Trade Infographic...")

    svg_content = """
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1414" style="background-color: #f8fafc;">
        <!-- Header -->
        <rect x="0" y="0" width="1000" height="150" fill="#0f172a"/>
        <text x="50" y="70" font-family="'Trebuchet MS', sans-serif" font-size="48" font-weight="bold" fill="#38bdf8">GLOBAL TRADE SHIFT</text>
        <text x="50" y="110" font-family="'Trebuchet MS', sans-serif" font-size="20" fill="#94a3b8">The evolving supply chains of semiconductors and critical minerals.</text>

        <!-- Main Map Area (Abstracted nodes for trade routes) -->
        <rect x="50" y="200" width="900" height="600" fill="#e2e8f0" stroke="#cbd5e1" stroke-width="2" rx="8"/>
        <text x="500" y="250" font-family="sans-serif" font-size="32" font-weight="bold" fill="#1e293b" text-anchor="middle">THE NEW SILICON PATH</text>

        <!-- Region Nodes -->
        <!-- North America -->
        <circle id="node_na" cx="200" cy="400" r="40" fill="#1e293b"/>
        <text x="200" y="390" font-family="sans-serif" font-size="20" font-weight="bold" fill="#fff" text-anchor="middle">NA</text>
        <text x="200" y="460" font-family="sans-serif" font-size="16" fill="#475569" text-anchor="middle">Consumer Base</text>

        <!-- Europe -->
        <circle id="node_eu" cx="500" cy="300" r="40" fill="#1e293b"/>
        <text x="500" y="290" font-family="sans-serif" font-size="20" font-weight="bold" fill="#fff" text-anchor="middle">EU</text>
        <text x="500" y="360" font-family="sans-serif" font-size="16" fill="#475569" text-anchor="middle">R&amp;D Hub</text>

        <!-- Asia Pacific -->
        <circle id="node_apac" cx="800" cy="500" r="60" fill="#1e293b"/>
        <text x="800" y="490" font-family="sans-serif" font-size="24" font-weight="bold" fill="#fff" text-anchor="middle">APAC</text>
        <text x="800" y="580" font-family="sans-serif" font-size="16" fill="#475569" text-anchor="middle">Manufacturing &amp; Mining</text>

        <!-- Flow Lines (Static placeholders, SIVO will animate over these) -->
        <path d="M 800,500 Q 500,600 200,400" fill="none" stroke="#94a3b8" stroke-width="4" stroke-dasharray="8,8"/>
        <path d="M 500,300 Q 350,300 200,400" fill="none" stroke="#94a3b8" stroke-width="4" stroke-dasharray="8,8"/>
        <path d="M 800,500 Q 650,400 500,300" fill="none" stroke="#94a3b8" stroke-width="4" stroke-dasharray="8,8"/>

        <!-- Detailed Breakdown Section -->
        <rect x="50" y="850" width="425" height="450" fill="#ffffff" stroke="#cbd5e1" stroke-width="2" rx="8"/>
        <text x="80" y="900" font-family="sans-serif" font-size="24" font-weight="bold" fill="#1e293b">Critical Minerals Crisis</text>
        <line x1="80" y1="920" x2="400" y2="920" stroke="#f59e0b" stroke-width="3"/>
        <foreignObject x="80" y="940" width="365" height="350">
            <div xmlns="http://www.w3.org/1999/xhtml" style="font-family: sans-serif; font-size: 16px; color: #475569; line-height: 1.8;">
                <p>The pivot to green energy and AI infrastructure has caused a massive supply bottleneck for Lithium, Cobalt, and Rare Earth Elements.</p>
                <p>APAC currently controls 85% of processing capacity, forcing Western nations to rapidly build out domestic alternatives at immense cost.</p>
                <p><b>Hover over the map nodes</b> above to see region-specific supply bottlenecks and investment figures.</p>
            </div>
        </foreignObject>

        <!-- Economic Chart Section -->
        <rect x="525" y="850" width="425" height="450" fill="#ffffff" stroke="#cbd5e1" stroke-width="2" rx="8"/>
        <text x="555" y="900" font-family="sans-serif" font-size="24" font-weight="bold" fill="#1e293b">Investment In Semiconductors</text>
        <line x1="555" y1="920" x2="875" y2="920" stroke="#38bdf8" stroke-width="3"/>

        <!-- Interactive Chart Placeholder -->
        <rect id="chart_investment" x="555" y="950" width="365" height="300" fill="#f1f5f9" rx="8"/>
        <text x="737" y="1100" font-family="sans-serif" font-size="16" font-style="italic" fill="#94a3b8" text-anchor="middle">Click to view YoY Investment Growth</text>
        <path d="M 600,1200 L 650,1100 L 700,1150 L 750,1050 L 800,1000" fill="none" stroke="#38bdf8" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
        <circle cx="800" cy="1000" r="8" fill="#0284c7"/>

        <!-- Footer -->
        <text x="500" y="1380" font-family="sans-serif" font-size="14" fill="#94a3b8" text-anchor="middle">Economy Weekly | Data from Global Trade Organization 2024</text>
    </svg>
    """

    custom_css = """
    body { background-color: #d1d5db; }
    #chart-container { display: flex; justify-content: center; padding: 40px 0; overflow-y: auto !important; align-items: flex-start !important; }
    .sivo-canvas-wrapper { min-height: 1414px; max-width: 1000px !important; margin: 0 auto; box-shadow: 0 10px 40px rgba(0,0,0,0.3); }
    #info-panel { background: rgba(255, 255, 255, 0.95) !important; color: #1e293b !important; border-left: 2px solid #38bdf8 !important; }
    .info-panel-content h3 { color: #0f172a; border-bottom: 2px solid #e2e8f0; font-family: sans-serif; }
    """

    sivo_app = Sivo.from_string(
        svg_content, title="Global Trade Economy", panel_width="450px", disable_zoom_controls=True,
        bounding_coords=[[0, 1414], [1000, 0]]
    )

    # Interactions
    sivo_app.map(
        element_id="node_apac",
        tooltip="Asia Pacific Region",
        hover_color="#0ea5e9", glow=True,
        html="""
        <h3>Asia Pacific Hub</h3>
        <p>Currently processes 85% of critical minerals and manufactures 60% of logic chips.</p>
        <p><b>Export Value:</b> $4.2 Trillion (Semiconductors + Minerals)</p>
        """
    )

    sivo_app.map(
        element_id="node_eu",
        tooltip="Europe Region",
        hover_color="#0ea5e9", glow=True,
        html="""
        <h3>Europe R&D</h3>
        <p>The primary designer and producer of the ultra-violet lithography machines required to print advanced chips.</p>
        <p><b>Investment Target:</b> €43 Billion by 2030 (EU Chips Act)</p>
        """
    )

    sivo_app.map(
        element_id="node_na",
        tooltip="North America Region",
        hover_color="#0ea5e9", glow=True,
        html="""
        <h3>North American Reshoring</h3>
        <p>Heavily focused on moving manufacturing back domestically to secure the supply chain for consumer electronics and defense.</p>
        <p><b>Investment Target:</b> $52 Billion (CHIPS and Science Act)</p>
        """
    )

    sivo_app.map(
        element_id="chart_investment",
        tooltip="View Interactive Chart",
        hover_color="#ffffff", glow=True,
        html="""
        <h3>Global Fab Investment</h3>
        <p>The massive spike in capital expenditure over the last 4 years is unprecedented in the semiconductor industry.</p>
        """,
        echarts_option={
            "tooltip": {"trigger": "axis"},
            "xAxis": {"type": "category", "data": ["2019", "2020", "2021", "2022", "2023", "2024"]},
            "yAxis": {"type": "value", "name": "Billion USD"},
            "series": [
                {"name": "CapEx", "type": "bar", "data": [90, 110, 150, 180, 160, 210], "itemStyle": {"color": "#38bdf8", "borderRadius": [5, 5, 0, 0]}}
            ]
        }
    )

    # Dynamic flows simulating trade
    sivo_app.add_connection("node_apac", "node_na", label="Finished Goods", flow_effect=True, effect_symbol='arrow', effect_size=10, color="#f59e0b")
    sivo_app.add_connection("node_eu", "node_apac", label="Lithography Tech", flow_effect=True, effect_symbol='circle', effect_size=6, color="#10b981")
    sivo_app.add_connection("node_eu", "node_na", label="R&D collaboration", flow_effect=True, effect_symbol='circle', effect_size=6, color="#8b5cf6")

    output_path = os.path.join(os.path.dirname(__file__), "economy_a4.html")
    sivo_app.to_html(output_path, custom_css=custom_css)
    print(f"Generated at: {output_path}")

if __name__ == "__main__":
    main()
