# Large Square with Two Vertically Stacked Squares

This example demonstrates how to create a responsive multi-block dashboard with a custom grid layout where the left column is a single large square area and the right column contains two smaller, vertically stacked square components.

By explicitly defining the CSS `grid-template-areas` using `dashboard.set_grid_layout()`, you can easily arrange SIVO components, details panels, and metrics side-by-side.

## Key Concepts
*   `SivoDashboard()`: Initialize the dashboard structure.
*   `dashboard.set_grid_layout()`: Define the grid structure using CSS `grid-template-areas`.
    - The desktop layout is defined as `"large right1" "large right2"`, meaning the `large` component spans two rows on the left, while `right1` and `right2` take up the top and bottom rows on the right respectively.
    - The mobile layout stacks them vertically: `"large" "right1" "right2"`.
*   `dashboard.add_sivo_block()`, `dashboard.add_details_panel()`, `dashboard.add_metrics_panel()`: Add components to the designated `grid_area`.
