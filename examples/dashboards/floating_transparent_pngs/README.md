# Floating Transparent PNGs Dashboard

This example demonstrates how to create a highly stylized dashboard featuring transparent PNGs that appear to "float" or "bob" seamlessly within the interface without the visual constraints of typical dashboard cards.

### Features Demonstrated:
1. **Responsive CSS Grids:** Using `set_grid_layout` to define structural templates that rearrange the layout of images depending on viewport width (e.g., 4 columns on desktop, 2x2 grid on mobile).
2. **Dashboard Background Image:** Applying a high-resolution backdrop behind the floating images by passing `background_image_url` directly to the dashboard config.
3. **Transparent Dashboard Theme:** Setting `theme="transparent"` during `SivoDashboard` initialization strips away the default card backgrounds, borders, and glassmorphism, creating a borderless layout suitable for floating graphics.
4. **Native SVG Image Rendering:** Using SIVO's `render_mode="svg"` alongside standard SVG `<image>` tags.
5. **CSS Animations:** Applying the built-in `sivo-floating-element` CSS class to the `<image>` tags. Because `render_mode="svg"` preserves native DOM structure and classes, the floating/bobbing CSS animation executes smoothly.
6. **Interactive Transparent Images:** Binding click interactions via `sivo.map()` to the images. Crucially, the SIVO engine automatically prevents ECharts from rendering an unwanted black square outline when these static invisible bounding boxes are hovered or clicked.
7. **Sliding Details Panel:** Setting `panel_position="right"` within the mapping to trigger a sliding side panel containing the tooltip details when an image is clicked.
8. **Click Callbacks:** Registering `callback_event` and `callback_payload` so that clicking the floating images emits events to the parent context.
