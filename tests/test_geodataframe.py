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

    # Check to_svg
    svg_str = sivo_app.to_svg()
    assert svg_str is not None
    assert "Area A" in svg_str
    assert "Area B" in svg_str
    assert "<svg" in svg_str

    import os
    import tempfile
    with tempfile.TemporaryDirectory() as tempdir:
        svg_file = os.path.join(tempdir, "test.svg")
        sivo_app.to_svg(output_path=svg_file)
        assert os.path.exists(svg_file)
        with open(svg_file, "r") as f:
            content = f.read()
            assert "Area A" in content
            assert "Area B" in content
            assert "<svg" in content

@pytest.mark.skipif(not HAS_GEOPANDAS, reason="geopandas is required for this test")
def test_from_geodataframe_simplify():
    # Polygon with an unnecessary vertex
    p1 = Polygon([(0, 0), (0.5, 0.01), (1, 0), (1, 1), (0, 1)])

    gdf = gpd.GeoDataFrame({
        'id': ['A'],
        'name': ['Area A'],
        'geometry': [p1]
    })

    # Convert without simplify
    sivo_app_unsimplified = Sivo.from_geodataframe(gdf, id_col='id', name_col='name')
    svg_unsimplified = sivo_app_unsimplified.to_svg()

    # Convert with simplify
    sivo_app_simplified = Sivo.from_geodataframe(gdf, id_col='id', name_col='name', simplify_tolerance=0.1)
    svg_simplified = sivo_app_simplified.to_svg()

    assert len(svg_simplified) < len(svg_unsimplified)
