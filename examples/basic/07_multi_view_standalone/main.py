import os
from sivo import Sivo
from sivo.core.project import SivoProject

def main():
    # 1. Initialize multiple independent SVG views
    # View 1: Main Map
    map_path = os.path.join(os.path.dirname(__file__), "sample.svg")
    map_view = Sivo.from_svg(map_path)

    # Map the house drill-down directly to a view ID ("floor_view")
    map_view.map(
        element_id="house",
        tooltip="Enter House",
        drill_to="floor_view",  # Note: mapped to an internal view ID, not a .svg file
        hover_color="orange"
    )

    map_view.map(element_id="mountain1", tooltip="A big mountain", color="#a0a0a0")

    # View 2: Floor Plan
    floor_path = os.path.join(os.path.dirname(__file__), "floor1.svg")
    floor_view = Sivo.from_svg(floor_path)

    floor_view.map(
        element_id="room101",
        tooltip="Living Room",
        color="#aaddff",
        hover_color="#5599ff"
    )
    floor_view.add_marker("room101", icon="🛋️", label="Living Room")

    # 2. Bundle multiple views into a single, offline HTML project
    project = SivoProject(initial_view_id="map_view")

    # Add views. The first view added is the default view.
    project.add_view("map_view", map_view)
    project.add_view("floor_view", floor_view)

    # 3. Export to a single bundled HTML file
    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    project.to_html(output_path)

    print(f"Exported offline multi-view interactive HTML to {output_path}")

if __name__ == "__main__":
    main()
