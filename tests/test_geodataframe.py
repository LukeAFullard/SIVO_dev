import pytest
from sivo.core.sivo import Sivo

try:
    import geopandas as gpd
    from shapely.geometry import Polygon
    HAS_GEOPANDAS = True
except ImportError:
    HAS_GEOPANDAS = False

@pytest.mark.skipif(not HAS_GEOPANDAS, reason="geopandas is required for this test")
def test_from_geodataframe():
    p1 = Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])
    p2 = Polygon([(1, 0), (2, 0), (2, 1), (1, 1)])

    gdf = gpd.GeoDataFrame({
        'id': ['A', 'B'],
        'name': ['Area A', 'Area B'],
        'geometry': [p1, p2]
    })

    sivo_app = Sivo.from_geodataframe(gdf, id_col='id', name_col='name')

    # Check that mappings were created for the areas
    mappings = sivo_app.infographic.mappings
    assert 'Area A' in mappings
    assert 'Area B' in mappings

    # Check that bounding coords were correctly set
    bounding_coords = sivo_app.infographic.bounding_coords
    assert bounding_coords is not None
    assert len(bounding_coords) == 2
    assert bounding_coords[0][0] == 0.0
    assert bounding_coords[0][1] == 0.0
    assert bounding_coords[1][0] == 2.0
    assert bounding_coords[1][1] == 1.0

    # Check that it exports correctly
    html_str = sivo_app.to_html()
    assert html_str is not None
    assert "Area A" in html_str
    assert "Area B" in html_str
