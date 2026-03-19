import sys
import os

# Add the src directory to the path so we can import sivo
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from sivo import Sivo

def create_transitions_example():
    # 1. Create three simple SVG strings that represent different "pages" or "views"

    # View 1: A blue square with a button to go to View 2
    svg_view1 = """
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
        <rect width="800" height="600" fill="#e0f2fe" />
        <text x="400" y="200" font-family="sans-serif" font-size="48" font-weight="bold" fill="#0369a1" text-anchor="middle">View 1: Overview</text>

        <g id="btn_next_1" cursor="pointer">
            <rect x="300" y="300" width="200" height="60" rx="8" fill="#0ea5e9" />
            <text x="400" y="338" font-family="sans-serif" font-size="24" fill="white" text-anchor="middle">Go to View 2 (Flip)</text>
        </g>
    </svg>
    """

    # View 2: A green square with buttons to go to View 3 or back to View 1
    svg_view2 = """
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
        <rect width="800" height="600" fill="#dcfce7" />
        <text x="400" y="200" font-family="sans-serif" font-size="48" font-weight="bold" fill="#15803d" text-anchor="middle">View 2: Details</text>

        <g id="btn_next_2" cursor="pointer">
            <rect x="420" y="300" width="220" height="60" rx="8" fill="#16a34a" />
            <text x="530" y="338" font-family="sans-serif" font-size="20" fill="white" text-anchor="middle">View 3 (Page Turn)</text>
        </g>

        <g id="btn_back_2" cursor="pointer">
            <rect x="160" y="300" width="220" height="60" rx="8" fill="#16a34a" />
            <text x="270" y="338" font-family="sans-serif" font-size="20" fill="white" text-anchor="middle">Back to 1 (Slide)</text>
        </g>
    </svg>
    """

    # View 3: A purple square with a button to go back to View 1
    svg_view3 = """
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
        <rect width="800" height="600" fill="#f3e8ff" />
        <text x="400" y="200" font-family="sans-serif" font-size="48" font-weight="bold" fill="#7e22ce" text-anchor="middle">View 3: Deep Dive</text>

        <g id="btn_home_3" cursor="pointer">
            <rect x="300" y="300" width="200" height="60" rx="8" fill="#9333ea" />
            <text x="400" y="338" font-family="sans-serif" font-size="24" fill="white" text-anchor="middle">Home (Slide Up)</text>
        </g>
    </svg>
    """

    # 2. Initialize Sivo instances for each view
    app1 = Sivo.from_string(svg_view1, disable_panel=True, disable_zoom_controls=True)
    app2 = Sivo.from_string(svg_view2, disable_panel=True, disable_zoom_controls=True)
    app3 = Sivo.from_string(svg_view3, disable_panel=True, disable_zoom_controls=True)

    # 3. Map the elements to trigger drilldowns with specific transition types

    # From View 1 -> View 2 using a 3D "flip" animation
    app1.map("btn_next_1", drill_to="view2", drill_transition="flip", hover_color="#0284c7")

    # From View 2 -> View 3 using a "page-turn" animation
    app2.map("btn_next_2", drill_to="view3", drill_transition="page-turn", hover_color="#15803d")

    # From View 2 -> View 1 using a "slide-right" animation (like going back)
    app2.map("btn_back_2", drill_to="view1", drill_transition="slide-right", hover_color="#15803d")

    # From View 3 -> View 1 using a "slide-up" animation
    app3.map("btn_home_3", drill_to="view1", drill_transition="slide-up", hover_color="#7e22ce")

    # 4. Combine them into a multi-view application using SivoProject
    from sivo.core.project import SivoProject
    project = SivoProject(initial_view_id="view1")
    project.add_view("view1", app1)
    project.add_view("view2", app2)
    project.add_view("view3", app3)

    # 5. Export to an HTML file
    output_path = os.path.join(os.path.dirname(__file__), 'index.html')

    project.to_html(output_path=output_path)

    print(f"Successfully generated example at: {output_path}")
    print("Open this file in a web browser to test the transition animations.")

if __name__ == "__main__":
    create_transitions_example()
