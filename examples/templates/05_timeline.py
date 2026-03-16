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
        theme="light"
    )

    # Header - Make it clear it's a financial/startup journey
    app.add_scalable_text("header_area", "Startup Funding Journey", left="5%", top="20%", width="90%", height="40%", font_size="35%", font_weight="900", color="#0f172a", align="left")
    app.add_scalable_text("header_area", "From Pre-Seed to Series C Valuation Growth", left="5%", top="60%", width="90%", height="20%", font_size="15%", font_weight="600", color="#64748b", align="left")

    # Node 1: Pre-Seed
    app.add_scalable_text("node_1_card", "2020: PRE-SEED ($500K)", left="5%", top="10%", width="90%", height="25%", font_size="15%", font_weight="800", color="#3b82f6")
    app.add_scalable_text("node_1_card", "Initial product development, core team assembly, and beta launch.", left="5%", top="40%", width="90%", height="30%", font_size="10%", font_weight="500", color="#475569", auto_shrink=True)
    app.add_scalable_text("node_1_card", "VALUATION: $2.5M", left="5%", top="75%", width="90%", height="15%", font_size="12%", font_weight="700", color="#64748b")

    # Node 2: Seed
    app.add_scalable_text("node_2_card", "2021: SEED ($2.5M)", left="5%", top="10%", width="90%", height="25%", font_size="15%", font_weight="800", color="#8b5cf6")
    app.add_scalable_text("node_2_card", "Product-market fit achieved. First 1,000 paying customers acquired.", left="5%", top="40%", width="90%", height="30%", font_size="10%", font_weight="500", color="#475569", auto_shrink=True)
    app.add_scalable_text("node_2_card", "VALUATION: $15M", left="5%", top="75%", width="90%", height="15%", font_size="12%", font_weight="700", color="#64748b")

    # Node 3: Series A (The big expansion)
    app.add_scalable_text("node_3_card", "2022: SERIES A ($12M)", left="5%", top="10%", width="90%", height="20%", font_size="15%", font_weight="800", color="#10b981")
    app.add_scalable_text("node_3_card", "Scaling GTM motion, international expansion.", left="5%", top="35%", width="90%", height="15%", font_size="10%", font_weight="500", color="#475569", auto_shrink=True)

    # Map a line chart here to show ARR growth leading to Series A
    app.map_line_chart(
        element_id="node_3_card",
        title="",
        categories=["Q1", "Q2", "Q3", "Q4"],
        data=[100, 300, 600, 1200],
        color="#10b981",
        smooth=True,
        extra_options={
            "grid": {"top": 60, "bottom": 30, "left": 40, "right": 20},
            "backgroundColor": "transparent"
        }
    )

    # Node 4: Series B
    app.add_scalable_text("node_4_card", "2024: SERIES B ($35M)", left="5%", top="10%", width="90%", height="25%", font_size="15%", font_weight="800", color="#f59e0b")
    app.add_scalable_text("node_4_card", "Acquisition of main competitor and launch of new product suite.", left="5%", top="40%", width="90%", height="30%", font_size="10%", font_weight="500", color="#475569", auto_shrink=True)

    # Show user growth progress bar
    app.add_scalable_text("node_4_card", "USER BASE GROWTH (1M TARGET)", left="5%", top="75%", width="50%", height="15%", font_size="8%", font_weight="700", color="#64748b")
    app.add_scalable_progress_bar("node_4_card", progress="85%", left="55%", top="80%", width="40%", height="5%", rx="4", bg_color="#e2e8f0", fill_color="#f59e0b")

    # Node 5: Series C (Current)
    app.add_scalable_text("node_5_card", "2026: SERIES C ($100M)", left="5%", top="10%", width="90%", height="25%", font_size="15%", font_weight="800", color="#ef4444")
    app.add_scalable_text("node_5_card", "Pre-IPO preparations, achieving profitability, and global dominance.", left="5%", top="40%", width="90%", height="30%", font_size="10%", font_weight="500", color="#475569", auto_shrink=True)

    app.add_scalable_text("node_5_card", "CURRENT VALUATION", left="5%", top="75%", width="50%", height="15%", font_size="10%", font_weight="700", color="#64748b")
    app.add_scalable_text("node_5_card", "$1.2B", left="55%", top="70%", width="40%", height="25%", font_size="25%", font_weight="900", color="#ef4444")


    output_path = os.path.join(os.path.dirname(__file__), "05_timeline.html")
    app.to_html(output_path)
    print(f"Generated: {output_path}")

if __name__ == "__main__":
    run()
