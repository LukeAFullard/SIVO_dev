# Drawing and Flow

This example demonstrates how to use SIVO's drawing tools and dynamic flow connections to visualize and interact with a network architecture diagram.

## Overview

The example uses a simple SVG string representing three server nodes (Database, API, and Client) and connects them to showcase how SIVO handles:
1.  **Drawing Tools**: By passing `enable_drawing_tools=True` when initializing SIVO, a drawing toolbar is provided on the canvas to allow users to add freehand drawings, text, and basic shapes on top of the interactive visualization.
2.  **Dynamic Flow Arrows**: The `sivo_app.add_connection()` method is used to draw animated data flow lines between the nodes in the SVG diagram.

## Key Code Highlights

### 1. Enabling Drawing Tools

When initializing SIVO from the SVG string, the drawing tools are enabled, and the side panel is disabled to maximize focus on the canvas itself.

```python
sivo_app = Sivo.from_string(
    svg_string,
    title="Network Architecture & Annotations",
    subtitle="Test the new Dynamic Flow Arrows and Drawing Tools.",
    enable_drawing_tools=True,  # Enables the top-right drawing toolbar
    theme="light",
    disable_panel=True          # Focus entirely on the canvas features
)
```

### 2. Adding Dynamic Connections

Connections are established between nodes by referencing their specific IDs. The lines are styled and animated using the built-in properties:

```python
# Data flow from Database to API
sivo_app.add_connection(
    source_id="node_database",
    target_id="node_api",
    label="Data Fetch",
    color="#3b82f6",
    width=3,
    animation_speed=4,
    type="dashed",
    flow_effect=True,
    effect_symbol="arrow",
    effect_size=12
)

# Data flow from API to Client
sivo_app.add_connection(
    source_id="node_api",
    target_id="node_client",
    label="Response",
    color="#10b981",
    width=3,
    animation_speed=3,
    type="solid",
    flow_effect=True,
    effect_symbol="circle", # Different effect style
    effect_size=8
)
```

### 3. Interactive Nodes

Hover effects and tooltips are bound to each node, demonstrating how standard interactivity functions seamlessly alongside drawing tools and connection overlays.

```python
sivo_app.map("node_database", tooltip="Primary SQL Database Cluster", hover_color="#2563eb", glow=True)
sivo_app.map("node_api", tooltip="GraphQL API Gateway", hover_color="#059669", glow=True)
sivo_app.map("node_client", tooltip="Web / Mobile Client Apps", hover_color="#7c3aed", glow=True)
```

## Running the Example

Run the script from the root directory:

```bash
PYTHONPATH=src python3 examples/advanced/drawing_and_flow/main.py
```

This will output an `output.html` file within the same directory. Open it in any modern browser to view the interactive diagram and test out the drawing tools!
