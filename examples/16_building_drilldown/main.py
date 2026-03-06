import os
from sivo import Sivo
from sivo.core.project import SivoProject

def main():
    base_dir = os.path.dirname(__file__)
    building_svg_path = os.path.join(base_dir, "building.svg")
    floorplan_svg_path = os.path.join(base_dir, "floorplan.svg")
    room_svg_path = os.path.join(base_dir, "room.svg")

    building_app = Sivo.from_svg(building_svg_path)
    floorplan_app = Sivo.from_svg(floorplan_svg_path)
    room_app = Sivo.from_svg(room_svg_path)

    # 1. Level 1: Building -> Drill down to Floorplan
    building_app.map(
        element_id="building1",
        tooltip="Click to enter Main Building",
        drill_to="floorplan_view",
        hover_color="#b6c99c",
        glow=True
    )

    # 2. Level 2: Floorplan -> Drill down to Room A
    floorplan_app.map(
        element_id="roomA",
        tooltip="Click to enter Room A",
        drill_to="room_view",
        hover_color="#ff8c85",
        glow=True
    )

    # Let's map Room B to something simple
    floorplan_app.map(
        element_id="roomB",
        tooltip="Room B (Locked)",
        color="#d3d3d3"
    )

    # 3. Level 3: Inside Room A
    room_app.map(
        element_id="desk1",
        tooltip="Jules's Desk",
        hover_color="#8b4513",
        glow=True
    )

    room_app.map(
        element_id="chair1",
        tooltip="Ergonomic Chair",
        hover_color="#5c9ac4"
    )

    # Assemble into a multi-view project
    project = SivoProject(initial_view_id="building_view")
    project.add_view("building_view", building_app)
    project.add_view("floorplan_view", floorplan_app)
    project.add_view("room_view", room_app)

    output_path = os.path.join(base_dir, "output.html")
    project.to_html(output_path)
    print(f"Exported interactive HTML with triple drill-down to {output_path}")

if __name__ == "__main__":
    main()
