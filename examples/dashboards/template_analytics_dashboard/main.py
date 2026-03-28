import os
from sivo import Sivo, SivoDashboard

def main():
    # --- 1. Top Row: Stats ---
    # We will use HTML blocks and a Sivo Metrics block for top KPI stats
    html_stat1 = """
    <div style="display: flex; flex-direction: column; justify-content: center;">
        <div style="font-size: 0.875rem; color: #6b7280; font-weight: 600; text-transform: uppercase;">Total Users</div>
        <div style="font-size: 2rem; font-weight: 700; color: #111827; margin: 0.5rem 0;">12,450</div>
        <div style="font-size: 0.875rem; color: #10b981; font-weight: 500;">+14% from last month</div>
    </div>
    """

    html_stat2 = """
    <div style="display: flex; flex-direction: column; justify-content: center;">
        <div style="font-size: 0.875rem; color: #6b7280; font-weight: 600; text-transform: uppercase;">Revenue</div>
        <div style="font-size: 2rem; font-weight: 700; color: #111827; margin: 0.5rem 0;">$84,200</div>
        <div style="font-size: 0.875rem; color: #10b981; font-weight: 500;">+2.5% from last month</div>
    </div>
    """

    # --- 2. Main Area: Charts ---
    bar_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300">
        <rect id="bg" width="400" height="300" fill="#ffffff" />
        <!-- Y-Axis -->
        <line x1="50" y1="250" x2="380" y2="250" stroke="#e5e7eb" stroke-width="2"/>
        <line x1="50" y1="50" x2="50" y2="250" stroke="#e5e7eb" stroke-width="2"/>

        <!-- Bars -->
        <rect id="bar1" x="80" y="150" width="40" height="100" fill="#3b82f6" rx="4" />
        <rect id="bar2" x="150" y="100" width="40" height="150" fill="#3b82f6" rx="4" />
        <rect id="bar3" x="220" y="50" width="40" height="200" fill="#3b82f6" rx="4" />
        <rect id="bar4" x="290" y="180" width="40" height="70" fill="#3b82f6" rx="4" />

        <!-- Labels -->
        <text x="100" y="270" font-family="sans-serif" font-size="12" fill="#6b7280" text-anchor="middle">Q1</text>
        <text x="170" y="270" font-family="sans-serif" font-size="12" fill="#6b7280" text-anchor="middle">Q2</text>
        <text x="240" y="270" font-family="sans-serif" font-size="12" fill="#6b7280" text-anchor="middle">Q3</text>
        <text x="310" y="270" font-family="sans-serif" font-size="12" fill="#6b7280" text-anchor="middle">Q4</text>
    </svg>"""
    sivo_bar = Sivo.from_string(bar_svg, theme="light", layout_size="90%")

    sivo_bar.map("bar1", hover_color="#2563eb", tooltip="Q1 Revenue: $15,000", callback_payload={"selected_quarter": "Q1", "revenue": "$15k"})
    sivo_bar.map("bar2", hover_color="#2563eb", tooltip="Q2 Revenue: $22,000", callback_payload={"selected_quarter": "Q2", "revenue": "$22k"})
    sivo_bar.map("bar3", hover_color="#2563eb", tooltip="Q3 Revenue: $35,000", callback_payload={"selected_quarter": "Q3", "revenue": "$35k"})
    sivo_bar.map("bar4", hover_color="#2563eb", tooltip="Q4 Revenue: $12,000", callback_payload={"selected_quarter": "Q4", "revenue": "$12k"})

    pie_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 300">
        <rect id="bg" width="300" height="300" fill="#ffffff" />
        <circle id="pie_base" cx="150" cy="150" r="100" fill="#e5e7eb" />
        <path id="pie_slice" d="M150,150 L150,50 A100,100 0 0,1 250,150 Z" fill="#10b981" />
        <circle id="pie_center" cx="150" cy="150" r="60" fill="#ffffff" />
        <text x="150" y="155" font-family="sans-serif" font-size="20" font-weight="bold" fill="#111827" text-anchor="middle">25%</text>
    </svg>"""
    sivo_pie = Sivo.from_string(pie_svg, theme="light", layout_size="90%")
    sivo_pie.map("pie_slice", hover_color="#059669", tooltip="New Users: 25%")


    # --- 3. Assemble Dashboard using 'analytics_dashboard' template ---
    dashboard = SivoDashboard(title="Acme Analytics", columns=3)
    dashboard.set_grid_layout(
        desktop='''
    "kpi1 kpi2 kpi3 kpi4"
"main main side side"
"bottom bottom bottom bottom"
        ''',
        mobile='''
    "kpi1"
"kpi2"
"kpi3"
"kpi4"
"main"
"side"
"bottom"
        '''
    )

    # Assign stats to the 'stats' slot (rendered in the top row)
    dashboard.add_html_block("stat_users", html_stat1, grid_area="stats")
    dashboard.add_html_block("stat_rev", html_stat2, grid_area="stats")
    dashboard.add_metrics_panel("live_metrics", title="Active Sessions", metrics=["current_users"], grid_area="stats")

    # Assign charts to the 'main' grid
    dashboard.add_sivo_block("revenue_trend", sivo_bar, grid_area="main")
    dashboard.add_sivo_block("user_demographics", sivo_pie, grid_area="main")

    # Bottom row panels
    dashboard.add_details_panel("quarter_details", title="Quarter Breakdown", placeholder="Click a bar above to see details.", grid_area="main")
    dashboard.add_metrics_panel("selected_stats", title="Selection Overview", metrics=["selected_quarter", "revenue"], grid_area="main")

    # Export
    output_file = os.path.join(os.path.dirname(__file__), "output.html")
    dashboard.to_html(output_file)
    print(f"Successfully generated dashboard: {output_file}")


if __name__ == "__main__":
    main()
