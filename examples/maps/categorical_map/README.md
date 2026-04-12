# Categorical Map Example

This example demonstrates how to create an interactive categorical map using SIVO from a GeoPandas DataFrame. It classifies different map regions into discrete categories and applies distinct colors to each.

## What it shows

- Creating dummy geospatial polygon data using `shapely` and mapping it to a `GeoDataFrame`.
- Generating an interactive map directly from the `GeoDataFrame` using `Sivo.from_geodataframe()`.
- Applying categorical data using `apply_categorical_map()`, which binds data rows to visual categories based on custom color palettes.
- Creating a draggable legend (`show_legend=True`, `legend_draggable=True`) to make exploring categorical regions easy.
- Removing default side panels using `disable_panel=True` for a full-screen view.

## Relevant Code

```python
    app = Sivo.from_geodataframe(
        gdf=gdf,
        id_col='id',
        name_col='name',
        title="Categorical Map Demo",
        subtitle="Land Cover Classification",
        theme="light",
        disable_panel=True
    )
```

This snippet generates the interactive base map canvas using a provided GeoDataFrame `gdf`.

```python
    # Custom color palette mapping categories to hex colors
    palette = {
        'Forest': '#22c55e',
        'Water': '#3b82f6',
        'Urban': '#cbd5e1',
        'Agriculture': '#fef08a'
    }

    app.apply_categorical_map(
        data_map=category_map,
        color_palette=palette,
        show_legend=True,
        legend_draggable=True,
        item_opacity=0.8,
        border_color="#0f172a",
        border_width=1.5
    )
```

This applies the specific classifications to the map regions, giving each polygon a distinct fill color based on the `land_cover` mapping, and generates a visual legend.

## How to Run

From the root of the repository, execute:

```bash
PYTHONPATH=src python3 examples/maps/categorical_map/main.py
```

This will output an `output.html` file in the same directory.
