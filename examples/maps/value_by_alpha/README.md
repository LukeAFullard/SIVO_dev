# Value-by-Alpha Map Example

## Purpose
This example demonstrates how to create a **Value-by-Alpha Map** using SIVO. A Value-by-Alpha map is a bivariate thematic map that uses color to represent one variable (the "value") and opacity to represent another variable (the "alpha").

In this specific example, the map visualizes:
- **Income Level** as the base color (the value).
- **Population Density** as the opacity (the alpha).

This technique allows areas with high population density to appear more opaque and distinct, while areas with low population density fade into the background, effectively preventing visually large but sparsely populated areas from dominating the map.

## How it works

1. **Creating the Map Geometries**: The script generates mock geospatial data with four adjacent square polygons using `shapely` and wraps it in a `geopandas.GeoDataFrame`. The mock data includes columns for `id`, `name`, `income_rate`, and `population_density`.

2. **Initializing the Application**:
   The `Sivo.from_geodataframe` method is called to initialize the SIVO app with the generated GeoDataFrame.
   - `disable_panel=True` is used to hide the sidebar panel, focusing the view purely on the generated map.

3. **Applying Value-by-Alpha Mapping**:
   The `apply_value_by_alpha()` method is called to style the geometries.
   ```python
   app.apply_value_by_alpha(
       base_data_map=income_map,
       alpha_data_map=density_map,
       min_color="#fee2e2",
       max_color="#7f1d1d",
       min_alpha=0.2,
       max_alpha=1.0,
       show_legend=True
   )
   ```
   - `base_data_map` maps region IDs to their corresponding income rates to determine the base color.
   - `alpha_data_map` maps region IDs to their corresponding population density to determine the opacity level.
   - `min_color` and `max_color` define the color gradient for the base value (Income).
   - `min_alpha` and `max_alpha` define the range of opacity for the alpha value (Population Density).
   - `show_legend=True` displays a combined, dual-axis legend in the rendered output.

4. **Generating Output**:
   Finally, the visualization is rendered as a standalone HTML file (`output.html`) using `app.to_html()`.

## Running the Example
To run this example, ensure you have the required dependencies installed (including `geopandas` and `shapely`) and execute the following command from the repository root:
```bash
PYTHONPATH=src python examples/maps/value_by_alpha/main.py
```
This will generate an `output.html` file in this directory which can be opened in any web browser.
