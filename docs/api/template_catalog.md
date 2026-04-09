---
Last Updated: 2026-04-09
SIVO Version: 0.1.0
---

# Template Catalog

SIVO includes a comprehensive library of built-in SVG templates organized by aspect ratios and specific use cases. These templates are designed to be instantiated directly using the `Sivo.from_template()` method, providing a quick start for various interactive data visualization and dashboard projects.

## Usage

You can load a built-in template by passing its filename (without the `.svg` extension if you prefer, though typically exact filenames are better if not specified) to `Sivo.from_template()`.

```python
from sivo import Sivo

# Load a 16:10 aspect ratio template
sivo_app = Sivo.from_template("split_comparison_glass_2026.svg")

# Or from dashboards directory
dashboard_template = Sivo.from_template("sidebar_layout_template.svg")
```

*(Note: The exact method parameter may just require the filename. Check your specific SIVO version's `Sivo.from_template()` documentation for exact path resolution rules, though typically it searches the template directories).*

## Catalog by Aspect Ratio

### 16:10 (Widescreen)
Ideal for standard modern laptop and desktop displays.
- `gis_digital_twin_dashboard_2026.svg`
- `gis_glassmorphic_overlay_2026.svg`
- `gis_multi_layer_compare_2026.svg`
- `gis_regional_command_minimap_2026.svg`
- `gis_split_screen_analysis_2026.svg`
- `large_node_with_text_and_button_16_10.svg`
- `neural_network_constellation_2026.svg`
- `premium_timeline_2026.svg`
- `small_node_left_grid_text_right_16_10.svg`
- `split_comparison_glass_2026.svg`

### 1:1 (Square)
Perfect for mobile views, social media, or grid-based dashboard blocks.
- `concentric_radar_2026.svg`
- `large_node_to_3_nodes.svg`
- `large_node_to_3_nodes_v2.svg`
- `large_node_to_4_nodes.svg`
- `large_node_to_5_nodes.svg`
- `large_node_to_6_nodes.svg`
- `large_node_to_7_nodes.svg`
- `large_node_to_8_nodes.svg`
- `large_node_with_text_and_button_1_1.svg`
- `modern_radial_node_2026.svg`
- `orbital_ecosystem_rings_2026.svg`
- `small_node_left_grid_text_right_1_1.svg`
- `swiss_typographic_grid_2026.svg`
- `timeline_3_nodes_template.svg`

### 3:2 (Classic Display)
A balanced aspect ratio often used for standard web content and presentations.
- `bento_grid_dashboard_2026.svg`
- `bento_grid_template.svg`
- `brutalist_process_flow_2026.svg`
- `circular_flow_template.svg`
- `circular_process_flow_2026.svg`
- `cool_blue_dashboard_2026.svg`
- `dark_cyber_ui_template.svg`
- `dashboard_template.svg`
- `fluid_motion_data_map_2026.svg`
- `glassmorphic_cards_template.svg`
- `glassmorphic_radial_dashboard_2026.svg`
- `hexagonal_grid_template.svg`
- `honeycomb_cluster_2026.svg`
- `isometric_layered_stack_2026.svg`
- `large_node_with_text_and_button_3_2.svg`
- `minimalist_journey_flow_2026.svg`
- `minimalist_process_template.svg`
- `minimalist_timeline_2026.svg`
- `modular_journey_map_2026.svg`
- `neumorphic_soft_ui_template.svg`
- `premium_data_viz_layout_2026.svg`
- `premium_layer_stack_2026.svg`
- `premium_minimalist_data_viz_2026.svg`
- `pyramid_hierarchy_template.svg`
- `radial_sunburst_dashboard_template.svg`
- `sleek_bento_stats_2026.svg`
- `small_node_left_grid_text_right_3_2.svg`
- `soft_ui_timeline_2026.svg`
- `sustainable_eco_layout_2026.svg`

### 4:3 (Traditional Monitor / Tablet)
- `glassmorphic_pipeline_funnel_2026.svg`
- `large_node_to_3_nodes_4_3.svg`
- `large_node_to_4_nodes_4_3.svg`
- `large_node_to_5_nodes_4_3.svg`
- `large_node_to_6_nodes_4_3.svg`
- `large_node_to_7_nodes_4_3.svg`
- `large_node_to_8_nodes_4_3.svg`
- `large_node_with_text_and_button_4_3.svg`
- `sleek_bento_grid_2026.svg`
- `sleek_pyramid_hierarchy_2026.svg`
- `small_node_left_grid_text_right_4_3.svg`

### 4:7 (Mobile Vertical)
- `mobile_app_dashboard_2026.svg`

### Dashboards
Templates specifically designed to act as structural layouts for `SivoDashboard` blocks.
- `four_quadrants_template.svg`
- `sidebar_layout_template.svg`

(Note: The dashboards folder also contains HTML templates like `analytics_dashboard.html`, `bento_box.html`, etc. These are typically used internally by the `SivoDashboard` CSS Grid Builder).

### Other / Specialty
- `tall_vertical_scrollytelling_template.svg`
- `timeline_5_nodes_template.svg` to `timeline_10_nodes_template.svg`
- `timeline_template.svg`

## Customization

Once loaded via `Sivo.from_template()`, you can customize the SVG using standard SIVO methods like `sivo_app.map()`, `sivo_app.add_scalable_text()`, and `sivo_app.fill_template_zone()`.
