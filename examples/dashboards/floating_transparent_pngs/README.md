# Floating Transparent PNGs Dashboard

This example demonstrates how to create a highly stylized dashboard featuring transparent PNGs that appear to "float" or "bob" seamlessly within the interface without the visual constraints of typical dashboard cards.

### Features Demonstrated:
1. **Transparent Dashboard Theme:** Setting `theme="transparent"` during `SivoDashboard` initialization strips away the default card backgrounds, borders, and glassmorphism, creating a borderless layout suitable for floating graphics.
2. **Native SVG Image Rendering:** Using SIVO's `render_mode="svg"` alongside standard SVG `<image>` tags.
3. **CSS Animations:** Applying the built-in `sivo-floating-element` CSS class to the `<image>` tags. Because `render_mode="svg"` preserves native DOM structure and classes, the floating/bobbing CSS animation executes smoothly.
4. **Interactive Transparent Images:** Binding click interactions via `sivo.map()` to the images. Crucially, the SIVO engine automatically prevents ECharts from rendering an unwanted black square outline when these static invisible bounding boxes are hovered or clicked.
5. **Sliding Details Panel:** Setting `panel_position="right"` within the mapping to trigger a sliding side panel containing the tooltip details when an image is clicked.
6. **Click Callbacks:** Registering `callback_event` and `callback_payload` so that clicking the floating images emits events to the parent context.
