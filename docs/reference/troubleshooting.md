---
Last Updated: 2026-04-09
SIVO Version: 1.0.0
---

# H-08: Troubleshooting Reference Plan

Common errors (e.g., Pydantic validation failures, SVG path clipping).

## Table of Contents

1. **Python Pydantic Validation Failures**
   - "Extra fields not permitted": Why `model_config = ConfigDict(extra="forbid")` causes errors and how to fix them.
2. **SVG Display Issues**
   - **Text Not Showing:** ECharts stripping `<text>` IDs. Why SIVO uses `name` attributes instead.
   - **Text Overflow:** ZRender ignoring `textLength`. How to use `auto_shrink_font`.
3. **Interactive Elements Not Responding**
   - Background clicking bugs.
   - Missing IDs in the original SVG file.
4. **Security/Browser Blocks**
   - CORS issues with `file:///` protocols when using iframes (e.g., `annotator.html`).
   - Autoplay audio blocked errors.
5. **Debugging the JS Runtime**
   - Inspecting the generated `window.SivoData` object.
   - JS Snippet for debug:
     ```javascript
     console.log("Current View Config:", window.SivoData.views[currentViewId]);
     ```
