# SIVO Web App Enhancement Plan

## 1. Executive Summary
This document outlines the comprehensive strategy to transform the current `examples/web_app` into a fully-featured, 100% serverless, zero-backend platform using WebAssembly (WASM), Pyodide, and IndexedDB (IDBFS). The goal is to provide dual workflows: one for developers via a Python IDE and one for non-coding experts via a visual, drag-and-drop builder, while exposing the complete capabilities of the SIVO framework (dashboards, scrollytelling, drill-downs, dynamic data binding).

## 2. Architecture & Storage Optimization (WASM & IDBFS)
To keep memory consumption low and allow processing of large files entirely in the browser:
*   **IDBFS Mounts:** The browser's IndexedDB will be mounted as a virtual file system (`/sivo_workspace`) via Pyodide.
*   **Zero-Memory Persistence:** Files (Images, SVGs, CSVs, XLSXs) uploaded by the user or fetched via URL will be directly written into IDBFS in chunks. Once written, Javascript memory buffers will be immediately cleared and garbage-collected.
*   **Lazy Loading via Python:** When the Python backend needs to parse a file (e.g., extracting data for a chart), it reads directly from the IDBFS mount (`/sivo_workspace/data.csv`) using standard Python I/O, preventing the entire file from bloating the browser's JS heap.

## 3. Input Handling (Local Files & URLs)
*   **Unified Upload Manager:** A new UI component allowing users to drag and drop local files or provide a URL.
*   **Fetch & Store Flow:** If a URL is provided, the JS layer fetches it as a `Blob` and streams it directly to IDBFS.
*   **Data Parsing Strategy:**
    *   **CSV/JSON:** Easily parsed via built-in Python libraries (`csv`, `json`).
    *   **XLSX:** We will leverage Pyodide's capability to install lightweight parsing wheels like `openpyxl` or we'll process it locally via client-side Javascript (e.g., `SheetJS`) which will convert it to CSV before saving to IDBFS. This saves Python memory space.

## 4. Dual-Interface System

### A. The Expert Workspace (Existing, Enhanced)
*   The current Python IDE will be retained for developers to script custom SIVO maps, attach specific data bindings, and use the full Python API.
*   **Enhancement:** Auto-complete snippets for standard SIVO methods and a dedicated file browser panel to inspect the contents of the `/sivo_workspace` IDBFS folder.

### B. The No-Code SIVO Builder (New)
A brand-new, visually driven React/Vanilla JS interface aimed at non-coders. It generates Python code or JSON configs under the hood and executes them via Pyodide.
*   **Asset Library:** View and select files (images, datasets) stored in IDBFS.
*   **Template Gallery:** A visual carousel exposing all built-in SIVO templates (16:10, 1:1, etc.).
*   **Visual Mapper:** Users click an SVG element in a preview iframe, opening a properties panel to attach tooltips, define colors, or map data columns.
*   **Data Binding Wizard:** Users select an IDBFS dataset (e.g., `sales.csv`) and visually map its columns to SVG element IDs to auto-generate a choropleth.

## 5. Implementing Complex SIVO Features in the No-Code UI

### Drill-Downs (Multi-Level Maps)
*   **UI Flow:** The user uploads multiple SVGs (e.g., `Campus Map`, `Building A`). In the Visual Mapper, clicking "Building A" in the main map opens a "Click Action" menu.
*   **Configuration:** The user selects "Drill-down to map" and picks `Building A` from the asset library. The UI generates `sivo_app.map("building_a", drill_to="building_a.svg")`.

### Scrollytelling & Guided Tours
*   **UI Flow:** A "Storyline Mode" tab at the bottom of the screen with a timeline/step UI.
*   **Configuration:** Users click "Add Step", select the target element, write a narrative text block, and set visual states (zoom, glow, highlight). The UI binds this to `ScrollytellingStepConfig` or `TourStepConfig` and injects it into the bundle.

### Interactive Dashboards & Graphs
*   **UI Flow:** A "Dashboard Layout" mode where users select CSS Grid block layouts (e.g., "Map + Sidebar + Graph").
*   **Graphing Integration:** When dropping a Graph Block, the wizard asks for a dataset. The user maps the X/Y axes from the uploaded CSV/XLSX. The builder uses SIVO's internal `map_bar_chart` / `map_line_chart` API to inject ECharts instances.


### Advanced Thematic Mapping & Infographics
*   **UI Flow:** A "Map Types" drawer allowing users to switch a base map into an advanced thematic map (Hexbin, Dot Density, Flow Map).
*   **Configuration:** For a Hexbin map, the wizard requests a dataset with coordinate columns. The builder uses `apply_hexbin()`. For infographics, users can drag and drop "KPI Card" components which dynamically map to the `Infographic` class's `add_card()` method.

### Dynamic UI Layers & Multimedia
*   **UI Flow:** An "Overlays & Media" toolbar.
*   **Configuration:** Users can visually drop Markers (via `add_marker`), Scalable Text (`add_scalable_text`), and Progress Bars (`add_scalable_progress_bar`) onto the map. In the Property Inspector, users can attach Video, Audio, or complex actions like `Explode` or `CycleState` to specific SVG elements.

### Live Data Binding & Timelines
*   **UI Flow:** A "Data Sources" manager with tabs for Static, Live API, WebSockets, and Timelines.
*   **Configuration:** Users can input a WebSocket URL for `bind_live` or an API endpoint for `bind_api` polling. For historical data, users can upload a time-series CSV and configure `bind_timeline` to automatically generate a Timeline UI playback control.

### External Integrations & Embeds
*   **UI Flow:** An "Integrations" catalog component within the Dashboard Layout mode or Property Inspector.
*   **Configuration:** Users select third-party services (e.g., Google Analytics, Shopify, Typeform, Tableau) and input API keys, endpoint URLs, or embed codes. The UI maps these to the `datasource` and `analytics` schemas or specific panel embeds.

### Accessibility (A11y) & Security
*   **UI Flow:** An "Accessibility & Security" settings menu for the project.
*   **Configuration:** Allows users to explicitly define ARIA roles, set `presentation_order` for sequential keyboard navigation, and configure strict CSP or DOMPurify options.

## 6. Modern UI/UX Design System & Productization
To elevate the web app from an "example" to a modern, production-grade product, the interface will undergo a complete design system overhaul.
*   **CSS Framework:** Migrate from raw CSS to a utility-first framework like Tailwind CSS, paired with highly accessible, pre-built component libraries (e.g., Shadcn UI or Radix UI) for clean modals, dropdowns, and context menus.
*   **Dark Mode & Theming:** Implement native system-level Dark Mode detection with seamless toggling. Code editors (Monaco/CodeMirror) and canvas backgrounds will automatically sync with the active theme.
*   **Drag-and-Drop UX:** Add fluid animations and clear visual drop zones (e.g., dashed borders, highlighting) when dragging files from the OS or moving blocks around in the Dashboard Layout mode.
*   **Onboarding & Empty States:** Implement guided interactive tooltips for first-time users (e.g., "Drag a CSV here to start"), and ensure robust empty states for panels rather than blank screens or console errors.
*   **State & Feedback:** Introduce non-blocking toast notifications for system events ("Saving to IDBFS...", "Error parsing CSV"), and skeletal loading screens during the initial WASM/Pyodide load phase.

## 7. Step-by-Step Implementation Roadmap

### Phase 1: Core Storage & File Management (Weeks 1-2)
1.  Extend the current `index.html` UI to include a robust File Manager Sidebar.
2.  Implement the drag-and-drop / URL fetcher in JS that streams directly to Pyodide IDBFS.
3.  Add memory cleanup routines to ensure large files are flushed from RAM after saving to IDBFS.
4.  Implement CSV/XLSX to IDBFS parsing utility.

### Phase 2: The No-Code UI Foundation (Weeks 3-4)
1.  Build the "App Builder" tab alongside "Annotator Studio" and "Python Workspace" using the new Tailwind/Shadcn design system.
2.  Implement the Visual Template Selector (reading from SIVO's built-in `src/sivo/templates`).
3.  Implement the Interactive Preview Pane (renders via `app.to_html()`).
4.  Build the Property Inspector panel (colors, text, hover states).

### Phase 3: Advanced No-Code Features (Weeks 5-6)
1.  **Data Binding Wizard:** Implement the UI to map CSV columns to SVG IDs for instant Choropleths.
2.  **Dashboard Mode:** Implement UI to add `SivoDashboard` blocks, metrics panels, and details panels.
3.  **Graph Generation:** Integrate logic that reads the parsed CSV and utilizes SIVO's native ECharts injection for custom graphs.


### Phase 4: Advanced Mapping, Live Data, & Integrations (Weeks 7-8)
1.  **Advanced Maps:** Integrate UI for Hexbins, Dot Density, and Flow Maps.
2.  **Live Binding:** Build the Data Sources manager for configuring WebSockets and API polling.
3.  **Integrations:** Add the Integration Catalog to allow embedding 3rd party services (Forms, E-commerce, BI).
4.  **A11y & Multimedia:** Expose Marker, Video, Audio, and Keyboard Navigation configurations in the Property Inspector.

### Phase 5: Scrollytelling & UX Polish (Weeks 9-10)

1.  **Timeline UI:** Add the timeline components for Scrollytelling and Tours.
2.  **Export/Share:** Implement a feature to export the finished multi-view/dashboard SIVO app as a single standalone HTML file directly downloaded from the browser.
3.  Extensive memory profiling to guarantee the browser does not crash on high-resolution SVGs or large datasets.

### Phase 6: AI Copilot Integration (Future Work)
To further enhance the developer and no-code experience, an intelligent AI Copilot will be integrated natively into the browser. This ensures a 100% serverless, private AI assistant that can generate SIVO maps and code at $0 cloud compute cost.

1.  **Train a SIVO Adapter (LoRA):** Parse the SIVO repository (examples, docs, tests) into instruction-response pairs to fine-tune a small, capable base model (e.g., Llama-3.2-1B, Qwen2.5-1.5B, or Phi-3-mini) using PEFT.
2.  **Model Export & Fusion:** Since client-side inference engines require bundled weights, the trained LoRA adapter will be merged into the base model and exported to an optimized ONNX format (quantized to int4/int8 to fit browser memory limits).
3.  **Inference via Transformers.js:** Utilize Hugging Face's `Transformers.js` (with WebGPU acceleration) to load the merged ONNX model directly in the browser.
4.  **Chat Interface & Execution:**
    *   Implement a Copilot chat sidebar.
    *   When the user prompts (e.g., "Make a hexbin map using this dataset"), `Transformers.js` streams the generated SIVO Python code.
    *   The generated code block is passed directly to `pyodide.runPythonAsync(code)`.
    *   Pyodide reads any user data from IDBFS, generates the interactive map, and instantly renders the result in the UI iframe.
