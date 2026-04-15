from sivo import Sivo
from sivo.core.dashboard import SivoDashboard

def main():
    dashboard = SivoDashboard(
        title="Floating Transparent PNGs",
        columns=2,
        theme="transparent"
    )

    sivo1 = Sivo.from_string('<svg xmlns="http://www.w3.org/2000/svg" width="200" height="200"><image href="https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png" x="0" y="0" width="200" height="200" id="img1" class="sivo-floating-element"/></svg>', render_mode="svg")
    sivo1.map(element_id="img1", tooltip="Floating PNG 1", panel_position="right", callback_event="image_clicked", callback_payload={"image_id": "img1"})

    sivo2 = Sivo.from_string('<svg xmlns="http://www.w3.org/2000/svg" width="200" height="200"><image href="https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png" x="0" y="0" width="200" height="200" id="img2" class="sivo-floating-element"/></svg>', render_mode="svg")
    sivo2.map(element_id="img2", tooltip="Floating PNG 2", panel_position="right", callback_event="image_clicked", callback_payload={"image_id": "img2"})

    dashboard.add_sivo_block(block_id="sivo1", sivo_app=sivo1)
    dashboard.add_sivo_block(block_id="sivo2", sivo_app=sivo2)

    dashboard.to_html(output_path="examples/dashboards/floating_transparent_pngs/output.html")
    print("Generated floating transparent PNGs dashboard")

if __name__ == "__main__":
    main()
