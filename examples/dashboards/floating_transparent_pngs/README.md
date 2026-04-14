# Floating Transparent PNGs Dashboard

This example demonstrates how to create a highly stylized, professional dashboard where the UI elements appear to "float" seamlessly over a background image, entirely without borders or visible card containers.

## Purpose

While `SivoDashboard` automatically applies a clean glassmorphism style (translucent background with a slight blur and border) to grid cards when a `background_image_url` is set, sometimes you want complete control over the aesthetics—such as rendering 3D transparent PNGs or custom SVG shapes that stand alone.

This example shows how to:
1. Load a dark, professional abstract background.
2. Set `theme="transparent"` during `SivoDashboard` initialization to automatically strip away all borders, backgrounds, and glassmorphism blurs from the grid layout.
3. Animate the elements using CSS keyframes to create a breathing, floating effect.
4. Apply CSS `drop-shadow` directly to the transparent PNGs so they cast realistic shadows onto the background, rather than applying `box-shadow` to the square container.

## Key Code Snippets

### Setting the Transparent Theme

```python
dashboard = SivoDashboard(
    title="Floating UI Dashboard",
    columns=3,
    background_image_url="...",
    theme="transparent"
)
```

### Applying Floating Animations to Images

```css
.floating-element {
    filter: drop-shadow(0px 20px 30px rgba(0, 0, 0, 0.5));
    animation: float 6s ease-in-out infinite;
    transition: transform 0.3s ease;
}

@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-20px); }
    100% { transform: translateY(0px); }
}
```

## Running the Example

Navigate to the root directory and execute:

```bash
python examples/dashboards/floating_transparent_pngs/main.py
```

This will generate an `output.html` file in this directory. Open it in your web browser to view the floating dashboard.