# Analytics Dashboard Template

This example demonstrates how to use the `analytics_dashboard` HTML template to create a modern, app-like SaaS layout in `SivoDashboard`.

## Key Concepts

- **Fixed Sidebar Navigation**: Features a static left navigation panel, giving the dashboard an application feel.
- **Top Stats Row (`slot="stats"`)**: A distinct grid area at the top of the main content view specifically designed for KPI cards and live metrics.
- **Main Grid (`slot="main"`)**: The primary content area for charts and details panels, utilizing a 3-column CSS Grid layout (`columns=3` and `col_span` mapping).

## Running the Example

Run the script directly:
```bash
python main.py
```
This will generate an `output.html` file in the same directory.
