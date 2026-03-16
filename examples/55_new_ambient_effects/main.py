from sivo import Sivo

def create_example():
    # We can create a dummy Sivo instance using from_string to avoid initialization issues
    dummy_svg = '<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><rect x="0" y="0" width="100" height="100" fill="transparent"/></svg>'

    # 1. Wind effect
    wind_app = Sivo.from_string(
        dummy_svg,
        title="Ambient Effect: Wind",
        ambient_effect="wind",
        theme="dark"
    )
    with open("examples/55_new_ambient_effects/wind_effect.html", "w") as f:
        f.write(wind_app.to_html())

    # 2. Water effect
    water_app = Sivo.from_string(
        dummy_svg,
        title="Ambient Effect: Water",
        ambient_effect="water",
        theme="dark"
    )
    with open("examples/55_new_ambient_effects/water_effect.html", "w") as f:
        f.write(water_app.to_html())

    # 3. Plants effect
    plants_app = Sivo.from_string(
        dummy_svg,
        title="Ambient Effect: Plants",
        ambient_effect="plants",
        theme="light"
    )
    with open("examples/55_new_ambient_effects/plants_effect.html", "w") as f:
        f.write(plants_app.to_html())

    # 4. Tree effect (With explicit 1.5x speed)
    tree_app = Sivo.from_string(
        dummy_svg,
        title="Ambient Effect: Tree",
        ambient_effect="tree",
        ambient_speed=1.5,
        theme="light"
    )
    with open("examples/55_new_ambient_effects/tree_effect.html", "w") as f:
        f.write(tree_app.to_html())

    print("Examples created successfully!")

if __name__ == "__main__":
    create_example()
