import os
from sivo import Sivo

svg_content = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
    <rect width="100%" height="100%" fill="transparent" />
    <g id="servers">
        <rect id="server-alpha" x="200" y="200" width="150" height="200" rx="10" fill="#e2e8f0" stroke="#94a3b8" stroke-width="2" />
        <rect id="server-beta" x="450" y="200" width="150" height="200" rx="10" fill="#e2e8f0" stroke="#94a3b8" stroke-width="2" />
    </g>
</svg>
"""

def main():
    print("Building Professional Polish Example...")

    # 1. Initialize Sivo with theme="dark" and fade_unselected=True
    sivo_app = Sivo.from_string(svg_content, theme="dark", fade_unselected=True)

    # Map a standard item to show empty state
    sivo_app.map(
        element_id="server-alpha",
        tooltip="Server Alpha"
    )

    # Map an item fetching data to show the sleek loading spinner
    sivo_app.map(
        element_id="server-beta",
        tooltip="Server Beta",
        fetch_url="https://jsonplaceholder.typicode.com/todos/1"
    )

    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    sivo_app.to_html(output_path)

    print(f"Map successfully generated at: {output_path}")

if __name__ == "__main__":
    main()
