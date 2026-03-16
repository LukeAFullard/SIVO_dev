from sivo import Sivo
import os
import lxml.etree as etree

def run():
    template_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "src", "sivo", "templates", "bento_grid_dashboard_2026.svg"
    )

    app = Sivo.from_svg(
        template_path,
        disable_zoom_controls=False,
        lock_canvas=True,
        theme="light"
    )

    # Header
    app.fill_template_zone("text_performance_overview", "FinTech Global Command Center", font_size="100%", font_weight="900", color="#0f172a")
    app.fill_template_zone("text_q3_2026_analytics_dashboard", "Real-time Transactions & Market Overview • Q3 2026", font_size="100%", color="#64748b")

    # Card Main: Global Map
    app.map_nested_map_chart(
        element_id="card-main",
        title="Active Trading Volumes",
        map_name="world",
        map_data="world",
        data=[
            {"name": "United States", "value": 1500},
            {"name": "United Kingdom", "value": 800},
            {"name": "China", "value": 1200},
            {"name": "Germany", "value": 600},
            {"name": "India", "value": 900},
            {"name": "Brazil", "value": 400}
        ],
        min_val=0,
        max_val=1500,
        title_size=24,
        title_color="#0f172a",
        extra_options={"visualMap": {"show": False}, "backgroundColor": "transparent"}
    )

    # Card Users: System Status & Infrastructure
    app.add_scalable_text("rect-users", "INFRASTRUCTURE", left="8%", top="15%", width="80%", height="15%", font_size="12%", font_weight="700", color="#64748b")
    app.add_scalable_text("rect-users", "Primary node latency across all global trading APIs remains stable.", left="8%", top="35%", width="80%", height="25%", font_size="8%", color="#475569", auto_shrink=True)

    app.add_scalable_text("rect-users", "UPTIME", left="8%", top="65%", width="20%", height="10%", font_size="10%", font_weight="700", color="#64748b")
    app.add_scalable_text("rect-users", "99.999%", left="8%", top="75%", width="30%", height="20%", font_size="18%", font_weight="800", color="#10b981")

    app.add_scalable_progress_bar("rect-users", progress="99.9%", left="40%", top="75%", width="50%", height="5%", rx="6", bg_color="#e2e8f0", fill_color="#10b981")

    # Card Conversion: Key Personnel or Market News
    # Add a shadow overlay text on the image
    app.add_scalable_text("rect-conversion", "MARKET ALERT", left="10%", top="20%", width="50%", height="15%", font_size="12%", font_weight="800", color="#ef4444")
    app.add_scalable_text("rect-conversion", "Crypto volatility spike detected in Asian markets. Automated hedging protocols active.", left="10%", top="45%", width="80%", height="40%", font_size="10%", font_weight="600", color="#0f172a", auto_shrink=True)

    # Bottom Cards: Engagement, Bounce, Satisfaction -> Revenue, Trades, Alerts
    # Card 1: Revenue
    app.add_scalable_text("card-engagement", "DAILY REVENUE", left="10%", top="20%", width="80%", height="15%", font_size="12%", font_weight="700", color="#64748b")
    app.add_scalable_text("card-engagement", "$2.4M", left="10%", top="45%", width="80%", height="35%", font_size="35%", font_weight="900", color="#3b82f6")
    app.add_scalable_text("card-engagement", "▲ 12.5% vs yesterday", left="10%", top="80%", width="80%", height="10%", font_size="8%", font_weight="600", color="#10b981")

    # Card 2: Trades
    app.add_scalable_text("card-bounce", "ACTIVE TRADES", left="10%", top="20%", width="80%", height="15%", font_size="12%", font_weight="700", color="#64748b")

    # Add a small line chart here instead of just text
    app.map_line_chart(
        element_id="card-bounce",
        title="",
        categories=["08:00", "09:00", "10:00", "11:00", "12:00"],
        data=[120, 300, 250, 400, 380],
        color="#8b5cf6",
        smooth=True,
        extra_options={
            "xAxis": {"show": False},
            "yAxis": {"show": False},
            "grid": {"top": 40, "bottom": 30, "left": 10, "right": 10},
            "backgroundColor": "transparent"
        }
    )
    app.add_scalable_text("card-bounce", "342K/hr", left="10%", top="75%", width="80%", height="15%", font_size="15%", font_weight="800", color="#0f172a")

    # Card 3: Alert Level
    app.add_scalable_text("card-satisfaction", "SYSTEM THREAT LEVEL", left="10%", top="20%", width="80%", height="15%", font_size="12%", font_weight="700", color="#64748b")
    app.add_scalable_text("card-satisfaction", "LOW", left="10%", top="45%", width="80%", height="35%", font_size="35%", font_weight="900", color="#10b981")
    app.add_scalable_text("card-satisfaction", "No active DDoS patterns.", left="10%", top="80%", width="80%", height="10%", font_size="8%", font_weight="600", color="#64748b")


    output_path = os.path.join(os.path.dirname(__file__), "02_bento_grid.html")
    app.to_html(output_path)
    print(f"Generated: {output_path}")

if __name__ == "__main__":
    run()
