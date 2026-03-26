import os
from sivo import Sivo

def main():
    # 1. Initialize Sivo from a pre-built SVG Dashboard Template
    # The 'dashboards/sidebar_layout' template contains a main panel and three sidebar metrics
    sivo_app = Sivo.from_template("dashboards/sidebar_layout")

    # 2. Map data and interactions to the template's placeholder regions
    sivo_app.map(
        "main_panel",
        hover_color="#f8fafc",
        tooltip="Primary Visualization Area",
        html="<p>This is where your main graph or map would go.</p>"
    )

    sivo_app.map(
        "metric_box_1",
        hover_color="#eff6ff",
        tooltip="Q1 Revenue Analysis"
    )

    sivo_app.map(
        "metric_box_2",
        hover_color="#ecfdf5",
        tooltip="Active User Growth"
    )

    sivo_app.map(
        "metric_box_3",
        hover_color="#fffbeb",
        tooltip="Customer Churn Rate"
    )

    # We can also dynamically update the text within the template
    # SIVO's 'add_scalable_text' can be used, or you can natively embed another SVG
    # Here we just show that the template has pre-built text boxes for styling.

    # 3. Export to HTML
    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    sivo_app.to_html(output_path)

    print(f"Exported SVG Template Dashboard to {output_path}")

if __name__ == "__main__":
    main()
