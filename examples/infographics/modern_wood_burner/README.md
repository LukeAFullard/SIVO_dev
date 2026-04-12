# Modern Wood-Burner Interactive Infographic

This example demonstrates how to create a highly visual, interactive infographic entirely from a raw SVG string created via Python, and make its parts fully interactive with SIVO. It does not require an external visualization file to get started since the base graphics (a wood burner and some logs) are generated in the script itself.

## Purpose

The main purpose of this example is to show:
1.  **Native SVG Animation inside SIVO**: Demonstrating the use of native `<animate>` tags inside the generated SVG that persist when parsed. In this case, simulating light smoke coming from a chimney using animated blurry circles.
2.  **Using Invisible Hitboxes**: Adding transparent `<rect>` elements (`fill="transparent"`) on top of complex or multiple overlapping elements (like the glass stove door or the individual wooden logs). This allows binding an interactive `Sivo.map()` action to a single simplified geometry rather than managing event listeners on every tiny path or circle.
3.  **Interactive Overlays**: Binding rich HTML information to native SVG elements so that when a user interacts with the image (e.g. clicking the stove or logs), informative tooltips popup as overlays.

## Key Code Sections

### 1. Embedded SVG Definition with Native Hitboxes
The native SVGs include custom hitboxes assigned with string ID's (`id="stove_glass"` and `id="dry_woodpile_hitbox"`). These are explicitly mapped to the SIVO app later.

```python
        # Invisible Hitbox for Glass
        <rect id="stove_glass" x="270" y="170" width="260" height="180" rx="5" ry="5" fill="transparent" stroke="transparent" />

        # Invisible hit box for interactivity
        <rect id="dry_woodpile_hitbox" x="610" y="340" width="130" height="110" fill="transparent" cursor="pointer" />
```

### 2. Overlays Configuration
When initializing `Sivo`, it ensures that tooltips properly display as an overlay since default behavior might hide maps (`default_panel_position="none"`).

```python
    app = Sivo.from_svg(
        svg_path,
        disable_zoom_controls=True,
        title="Modern Wood-Burner",
        subtitle="Clean burning example",
        default_panel_position="overlay" # Crucial to show floating overlays
    )
```

### 3. Binding Interactivity to Hitboxes
The invisible hitboxes are targeted with `sivo_app.map()`, binding descriptive HTML payloads and setting custom highlight properties when hovered over (`hover_color`).

```python
    app.map(
        "dry_woodpile_hitbox",
        html="""...""",
        hover_color="rgba(46, 204, 113, 0.3)", # Light green highlight on hover
        color="transparent", # Keep the hitbox invisible by default
        panel_position="overlay"
    )
```

## Running the Example

Run the main file to generate the updated SVG and HTML files:

```bash
PYTHONPATH=src python3 examples/infographics/modern_wood_burner/main.py
```

Then open `index.html` in your web browser to interact with the modern wood burner and wood logs.
