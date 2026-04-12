import geopandas as gpd
from urllib.request import urlopen
from zipfile import ZipFile
from io import BytesIO
import os
from sivo import Sivo
import shutil

def main():
    url = "https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip"

    print(f"Downloading {url}...")
    try:
        http_response = urlopen(url)
        zipfile = ZipFile(BytesIO(http_response.read()))

        os.makedirs("/tmp/naturalearth_geocoder", exist_ok=True)
        zipfile.extractall(path="/tmp/naturalearth_geocoder")

        print("Loading geodataframe...")
        gdf = gpd.read_file("/tmp/naturalearth_geocoder/ne_110m_admin_0_countries.shp")

        print("Generating SIVO app with geocoder enabled...")
        sivo_app = Sivo.from_geodataframe(
            gdf,
            id_col="ISO_A2",
            name_col="NAME",
            enable_geocoder=True,
            geocode_provider="nominatim",
            default_panel_position="none",
            layout_size="90%"
        )

        output_path = os.path.join(os.path.dirname(__file__), "output.html")
        sivo_app.to_html(output_path)
        print(f"Successfully generated {output_path}")

    finally:
        shutil.rmtree("/tmp/naturalearth_geocoder", ignore_errors=True)

if __name__ == "__main__":
    main()
