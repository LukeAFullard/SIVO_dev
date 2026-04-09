---
Last Updated: 2026-04-09
SIVO Version: 0.1.0
---

# Troubleshooting Guide

This guide covers common issues you might encounter while using SIVO and provides solutions to help you get back on track.

## 1. Python Pydantic Validation Failures

**Error:** `pydantic_core._pydantic_core.ValidationError: 1 validation error for ... Extra inputs are not permitted`

**Why it happens:**
SIVO enforces strict data validation on its core Pydantic models (like configuration and actions models) by utilizing `model_config = ConfigDict(extra="forbid")`. This ensures that typos or unsupported parameters in your Python code are caught early, rather than failing silently on the frontend.

**How to fix:**
Check the API documentation for the exact class or method you are calling. Ensure you are only passing valid keyword arguments. For example, if you mistakenly pass `fill_color` instead of `fill`, Pydantic will reject it.

## 2. SVG Display Issues

### Text Not Showing
**Issue:** Text labels present in your original SVG do not appear when rendered in SIVO.
**Why it happens:** ECharts handles text rendering differently and often strips raw `<text>` IDs or ignores them depending on the series configuration.
**How to fix:** SIVO uses the `name` attribute of the SVG element to bind data. Ensure your text elements have proper IDs/names, and configure label visibility in your map options (e.g., set `label: { show: true }` if you want element IDs displayed, though it defaults to `false` to avoid messy text).

### Text Overflow
**Issue:** Long text labels overflow their designated bounding boxes in the SVG.
**Why it happens:** The underlying ZRender engine does not strictly enforce the `textLength` SVG attribute natively.
**How to fix:** Use the SIVO auto-shrink functionality. Make sure the font configuration uses features designed to wrap or scale text appropriately to fit within its container.

## 3. Interactive Elements Not Responding

### Background Clicking Bugs
**Issue:** Clicking an element doesn't trigger its action, or clicking the background triggers the wrong event.
**How to fix:** Ensure that the interactive element is correctly layered in the SVG. Transparent shapes covering the desired target can intercept mouse events. Use tools like `sivo annotate` to verify that the bounding box of your target element is correct.

### Missing IDs in the Original SVG File
**Issue:** You've mapped an action to an element, but nothing happens.
**How to fix:** SIVO connects Python configuration to SVG paths via element `id` attributes. If your SVG path lacks an `id`, SIVO cannot target it. Open your SVG in a text editor or use the `sivo annotate` tool to add or verify IDs.

## 4. Security/Browser Blocks

### CORS Issues with `file:///` Protocols
**Issue:** When opening your exported HTML file locally, iframes (like the `annotator.html` UI) fail to load or throw cross-origin errors in the console.
**Why it happens:** Browser security policies (CORS) block local resource loading via the `file:///` protocol for iframe `src` attributes.
**How to fix:** To run the SIVO serverless web app completely locally without an HTTP server, SIVO embeds the `annotator.html` content directly inside an HTML5 `<template>` tag and dynamically injects it into the iframe's `srcdoc` property using JavaScript. Ensure you are using the correct embedding method instead of directly linking local files. Avoid using `<script type="text/template">` if the embedded HTML contains its own `<script>` tags. It is generally recommended to serve your files via a local HTTP server (e.g., `python -m http.server`).

### Autoplay Audio Blocked Errors
**Issue:** Audio actions fail to play upon loading or interaction.
**Why it happens:** Modern browsers enforce strict autoplay policies, blocking audio playback until the user interacts with the document.
**How to fix:** Ensure audio playback is tied to a user action (like a click event). In SIVO's frontend templates, asynchronous media playback (like `audio.play()`) is wrapped with a `.catch()` block to gracefully handle these promise rejections. If audio fails to play automatically, prompt the user to interact with the map first.

## 5. Debugging the JS Runtime

If an issue persists on the frontend, you can inspect the browser console. SIVO attaches its configuration state to the `window.SivoData` object.

You can inspect this object using the developer console (F12):
```javascript
// View the entire data payload injected by SIVO
console.log(window.SivoData);

// Inspect the configuration for the currently active view
console.log("Current View Config:", window.SivoData.views[currentViewId]);
```
