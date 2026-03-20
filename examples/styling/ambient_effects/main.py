import os
from sivo import Sivo

def main():
    svg_string = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 600">
        <rect id="bg" width="1000" height="600" fill="#0f172a" />
        <path id="mountain" d="M0,600 L300,300 L600,600 Z" fill="#1e293b" />
        <path id="mountain2" d="M400,600 L700,200 L1000,600 Z" fill="#334155" />
    </svg>"""

    # Initialize Sivo with a dark theme and 'snow' ambient effect
    sivo_app = Sivo.from_string(
        svg_string,
        title="Winter Mountains",
        subtitle="Testing the 'snow' ambient effect overlay",
        theme="dark",
        ambient_effect="snow",
        disable_panel=True
    )

    sivo_app.map("mountain", tooltip="Peak 1")
    sivo_app.map("mountain2", tooltip="Peak 2")

    output_file = os.path.join(os.path.dirname(__file__), 'output.html')
    sivo_app.to_html(output_file)
    print(f"Generated Ambient Effects Example at {output_file}")

if __name__ == "__main__":
    main()
