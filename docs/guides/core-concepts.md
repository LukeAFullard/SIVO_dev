---
Last Updated: 2026-04-09
SIVO Version: 1.0.0
---

# H-03: Core Concepts

Explaining the 'Bridge': How Python objects become interactive frontend elements.

## Table of Contents

1. **The SIVO Philosophy**
2. **The Lifecycle of a SIVO Object**
3. **Pydantic Model Integration**
4. **State Management in Python vs JS**
5. **Sanitization and Security boundary**

## 1. The SIVO Philosophy

SIVO (SVG Interactive Vector Objects) is designed to bridge the gap between static SVG files and highly interactive, data-driven web applications. The core philosophy centers on two main principles:

*   **Declarative Data-Binding to SVG Shapes:** Instead of writing complex JavaScript to manipulate DOM nodes, you use Python to map data, tooltips, events, and styles to specific SVG element IDs. SIVO handles the translation, mapping your declarative Python configurations to the underlying JavaScript engine (Apache ECharts).
*   **No Backend Required (Serverless Architecture):** SIVO generates a single, self-contained HTML bundle containing the SVG template, ECharts, and all interaction logic. This means you can deploy the result anywhere—GitHub Pages, AWS S3, or simply open the file locally in a browser—without needing an active Python server or database. It fully supports WASM environments like Pyodide for 100% browser-based Python execution.

## 2. The Lifecycle of a SIVO Object

Understanding how a SIVO object transitions from a Python script to a visual frontend element is crucial. The lifecycle consists of four main steps:

### Step 1: Ingestion

The process begins by loading an SVG template. SIVO uses `lxml` to securely parse the SVG content (with network entity resolution disabled to prevent XXE attacks). It validates the XML structure and identifies elements by their `id` attributes. This allows the framework to know which shapes are available for interaction.

### Step 2: Configuration

You define interactions and styles using the SIVO Python API. When you call methods like `sivo.map(element_id="my_shape", tooltip="Click me")`, SIVO constructs a strongly-typed Pydantic configuration tree. This stage validates all data and parameters before any code is generated.

### Step 3: Bundling

When you export the project (e.g., `sivo.to_html()`), SIVO hands the Pydantic configuration over to `bundle_generator.py`. This component uses Jinja2 templates (`echarts.html` or `dashboard_blocks.html`) to inject the SVG string and the JSON-serialized configuration into a static HTML file. The JSON payload is rigorously sanitized (replacing `<`, `>`, and `&` with unicode escapes) to prevent XSS vulnerabilities.

### Step 4: Runtime

The final HTML file is loaded in the user's browser. The embedded JavaScript initializes Apache ECharts, registers the SVG string as a map, and parses the configuration. ECharts natively handles the rendering, zooming, panning, and interaction events based on the declarative rules defined in Step 2.

## 3. Pydantic Model Integration

SIVO relies heavily on Pydantic to ensure that the Python-to-JS bridge is robust and predictable.

*   **How Python types map to JS logic:** Every interactive capability (tooltips, click actions, animations) is backed by a Pydantic model in Python, which perfectly mirrors the expected JSON structure in the JavaScript runtime. This guarantees that if the Python code passes validation, the JS code will not fail due to missing or incorrect parameters.
*   **Strict Validation:** Core models like `ElementConfig` and `ActionConfig` utilize `model_config = ConfigDict(extra="forbid")`. This catches unexpected keyword arguments during configuration, throwing explicit errors rather than silently failing during browser rendering.

**Example Mapping Model:**

```python
from pydantic import BaseModel, ConfigDict
from typing import Optional

class ElementConfig(BaseModel):
    id: str
    tooltip: Optional[str] = None
    hover_color: Optional[str] = None
    # Strict validation prevents malformed configs
    model_config = ConfigDict(extra="forbid")
```

## 4. State Management in Python vs JS

A key concept in SIVO is understanding where state "lives".

*   **Static Generation in Python:** The Python script generates the *initial* state and the *rules* for state transitions. Python does not actively manage the map while the user interacts with it (unless using live WebSockets or polling).
*   **Runtime Interactions in JS:** Once the HTML bundle is generated, all interaction state is managed entirely in the browser by JavaScript.
    *   **The `viewHistory` Stack:** Navigation through multiple map levels (drilldowns) is handled by pushing and popping states onto a `viewHistory` array in JS.
    *   **Dynamic Logic (e.g., `cycle_state`):** Actions like toggling colors or text dynamically update ECharts configurations natively via `setOption()`. For example, multiline SVG text updates manipulate ECharts' `series[i].label` rather than directly mutating the DOM `<text>` nodes, ensuring stability across redraw cycles.

## 5. Sanitization and Security Boundary

Because SIVO injects user-defined data and configuration into HTML files, security is paramount. SIVO enforces strict boundaries to mitigate vulnerabilities:

*   **JSON Serialization Escaping:** During bundling, dictionaries are serialized to JSON with `<, >, &` explicitly escaped to unicode sequences (`\u003c`, etc.) to prevent malicious payload execution within `<script>` tags.
*   **DOMPurify:** The SIVO frontend strictly enforces the use of the `DOMPurify` library. Any dynamic assignment to `.innerHTML` (e.g., in click panels or custom HTML tooltips) is wrapped with `window.DOMPurify.sanitize()`. This sanitizes potentially unsafe HTML before it enters the DOM, effectively blocking XSS attacks. A fail-closed or basic escaping fallback is implemented if the library fails to load.
*   **Content-Security-Policy (CSP):** The generated HTML bundles include a strict CSP meta tag to restrict the execution of unauthorized scripts and block embedded objects (`object-src 'none'`), ensuring the map runs safely even if embedded in untrusted environments.
