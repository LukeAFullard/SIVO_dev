import os
from sivo import Sivo

def main():
    svg_path = os.path.join(os.path.dirname(__file__), "sample.svg")

    sivo_app = Sivo.from_svg(svg_path)

    # Click the shape to dynamically fetch data and display it in the side panel.
    # By providing fetch_data_path="fact", SIVO will extract only the "fact" string
    # from the JSON response instead of printing the whole object.
    sivo_app.map(
        element_id="play_button",
        tooltip="Click to fetch cat fact",
        fetch_url="https://catfact.ninja/fact",
        fetch_data_path="fact",
        panel_position="top",
        hover_color="#e68a00",
        glow=True
    )

    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    sivo_app.to_html(output_path)
    print(f"Exported API Fetch interactive HTML to {output_path}")

if __name__ == "__main__":
    main()
