---
Last Updated: 2026-04-09
SIVO Version: 0.1.0
---

# Styling and Layout in SIVO

Welcome to the comprehensive guide on styling, layout, and visual presentation in SIVO. This guide covers how SIVO leverages SVG properties, integrates with CSS, handles complex dashboard layouts, and dynamically generates UI elements directly from your Python code.

## 1. SVG Attributes and ECharts

At its core, SIVO relies on Apache ECharts and its underlying ZRender engine to render interactive SVGs. Understanding how ZRender parses SVG attributes is crucial for predictable styling.

### How ZRender Handles SVG

When you load an SVG into SIVO, ZRender maps standard SVG attributes (like `fill`, `stroke`, `stroke-width`, `opacity`) into ECharts visual configurations. However, there are some specific limitations and behaviors you should keep in mind:

- **Text Nodes and IDs**: For `<text>` nodes to be reliably targeted and manipulated by SIVO, they must have unique `id` attributes in your SVG. Unnamed text nodes might be ignored or difficult to bind to actions.
- **Ignored Attributes**: Certain complex SVG attributes, such as `textLength`, are generally ignored by ZRender. Standard font properties (`font-family`, `font-size`) are supported but may require specific configurations to scale dynamically.
- **Handling Multi-line Text**: To dynamically update multiline SVG text in SIVO, you should use ECharts' native `series[i].label` configuration. For example, using `formatter: properties.text` and `overflow: 'break'` via `setOption()` is the correct approach. Directly mutating ZRender/DOM `<text>` nodes or `<tspan>` elements is highly unstable and will be overwritten by ECharts' internal redraw cycles. The best practice is to hide the original SVG text placeholder node (by setting its `itemStyle.opacity` to 0) and overlay the ECharts label.
- **Default Labels**: To prevent element IDs from being displayed as messy text across the SVG map by default, SIVO explicitly sets the `label: { show: false }` configuration on the main "SIVO Series" map series in its templates.

## 2. Injecting CSS into SIVO

SIVO allows you to inject custom CSS to style HTML overlays, side panels, and tooltips, without requiring you to edit the base templates.

### Using `panel_css` and `global_css`

You can pass raw CSS strings when initializing your `Sivo` map or within specific UI elements. This allows you to precisely theme your interactive map.

- `panel_css`: Specifically styles the HTML sidebar panel that opens when a user interacts with elements configured with the `html` parameter.
- `global_css`: Applied globally to the rendered HTML document, affecting tooltips, layout wrappers, and any custom HTML injected via blocks.

### Security Considerations (CSS Sanitization)

Security is a primary concern in SIVO. When dynamically injecting CSS strings into SIVO templates (e.g., via `panel_css`), the system ensures that the input is sanitized to prevent CSS-based HTML breakout vulnerabilities. This involves escaping HTML brackets and closing tags (e.g., replacing `</style>`, `<`, and `>` with their safe equivalents like `\3C/style\3E`, `\3C`, and `\3E`). Ensure that your custom CSS relies on standard selectors and avoids embedding raw executable scripts or unescaped HTML content.

## 3. Layout Containers

SIVO supports two primary modes for rendering your projects, each with its own layout strategy.

### ECharts Single-View Runtime

The standard runtime (`src/sivo/runtime/templates/echarts.html`) is designed for full-screen, single-view interactive maps. In this mode, the SVG stretches to fit its container while maintaining its aspect ratio, ensuring that coordinates and interactions remain perfectly aligned regardless of the device screen size.

### Dashboard Blocks Runtime

For more complex applications, SIVO provides the Dashboard Blocks runtime (`src/sivo/runtime/templates/dashboard_blocks.html`). This runtime allows you to compose multi-block interactive dashboards using CSS Grid. You can place your interactive SVG map alongside external ZRender charts, HTML text blocks, or data tables, maintaining responsive behavior across different screen sizes. Ensure that any frontend JavaScript logic changes are synchronized between these two templates to prevent feature desynchronization.

## 4. Programmatic Card Generation

Instead of manually drawing every UI element in your SVG editor, SIVO provides tools to generate visual components programmatically based on your data.

### Using `Sivo.add_card()`

The `add_card()` method automatically generates a perfectly scaled, native SVG card relative to the bounding box of a target element. This is useful for building dynamic dashboards where the text and values change based on underlying Python data.

**Example Python Snippet:**

```python
sivo.add_card(
    element_id="background_rect",  # The ID of the target SVG element to anchor to
    title="Sales Data",
    value="$1M",
    subtitle="Q3 Results",
    shape="pill",
    bg_color="#ffffff",
    title_color="#64748b",
    value_color="#0f172a"
)
```

This will automatically create a group containing the card background and correctly positioned text elements for the title, value, and subtitle, anchored precisely to `background_rect`.

## 5. Interactive Image Fills

You can dynamically change the visual appearance of SVG elements beyond flat colors by using interactive image fills.

### Setting `fill_pattern` and `hover_image`

When defining a state or mapping for an element, you can apply images to the fill properties:

- `fill_pattern`: Replaces the default fill color with a repeating or scaled image pattern.
- `hover_image`: Displays an image within the boundaries of the SVG shape when the user hovers over it.

These properties are especially powerful for creating "x-ray" effects, revealing photographs within map boundaries, or dynamically changing textures based on data states.


### Tooltip Styling and z-index

To ensure tooltips are never clipped or hidden behind SVG shapes or sidebars, SIVO configures ECharts tooltips with `appendToBody: true` and applies `z-index: 99999 !important` via `extraCssText`. This renders the tooltips at the absolute highest level in the DOM structure, solving overflow issues within smaller embedding containers.
