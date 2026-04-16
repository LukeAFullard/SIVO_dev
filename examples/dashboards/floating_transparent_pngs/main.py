from sivo import Sivo
from sivo.core.dashboard import SivoDashboard

def main():
    dashboard = SivoDashboard(
        title="Floating Transparent PNGs",
        columns=4,
        theme="transparent",
        background_image_url="https://images.unsplash.com/photo-1557683316-973673baf926?q=80&w=2000&auto=format&fit=crop"
    )

    dashboard.set_grid_layout(
        desktop='''
        "img1 img2 img3 img4"
        ''',
        mobile='''
        "img1 img2"
        "img3 img4"
        '''
    )

    sivo1 = Sivo.from_string('<svg xmlns="http://www.w3.org/2000/svg" width="200" height="200"><image href="https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png" x="0" y="0" width="200" height="200" id="img1" class="sivo-floating-element"/></svg>', render_mode="svg", theme="transparent")
    sivo1.map(element_id="img1", tooltip="Floating PNG 1", panel_position="right", callback_event="image_clicked", callback_payload={"image_id": "img1"})

    sivo2 = Sivo.from_string('<svg xmlns="http://www.w3.org/2000/svg" width="200" height="200"><image href="https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png" x="0" y="0" width="200" height="200" id="img2" class="sivo-floating-element"/></svg>', render_mode="svg", theme="transparent")
    sivo2.map(element_id="img2", tooltip="Floating PNG 2", panel_position="right", callback_event="image_clicked", callback_payload={"image_id": "img2"})

    sivo3 = Sivo.from_string('<svg xmlns="http://www.w3.org/2000/svg" width="200" height="200"><image href="https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png" x="0" y="0" width="200" height="200" id="img3" class="sivo-floating-element"/></svg>', render_mode="svg", theme="transparent")
    sivo3.map(element_id="img3", tooltip="Floating PNG 3", panel_position="right", callback_event="image_clicked", callback_payload={"image_id": "img3"})

    sivo4 = Sivo.from_string('<svg xmlns="http://www.w3.org/2000/svg" width="200" height="200"><image href="https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png" x="0" y="0" width="200" height="200" id="img4" class="sivo-floating-element"/></svg>', render_mode="svg", theme="transparent")
    sivo4.map(element_id="img4", tooltip="Floating PNG 4", panel_position="right", callback_event="image_clicked", callback_payload={"image_id": "img4"})

    dashboard.add_sivo_block(block_id="sivo1", sivo_app=sivo1, grid_area="img1")
    dashboard.add_sivo_block(block_id="sivo2", sivo_app=sivo2, grid_area="img2")
    dashboard.add_sivo_block(block_id="sivo3", sivo_app=sivo3, grid_area="img3")
    dashboard.add_sivo_block(block_id="sivo4", sivo_app=sivo4, grid_area="img4")

    dashboard.to_html(output_path="examples/dashboards/floating_transparent_pngs/output.html")
    print("Generated floating transparent PNGs dashboard")

if __name__ == "__main__":
    main()
