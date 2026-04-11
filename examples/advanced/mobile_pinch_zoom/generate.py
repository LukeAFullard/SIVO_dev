import sys
import os

# Ensure PYTHONPATH is set so sivo module can be found
sys.path.insert(0, os.path.abspath('src'))

from sivo import Sivo

def create_example():
    # Set default_panel_position so that mapped HTML is actually displayed
    app = Sivo.from_string('<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><rect id="box" x="10" y="10" width="80" height="80" fill="lightblue"/></svg>', default_panel_position="overlay")

    app.map("box", html="<h2>Pinch to zoom!</h2><p>Try it on mobile.</p>", hover_color="lightgreen")

    app.to_html("examples/advanced/mobile_pinch_zoom/index.html")

    print("Example generated successfully at examples/advanced/mobile_pinch_zoom/index.html")

if __name__ == "__main__":
    create_example()
