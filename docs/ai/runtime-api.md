---
Last Updated: 2026-04-09
SIVO Version: 1.0.0
---

# A-04: Runtime JS API Specification

This document details the internal architecture and APIs of SIVO's frontend JavaScript runtime engines, specifically \`echarts.html\` and \`dashboard_blocks.html\`. AI agents should refer to this spec when reasoning about data bindings, event listeners, and JS logic within SIVO's browser execution context.

## 1. The \`viewsData\` Payload

SIVO bridges Python configuration state into the JavaScript environment via Jinja2 template injection. The Python backend serializes mapping dictionaries and action configurations into a JSON object.

### Injection Mechanism

In both \`echarts.html\` and \`dashboard_blocks.html\`, the data is injected securely (with Python-side replacement of \`<\`, \`>\`, and \`&\` to prevent inline script breakouts):

\`\`\`javascript
// In src/sivo/runtime/templates/echarts.html
var viewsData = {{ views_data | safe }};
\`\`\`

The \`viewsData\` object contains all views, maps, SVGs, and formatted data arrays required by ECharts to render the graphic and attach event listeners dynamically.

## 2. ECharts Initialization Lifecycle

SIVO relies on Apache ECharts (and ZRender) to handle the low-level rendering and interaction of SVGs.

### Registration and Setup

1. **SVG Registration**: The raw SVG content (stored in \`viewsData[currentView].svg\`) is registered with ECharts using \`echarts.registerMap(mapName, { svg: svgString })\`.
2. **Chart Instantiation**: A new instance is created on the \`#chart-container\` element using \`echarts.init(domNode, null, { renderer: 'svg' })\`.
3. **Series Configuration**: SIVO dynamically generates the \`series\` option array based on the data payload, utilizing the \`map\` series type.
4. **Image Fills**: If an element uses an \`image_url\`, SIVO creates an \`HTMLImageElement\`, loads the source, and configures an \`image\` pattern fill via the ECharts \`itemStyle\` object.

## 3. Event Listener Hooks

SIVO implements interactivity by attaching listeners to the ECharts instance.

\`\`\`javascript
myChart.on('click', function(params) {
    var componentName = params.name; // This correlates to the SVG node's 'name' attribute
    // ... logic to lookup actions from viewsData for this componentName
});
\`\`\`

### Testing Implications (Playwright)

When writing automated End-to-End tests using Playwright, triggering a standard DOM click event on an SVG element might fail because ZRender intercepts raw DOM events.

**Agent Directive:** To simulate clicks effectively in tests, execute a script within the page context to trigger the ECharts internal event API:

\`\`\`javascript
// Example Playwright test strategy
await page.evaluate((elemName) => {
    window.myChart.dispatchAction({
        type: 'downplay'
    });
    // Or trigger a custom wrapper if exposed
}, "my_element_id");
\`\`\`

## 4. Security Enforcement

In the runtime, all dynamic UI modifications that inject strings into the DOM must be sanitized.

\`\`\`javascript
// Fail-safe sanitization pattern used in SIVO runtime
let cleanHTML = window.DOMPurify ? window.DOMPurify.sanitize(dirtyHTML) : dirtyHTML.replace(/</g, "&lt;");
targetElement.innerHTML = cleanHTML;
\`\`\`

**Agent Directive:** If you are modifying \`echarts.html\` to add a new feature that updates DOM content (like a tooltip or a panel), you *must* use \`window.DOMPurify.sanitize()\`.

## 5. Architectural Divergence: Single-View vs. Dashboards

SIVO maintains two distinct runtime templates located in \`src/sivo/runtime/templates/\`:

### \`echarts.html\`
* **Purpose**: Single interactive graphic canvas with built-in drilldown mechanics via a "View History" stack.
* **Layout**: Full viewport canvas, with optional overlapping UI panels (sidebars, modals).
* **Navigation**: Features a \`viewHistory\` array for pushing and popping views (drilldowns) and restoring ECharts zoom/pan states.

### \`dashboard_blocks.html\`
* **Purpose**: Multi-block dashboards where multiple SIVO views render simultaneously.
* **Layout**: Utilizes CSS Grid Builder to arrange independent chart containers on the screen.
* **Architecture**: Iterates through an array of configured blocks, initializing separate ECharts instances (\`myChart_block1\`, \`myChart_block2\`) for each container. Cross-communication between blocks is handled via window-level event dispatching rather than a single shared \`myChart\` instance.
