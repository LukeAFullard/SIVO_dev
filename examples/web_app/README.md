# Serverless SIVO (WebAssembly Browser App)

This example demonstrates how to build a 100% serverless, zero-backend web application using SIVO, Pyodide, and IndexedDB.

The app features a split-pane layout:
1. **The Annotator**: An `iframe` embedding `src/sivo/cli/tools/annotator.html`. Because the HTML tool automatically detects `window.parent.pyodide`, it seamlessly links to the app's Virtual File System and saves SVG templates directly to the browser's IndexedDB.
2. **Python IDE**: A basic code editor where users write standard SIVO Python code.
3. **Interactive Output**: An `iframe` rendering the resulting `app.to_html()` string securely.

## How to Run This Example

Because this app relies on Python modules and Pyodide, it must be served over an HTTP server to avoid CORS/file protocol restrictions, and the SIVO Python package must be built into a `.whl` (Wheel) file so Pyodide can install it in the browser memory.

### 1. Build the SIVO Wheel

From the root of the repository, generate a Python wheel:

```bash
python -m pip install build
python -m build
```

This will create a `.whl` file in the `dist/` directory (e.g., `sivo-0.1.0-py3-none-any.whl`).

### 2. Copy the Wheel to the Web App Directory

Copy the generated wheel into this example folder so the browser can fetch it:

```bash
cp dist/sivo-*.whl examples/web_app/sivo.whl
```

### 3. Update the `index.html` Initialization Script

In `examples/web_app/index.html`, uncomment and update the `micropip.install` line to install the local wheel:

```javascript
// Change this block in index.html:
await micropip.install(['lxml', 'pydantic', 'Jinja2']);
await micropip.install('./sivo.whl'); // <- Add this line
```

### 4. Serve the App Locally

Start a simple Python HTTP server from the root of the repository (so the `iframe` src path resolves correctly):

```bash
cd ../../
python -m http.server 8000
```

### 5. Visit the App

Open your browser and navigate to: [http://localhost:8000/examples/web_app/index.html](http://localhost:8000/examples/web_app/index.html)

You can now drag an image into the left pane, trace a shape, click **Save to Pyodide FS**, and then click **Run SIVO** in the middle pane to instantly render a fully interactive vector map on the right pane!
