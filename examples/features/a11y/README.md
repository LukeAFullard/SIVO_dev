# Accessibility (A11y) Engine

This example demonstrates how SIVO natively generates accessibility (A11y) DOM elements and handles keyboard navigation, allowing interactive maps and graphics to be accessible to screen readers and keyboard users.

SIVO automatically creates visually hidden, focusable `<div>` tags positioned exactly over the corresponding SVG regions. This allows standard screen readers (VoiceOver, NVDA) to read out the region's `aria-label` and allows the browser to draw a native focus ring around the region when tabbing.

## Features Demonstrated

1. **Aria Labels & Roles**: Using the `aria_label`, `role`, and `tabindex` parameters in `app.map()` to dynamically inject metadata.
2. **Keyboard Navigation**: Using the `presentation_order` parameter during initialization to dictate the logical `ArrowRight` / `ArrowLeft` keyboard flow.
3. **Focus Ring Alignment**: SIVO automatically tracks the bounding box of elements so that tabbing through regions highlights them exactly as they appear on the screen.

## Code Snippet

To enable accessibility features, set `enable_a11y=True` during initialization and map accessible metadata to your regions:

```python
from sivo import Sivo

# Initialize with presentation order and A11y enabled
app = Sivo.from_string(
    svg_string,
    presentation_order=["regionA", "regionB"],
    enable_a11y=True
)

# Map the region with specific screen reader instructions
app.map(
    "regionA",
    tooltip="Region A",
    html="<h2>Region A</h2><p>Data.</p>",
    aria_label="First Region, press Enter to open details",
    role="button",
    tabindex="0"
)
```

## Running the Example

Run the script to generate the interactive HTML file:

```bash
python a11y_map.py
```

Open `a11y_example.html` in a web browser.

### How to test:
1. **Tab Navigation**: Click anywhere on the white background to focus the window, then press `Tab` on your keyboard. You will see a blue focus ring appear around "Region A".
2. **Triggering**: Press `Enter` or `Space` to simulate a click and open the side panel for Region A.
3. **Presentation Navigation**: Press the `ArrowRight` key to naturally sequence through the map (from Region A to Region B), simulating a presentation flow without needing to use `Tab`.
4. **Screen Readers**: Turn on VoiceOver (Mac) or NVDA (Windows). When focusing a region, it will announce: "First Region, press Enter to open details".
