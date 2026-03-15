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
    # 3. Add Custom Text Overlays to replace "Blank Zone" SVGs
    # ---------------------------------------------------------

    # Using scale_with_zoom=True forces ECharts to render the div natively matching the zoom level.
    # The font-size is specified relative to the 1200x800 viewBox pixel space. We adjust standard positioning by adding offsets.

    # Header
    app.add_overlay("header-subtitle-top-placeholder", "<div style='color: #64748b; font-family: -apple-system, sans-serif; font-weight: 600; letter-spacing: 2px; font-size: 14px; white-space: nowrap;'>UN ENVIRONMENTAL PROGRAM</div>", scale_with_zoom=True, offset_y=-5)
    app.add_overlay("header-title-top-placeholder", "<div style='color: #0f172a; font-family: -apple-system, sans-serif; font-weight: 800; font-size: 38px; white-space: nowrap;'>Climate Action 2026</div>", scale_with_zoom=True, offset_y=10)

    # Center Hub (Earth Health Index)
    app.add_overlay("center-subtitle-placeholder", "<div style='color: #64748b; font-family: -apple-system, sans-serif; font-weight: bold; font-size: 14px; text-align: center; white-space: nowrap;'>Global Target Limit</div>", scale_with_zoom=True, offset_y=-5)
    app.add_overlay("center-value-placeholder", "<div style='color: #ef4444; font-family: -apple-system, sans-serif; font-weight: 800; font-size: 60px;'>1.5°C</div>", scale_with_zoom=True, offset_y=20)

    # Card 1 (Top Left) - CO2 Levels
    app.add_overlay("card-1-title-placeholder", "<div style='color: #1e293b; font-family: -apple-system, sans-serif; font-weight: 700; font-size: 18px; white-space: nowrap;'>Global CO2 Levels</div>", scale_with_zoom=True, offset_y=0)
    app.add_overlay("card-1-value-placeholder", "<div style='color: #3b82f6; font-family: -apple-system, sans-serif; font-weight: 800; font-size: 32px; white-space: nowrap;'>421 ppm</div>", scale_with_zoom=True, offset_y=30)

    # Card 2 (Top Right) - Sea Level Rise
    app.add_overlay("card-2-title-placeholder", "<div style='color: #1e293b; font-family: -apple-system, sans-serif; font-weight: 700; font-size: 18px; white-space: nowrap;'>Sea Level Rise</div>", scale_with_zoom=True, offset_y=0)
    app.add_overlay("card-2-value-placeholder", "<div style='color: #8b5cf6; font-family: -apple-system, sans-serif; font-weight: 800; font-size: 32px; white-space: nowrap;'>+3.4 mm/yr</div>", scale_with_zoom=True, offset_y=30)

    # Card 3 (Bottom Left) - Global Temp Anomaly
    app.add_overlay("card-3-title-placeholder", "<div style='color: #1e293b; font-family: -apple-system, sans-serif; font-weight: 700; font-size: 18px; white-space: nowrap;'>Temp Anomaly</div>", scale_with_zoom=True, offset_y=0)
    app.add_overlay("card-3-value-placeholder", "<div style='color: #ec4899; font-family: -apple-system, sans-serif; font-weight: 800; font-size: 32px; white-space: nowrap;'>+1.1°C</div>", scale_with_zoom=True, offset_y=30)

    # Card 4 (Bottom Right) - Arctic Ice Minimum
    app.add_overlay("card-4-title-placeholder", "<div style='color: #1e293b; font-family: -apple-system, sans-serif; font-weight: 700; font-size: 18px; white-space: nowrap;'>Arctic Ice Extent</div>", scale_with_zoom=True, offset_y=0)
    app.add_overlay("card-4-value-placeholder", "<div style='color: #10b981; font-family: -apple-system, sans-serif; font-weight: 800; font-size: 32px; white-space: nowrap;'>-12.6%</div>", scale_with_zoom=True, offset_y=30)

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