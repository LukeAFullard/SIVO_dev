from sivo import Sivo
import os
import lxml.etree as etree

def run():
    template_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "src", "sivo", "templates", "timeline_5_nodes_template.svg"
    )

    app = Sivo.from_svg(
        template_path,
        disable_zoom_controls=False,
        lock_canvas=True,
        theme="light",
        ambient_effect="stars"
    )

    # Header - Make it a clinical trial pipeline
    app.add_scalable_text("header_area", "Oncology Drug Development Timeline", left="5%", top="20%", width="90%", height="40%", font_size="35%", font_weight="900", color="#0f172a", align="left")
    app.add_scalable_text("header_area", "Compound XYZ-123: Targeted Immunotherapy Progression • 2021 - 2026", left="5%", top="60%", width="90%", height="20%", font_size="15%", font_weight="600", color="#64748b", align="left")

    # Node 1: Pre-Clinical
    app.add_scalable_text("node_1_card", "2021: PRE-CLINICAL", left="5%", top="5%", width="90%", height="20%", font_size="15%", font_weight="800", color="#3b82f6")
    app.add_scalable_text("node_1_card", "In vitro/vivo testing. Pharmacodynamics established.", left="5%", top="25%", width="90%", height="20%", font_size="10%", font_weight="500", color="#475569", auto_shrink=True)

    # Add a small pie chart for resource allocation
    app.map_pie_chart(
        element_id="node_1_card",
        title="",
        data=[
            {"name": "R&D", "value": 70},
            {"name": "Legal", "value": 20},
            {"name": "Admin", "value": 10}
        ],
        extra_options={
            "series": [{"radius": ["30%", "60%"], "center": ["50%", "75%"], "label": {"show": False}}],
            "color": ["#3b82f6", "#93c5fd", "#e0f2fe"],
            "backgroundColor": "transparent",
            "tooltip": {"trigger": "item"}
        }
    )
    app.map("node_1_card", hover_color="#eff6ff", glow=True)

    # Node 2: Phase 1
    app.add_scalable_text("node_2_card", "2022: PHASE I", left="5%", top="5%", width="90%", height="20%", font_size="15%", font_weight="800", color="#8b5cf6")
    app.add_scalable_text("node_2_card", "Safety and dose escalation in 50 subjects.", left="5%", top="25%", width="90%", height="20%", font_size="10%", font_weight="500", color="#475569", auto_shrink=True)

    # Add a bar chart for dose tolerance
    app.map_bar_chart(
        element_id="node_2_card",
        title="",
        categories=["10mg", "25mg", "50mg"],
        data=[100, 95, 80],
        color="#8b5cf6",
        extra_options={
            "grid": {"top": "50%", "bottom": "15%", "left": "15%", "right": "15%"},
            "xAxis": {"axisLabel": {"fontSize": 8}},
            "yAxis": {"show": False},
            "backgroundColor": "transparent"
        }
    )
    app.map("node_2_card", hover_color="#faf5ff", glow=True)

    # Node 3: Phase 2 (Efficacy)
    app.add_scalable_text("node_3_card", "2023-2024: PHASE II", left="5%", top="10%", width="90%", height="20%", font_size="15%", font_weight="800", color="#10b981")
    app.add_scalable_text("node_3_card", "Efficacy in 300 patients vs standard care.", left="5%", top="35%", width="90%", height="15%", font_size="10%", font_weight="500", color="#475569", auto_shrink=True)
    app.map("node_3_card", hover_color="#f0fdf4", glow=True)

    # Line chart showing tumor reduction (negative value line chart)
    app.map_line_chart(
        element_id="node_3_card",
        title="Mean Tumor Volume Change (%)",
        categories=["Wk 0", "Wk 4", "Wk 8", "Wk 12", "Wk 16"],
        data=[
            {"name": "XYZ-123", "type": "line", "data": [0, -15, -35, -52, -68], "itemStyle": {"color": "#10b981"}, "smooth": True, "lineStyle": {"width": 3}},
            {"name": "Control", "type": "line", "data": [0, -5, -8, -10, -12], "itemStyle": {"color": "#94a3b8"}, "smooth": True, "lineStyle": {"type": "dashed"}}
        ],
        extra_options={
            "grid": {"top": 80, "bottom": 30, "left": 50, "right": 20},
            "legend": {"show": True, "top": 25, "textStyle": {"fontSize": 10}},
            "backgroundColor": "transparent",
            "title": {"textStyle": {"fontSize": 12, "color": "#1e293b"}},
            "tooltip": {"trigger": "axis"}
        }
    )

    # Node 4: Phase 3
    app.add_scalable_text("node_4_card", "2025: PHASE III", left="5%", top="10%", width="90%", height="25%", font_size="15%", font_weight="800", color="#f59e0b")
    app.add_scalable_text("node_4_card", "Global multi-center trials (3,500 patients).", left="5%", top="40%", width="90%", height="30%", font_size="10%", font_weight="500", color="#475569", auto_shrink=True)
    app.map("node_4_card", hover_color="#fffbeb", glow=True)

    # Enrollment progress bar
    app.add_scalable_text("node_4_card", "ENROLLMENT PROGRESS", left="5%", top="75%", width="50%", height="15%", font_size="10%", font_weight="700", color="#64748b")
    app.add_scalable_progress_bar("node_4_card", progress="100%", left="55%", top="80%", width="40%", height="5%", rx="4", bg_color="#e2e8f0", fill_color="#f59e0b")

    # Node 5: FDA Approval
    app.add_scalable_text("node_5_card", "2026: FDA APPROVAL", left="5%", top="10%", width="90%", height="25%", font_size="15%", font_weight="800", color="#ef4444")
    app.add_scalable_text("node_5_card", "NDA submitted. Priority review granted.", left="5%", top="40%", width="90%", height="30%", font_size="10%", font_weight="500", color="#475569", auto_shrink=True)
    app.map("node_5_card", hover_color="#fef2f2", glow=True)

    app.add_scalable_text("node_5_card", "EST. PEAK SALES", left="5%", top="75%", width="50%", height="15%", font_size="10%", font_weight="700", color="#64748b")
    app.add_scalable_text("node_5_card", "$3.4B", left="55%", top="70%", width="40%", height="25%", font_size="25%", font_weight="900", color="#ef4444")

    output_path = os.path.join(os.path.dirname(__file__), "05_timeline.html")
    app.to_html(output_path)
    print(f"Generated: {output_path}")

if __name__ == "__main__":
    run()
