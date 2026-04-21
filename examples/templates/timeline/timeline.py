from sivo import Sivo
import os
import lxml.etree as etree

def run():
    template_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))),
        "src", "sivo", "templates", "other", "timeline_5_nodes_template.svg"
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

    # Custom HTML Overlay for a Pie Chart directly on Node 1
    node_1_pie = """
    <div style="width: 100%; height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: flex-end; padding-bottom: 2cqh; container-type: size;">
        <svg width="25cqw" height="25cqw" viewBox="0 0 32 32">
            <!-- R&D 70% -->
            <circle r="16" cx="16" cy="16" fill="#3b82f6" stroke-width="32" stroke-dasharray="70 100" />
            <!-- Legal 20% -->
            <circle r="16" cx="16" cy="16" fill="#93c5fd" stroke-width="32" stroke-dasharray="20 100" stroke-dashoffset="-70" />
            <!-- Admin 10% -->
            <circle r="16" cx="16" cy="16" fill="#e0f2fe" stroke-width="32" stroke-dasharray="10 100" stroke-dashoffset="-90" />
            <!-- Inner hole for donut -->
            <circle r="8" cx="16" cy="16" fill="#ffffff" />
        </svg>
    </div>
    """
    app.add_overlay("node_1_card", node_1_pie)
    app.map("node_1_card", hover_color="#eff6ff", glow=True)

    # Node 2: Phase 1
    app.add_scalable_text("node_2_card", "2022: PHASE I", left="5%", top="5%", width="90%", height="20%", font_size="15%", font_weight="800", color="#8b5cf6")
    app.add_scalable_text("node_2_card", "Safety and dose escalation in 50 subjects.", left="5%", top="25%", width="90%", height="20%", font_size="10%", font_weight="500", color="#475569", auto_shrink=True)

    # Custom HTML Overlay for a Bar Chart directly on Node 2
    node_2_bars = """
    <div style="width: 100%; height: 100%; display: flex; align-items: flex-end; justify-content: center; gap: 4cqw; padding-bottom: 2cqh; container-type: size;">
        <div style="display: flex; flex-direction: column; align-items: center;">
            <div style="width: 6cqw; height: 18cqh; background-color: #8b5cf6; border-radius: 2px 2px 0 0;"></div>
            <span style="font-size: 5cqw; color: #64748b; font-family: sans-serif; margin-top: 2px;">10mg</span>
        </div>
        <div style="display: flex; flex-direction: column; align-items: center;">
            <div style="width: 6cqw; height: 17cqh; background-color: #a78bfa; border-radius: 2px 2px 0 0;"></div>
            <span style="font-size: 5cqw; color: #64748b; font-family: sans-serif; margin-top: 2px;">25mg</span>
        </div>
        <div style="display: flex; flex-direction: column; align-items: center;">
            <div style="width: 6cqw; height: 12cqh; background-color: #c4b5fd; border-radius: 2px 2px 0 0;"></div>
            <span style="font-size: 5cqw; color: #64748b; font-family: sans-serif; margin-top: 2px;">50mg</span>
        </div>
    </div>
    """
    app.add_overlay("node_2_card", node_2_bars)
    app.map("node_2_card", hover_color="#faf5ff", glow=True)

    # Node 3: Phase 2 (Efficacy)
    app.add_scalable_text("node_3_card", "2023-2024: PHASE II", left="5%", top="5%", width="90%", height="20%", font_size="15%", font_weight="800", color="#10b981")
    app.add_scalable_text("node_3_card", "Efficacy in 300 patients vs standard care.", left="5%", top="25%", width="90%", height="15%", font_size="10%", font_weight="500", color="#475569", auto_shrink=True)

    # Custom HTML Overlay for a Line Chart directly on Node 3
    node_3_lines = """
    <div style="width: 100%; height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: flex-end; padding-bottom: 2cqh; container-type: size;">
        <svg width="60cqw" height="25cqh" viewBox="0 0 100 50" preserveAspectRatio="none">
            <!-- Grid lines -->
            <line x1="0" y1="25" x2="100" y2="25" stroke="#e2e8f0" stroke-width="1" />
            <!-- XYZ-123 (Negative trend) -->
            <polyline points="0,25 25,35 50,45 75,50 100,55" fill="none" stroke="#10b981" stroke-width="3" />
            <!-- Control -->
            <polyline points="0,25 25,28 50,30 75,32 100,35" fill="none" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4" />
        </svg>
    </div>
    """
    app.add_overlay("node_3_card", node_3_lines)
    app.map("node_3_card", hover_color="#f0fdf4", glow=True)


    # Node 4: Phase 3
    app.add_scalable_text("node_4_card", "2025: PHASE III", left="5%", top="10%", width="90%", height="25%", font_size="15%", font_weight="800", color="#f59e0b")
    app.add_scalable_text("node_4_card", "Global multi-center trials (3,500 patients).", left="5%", top="40%", width="90%", height="30%", font_size="10%", font_weight="500", color="#475569", auto_shrink=True)
    app.map("node_4_card", hover_color="#fffbeb", glow=True)

    # Enrollment progress bar directly via native SVG helper
    app.add_scalable_text("node_4_card", "ENROLLMENT PROGRESS", left="5%", top="75%", width="50%", height="15%", font_size="10%", font_weight="700", color="#64748b")
    app.add_scalable_progress_bar("node_4_card", progress="100%", left="55%", top="80%", width="40%", height="5%", rx="4", bg_color="#e2e8f0", fill_color="#f59e0b")

    # Node 5: FDA Approval
    app.add_scalable_text("node_5_card", "2026: FDA APPROVAL", left="5%", top="10%", width="90%", height="25%", font_size="15%", font_weight="800", color="#ef4444")
    app.add_scalable_text("node_5_card", "NDA submitted. Priority review granted.", left="5%", top="40%", width="90%", height="30%", font_size="10%", font_weight="500", color="#475569", auto_shrink=True)
    app.map("node_5_card", hover_color="#fef2f2", glow=True)

    app.add_scalable_text("node_5_card", "EST. PEAK SALES", left="5%", top="75%", width="50%", height="15%", font_size="10%", font_weight="700", color="#64748b")
    app.add_scalable_text("node_5_card", "$3.4B", left="55%", top="70%", width="40%", height="25%", font_size="25%", font_weight="900", color="#ef4444")

    output_path = os.path.join(os.path.dirname(__file__), "timeline.html")
    app.to_html(output_path)
    print(f"Generated: {output_path}")

if __name__ == "__main__":
    run()
