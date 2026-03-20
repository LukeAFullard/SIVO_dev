import os
from sivo import Sivo

def main():
    svg_path = os.path.join(os.path.dirname(__file__), "sample.svg")

    sivo_app = Sivo.from_svg(svg_path)

    # Click the shape to open a native HTML form in the panel.
    # Submission emits a 'sivo_click' event to parent window (e.g. Streamlit backend)
    sivo_app.map(
        element_id="play_button",
        tooltip="Click to report an issue",
        form_fields=[
            {"name": "username", "label": "Your Name", "type": "text"},
            {"name": "issue", "label": "Describe the Issue", "type": "textarea"}
        ],
        form_submit_event="issue_reported",
        panel_position="left",
        hover_color="#cc0000",
        glow=True
    )

    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    sivo_app.to_html(output_path)
    print(f"Exported Form interactive HTML to {output_path}")

if __name__ == "__main__":
    main()
