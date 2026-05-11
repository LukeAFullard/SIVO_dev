import sys
import os

# Add src to the path to import sivo
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from sivo import SivoDashboard, Sivo

def create_shapes_dashboard():
    # Initialize dashboard
    dashboard = SivoDashboard(
        title="SIVO Shapes Example",
                        theme="light",
        gap="normal"
    )

    # We need a basic SVG element to act as a canvas for our shapes to bind to.
    svg_canvas = '''
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 600" width="1000" height="600">
        <!-- Grid layout placeholders for our shapes to bind to -->
        <rect id="box_fish" x="50" y="50" width="250" height="200" fill="transparent" stroke="#ddd" stroke-dasharray="5,5" />
        <rect id="box_tap" x="350" y="50" width="250" height="200" fill="transparent" stroke="#ddd" stroke-dasharray="5,5" />
        <rect id="box_koura" x="650" y="50" width="250" height="200" fill="transparent" stroke="#ddd" stroke-dasharray="5,5" />

        <rect id="box_phone" x="50" y="300" width="250" height="200" fill="transparent" stroke="#ddd" stroke-dasharray="5,5" />
        <rect id="box_internet" x="350" y="300" width="250" height="200" fill="transparent" stroke="#ddd" stroke-dasharray="5,5" />
        <rect id="box_globe" x="650" y="300" width="250" height="200" fill="transparent" stroke="#ddd" stroke-dasharray="5,5" />
    </svg>
    '''

    # Initialize a Sivo canvas instance with the SVG
    sivo_canvas = Sivo.from_string(svg_canvas, layout_size="100%", mobile_layout_size="100%")

    # Render Fish
    sivo_canvas.add_card("box_fish", title="Organic Fish", value="$1.2M", subtitle="Revenues", shape="fish", bg_color="#e0f2fe", border_color="#38bdf8", shadow=True, title_above=True)

    # Render Tap
    sivo_canvas.add_card("box_tap", title="Water Splash", value="85%", subtitle="Capacity", shape="tap_splash", bg_color="#dbeafe", border_color="#60a5fa", shadow=True)

    # Render Koura
    sivo_canvas.add_card("box_koura", title="Koura Crayfish", value="340", subtitle="Population", shape="koura", bg_color="#fee2e2", border_color="#f87171", shadow=True, title_above=True)

    # Render Mobile Phone
    sivo_canvas.add_card("box_phone", title="Mobile Phone", value="App", subtitle="Downloads", shape="mobile_phone", bg_color="#f3f4f6", border_color="#9ca3af", shadow=True)

    # Render Internet
    sivo_canvas.add_card("box_internet", title="The Internet", value="99.9%", subtitle="Uptime", shape="internet", bg_color="#fef3c7", border_color="#fbbf24", shadow=True)

    # Render Globe
    sivo_canvas.add_card("box_globe", title="Global Earth", value="24", subtitle="Regions", shape="globe", bg_color="#ecfdf5", border_color="#34d399", shadow=True)

    # Add the Sivo instance to the dashboard layout block
    dashboard.add_sivo_block("shapes_block", sivo_canvas)

    dashboard.set_grid_layout(
        desktop='''
            "shapes_block"
        ''',
        mobile='''
            "shapes_block"
        '''
    )

    # Generate the output HTML
    output_path = os.path.join(os.path.dirname(__file__), 'dashboard_shapes_output.html')
    with open(output_path, "w") as f:
        f.write(dashboard.to_html())

    print(f"Dashboard successfully generated at: {output_path}")

if __name__ == "__main__":
    create_shapes_dashboard()
