---
Last Updated: 2026-04-09
SIVO Version: 1.0.0
---

# A-04: Runtime JS API Specification Plan

Detailed technical spec of the JS runtime (echarts.html, dashboard_blocks.html).

## Table of Contents

1. **The `window.SivoData` Payload**
   - Structure of injected configuration data.
2. **ECharts Initialization**
   - Registering the SVG map.
   - Setting up the main `series` object.
   - Handling image fills (`HTMLImageElement` instantiation).
3. **Event Listener Hooks**
   - `myChart.on('click', ...)` implementations.
   - Triggering simulated clicks (Playwright testing strategy: `myChart.trigger('click', ...)`).
4. **JS Helper Functions Reference**
   - DOM manipulation functions (`applyPanelPosition`, `updateBackButton`).
   - Example JS Snippet:
     ```javascript
     function applyPanelPosition(position) {
         if (window.sivoDisablePanel || position === 'none') {
             closePanel(); return;
         }
         // ... positioning logic
     }
     ```
5. **Divergence: `echarts.html` vs `dashboard_blocks.html`**
   - Architectural differences between single-view and multi-block runtimes.
