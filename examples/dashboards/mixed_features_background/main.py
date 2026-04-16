from sivo import Sivo
from sivo.core.dashboard import SivoDashboard

def main():
    dashboard = SivoDashboard(
        title="Mixed Features Dashboard",
        columns=2,
        background_image_url="https://images.unsplash.com/photo-1557683316-973673baf926?q=80&w=2000&auto=format&fit=crop"
    )

    dashboard.set_grid_layout(
        desktop='''
        "video text"
        "sivo1 sivo2"
        ''',
        mobile='''
        "video"
        "text"
        "sivo1"
        "sivo2"
        '''
    )

    dashboard.add_html_block(
        block_id="video",
        html_content='''
        <iframe width="100%" height="100%" src="https://www.youtube.com/embed/dQw4w9WgXcQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="min-height: 300px;"></iframe>
        ''',
        grid_area="video"
    )

    dashboard.add_html_block(
        block_id="text",
        html_content='''
        <div style="padding: 20px;">
            <h2>Dashboard Text Block</h2>
            <p>This is a text block demonstrating mixing raw HTML with Sivo blocks.</p>
            <img src="https://via.placeholder.com/150" alt="placeholder" style="max-width: 100%; border-radius: 8px;">
        </div>
        ''',
        grid_area="text"
    )

    sivo1 = Sivo.from_string('<svg width="200" height="200"><circle cx="100" cy="100" r="50" fill="blue" id="c1"/></svg>', theme="transparent")
    sivo1.map(element_id="c1", tooltip="A blue circle")
    dashboard.add_sivo_block(block_id="sivo1", sivo_app=sivo1, grid_area="sivo1")

    sivo2 = Sivo.from_string('<svg width="200" height="200"><rect x="50" y="50" width="100" height="100" fill="red" id="r1"/></svg>', theme="transparent")
    sivo2.map(element_id="r1", tooltip="A red square")
    dashboard.add_sivo_block(block_id="sivo2", sivo_app=sivo2, grid_area="sivo2")

    html = dashboard.to_html(output_path="examples/dashboards/mixed_features_background/output.html")
    print("Generated mixed features dashboard")

if __name__ == "__main__":
    main()
