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

### Animations & Dynamic Styling
*   **UI Flow:** An "Animations & Styling" sub-panel within the Property Inspector.
*   **Configuration:** Users can toggle standard CSS keyframe animations (like `pulse` and `fade`), set interactive image fills (`fill_pattern`, `hover_image`), and configure auto-shrinking text logic for regions where ZRender ignores `textLength`.

### Advanced Injections & Overlays
*   **UI Flow:** A "Dynamic Regions" tool that allows dragging content (HTML or scaled text) onto specific SVG paths.
*   **Configuration:** Maps directly to `fill_template_zone` (for replacing placeholders with scaled native SVG text) and `clip_html_to_shape` (for clipping raw HTML to the exact shape of an SVG element).

### Advanced Controls & Navigation
*   **UI Flow:** A global "Controls" settings tab for the map/dashboard view.
*   **Configuration:** Users can toggle built-in Zoom UI controls (`lock_zoom_out`), configure "Zoom on Click" interactions, enable Minimap overviews, set up Layer Toggles, and configure URL Navigation for SVG elements.

### Presentation Mode
*   **UI Flow:** A "Presentation Settings" tab next to Storyline Mode.
*   **Configuration:** Users can configure Auto-Play intervals (`presentation_autoplay_ms`), enable a visual Progress Indicator (`Slide X of Y`), select a Laser Pointer tool variant, configure Speaker Notes to render in a side-channel, and set up an Overview Step (`Escape`/`Home` shortcut) to zoom out to the map view.

### Geocoding & Thematic Mapping Extensibility
*   **UI Flow:** A "Geocoding & Data" panel when configuring maps.
*   **Configuration:** Users can input Mapbox or Google API keys to seamlessly geocode data coordinates. It also automatically generates interactive legends when a Choropleth or other data-driven map is created.

### Dynamic Odometers & Multi-View Projects
*   **UI Flow:** An "Odometers & Multi-View" manager.
*   **Configuration:** Users can drag-and-drop Dynamic Odometers onto the canvas to visualize numerical changes. Additionally, the builder manages `SivoProject` structures, allowing users to register multiple interconnected views (`add_view`) without being limited to just drill-downs.

### Publishing & Integrations (Offline, Streamlit, & Export Formats)
*   **UI Flow:** An "Export & Publish" wizard.
*   **Configuration:** Allows users to select output formats: standard HTML, offline HTML (triggers `build_js=True` bundling pipeline), PDF (via jsPDF), Image, JSON, or auto-generates Streamlit V2 Custom Component code snippets for embedding in Streamlit.


### Interactive Callbacks & Rich HTML Tooltips
*   **UI Flow:** A "Tooltips & Interactivity" configuration area in the Property Inspector.
*   **Configuration:** Users can attach rich HTML content (rendered securely inside a Shadow DOM) and define callback payloads (`callback_payload`) when elements are interacted with.

### Custom CSS, JS Injection & Layout Control
*   **UI Flow:** A "Code & Layout" settings panel within the main settings.
*   **Configuration:** Users can inject raw `custom_css` and `custom_js` during the `sivo.to_html()` export, and set the `default_panel_position` to control the overall side panel alignment.

### Declarative JSON Import & State Hydration
*   **UI Flow:** An "Import Project" function in the main File Manager Sidebar.
*   **Configuration:** Allows users to upload a SIVO JSON configuration payload which the builder automatically uses to hydrate the project state via `Sivo.from_config()`.

### Dynamic State Transitions (Image Toggles)
*   **UI Flow:** A "State Actions" sub-panel within the Property Inspector.
*   **Configuration:** Users can configure click interactions to dynamically toggle states, mapping to SIVO's `ToggleImageAction` to cycle through image overlays on map elements.

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
4.  Build the Property Inspector panel (colors, text, hover states, Rich HTML Tooltips, Interactive Callbacks, and Dynamic State Transitions via `ToggleImageAction`).
5.  Implement Declarative JSON Import to allow full project state hydration using `Sivo.from_config()`.

### Phase 3: Advanced No-Code Features (Weeks 5-6)
1.  **Data Binding Wizard:** Implement the UI to map CSV columns to SVG IDs for instant Choropleths.
2.  **Dashboard Mode:** Implement UI to add `SivoDashboard` blocks, metrics panels, and details panels.
3.  **Graph Generation:** Integrate logic that reads the parsed CSV and utilizes SIVO's native ECharts injection for custom graphs.


### Phase 4: Advanced Mapping, Live Data, & Integrations (Weeks 7-8)
1.  **Advanced Maps:** Integrate UI for Hexbins, Dot Density, and Flow Maps.
2.  **Live Binding:** Build the Data Sources manager for configuring WebSockets and API polling.
3.  **Integrations:** Add the Integration Catalog to allow embedding 3rd party services (Forms, E-commerce, BI).
4.  **A11y, Styling & Multimedia:** Expose Marker, Video, Audio, Animations, Image Fills, Keyboard Navigation, Custom CSS/JS Injection, and Layout Control (`default_panel_position`) configurations.

### Phase 5: Scrollytelling, Overlays, & Navigation (Weeks 9-10)

1.  **Timeline UI & Presentation:** Add the timeline components for Scrollytelling, Tours, and the new Presentation Mode (Auto-play, Progress Indicators, Laser Pointer, Speaker Notes).
2.  **Dynamic Regions & Odometers:** Implement UI for `fill_template_zone`, `clip_html_to_shape` mappings, and dropping Dynamic Odometers.
3.  **Global Controls:** Expose Zoom UI, Minimap, Layer Toggles, URL Navigation, and Zoom on Click configurations.

### Phase 6: Geocoding, Multi-View, & Advanced Export (Weeks 11-12)
1.  **Geocoding & Legends:** Integrate Mapbox/Google geocoding UI and Auto-Generated Legends.
2.  **Multi-View Projects:** Implement the overarching `SivoProject` manager for comprehensive multi-view structures.
3.  **Export/Share Expansion:** Implement the "Export & Publish" wizard to allow downloading standalone HTML, Offline HTML (`build_js=True`), PDF, Image, JSON exports, or Streamlit integration snippets.
4.  Extensive memory profiling to guarantee the browser does not crash on high-resolution SVGs or large datasets.

### Phase 7: AI Copilot Integration (Future Work)
To further enhance the developer and no-code experience, an intelligent AI Copilot will be integrated natively into the browser. This ensures a 100% serverless, private AI assistant that can generate SIVO maps and code at $0 cloud compute cost.

1.  **Train a SIVO Adapter (LoRA):** Parse the SIVO repository (examples, docs, tests) into instruction-response pairs to fine-tune a small, capable base model (e.g., Llama-3.2-1B, Qwen2.5-1.5B, or Phi-3-mini) using PEFT.
2.  **Model Export & Fusion:** Since client-side inference engines require bundled weights, the trained LoRA adapter will be merged into the base model and exported to an optimized ONNX format (quantized to int4/int8 to fit browser memory limits).
3.  **Inference via Transformers.js:** Utilize Hugging Face's `Transformers.js` (with WebGPU acceleration) to load the merged ONNX model directly in the browser.
4.  **Chat Interface & Execution:**
    *   Implement a Copilot chat sidebar.
    *   When the user prompts (e.g., "Make a hexbin map using this dataset"), `Transformers.js` streams the generated SIVO Python code.
    *   The generated code block is passed directly to `pyodide.runPythonAsync(code)`.
    *   Pyodide reads any user data from IDBFS, generates the interactive map, and instantly renders the result in the UI iframe.
