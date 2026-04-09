---
Last Updated: 2026-04-09
SIVO Version: 0.1.0
---

# Serverless Web Apps with SIVO and Pyodide

This guide explains how to use SIVO in a completely serverless environment within the browser using **Pyodide** (Python compiled to WebAssembly). This allows you to build interactive data dashboards, annotation tools, and visualizations that run 100% locally on the client-side, with zero backend required.

## 1. Introduction

Running Python in the browser unlocks powerful capabilities. Instead of relying on a Flask or Django backend, your SIVO Python code runs directly in the user's browser via WebAssembly (WASM). This means:
*   **Zero Infrastructure:** You don't need to deploy a server to host your Python logic.
*   **Offline Support:** Once loaded, SIVO applications can function entirely offline.
*   **Security:** Code executes in a safe, sandboxed browser environment.

## 2. Architecture

When running SIVO in the browser, the architecture relies on several core browser technologies:

*   **Pyodide:** The CPython interpreter compiled to WASM. It allows SIVO (and its dependencies like `lxml` and `pydantic`) to run inside the JavaScript V8 engine.
*   **Emscripten IDBFS:** The browser's file system is strictly isolated. Pyodide uses the Emscripten IndexedDB File System (IDBFS) to persist data (like SVG files, SIVO project configurations, or exported HTML bundles) locally across page reloads.
*   **Iframes:** SIVO's interactive rendering (the `echarts.html` or `dashboard_blocks.html` bundles) and tools (like the Annotator) are often embedded within iframes to isolate their DOM and CSS styles from the main application page.

## 3. Setting up Pyodide

To run SIVO in the browser, you first need to initialize Pyodide and set up a virtual file system.

### Loading Pyodide

Include the Pyodide JavaScript library in your HTML page:

```html
<script src="https://cdn.jsdelivr.net/pyodide/v0.25.0/full/pyodide.js"></script>
```

### Initializing the Virtual File System (IDBFS)

SIVO requires access to files (e.g., to read an SVG template using `Sivo.from_svg()`). You must mount a persistent IDBFS directory.

**Important Rule:** Always create a custom mount point, such as `/sivo_workspace`, rather than using the default `/home/pyodide` directory. Additionally, you must wrap `FS.mkdir()` calls in a `try...catch` block to gracefully ignore `EEXIST` (File exists) errors, which naturally occur on subsequent page reloads after the directory has been persisted.

```javascript
async function initPyodide() {
    let pyodide = await loadPyodide();

    // 1. Mount IDBFS
    const mountDir = "/sivo_workspace";
    try {
        pyodide.FS.mkdir(mountDir);
    } catch (e) {
        if (e.code === 'EEXIST') {
            console.log("Directory already exists. Continuing.");
        } else {
            console.error("Error creating directory:", e);
        }
    }

    pyodide.FS.mount(pyodide.FS.filesystems.IDBFS, {}, mountDir);

    // 2. Sync the file system before using it
    await new Promise((resolve, reject) => {
        pyodide.FS.syncfs(true, function (err) {
            if (err) reject(err);
            else resolve();
        });
    });

    console.log("Pyodide and IDBFS initialized.");
    return pyodide;
}
```

## 4. Deploying Local Web Apps without a Server

SIVO includes tools like the Annotator UI, which is essentially a standalone web application. When building entirely local, serverless solutions, you often run into browser security policies (CORS).

### Handling Browser Security Policies (CORS)

If you attempt to load a local HTML file (e.g., `annotator.html`) into an iframe using the `file:///` protocol via the `src` attribute, the browser will block it due to strict CORS (Cross-Origin Resource Sharing) policies.

```html
<!-- This will FAIL when running locally over file:/// -->
<iframe src="annotator.html"></iframe>
```

### The Solution: Using `<template>` and `srcdoc`

To run SIVO serverless web apps completely locally *without* an HTTP server, you must embed the HTML content directly inside your main HTML file using a `<template>` tag and dynamically inject it into the iframe's `srcdoc` property using JavaScript.

**Critical Note:** Do *not* use `<script type="text/template">` if the embedded HTML contains its own `<script>` tags, as the browser parser will prematurely terminate the script block. Always use the HTML5 `<template>` tag.

**Example Implementation:**

```html
<!DOCTYPE html>
<html>
<head>
    <title>SIVO Local Serverless App</title>
</head>
<body>

    <!-- 1. The Iframe container -->
    <iframe id="sivo-app-frame" style="width: 100%; height: 800px; border: none;"></iframe>

    <!-- 2. The embedded HTML content inside a template tag -->
    <template id="annotator-template">
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body { font-family: sans-serif; background: #f0f0f0; }
            </style>
        </head>
        <body>
            <h1>SIVO Annotator Embedded</h1>
            <p>Running locally without a server!</p>
            <script>
                console.log("Embedded script executing within iframe srcdoc!");
            </script>
        </body>
        </html>
    </template>

    <!-- 3. The injection logic -->
    <script>
        document.addEventListener("DOMContentLoaded", () => {
            const iframe = document.getElementById("sivo-app-frame");
            const template = document.getElementById("annotator-template");

            // Get the raw HTML content from the template
            const htmlContent = template.innerHTML;

            // Inject directly into the iframe, bypassing file:/// CORS restrictions
            iframe.srcdoc = htmlContent;
        });
    </script>

</body>
</html>
```

By combining Pyodide's IDBFS persistence with `srcdoc` iframe injection, you can distribute fully-functional, interactive SIVO applications as a single HTML file that users can double-click and run safely on their local machines.
