---
Last Updated: 2026-04-09
SIVO Version: 0.1.0
---

# Accessibility (A11y) in SIVO

Creating accessible interactive graphics is a core principle in SIVO. Visualizations should be usable by everyone, including individuals who rely on screen readers or keyboard navigation. SIVO provides several built-in tools to help you meet Web Content Accessibility Guidelines (WCAG).

## The Accessibility Container (`a11y-container`)

When a SIVO map is rendered and `enable_a11y=True` is set during instantiation (which is the default), SIVO dynamically generates a hidden DOM element called the `a11y-container`.

This container:
- Is visually hidden from the screen using the `.sr-only` class.
- Replicates the interactive elements of your SVG as native HTML elements (like buttons or regions).
- Announces state changes and data to screen readers.

### Enabling Accessibility

Accessibility is enabled by default. However, you can explicitly control it when creating your `Sivo` instance:

```python
from sivo.core.sivo import Sivo

sivo = Sivo.from_svg(
    "map.svg",
    enable_a11y=True  # Default is True
)
```

## Configuring Elements for Accessibility

When mapping elements in your SVG using `sivo.map()`, you can provide explicit ARIA (Accessible Rich Internet Applications) attributes to define how screen readers interpret the elements.

The key parameters are:
- `aria_label`: A descriptive string that screen readers will announce when the element is focused.
- `role`: The ARIA role of the element (e.g., `button`, `img`, `region`). SIVO defaults this to `button` if not provided.
- `tabindex`: Controls whether the element is focusable and its order. A value of `0` makes it focusable in the logical order of the page.

### Example: Making a Map Region Accessible

```python
sivo.map(
    element_id="california",
    color="#FF5733",
    hover_color="#C70039",
    aria_label="State of California. Population 39 million.",
    role="button",
    tabindex="0"
)
```

In the generated frontend, SIVO creates a hidden focusable element corresponding to this SVG region. When a user tabs to it, the screen reader will announce "State of California. Population 39 million, button".

## Keyboard Navigation and `presentation_order`

By default, the keyboard navigation order (the order in which elements receive focus when pressing the `Tab` key) follows the order in which elements are mapped or structured in the SVG.

To provide a logical reading order—which is critical for spatial data or storytelling—you can explicitly define the `presentation_order` during instantiation.

### Setting Presentation Order

Pass a list of SVG element IDs to `presentation_order` to dictate the exact sequence of focus:

```python
sivo = Sivo.from_svg(
    "usa_map.svg",
    presentation_order=["west_coast", "midwest", "east_coast", "south"]
)
```

When users navigate using the keyboard, focus will move strictly from `west_coast` to `midwest` to `east_coast` to `south`, regardless of their physical arrangement in the SVG file.

## High Contrast and Theming

SIVO supports high contrast modes via the `theme` parameter:

```python
sivo = Sivo.from_svg("dashboard.svg", theme="dark")
```

Ensure the colors you map have sufficient contrast ratios (at least 4.5:1 for normal text and 3:1 for large text/graphics) against your selected background to meet WCAG AA standards.

## Summary Checklist for A11y
1. Leave `enable_a11y=True` enabled.
2. Provide descriptive `aria_label` strings for every interactive element.
3. Use `presentation_order` to create logical keyboard paths.
4. Verify color contrast ratios.
