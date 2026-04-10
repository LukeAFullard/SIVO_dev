import os
from sivo import Sivo
from sivo.core.project import SivoProject


def main():
    base_dir = os.path.dirname(__file__)
    svg_path = os.path.join(base_dir, "sample.svg")
    floor1_svg_path = os.path.join(base_dir, "floor1.svg")

    # Main view
    main_view = Sivo.from_svg(svg_path)
    main_view.map(
        element_id="house",
        tooltip="Click to enter the house",
        drill_to="floor1_view",
        hover_color="orange",
        glow=True
    )
    main_view.map(
        element_id="sun",
        tooltip="The Sun",
        color="gold"
    )

    # Secondary view (drilldown target)
    floor1_view = Sivo.from_svg(floor1_svg_path)
    floor1_view.map(
        element_id="room101",
        tooltip="Room 101",
        hover_color="lightblue"
    )

    # Register both views in a SivoProject
    project = SivoProject(initial_view_id="main_view")
    project.add_view("main_view", main_view)
    project.add_view("floor1_view", floor1_view)

    output_path = os.path.join(base_dir, "output.html")
    project.to_html(output_path)
    print(f"Exported interactive HTML to {output_path}")


if __name__ == "__main__":
    main()
