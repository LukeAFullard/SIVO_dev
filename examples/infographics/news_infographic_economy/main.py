import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from sivo import Sivo

def main():
    print("Building Professional Global Trade Infographic...")

    # Professional Financial Times / Bloomberg aesthetic
    svg_content = """
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1414" style="background-color: #fef0dd;">
        <!-- Warm ivory background common in financial papers -->
        <rect width="1000" height="1414" fill="#fdfbf7"/>

        <!-- Header -->
        <line x1="40" y1="40" x2="960" y2="40" stroke="#000000" stroke-width="4"/>
        <text x="40" y="80" font-family="'Times New Roman', serif" font-size="36" font-weight="normal" fill="#000000" letter-spacing="2">GLOBAL ECONOMY WEEKLY</text>
        <line x1="40" y1="100" x2="960" y2="100" stroke="#000000" stroke-width="1"/>
        <line x1="40" y1="104" x2="960" y2="104" stroke="#000000" stroke-width="1"/>

        <text x="40" y="160" font-family="'Times New Roman', serif" font-size="48" font-weight="900" fill="#000000">THE SILICON SHUFFLE</text>
        <text x="40" y="195" font-family="'Helvetica Neue', sans-serif" font-size="16" fill="#4b5563">The supply chains of advanced semiconductors and critical minerals are actively being rewritten by geopolitical pressure and massive domestic subsidies.</text>

        <!-- Main Map Area (Abstracted nodes for trade routes) -->
        <rect x="40" y="240" width="920" height="550" fill="#f4f4f5" stroke="#d1d5db" stroke-width="1"/>
        <text x="500" y="275" font-family="'Helvetica Neue', sans-serif" font-size="14" font-weight="bold" fill="#000" text-anchor="middle" letter-spacing="1">SIMPLIFIED SEMICONDUCTOR TRADE FLOWS (2024)</text>

        <!-- Region Nodes: Elegant Outlined Circles -->
        <!-- North America -->
        <circle id="node_na" cx="200" cy="450" r="50" fill="#ffffff" stroke="#2563eb" stroke-width="4" filter="drop-shadow(0 4px 6px rgba(0,0,0,0.05))"/>
        <text x="200" y="445" font-family="'Helvetica Neue', sans-serif" font-size="18" font-weight="bold" fill="#000" text-anchor="middle">N. America</text>
        <text x="200" y="465" font-family="'Times New Roman', serif" font-size="14" fill="#6b7280" text-anchor="middle">Design &amp; IP</text>

        <!-- Europe -->
        <circle id="node_eu" cx="500" cy="350" r="45" fill="#ffffff" stroke="#16a34a" stroke-width="4" filter="drop-shadow(0 4px 6px rgba(0,0,0,0.05))"/>
        <text x="500" y="345" font-family="'Helvetica Neue', sans-serif" font-size="18" font-weight="bold" fill="#000" text-anchor="middle">Europe</text>
        <text x="500" y="365" font-family="'Times New Roman', serif" font-size="14" fill="#6b7280" text-anchor="middle">EUV Tech Hub</text>

        <!-- Asia Pacific -->
        <circle id="node_apac" cx="800" cy="550" r="60" fill="#ffffff" stroke="#dc2626" stroke-width="4" filter="drop-shadow(0 4px 6px rgba(0,0,0,0.05))"/>
        <text x="800" y="540" font-family="'Helvetica Neue', sans-serif" font-size="22" font-weight="bold" fill="#000" text-anchor="middle">APAC</text>
        <text x="800" y="565" font-family="'Times New Roman', serif" font-size="14" fill="#6b7280" text-anchor="middle">Fab &amp; Assembly</text>

        <!-- Static background curves (to be traced by sivo flow arrows) -->
        <path d="M 740,550 Q 400,600 250,450" fill="none" stroke="#d1d5db" stroke-width="8" stroke-dasharray="10,5"/>
        <path d="M 455,350 Q 300,350 220,410" fill="none" stroke="#d1d5db" stroke-width="8" stroke-dasharray="10,5"/>
        <path d="M 770,500 Q 650,400 545,350" fill="none" stroke="#d1d5db" stroke-width="8" stroke-dasharray="10,5"/>

        <!-- Details Section -->
        <rect x="40" y="830" width="440" height="500" fill="#ffffff" stroke="#e5e7eb" stroke-width="1"/>
        <text x="70" y="880" font-family="'Helvetica Neue', sans-serif" font-size="20" font-weight="bold" fill="#000">The Mineral Chokepoint</text>
        <line x1="70" y1="895" x2="440" y2="895" stroke="#000" stroke-width="2"/>
        <foreignObject x="70" y="910" width="380" height="400">
            <div xmlns="http://www.w3.org/1999/xhtml" style="font-family: 'Times New Roman', serif; font-size: 18px; color: #374151; line-height: 1.8;">
                <p>The geopolitical race for tech supremacy is fundamentally tied to raw materials. Processing of rare earth elements—essential for everything from EV batteries to fighter jets—is highly centralized.</p>
                <p>APAC regions currently command upwards of 85% of global refinement capacity. As a result, Western economies are actively subsidizing domestic processing facilities at an unprecedented scale to de-risk their supply chains.</p>
                <p style="color: #d97706; font-family: 'Helvetica Neue', sans-serif; font-size: 14px; margin-top: 30px;"><b>&#x2192; Hover over map nodes to view regional subsidy data.</b></p>
            </div>
        </foreignObject>

        <!-- Interactive Chart Placeholder -->
        <rect x="520" y="830" width="440" height="500" fill="#ffffff" stroke="#e5e7eb" stroke-width="1"/>
        <text x="550" y="880" font-family="'Helvetica Neue', sans-serif" font-size="20" font-weight="bold" fill="#000">Global Fab Construction Spending</text>
        <line x1="550" y1="895" x2="920" y2="895" stroke="#000" stroke-width="2"/>

        <rect id="chart_investment" x="550" y="920" width="380" height="350" fill="#fdfbf7"/>

        <!-- Call to action over chart -->
        <rect x="650" y="1050" width="180" height="40" rx="20" fill="#2563eb" opacity="0.1"/>
        <text x="740" y="1075" font-family="'Helvetica Neue', sans-serif" font-size="14" font-weight="bold" fill="#2563eb" text-anchor="middle">CLICK TO REVEAL CHART</text>
        <path d="M 600,1200 L 650,1100 L 700,1150 L 750,1050 L 800,1000" fill="none" stroke="#94a3b8" stroke-width="3" opacity="0.5"/>

        <!-- Footer -->
        <line x1="40" y1="1360" x2="960" y2="1360" stroke="#000" stroke-width="1"/>
        <text x="40" y="1390" font-family="'Helvetica Neue', sans-serif" font-size="12" fill="#6b7280">Produced by SIVO Infographics Desk</text>
    </svg>
    """

    custom_css = """
    body { background-color: #d1d5db; }
    #chart-container { display: flex; justify-content: center; padding: 40px 0; overflow-y: auto !important; align-items: flex-start !important; }
    .sivo-canvas-wrapper { min-height: 1414px; max-width: 1000px !important; margin: 0 auto; box-shadow: 0 10px 40px rgba(0,0,0,0.3); border: 1px solid #d1d5db;}
    /* Financial Paper Panel Styling */
    #info-panel { background: #fdfbf7 !important; color: #111827 !important; border-left: 1px solid #000 !important; box-shadow: -10px 0 25px rgba(0,0,0,0.05) !important;}
    .info-panel-content h3 { color: #000; font-family: 'Times New Roman', serif; font-size: 1.8rem; border-bottom: 2px solid #000; padding-bottom: 5px; margin-bottom: 10px; font-weight: normal;}
    .info-panel-content p { font-family: 'Helvetica Neue', sans-serif; font-size: 1.05rem; line-height: 1.6; color: #374151;}
    .close-btn { color: #9ca3af !important; } .close-btn:hover { color: #111827 !important; background: #e5e7eb !important; }
    """

    sivo_app = Sivo.from_string(
        svg_content, title="Global Trade Economy", panel_width="450px", disable_zoom_controls=True,
        bounding_coords=[[0, 1414], [1000, 0]]
    )

    # Interactions
    sivo_app.map(
        element_id="node_apac",
        tooltip="Asia Pacific: Fabrication",
        hover_color="#fef2f2", glow=True,
        html="""
        <h3>APAC Manufacturing</h3>
        <p>The unquestioned leader in advanced node fabrication (logic chips below 5nm) and memory. Taiwan alone accounts for nearly 60% of foundry revenue globally.</p>
        <p style="font-size: 1.5rem; color: #dc2626; font-weight: bold; margin-top: 20px;">$4.2 Trillion</p>
        <p style="color: #6b7280; font-size: 0.9rem; margin-top: -10px;">Est. 2024 Tech Export Value</p>
        """
    )

    sivo_app.map(
        element_id="node_eu",
        tooltip="Europe: R&D & Machinery",
        hover_color="#f0fdf4", glow=True,
        html="""
        <h3>European Tech Sector</h3>
        <p>Europe holds a monopoly on the complex machinery required to manufacture leading-edge semiconductors (EUV lithography). The EU Chips Act aims to double the region's global market share by 2030.</p>
        <p style="font-size: 1.5rem; color: #16a34a; font-weight: bold; margin-top: 20px;">€43 Billion</p>
        <p style="color: #6b7280; font-size: 0.9rem; margin-top: -10px;">Public & Private Investments (2030 target)</p>
        """
    )

    sivo_app.map(
        element_id="node_na",
        tooltip="North America: Design",
        hover_color="#eff6ff", glow=True,
        html="""
        <h3>North American Reshoring</h3>
        <p>While dominating chip design and software architecture, manufacturing fell from 37% in 1990 to just 12% today. Historic legislation is actively funding domestic factory construction to reverse this trend.</p>
        <p style="font-size: 1.5rem; color: #2563eb; font-weight: bold; margin-top: 20px;">$52.7 Billion</p>
        <p style="color: #6b7280; font-size: 0.9rem; margin-top: -10px;">Allocated in CHIPS & Science Act Grants</p>
        """
    )

    sivo_app.map(
        element_id="chart_investment",
        tooltip="View Financial Growth",
        hover_color="#ffffff", glow=True,
        html="""
        <h3>Capital Expenditure Surge</h3>
        <p>Annual spending on semiconductor fabrication plants has more than doubled since 2019, driven by demand for AI processing and geopolitical reshoring initiatives.</p>
        """,
        echarts_option={
            "tooltip": {"trigger": "axis", "axisPointer": {"type": "cross"}},
            "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
            "xAxis": {
                "type": "category", "data": ["2019", "2020", "2021", "2022", "2023", "2024(E)"],
                "axisLine": {"lineStyle": {"color": "#9ca3af"}}, "axisTick": {"show": False}
            },
            "yAxis": {
                "type": "value", "name": "Billion USD", "splitLine": {"lineStyle": {"color": "#e5e7eb", "type": "dashed"}},
                "axisLine": {"show": False}, "axisTick": {"show": False}
            },
            "series": [
                {
                    "name": "Global CapEx", "type": "bar", "data": [106, 113, 152, 185, 169, 215],
                    "itemStyle": {"color": "#0f172a"},
                    "label": {"show": True, "position": "top", "color": "#000", "fontFamily": "Times New Roman"}
                }
            ]
        }
    )

    # Add dynamic flow lines over the static dashed paths
    # Setting explicit anchor coordinates as we don't have bounding boxes for the paths directly
    sivo_app.add_connection("node_apac", "node_na", label="Hardware", flow_effect=True, effect_symbol='arrow', effect_size=8, color="#000000", width=2, opacity=0.8)
    sivo_app.add_connection("node_eu", "node_apac", label="Machinery", flow_effect=True, effect_symbol='circle', effect_size=5, color="#16a34a", width=2, opacity=0.8)
    sivo_app.add_connection("node_eu", "node_na", label="IP", flow_effect=True, effect_symbol='circle', effect_size=5, color="#2563eb", width=2, opacity=0.8)

    output_path = os.path.join(os.path.dirname(__file__), "economy_a4.html")
    sivo_app.to_html(output_path, custom_css=custom_css)
    print(f"Generated at: {output_path}")

if __name__ == "__main__":
    main()
