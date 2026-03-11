import os
from sivo import Sivo

def main():
    # Provide a simple SVG representing a basic dashboard element
    svg = """
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 200">
        <rect id="button_dashboard" x="50" y="50" width="300" height="100" fill="#4CAF50" rx="10" />
        <text x="200" y="110" font-family="Arial" font-size="24" fill="white" text-anchor="middle" pointer-events="none">Click to Drill-Through</text>
    </svg>
    """

    sivo_app = Sivo.from_string(svg, title="Drill-Through Action Example")

    # Map the button to drill-through to a new URL
    sivo_app.map(
        element_id="button_dashboard",
        tooltip="Navigates to example.com in same tab",
        drill_through="https://example.com"
    )

    output_path = os.path.join(os.path.dirname(__file__), "drill_through_example.html")
    sivo_app.to_html(output_path)
    print(f"Drill-Through example generated at {output_path}")

if __name__ == "__main__":
    main()
