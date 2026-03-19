import sys
import os

# Ensure PYTHONPATH is set so sivo module can be found
sys.path.insert(0, os.path.abspath('src'))

from sivo import Sivo

def create_example():
    app = Sivo.from_string('<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><rect id="box" x="10" y="10" width="80" height="80" fill="lightblue"/></svg>')

    app.map("box", html="<h2>Pinch to zoom!</h2><p>Try it on mobile.</p>", hover_color="lightgreen")

    html_content = app.to_html()

    with open("examples/mobile_pinch_zoom/index.html", "w") as f:
        f.write(html_content)

    print("Example generated successfully at examples/mobile_pinch_zoom/index.html")

if __name__ == "__main__":
    create_example()
