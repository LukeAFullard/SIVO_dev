# GeoDataFrame to SVG Example

This example demonstrates how to convert a Geopandas `GeoDataFrame` directly into an interactive SIVO SVG/HTML map, including geometry simplification and data mapping (choropleth).

## What is being shown
- Converting a `GeoDataFrame` to a SIVO instance using `Sivo.from_geodataframe()`.
- Automatically simplifying complex polygons by specifying `simplify_tolerance`.
- Creating a choropleth map by calling `apply_choropleth()` to map scalar values to colors for each region.

## Relevant Code

```python
import geopandas as gpd
from shapely.geometry import Polygon
from sivo.core.sivo import Sivo

# 1. Create your GeoDataFrame (or load from file)
p1 = Polygon([(0, 0), (2, 0), (2, 2), (0, 2)])
# ...
gdf = gpd.GeoDataFrame({
    'id': ['region_1', ...],
    'name': ['West Sector', ...],
    'value': [100, ...],
    'geometry': [p1, ...]
})

# 2. Convert to Sivo map, simplifying complex geometries
app = Sivo.from_geodataframe(
    gdf,
    id_col='id',
    name_col='name',
    simplify_tolerance=0.2,
    default_panel_position="overlay"
)

# 3. Map values to create a choropleth
app.apply_choropleth(
    data_map={'region_1': 100, 'region_2': 200, 'region_3': 300},
    min_color="#e0f3f8",
    max_color="#014636"
)
```

## Running the Example

Run the main file to generate `output.html` and `output.svg`:

```bash
PYTHONPATH=src python examples/maps/geodataframe_to_svg/main.py
```
