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
Embedded SVG Background Images
UI Flow: A canvas settings panel allowing users to upload or link an image to embed directly within the SVG layer so it pans and zooms alongside the vector elements.
Configuration: Maps directly to the `svg_background_image_url` and `svg_background_image_insert_after` parameters in `Sivo.from_svg()`.

Absolute Image Overlays
UI Flow: Users can drag and drop standalone image assets directly onto the builder canvas, locking them to specific map coordinates with scaling rules.
Configuration: Translates to `sivo_app.add_image_overlay()` to position images over element centers, optionally setting `scale_with_zoom`.


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
*   **Configuration:** Users can visually drop Markers (via `add_marker`), Scalable Text (`add_scalable_text`), and Progress Bars (`add_scalable_progress_bar`) onto the map. In the Property Inspector, users can attach Video, Audio, or complex actions like `Explode`  to specific SVG elements.

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

### Visual Annotation & Element Inspection
* **UI Flow:** An "Annotator Studio" mode where users can click on SVG elements in a preview pane to instantly view their IDs, bounding boxes, and coordinates.
* **Configuration:** Emulates the `sivo annotate` CLI command by integrating `annotator.html` logic to visually inspect and annotate SVGs directly within the browser workspace.

### Project Validation & Diagnostics
* **UI Flow:** A "Validate Project" tool that runs an automated health check, highlighting disconnected nodes or configuration errors directly on the canvas with warning icons.
* **Configuration:** Maps to the `sivo validate` CLI command logic, validating the JSON configuration payload against the parsed SVG structure to ensure all mapped element IDs are present.

### Project Initialization & Scaffolding
* **UI Flow:** A "New Project" wizard that takes an uploaded SVG and automatically scaffolds a baseline configuration with all discoverable element IDs.
* **Configuration:** Emulates the `sivo init` CLI command to create the initial `ProjectConfig` and extract available SVG IDs into a starter declarative JSON payload.

### Complex SVG Normalization & Style Preservation
* **UI Flow:** Users upload complex SVGs directly from design tools (like Illustrator or Figma), and the builder automatically flattens groups and retains original colors without manual styling.
* **Configuration:** Under the hood, the builder relies on SIVO's `SVGParser` to correctly handle nested `<g>` tags and `<use>` symbol references, automatically mapping native `fill` attributes to `theme.color`.

### Automated E2E Testing Scaffolding
* **UI Flow:** A "Testing & QA" toggle within the project settings allowing enterprise users to generate end-to-end test suites for their exported dashboards.
* **Configuration:** Sets the `enable_e2e_testing` flag to `True` in `ProjectConfig`, seamlessly generating scaffolded Playwright tests to ensure custom interactive SVGs scale correctly across browsers.

### Built-in SVG Templates
* **UI Flow:** A visual "Template Library" overlay where users can browse pre-configured aspect ratios (16:10, 1:1, etc.) instead of uploading an SVG.
* **Configuration:** The builder directly instantiates the canvas using `Sivo.from_template('template_name')` to start a new project.

### Dashboard Details & Metrics Panels
* **UI Flow:** In Dashboard Mode, users can drag pre-configured panel components (like a live feed or data readout) onto the CSS Grid alongside their map.
* **Configuration:** These visual blocks map directly to the `dashboard.add_details_panel` and `dashboard.add_metrics_panel` methods for automatic click-event rendering.

### Streamlit Bidirectional Communication
* **UI Flow:** A "Streamlit Connection" toggle in the export settings that enables real-time messaging between the web UI and a Python host.
* **Configuration:** Generates a custom component snippet utilizing `sivo_component` with iframe message passing to support bidirectional click/hover callbacks, dynamic color updates, and programmatic zooming.

### Shadow DOM Custom Styling & DOMPurify
* **UI Flow:** An "Advanced HTML Style" editor for components allowing users to write inline CSS specifically scoped to an element's tooltip or panel.
* **Configuration:** The builder configures DOMPurify with `FORCE_BODY: true` to allow `<style>` tags at the root of the string, which securely styles the content isolated inside the `#info-content-host` Shadow DOM.

### Selective ECharts Hover Effects
* **UI Flow:** A "Hover Feedback" toggle switch on non-interactive aesthetic elements to prevent distracting glow or color changes when moused over.
* **Configuration:** Sets `emphasis.disabled = true` per-element in the generated payload, turning off ECharts' default interactive highlights for unmapped nodes.

### Runtime Debugging & State Inspection
* **UI Flow:** A "Debug Console" panel in the builder that displays the live JSON payload of the currently rendered map.
* **Configuration:** Intercepts and parses the global `window.SivoData` object from the injected JS runtime to display the raw compiled Pydantic state.

### Programmatic Panel Dismissal
* **UI Flow:** A visual "Close Button" behavior that can be mapped to custom SVG elements, letting users create their own modal close triggers.
* **Configuration:** Binds the `onClick` event of the targeted element to the global `closePanel()` JavaScript function.

### XXE Security Mitigation
* **UI Flow:** An invisible, foundational security feature that safely parses user-uploaded XML files without risk of external attacks.
* **Configuration:** Under the hood, SIVO sets `resolve_entities=False` and `no_network=True` within the `lxml` parser to prevent XML External Entity (XXE) injection.

### JSON Serialization XSS Mitigation
* **UI Flow:** A built-in security guarantee that ensures no custom text or data entered by the user in the builder can break the exported output.
* **Configuration:** The builder serializes data and safely escapes `<` and `>` into `\u003c` and `\u003e` before injecting the `views_data` payload into JS templates, preventing XSS breakout.

### Nested ECharts Actions
* **UI Flow:** In the graphing setup, users can configure interactive charts to dispatch events that SIVO listens to, tying chart data selection directly back to the visual SVG map.
* **Configuration:** The builder maps standard ECharts events to the `NestedEchartsAction` mechanism in SIVO.

### Document & Map Embeds
* **UI Flow:** A specific component block allowing users to drag full PDF or external live map iframes into the interactive interface.
* **Configuration:** Configures the `add_document_embed` or `add_map_embed` functionality inside the generated Pydantic output.

### HTML/DOM Overlays
* **UI Flow:** A tool that allows users to place raw HTML or DOM elements directly on top of the map.
* **Configuration:** Users can map custom HTML directly via the SIVO API to float above the canvas.

### Proportional Symbols Map
* **UI Flow:** A tool in the "Map Types" drawer allowing users to scale circles over map regions based on numerical data.
* **Configuration:** Maps directly to `apply_proportional_symbols()` in the `Infographic` class to auto-generate scaled visual indicators.

### Spike Map
* **UI Flow:** An option in the "Map Types" drawer where users can select data columns to render 3D-like spikes emerging from map coordinates.
* **Configuration:** Maps to `apply_spike_map()` to automatically calculate and inject spike paths based on data values.

### Bivariate Choropleths (Value by Alpha)
* **UI Flow:** A mapping wizard that lets users select two separate data columns (one for color hue, one for opacity/alpha) to create complex data intersections.
* **Configuration:** Utilizes `apply_value_by_alpha()` to cross-reference two datasets against a unified map layer.

### Categorical Maps
* **UI Flow:** A simple configuration tab to bind string or categorical datasets to discrete colors (e.g., zoning maps or sales territories) with auto-generated legends.
* **Configuration:** Triggers `apply_categorical_map()` to securely map qualitative data blocks to SVG color properties.

### Path Connections
* **UI Flow:** A drag-and-drop relationship tool allowing users to draw animated flow lines or solid connectors between two different SVG nodes.
* **Configuration:** Maps visual endpoints to the `add_connection()` method to render SVG curves between calculated bounding boxes.

### Lottie Animations
* **UI Flow:** A widget in the Overlays toolbar where users can upload or link Lottie JSON files to render high-quality vector animations directly on the map.
* **Configuration:** Configures the `LottieAction` to inject the player script and animation data.

### Visual Comparisons
* **UI Flow:** A split-screen interaction block where users can configure "Before" and "After" images with a draggable slider.
* **Configuration:** Maps the configuration inputs to the `CompareAction` or leverages `sivo.to_html_compare()` for full map diffing.

### Gamification & Loaders
* **UI Flow:** A fun engagement settings panel where users can trigger celebratory confetti on clicks or custom loading animations while fetching external data.
* **Configuration:** Implements the `ConfettiAction` and `LoadingAction` within element interaction payloads.

### Path Morphing
* **UI Flow:** An advanced animation setting that lets users link an element's path to another element, enabling fluid shape transitions on click or hover.
* **Configuration:** Embeds `morph_to_path` and `morph_duration_ms` parameters inside the element's `ThemeOverride` configuration.

### Image Shape Clipping
* **UI Flow:** A masking tool that lets users drag an image file and strictly clip it to the exact bounds of a complex SVG path (e.g., fitting a photo inside a country border).
* **Configuration:** Calls `clip_image_to_shape()` to inject a dynamic SVG clip-path referencing the target node.

### Interactive Drawing Tools
* **UI Flow:** A drawing toolbar on the canvas allowing users to sketch or annotate freely on top of the loaded SVG map or dashboard.
* **Configuration:** The builder sets `enable_drawing_tools=True` when instantiating the canvas, enabling native interactive drawing layer support.

### SVG Affine Transformations
* **UI Flow:** A "Transform" panel within the Property Inspector where users can visually rotate, scale, and translate SVG elements using sliders or input fields.
* **Configuration:** When the builder is running with `render_mode="svg"`, the user's inputs are compiled into a valid transformation string and passed to the `transform` property of `Sivo.map()`.

### Geographic Coordinate Mapping
* **UI Flow:** A configuration dialog that lets users bind the canvas to real-world latitude and longitude bounds, mapping pixel space to geographic space for accurate data plotting.
* **Configuration:** The user defines the geo-bounds, which are passed to the `bounding_coords` parameter in `Sivo.from_svg()`, enabling exact geographic placement of proportional symbols and other elements.

### Native SVG Shape Generation
* **UI Flow:** A "Shapes" library that allows users to drag-and-drop basic geometry (rectangles, circles, lines) or text nodes directly onto a blank or existing canvas.
* **Configuration:** The builder translates these actions into programmatic calls to `sivo_app.add_shape()`, injecting native scalable geometry or text (via the `text_content` attribute) into the layout.


### Drill-Through Page Transitions
* **UI Flow:** An interaction setting where users can define a URL or file path and a page transition animation (e.g., 'flip', 'slide-left') to navigate completely away from the current map view.
* **Configuration:** Maps the user inputs to the `drill_through` and `drill_transition` parameters in the `sivo.map()` API for multi-page routing.

### Markdown & Image Gallery Rendering
* **UI Flow:** A rich content tab where users can drop Markdown text blocks or upload a series of images to display when an element is clicked.
* **Configuration:** The builder parses these inputs and binds them to `MarkdownAction` and `GalleryAction` within the interaction mapping payload.

### Contextual Footnotes
* **UI Flow:** A text input field in the Property Inspector to add small contextual annotations or citations that appear dynamically below the main map view when hovering or clicking an element.
* **Configuration:** Passes the text string to the `FootnoteAction` model to render non-intrusive supplementary information.

### Dynamic API Fetching on Click
* **UI Flow:** An advanced action setting where users can provide a REST endpoint URL to be queried in real-time only when a specific SVG element is interacted with, displaying the result.
* **Configuration:** Binds the endpoint URL to `FetchAction` to securely retrieve and inject external JSON/HTML data upon user click.

### Hover Callbacks
* **UI Flow:** A specific interactivity toggle allowing users to send data payloads back to the host system immediately upon hovering over an element, rather than waiting for a click.
* **Configuration:** Compiles the configured payload and triggers the `HoverCallbackAction` to enable bidirectional communication on mouse-over events.


### Visual Data Flow Connections
* **UI Flow:** A "Connect Nodes" tool allowing users to click and drag lines between two SVG elements to show relationships or logic flows.
* **Configuration:** Calls `sivo_app.add_connection()` to dynamically draw SVG connection paths between the calculated bounding boxes of the targeted elements.

### Ecommerce Embeds
* **UI Flow:** A dedicated widget in the Integrations catalog that lets users paste a product link or embed code from Stripe, Shopify, or other providers to create a native shoppable panel.
* **Configuration:** The builder maps the inputs directly to the `EcommerceAction` model for rendering external e-commerce checkouts.

### Rich Media Embeds
* **UI Flow:** A multimedia block where users can provide links for Vimeo, Spotify, SoundCloud, or Twitch, instantly pulling in the playable media widget.
* **Configuration:** Maps the user's media link and settings to the `RichMediaAction` to embed responsive third-party media players inside the dashboard.

### Business Intelligence Embeds
* **UI Flow:** A specialized analytics widget allowing users to drop an embed link or iframe snippet for external BI tools like Tableau, Metabase, or PowerBI.
* **Configuration:** The inputs are mapped to the `BIAction` model, injecting interactive, data-dense third-party visualisations directly into SIVO panels.

### External Forms
* **UI Flow:** A widget in the Integration Catalog that allows users to embed external lead generation or survey forms (e.g. HubSpot, Jotform, Qualtrics).
* **Configuration:** Maps the user-provided form URLs directly to the `ExternalFormAction` model to render the external interactive forms securely.

### Scratchoff Reveal Layers
* **UI Flow:** An interaction toggle that lets a user apply a digital "scratch-off" mask over a visual element, hiding underlying text or graphics until the viewer manually interacts.
* **Configuration:** Translates the visual masking settings to the `ScratchoffConfig` model, applying a dynamic reveal layer to the targeted element.

### Form, Social & Replit Embeds
* **UI Flow:** Dedicated widgets in the Integration Catalog that allow users to drop in URLs for Typeform, Reddit, or Replit to instantly render embedded iframes.
* **Configuration:** Maps the user inputs directly to the `FormAction`, `SocialAction`, and `ReplitAction` models within the interaction mapping logic.



### Dramatic UI Transitions (Explode)
*   **UI Flow:** An interaction toggle where users can configure a visual effect that dramatically transitions the UI by exploding the clicked element into a new layout.
*   **Configuration:** Maps the interaction directly to the `ExplodeAction` to securely transition the UI.

### High Contrast Theming
*   **UI Flow:** A "Theme" dropdown in the accessibility and styling settings that allows users to toggle between standard, dark, and high-contrast visuals.
*   **Configuration:** The builder passes the user's choice directly to the `theme` parameter during canvas instantiation to enforce accessible color profiles.

### Ambient Effects
*   **UI Flow:** An "Environment Effects" toggle in the styling panel that allows users to select atmospheric particle overlays (like snow, rain, or fireflies) and adjust their speed.
*   **Configuration:** The builder sets the `ambient_effect` and `ambient_speed` parameters on the `Sivo` instance to natively render particle animations over the map.

### Brush Selection
*   **UI Flow:** A tool in the Global Controls panel that allows end-users to click and drag a lasso or rectangular brush over the map to select multiple elements at once.
*   **Configuration:** Maps the user's toggle to the `enable_brush_selection` parameter during canvas instantiation.

### Watermarks & Attribution
*   **UI Flow:** A "Branding & Metadata" section in the project settings where users can input custom text for map titles, subtitles, attribution, or upload a watermark logo.
*   **Configuration:** The builder assigns the inputs to the `title`, `subtitle`, `attribution`, and `watermark` arguments in the SIVO constructor.

### Built-in Canvas Search
*   **UI Flow:** A toggle in the Global Controls to enable a search bar overlay on the final map, allowing users to find specific mapped elements by name or ID.
*   **Configuration:** The builder sets the `enable_search` parameter to `True` on the `Sivo` instance to natively generate the search UI.

### Canvas Backgrounds & Borders
*   **UI Flow:** A "Canvas Backdrop" settings menu where users can upload or link images to serve as the map's background or border frame, adjusting opacity and grayscale.
*   **Configuration:** Translates inputs into the `background_image_url`, `border_image_url`, and related opacity/grayscale parameters during initialization.

### Export & Sharing Overlays
*   **UI Flow:** Toggles in the Global Controls enabling end-users to enter fullscreen mode, download the raw data, or share the view via an overlay menu.
*   **Configuration:** Maps the selections to `enable_fullscreen`, `enable_data_download`, and `enable_share` flags in the SIVO setup.

### ECharts Tooltip Z-Index Enforcement
*   **UI Flow:** A "Tooltip Layering" override in the Property Inspector that guarantees tooltip boxes always float visually above complex or overlapping elements.
*   **Configuration:** The builder appends `z-index: 9999;` to the `extraCssText` configuration inside the ECharts payload to force tooltip layering.

## 6. Modern UI/UX Design System & Productization
To elevate the web app from an "example" to a modern, production-grade product, the interface will undergo a complete design system overhaul.
*   **CSS Framework:** Migrate from raw CSS to a utility-first framework like Tailwind CSS, paired with highly accessible, pre-built component libraries (e.g., Shadcn UI or Radix UI) for clean modals, dropdowns, and context menus.
*   **Dark Mode & Theming:** Implement native system-level Dark Mode detection with seamless toggling. Code editors (Monaco/CodeMirror) and canvas backgrounds will automatically sync with the active theme.
*   **Drag-and-Drop UX:** Add fluid animations and clear visual drop zones (e.g., dashed borders, highlighting) when dragging files from the OS or moving blocks around in the Dashboard Layout mode.
*   **Onboarding & Empty States:** Implement guided interactive tooltips for first-time users (e.g., "Drag a CSV here to start"), and ensure robust empty states for panels rather than blank screens or console errors.
*   **State & Feedback:** Introduce non-blocking toast notifications for system events ("Saving to IDBFS...", "Error parsing CSV"), and skeletal loading screens during the initial WASM/Pyodide load phase.

## 7. UX Strategy: Managing Complexity & Cognitive Load
With a feature set this extensive, a core product risk is overwhelming non-technical users. To ensure the SIVO No-Code Builder remains accessible, the following UX principles must be strictly implemented:

*   **Progressive Disclosure:** By default, the Property Inspector will only show basic settings (e.g., Tooltip Text, Color, Hover Color). Complex configurations like Interactive Callbacks, Custom CSS Injection, and E2E Testing scaffolding must be hidden behind an "Advanced Settings" toggle or a collapsible accordion to reduce visual clutter.
*   **Contextual Tooling:** Features should only appear when relevant. For example, the "Map Types" drawer (Choropleth, Hexbin) should only activate when a dataset is successfully linked to an SVG. Data binding options should not be visible when editing purely cosmetic elements like SVGs or Images.
*   **Task-Based Workspaces:** Instead of one massive editor, the UI should be divided into distinct modes:
    *   **Design Mode:** Focuses on layout, SVG normalization, theming, and aesthetics.
    *   **Data Mode:** Focuses on the CSV binding wizard, live data connections, and multi-view project linking.
    *   **Publish Mode:** Focuses on accessibility, E2E testing, geocoding API keys, and export formats.
*   **Command Palette (Cmd+K):** A quick-action search bar will allow power users to bypass the UI to find specific tools (e.g., "Add Timeline", "Validate Project") instantly without deep menu navigation.
*   **Opinionated Defaults & Templates:** The "New Project" wizard should offer pre-configured, best-practice templates (e.g., "Basic Sales Dashboard", "Scrollytelling Map") that automatically wire up standard interactions, rather than presenting a blank canvas.
*   **Interactive Previews & Pre-generation:** Complex state changes (like adding a custom CSS animation, testing a hover callback, or simulating an auto-play presentation) should include an on-demand "Preview" action within their configuration panels, allowing the user to view the isolated effect before applying it to the entire canvas.

## 8. Step-by-Step Implementation Roadmap

### Phase 1: Core Storage & File Management (Weeks 1-2)
1.  Extend the current `index.html` UI to include a robust File Manager Sidebar.
2.  Implement the drag-and-drop / URL fetcher in JS that streams directly to Pyodide IDBFS.
3.  Add memory cleanup routines to ensure large files are flushed from RAM after saving to IDBFS.
4.  Implement CSV/XLSX to IDBFS parsing utility.
5.  **Complex SVG Normalization:** Integrate SIVO's `SVGParser` to properly flatten groups, support `<use>` references, and preserve native styling for incoming files.
6.  **XXE Security Mitigation:** Ensure all uploaded XML/SVG parsing relies securely on `resolve_entities=False` and `no_network=True` to prevent injection attacks.
7.  **JSON Serialization XSS Mitigation:** Integrate the safe escaping logic for injected JSON `views_data` to secure templates from cross-site scripting natively.

### Phase 2: The No-Code UI Foundation (Weeks 3-4)
1.  Build the "App Builder" tab alongside "Annotator Studio" and "Python Workspace" using the new Tailwind/Shadcn design system.
2.  Implement the Visual Template Selector (reading from SIVO's built-in `src/sivo/templates`) for launching **Built-in SVG Templates**.
3.  Implement the Interactive Preview Pane (renders via `app.to_html()`).
4.  Build the Property Inspector panel (colors, text, hover states, Rich HTML Tooltips, Interactive Callbacks, **Hover Callbacks**, **Contextual Footnotes**, and Dynamic State Transitions via `ToggleImageAction`), and add the **Selective ECharts Hover Effects** toggle and **ECharts Tooltip Z-Index Enforcement**.
5.  Implement Declarative JSON Import to allow full project state hydration using `Sivo.from_config()`.
6.  **Project Initialization & Annotation:** Integrate the "New Project" scaffolding logic (`sivo init` equivalent) and visual element inspection (`sivo annotate` equivalent) into the primary workspace.

### Phase 3: Advanced No-Code Features (Weeks 5-6)
1.  **Data Binding Wizard:** Implement the UI to map CSV columns to SVG IDs for instant Choropleths.
2.  **Dashboard Mode:** Implement UI to add `SivoDashboard` blocks, integrating **Dashboard Details & Metrics Panels**.
3.  **Graph Generation:** Integrate logic that reads the parsed CSV and utilizes SIVO's native ECharts injection for custom graphs, adding support for **Nested ECharts Actions** configuration.
4.  **Project Validation:** Introduce the "Validate Project" diagnostics tool (`sivo validate` equivalent) to check for missing nodes or bad mappings, alongside **Runtime Debugging & State Inspection**.


### Phase 4: Advanced Mapping, Live Data, & Integrations (Weeks 7-8)
1.  **Advanced Maps:** Integrate UI for Hexbins, Dot Density, Flow Maps, Proportional Symbols, Spike Maps, Categorical Maps, and Bivariate Choropleths (Value by Alpha).
2.  **Live Binding:** Build the Data Sources manager for configuring WebSockets, API polling, and **Dynamic API Fetching on Click**.
3.  **Integrations:** Add the Integration Catalog to allow embedding 3rd party services (E-commerce, BI) and support for **Document & Map Embeds**, **Ecommerce Embeds**, **Rich Media Embeds**, **Business Intelligence Embeds**, **External Forms**, as well as **Form, Social & Replit Embeds**.
4.  **A11y, Styling & Multimedia:** Expose Marker, Video, Audio, **Markdown & Image Gallery Rendering**, Animations, Image Fills, Keyboard Navigation, Custom CSS/JS Injection, Layout Control (`default_panel_position`) configurations, Lottie Animations, Gamification & Loaders, Path Morphing, Image Shape Clipping, **SVG Affine Transformations**, **High Contrast Theming**, **Ambient Effects**, **Canvas Backgrounds & Borders**, **Embedded SVG Background Images**, **Dramatic UI Transitions**, and **Shadow DOM Custom Styling & DOMPurify** support.

### Phase 5: Scrollytelling, Overlays, & Navigation (Weeks 9-10)

1.  **Timeline UI & Presentation:** Add the timeline components for Scrollytelling, Tours, and the new Presentation Mode (Auto-play, Progress Indicators, Laser Pointer, Speaker Notes).
2.  **Dynamic Regions & Odometers:** Implement UI for `fill_template_zone`, `clip_html_to_shape` mappings, dropping Dynamic Odometers, Path Connections, **Visual Data Flow Connections**, Visual Comparisons, **Native SVG Shape Generation**, **Absolute Image Overlays**, **Scratchoff Reveal Layers**, and configuring **HTML/DOM Overlays**.
3.  **Global Controls:** Expose Zoom UI, Minimap, Layer Toggles, URL Navigation, Zoom on Click configurations, **Interactive Drawing Tools**, **Brush Selection**, **Built-in Canvas Search**, and **Programmatic Panel Dismissal** mappings.

### Phase 6: Geocoding, Multi-View, & Advanced Export (Weeks 11-12)
1.  **Geocoding & Legends:** Integrate Mapbox/Google geocoding UI, Auto-Generated Legends, and **Geographic Coordinate Mapping**.
2.  **Multi-View Projects:** Implement the overarching `SivoProject` manager for comprehensive multi-view structures, including **Drill-Through Page Transitions**.
3.  **Export/Share Expansion:** Implement the "Export & Publish" wizard to allow downloading standalone HTML, Offline HTML (`build_js=True`), PDF, Image, JSON exports, or Streamlit integration snippets with **Streamlit Bidirectional Communication** capabilities, and expose **Watermarks & Attribution** and **Export & Sharing Overlays**.
4.  **Automated E2E Testing Scaffolding:** Expose the `enable_e2e_testing` configuration parameter to support generating scaffolded tests for the output dashboards.
5.  Extensive memory profiling to guarantee the browser does not crash on high-resolution SVGs or large datasets.

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
