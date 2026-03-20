import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from sivo import Sivo

def main():
    print("Building Professional Breaking News Infographic...")

    # Professional Architectural / Engineering aesthetic
    svg_content = """
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1414" style="background-color: #f1f5f9;">
        <!-- Header: Breaking News -->
        <rect x="0" y="0" width="1000" height="120" fill="#dc2626"/>
        <text x="40" y="75" font-family="'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="42" font-weight="900" fill="#ffffff" letter-spacing="1">BREAKING NEWS</text>
        <text x="40" y="105" font-family="'Inter', sans-serif" font-size="18" font-weight="600" fill="#fecaca" letter-spacing="0.5">STRUCTURAL COLLAPSE AT PORT TERMINAL 4: ONGOING INCIDENT</text>

        <!-- Main Engineering Diagram -->
        <rect x="40" y="160" width="920" height="650" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>

        <!-- Blueprint Grid -->
        <pattern id="blueprint-grid" width="40" height="40" patternUnits="userSpaceOnUse">
            <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#e2e8f0" stroke-width="1"/>
        </pattern>
        <rect x="40" y="160" width="920" height="650" fill="url(#blueprint-grid)"/>

        <!-- Title inside diagram -->
        <rect x="60" y="180" width="450" height="60" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>
        <text x="80" y="215" font-family="'Inter', sans-serif" font-size="20" font-weight="700" fill="#0f172a" letter-spacing="1">SCHEMATIC: TERMINAL 4 IMPACT ZONE</text>
        <text x="80" y="232" font-family="'Inter', sans-serif" font-size="12" fill="#64748b">Cross-section view. Not strictly to scale.</text>

        <!-- Abstracted Shapes for the Diagram -->

        <!-- Water Level Line -->
        <line x1="40" y1="650" x2="960" y2="650" stroke="#3b82f6" stroke-width="4" stroke-dasharray="20,10"/>
        <text x="900" y="675" font-family="sans-serif" font-size="12" font-weight="bold" fill="#3b82f6">SEA LEVEL</text>
        <rect x="40" y="650" width="920" height="160" fill="#bfdbfe" opacity="0.4"/>

        <!-- Pier Foundation -->
        <rect x="40" y="600" width="400" height="50" fill="#94a3b8"/> <!-- Deck -->
        <rect x="100" y="650" width="30" height="160" fill="#64748b"/> <!-- Piling 1 -->
        <rect x="300" y="650" width="30" height="160" fill="#64748b"/> <!-- Piling 2 -->

        <!-- Container Ship -->
        <path d="M 450 600 L 900 600 L 850 720 L 500 720 Z" fill="#475569"/> <!-- Hull -->
        <rect x="520" y="520" width="120" height="80" fill="#cbd5e1"/> <!-- Bridge -->
        <rect x="550" y="470" width="40" height="50" fill="#f59e0b"/> <!-- Funnel -->

        <!-- Damaged Crane (Hotspot 1) -->
        <g id="hotspot_crane">
            <line x1="200" y1="600" x2="200" y2="300" stroke="#f87171" stroke-width="25"/> <!-- Tower bent/red -->
            <line x1="180" y1="300" x2="650" y2="400" stroke="#f87171" stroke-width="20" stroke-linecap="round"/> <!-- Boom fallen -->

            <!-- Snapped Tension Cable -->
            <path d="M 200 300 Q 150 400 120 450" fill="none" stroke="#dc2626" stroke-width="6" stroke-dasharray="10,5"/>

            <!-- Red Pulse Impact Center -->
            <circle cx="600" cy="385" r="40" fill="#ef4444" opacity="0.3"/>
            <circle cx="600" cy="385" r="15" fill="#dc2626" />
            <text x="600" y="435" font-family="'Inter', sans-serif" font-size="14" font-weight="bold" fill="#dc2626" text-anchor="middle">PRIMARY IMPACT</text>
        </g>

        <!-- Crushed Containers (Hotspot 2) -->
        <g id="hotspot_cargo">
            <rect x="700" y="520" width="80" height="80" fill="#0ea5e9" stroke="#0284c7" stroke-width="3"/>
            <rect x="700" y="440" width="80" height="80" fill="#fcd34d" stroke="#d97706" stroke-width="3"/>
            <path d="M 680 430 L 790 450 L 780 500 L 690 490 Z" fill="#10b981" stroke="#047857" stroke-width="3" opacity="0.8"/> <!-- Crushed container falling -->

            <!-- Warning Box -->
            <rect x="790" y="380" width="140" height="30" fill="#fef08a" stroke="#ca8a04" stroke-width="2"/>
            <text x="860" y="400" font-family="sans-serif" font-size="12" font-weight="bold" fill="#854d0e" text-anchor="middle">HAZMAT CARGO</text>
        </g>

        <!-- Instructions -->
        <rect x="40" y="830" width="920" height="40" fill="#f1f5f9"/>
        <text x="500" y="855" font-family="'Inter', sans-serif" font-size="14" font-weight="bold" fill="#3b82f6" text-anchor="middle">INTERACTIVE: CLICK HIGHLIGHTED RED AND YELLOW ZONES FOR LIVE INCIDENT REPORTS</text>

        <!-- Clean Timeline Section -->
        <rect x="40" y="890" width="920" height="420" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>
        <text x="80" y="940" font-family="'Inter', sans-serif" font-size="28" font-weight="800" fill="#0f172a">Incident Timeline (EST)</text>
        <line x1="80" y1="960" x2="920" y2="960" stroke="#e2e8f0" stroke-width="2"/>

        <!-- Timeline Axis -->
        <line x1="100" y1="1050" x2="850" y2="1050" stroke="#94a3b8" stroke-width="4" stroke-linecap="round"/>

        <!-- Node 1 -->
        <circle cx="150" cy="1050" r="10" fill="#0f172a" stroke="#ffffff" stroke-width="3"/>
        <text x="150" y="1025" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">04:15 AM</text>
        <foreignObject x="90" y="1080" width="120" height="150">
            <div xmlns="http://www.w3.org/1999/xhtml" style="font-family: 'Inter', sans-serif; font-size: 14px; color: #475569; text-align: center;">
                Vessel "MV Titan" docks. Unloading sequence begins.
            </div>
        </foreignObject>

        <!-- Node 2 -->
        <circle cx="450" cy="1050" r="10" fill="#dc2626" stroke="#ffffff" stroke-width="3"/>
        <text x="450" y="1025" font-family="sans-serif" font-size="16" font-weight="bold" fill="#dc2626" text-anchor="middle">06:32 AM</text>
        <foreignObject x="390" y="1080" width="120" height="150">
            <div xmlns="http://www.w3.org/1999/xhtml" style="font-family: 'Inter', sans-serif; font-size: 14px; color: #475569; text-align: center;">
                <b>Critical Failure.</b> Tension cable 4 snaps. Boom collapses onto deck.
            </div>
        </foreignObject>

        <!-- Node 3 -->
        <circle cx="750" cy="1050" r="10" fill="#f59e0b" stroke="#ffffff" stroke-width="3"/>
        <text x="750" y="1025" font-family="sans-serif" font-size="16" font-weight="bold" fill="#f59e0b" text-anchor="middle">06:45 AM</text>
        <foreignObject x="690" y="1080" width="120" height="150">
            <div xmlns="http://www.w3.org/1999/xhtml" style="font-family: 'Inter', sans-serif; font-size: 14px; color: #475569; text-align: center;">
                First responders on scene. Port operations halted indefinitely.
            </div>
        </foreignObject>

        <!-- Footer -->
        <line x1="40" y1="1350" x2="960" y2="1350" stroke="#cbd5e1" stroke-width="1"/>
        <text x="40" y="1380" font-family="'Inter', sans-serif" font-size="12" fill="#64748b">Graphics: Engineering Desk | Last Updated: 10 mins ago | Based on preliminary structural assessments.</text>
    </svg>
    """

    custom_css = """
    body { background-color: #f8fafc; }
    #chart-container { display: flex; justify-content: center; padding: 40px 0; overflow-y: auto !important; align-items: flex-start !important; }
    .sivo-canvas-wrapper { min-height: 1414px; max-width: 1000px !important; margin: 0 auto; box-shadow: 0 10px 30px -10px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; }
    #info-panel { background: #ffffff !important; border-left: 4px solid #dc2626 !important; font-family: 'Inter', sans-serif !important; box-shadow: -15px 0 30px rgba(0,0,0,0.1) !important;}
    .info-panel-content h3 { color: #dc2626; font-weight: 900; text-transform: uppercase; font-size: 1.4rem; border-bottom: 2px solid #fecaca; margin-bottom: 0.5rem; padding-bottom: 0.25rem;}
    .info-panel-content p { color: #334155; font-size: 1.1rem; line-height: 1.6;}
    .close-btn { color: #94a3b8 !important; } .close-btn:hover { color: #0f172a !important; background: #f1f5f9 !important; }
    """

    sivo_app = Sivo.from_string(
        svg_content, title="Incident Report: Pier 42", panel_width="450px", disable_zoom_controls=True,
        bounding_coords=[[0, 1414], [1000, 0]]
    )

    # Interactions
    sivo_app.map(
        element_id="hotspot_crane",
        tooltip="Crane A Failure Zone",
        hover_color="#fca5a5", glow=True,
        html="""
        <h3>Structural Failure</h3>
        <p>Engineers report that the primary rear tension cable snapped under a 40-ton load. Preliminary findings suggest severe metal fatigue that went unnoticed during the last bi-annual inspection.</p>
        <p style="background: #fef2f2; padding: 10px; border-left: 3px solid #dc2626; font-family: monospace;">
            <b>STATUS:</b> Area Secured<br/>
            <b>CASUALTIES:</b> 0<br/>
            <b>INJURIES:</b> 2 (Crane Operator, Deckhand)
        </p>
        """
    )

    sivo_app.map(
        element_id="hotspot_cargo",
        tooltip="Hazmat Cargo Impact",
        hover_color="#fde68a", glow=True,
        html="""
        <h3>Cargo Impact & Hazmat</h3>
        <p>The falling boom crushed three stacked containers. One container (yellow) was carrying industrial solvents. Emergency crews have deployed containment booms in the water to prevent spread.</p>
        """,
        echarts_option={
            "title": {"text": "Estimated Financial Damages (Millions USD)", "textStyle": {"fontSize": 14, "fontFamily": "Inter"}},
            "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
            "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
            "xAxis": {"type": "value", "show": False},
            "yAxis": {"type": "category", "data": ["Crane Replacement", "Vessel Repair", "Lost Cargo", "Hazmat Cleanup"], "axisTick": {"show": False}, "axisLine": {"show": False}},
            "series": [
                {"name": "Cost", "type": "bar", "data": [12.5, 4.2, 1.8, 3.5], "itemStyle": {"color": "#dc2626", "borderRadius": [0, 5, 5, 0]}, "label": {"show": True, "position": "right", "formatter": "${c}M"}}
            ]
        }
    )

    output_path = os.path.join(os.path.dirname(__file__), "breaking_a4.html")
    sivo_app.to_html(output_path, custom_css=custom_css)
    print(f"Generated at: {output_path}")

if __name__ == "__main__":
    main()
