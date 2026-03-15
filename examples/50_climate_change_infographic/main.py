from sivo import Sivo
import os

def build_climate_dashboard():
    template_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "src", "sivo", "templates", "glassmorphic_radial_dashboard_2026.svg"
    )
    output_dir = os.path.dirname(__file__)

    # 1. Initialize Sivo from the Glassmorphic Radial Dashboard template
    app = Sivo.from_svg(
        template_path,
        # Remove the top-left HTML title overlay since we inject a beautiful SVG native header
        disable_zoom_controls=True,
        lock_canvas=True,
        theme="light"
    )

    # 2. Apply the premium glassmorphism template style
    app.apply_template_style("glassmorphism")

    # ---------------------------------------------------------
    # 3. Add Custom Native SVG Text to "Blank Zone" placehders
    # ---------------------------------------------------------

    # We use the new `fill_template_zone` which natively injects `<text>` into the SVG node hierarchy.
    # This completely eliminates HTML DOM scaling overlaps on mobile devices and renders flawlessly natively.

    # Header
    app.fill_template_zone("header-subtitle-top-placeholder", "UN ENVIRONMENTAL PROGRAM", font_size=14, font_weight="600", color="#64748b")
    app.fill_template_zone("header-title-top-placeholder", "Climate Action 2026", font_size=38, font_weight="800", color="#0f172a")

    # Center Hub (Earth Health Index)
    app.fill_template_zone("center-subtitle-placeholder", "Global Target Limit", font_size=14, font_weight="bold", color="#64748b", align="center")
    app.fill_template_zone("center-value-placeholder", "1.5°C", font_size=60, font_weight="800", color="#ef4444", align="center")

    # Card 1 (Top Left) - CO2 Levels
    app.fill_template_zone("card-1-title-placeholder", "Global CO2 Levels", font_size=18, font_weight="700", color="#1e293b")
    app.fill_template_zone("card-1-value-placeholder", "421 ppm", font_size=32, font_weight="800", color="#3b82f6")

    # Card 2 (Top Right) - Sea Level Rise
    app.fill_template_zone("card-2-title-placeholder", "Sea Level Rise", font_size=18, font_weight="700", color="#1e293b")
    app.fill_template_zone("card-2-value-placeholder", "+3.4 mm/yr", font_size=32, font_weight="800", color="#8b5cf6")

    # Card 3 (Bottom Left) - Global Temp Anomaly
    app.fill_template_zone("card-3-title-placeholder", "Temp Anomaly", font_size=18, font_weight="700", color="#1e293b")
    app.fill_template_zone("card-3-value-placeholder", "+1.1°C", font_size=32, font_weight="800", color="#ec4899")

    # Card 4 (Bottom Right) - Arctic Ice Minimum
    app.fill_template_zone("card-4-title-placeholder", "Arctic Ice Extent", font_size=18, font_weight="700", color="#1e293b")
    app.fill_template_zone("card-4-value-placeholder", "-12.6%", font_size=32, font_weight="800", color="#10b981")

    # ---------------------------------------------------------
    # 4. Map Interactive Tooltips and Charts to the Glass Cards
    # ---------------------------------------------------------

    # Map interactive line chart to Card 1
    app.map_line_chart(
        element_id="glass-card-1",
        title="Historical CO2 Emissions",
        categories=["2010", "2015", "2020", "2023", "2026"],
        data=[389.9, 400.8, 412.5, 421.0, 426.4],
        color="#3b82f6",
        tooltip="Click to view historical atmospheric CO2 concentrations (ppm).",
        panel_position="left"
    )

    # Map bar chart to Card 2
    app.map_bar_chart(
        element_id="glass-card-2",
        title="Global Sea Level Rise",
        categories=["1990", "2000", "2010", "2020"],
        data=[21, 55, 93, 131],
        color="#8b5cf6",
        tooltip="Click to see cumulative sea level rise since 1993 (mm).",
        panel_position="right"
    )

    # Map trendline scatter to Card 3
    app.map_trendline_chart(
        element_id="glass-card-3",
        title="Global Surface Temperature Anomaly",
        data=[
            [2015, 0.90], [2016, 1.01], [2017, 0.92],
            [2018, 0.85], [2019, 0.98], [2020, 1.02],
            [2021, 0.85], [2022, 0.89], [2023, 1.18]
        ],
        trendline_color="#ec4899",
        trendline_width=3,
        color="#fb7185",
        tooltip="Click to view global surface temperature anomalies relative to 1880-1920 average.",
        panel_position="left"
    )

    # Simple tooltip for Center Hub
    app.map(
        element_id="center-hub",
        tooltip="Global Temperature Target",
        html="<h3>The 1.5°C Target</h3><p>The Paris Agreement sets out a global framework to avoid dangerous climate change by limiting global warming to well below 2°C and pursuing efforts to limit it to 1.5°C.</p>",
        glow=True
    )

    # 5. Export the Final Interactive HTML Bundle
    output_path = os.path.join(output_dir, "climate_change_dashboard.html")
    app.to_html(output_path)
    print(f"Climate Change Dashboard generated successfully at: {output_path}")

if __name__ == "__main__":
    build_climate_dashboard()