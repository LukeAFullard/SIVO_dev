"""
Adding Information Cards to SVG Elements
========================================

This example demonstrates how to use the `add_card()` API to dynamically inject
perfectly-scaled information cards (containing a title, value, subtitle, and body text)
anchored directly to the bounding boxes of target SVG elements.

It also showcases different card shapes (rect, circle, pill, ellipse) and how text
is automatically clipped and shrunken to prevent overflowing the card boundaries.
"""

from sivo import Sivo
import os

def main():
    # Initialize a Sivo app using the four_quadrants built-in dashboard template
    # We use this because it has four clearly defined named rectangle regions.
    sivo_app = Sivo.from_template("dashboards/four_quadrants", layout_size="95%")

    # Add interactive mapping for the quadrants so they are clickable
    sivo_app.map("quadrant_1", hover_color="#f1f5f9", tooltip="Water Quality Station A")
    sivo_app.map("quadrant_2", hover_color="#f1f5f9", tooltip="Water Quality Station B")
    sivo_app.map("quadrant_3", hover_color="#f1f5f9", tooltip="Water Quality Station C")
    sivo_app.map("quadrant_4", hover_color="#f1f5f9", tooltip="Water Quality Station D")

    # Add an Informational Card with a Body paragraph
    # We set width and height slightly smaller than the region to create padding.
    sivo_app.add_card(
        "quadrant_1",
        title="E. coli Levels",
        value="Elevated",
        subtitle="Warning: Unsafe for swimming",
        body="High levels of E. coli bacteria in water bodies pose significant risks to human health. Exposure through swimming or accidental ingestion can lead to severe gastrointestinal illness, stomach cramps, nausea, and diarrhea. Vulnerable populations, such as children and the elderly, are at an increased risk of severe complications.",
        width="80%",
        height="80%",
        left="10%",
        top="10%",
        shape="rect",
        bg_color="#ffffff",
        border_color="#ef4444",
        border_width="2px",
        rx="12",
        title_color="#991b1b",
        value_color="#dc2626",
        subtitle_color="#ef4444",
        body_color="#475569"
    )

    # Add a circular card to Quadrant 2
    # Notice the text is centered for circle and ellipse shapes
    sivo_app.add_card(
        "quadrant_2",
        title="Active Users",
        value="45k",
        subtitle="This week",
        width="60%",
        height="60%",
        left="20%",
        top="20%",
        shape="circle",
        bg_color="#1e293b", # Dark mode card
        border_color="#334155",
        title_color="#94a3b8",
        value_color="#f8fafc",
        subtitle_color="#cbd5e1"
    )

    # Add an elliptical card to Quadrant 3
    # We use a very long title and value here to demonstrate the auto-shrink textLength feature
    sivo_app.add_card(
        "quadrant_3",
        title="Server Load (Extremely Long Title Example)",
        value="94% Capacity Reached",
        subtitle="Critical Action Required Immediately",
        width="80%",
        height="60%",
        left="10%",
        top="20%",
        shape="ellipse",
        bg_color="#fef2f2",
        border_color="#ef4444",
        border_width="2px",
        title_color="#991b1b",
        value_color="#dc2626",
        subtitle_color="#ef4444"
    )

    # Add a pill-shaped card to Quadrant 4
    sivo_app.add_card(
        "quadrant_4",
        title="Customer Satisfaction",
        value="4.8/5.0",
        subtitle="Based on 1,024 reviews",
        width="80%",
        height="40%",
        left="10%",
        top="30%",
        shape="pill",
        bg_color="#fdfbeb",
        border_color="#fde047",
        title_color="#854d0e",
        value_color="#ca8a04",
        subtitle_color="#a16207"
    )

    # Generate the output HTML
    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    print(f"Generating HTML bundle to '{output_path}'...")
    sivo_app.to_html(output_path)
    print("Done!")

if __name__ == "__main__":
    main()
