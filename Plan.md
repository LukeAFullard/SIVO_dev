# Project Plan: **SIVO (SVG Interactive Vector Objects)**

*A Python Framework for Interactive, SVG-Driven Web Infographics with Streamlit Integration*

---

# 1. Executive Summary

**SIVO (SVG Interactive Vector Objects)** is a Python framework that converts static SVG graphics into responsive, interactive web infographics using a Python-first workflow. It allows designers, analysts, and developers to attach behaviors—tooltips, drill-downs, navigation, and dynamic updates—to individual SVG paths without writing JavaScript.

The system bridges the gap between **vector design tools** and **interactive web data visualization**. A user provides an SVG file and maps SVG element IDs to Python-defined actions. SIVO processes the SVG into a canonicalized form, generates an interaction manifest, and exports a fully functional interactive web asset.

The primary deployment target is **Python applications built with** Streamlit, enabling live dashboards and operational interfaces. The system also supports static HTML export for standalone deployment.

---

# 2. Project Goals

### Primary Goals

1. Convert static SVG diagrams into interactive web experiences.
2. Enable Python developers to define interaction logic without writing JavaScript.
3. Provide seamless integration with Streamlit applications.
4. Ensure robustness against real-world SVG complexity.
5. Produce responsive and mobile-friendly visual interfaces.

### Non-Goals (Version 1)

The first release will not attempt to:

* Replace full visualization libraries.
* Provide complex charting systems.
* Support animated SVG editing pipelines.
* Serve as a full design tool.

Instead, SIVO focuses strictly on **interaction layers for existing SVG artwork**.

---

# 3. Core Concepts

## 3.1 SVG Interactive Vector Object

A **SIVO object** represents a single identifiable SVG element that can respond to user interactions.

Examples:

| SVG Element            | Possible Interaction             |
| ---------------------- | -------------------------------- |
| `<path id="room101">`  | Tooltip with room data           |
| `<rect id="machineA">` | Click to open status panel       |
| `<g id="floor1">`      | Drill down to floor plan         |
| `<path id="pipeline">` | Color change when sensor updates |

Each SIVO object maps to a Python action definition.

---

## 3.2 Action Objects

Actions define behavior associated with SVG IDs.

### Action Types

| Action    | Description                    |
| --------- | ------------------------------ |
| Tooltip   | Display contextual information |
| URL       | Navigate to external link      |
| DrillDown | Load another SVG               |
| Callback  | Send event to Streamlit        |
| Highlight | Change visual state            |

---

# 4. System Architecture

SIVO is composed of five primary subsystems.

| Component        | Role                                |
| ---------------- | ----------------------------------- |
| SVG Normalizer   | Parses and canonicalizes SVG files  |
| Mapping Engine   | Connects SVG IDs to Python actions  |
| Bundle Generator | Creates interactive HTML packages   |
| Frontend Runtime | Handles interactions in browser     |
| Streamlit Bridge | Integrates SIVO with Streamlit apps |

---

# 5. SVG Normalization Engine

Real-world SVG files contain nested transforms, symbol references, and inconsistent coordinate systems. SIVO solves this by **canonicalizing the SVG before interaction logic is applied**.

### Responsibilities

1. Parse SVG structure
2. Resolve `<use>` references
3. Flatten nested `<g>` transforms
4. Convert all paths into absolute coordinates
5. Extract bounding boxes
6. Generate metadata for hit detection

### Output

```
canonical_svg
metadata.json
```

Metadata example:

```json
{
  "objects": [
    {
      "id": "buildingA",
      "bbox": [12.1, 45.6, 210.4, 160.2],
      "type": "path"
    }
  ]
}
```

### Python Libraries

The normalizer will use:

* lxml
* BeautifulSoup

These provide reliable XML parsing and manipulation.

---

# 6. Mapping Engine

The mapping engine connects Python code to SVG elements.

## Sivo Orchestrator Class

Primary user-facing API, wrapping the internal `Infographic` logic to provide a seamless declarative interface.

```python
from sivo import Sivo

sivo_app = Sivo.from_svg("campus.svg")

sivo_app.map(
    "buildingA",
    tooltip="<h3>Building A</h3>",
    drill_to="buildingA.svg"
)

sivo_app.to_html("output.html")
```

### Responsibilities

* Track mapped IDs
* Validate actions
* Generate interaction manifest
* Provide export functionality

---

# 7. Manifest Format

All interactions are serialized into a **manifest JSON file** consumed by the browser runtime.

Example:

```json
{
  "objects": {
    "buildingA": {
      "tooltip": "<h3>Building A</h3>",
      "drill_to": "buildingA.svg"
    }
  }
}
```

This decouples Python logic from frontend execution.

---

# 8. Frontend Runtime

The runtime handles all browser interactions.

Responsibilities:

* SVG rendering
* Hit detection
* Tooltip management
* Drill-down transitions
* Responsive scaling

Optional rendering layers may use:

* Apache ECharts for map-style rendering if needed.

However, SIVO primarily relies on **native SVG interaction**.

---

# 9. Responsive Rendering System

SVG elements must scale correctly inside flexible layouts.

SIVO implements:

### ResizeObserver-based scaling

The runtime monitors container dimensions and rescales the SVG accordingly.

Key behaviors:

* Maintain aspect ratio from `viewBox`
* Correct hit detection after scaling
* Maintain pointer accuracy

---

# 10. Hit Detection Strategy

Small paths can become difficult to click.

SIVO implements two mechanisms:

### Invisible Hit Padding

Adds invisible expanded shapes behind small paths.

### Optional Spatial Index

For large SVGs (>500 paths), SIVO creates a client-side spatial index to speed up hit detection.

---

# 11. Tooltip System

SIVO tooltips use **Shadow DOM encapsulation**.

Benefits:

* Prevent CSS conflicts
* Support complex HTML
* Allow embedded media

Capabilities:

| Feature             | Supported       |
| ------------------- | --------------- |
| HTML content        | Yes             |
| Embedded dashboards | Yes             |
| iframes             | Yes (sandboxed) |
| dynamic updates     | Yes             |

---

# 12. Security Model

User-provided HTML can create security risks.

SIVO implements:

### HTML Sanitization

HTML content is sanitized before export.

### Iframe Sandbox

Embedded iframes include strict sandbox rules.

### Content Security Policy

Example CSP provided for deployment.

---

# 13. Drill-Down Navigation

Hierarchical navigation enables complex visual storytelling.

Example:

```
Campus Map
  └ Building A
        └ Floor 1
```

### Mechanism

1. User clicks SVG object
2. Runtime loads secondary SVG
3. Transition animation plays
4. Breadcrumb navigation updates

### Transition Types

* Crossfade (default)
* Scale transition
* Optional morphing

---

# 14. Theme System

Themes control visual styles across interactions.

Example:

```python
Theme(
    hover_color="#ff6600",
    border_width=2,
    glow=True
)
```

Theme controls:

* hover colors
* outline thickness
* highlight styles
* animation duration

---

# 15. Streamlit Integration

SIVO provides first-class integration with:

Streamlit

### Streamlit Component

A custom component renders the SIVO bundle inside a Streamlit app. **Note: Any Streamlit component MUST be a V2 component (`st.components.v2.component`).** See [V2 Components Documentation](https://docs.streamlit.io/develop/api-reference/custom-components/st.components.v2.component) and [V2 Components with file-backed assets](https://discuss.streamlit.io/t/how-do-i-use-components-v2-with-file-backed-css-html-and-or-js/120290) for more information.

Capabilities:

| Feature               | Supported |
| --------------------- | --------- |
| Live tooltip updates  | Yes       |
| Click callbacks       | Yes       |
| Dynamic coloring      | Yes       |
| Drill-down navigation | Yes       |

### Example

```python
import streamlit as st
from sivo import Sivo
from sivo.streamlit.component import sivo_component

sivo_app = Sivo.from_svg("factory.svg")

sivo_app.map("machineA", tooltip="Machine A")

result = sivo_component(sivo_app.infographic, key="sivo_example")
```

---

# 16. Command Line Interface

The CLI assists users in preparing SVG projects.

### Commands

Initialize project

```
sivo init diagram.svg
```

Export bundle

```
sivo export project.yml
```

Validate SVG

```
sivo validate diagram.svg
```

---

# 17. Project Structure

```
sivo/
  __init__.py

  core/
    sivo.py
    infographic.py
    actions.py
    config.py

  svg/
    normalizer.py
    parser.py
    transforms.py

  runtime/
    bundle_generator.py
    templates/

  frontend/
    sivo_runtime.js
    tooltip.js
    drilldown.js

  streamlit/
    component.py

  cli/
    commands.py

tests/
examples/
docs/
```

---

# 18. Development Roadmap

## Phase 1 — SVG Processing

Deliverables:

* [x] SVG parser
* [x] canonicalizer (Robust `<use>` reference resolution, proper wrapping, and cycle detection completed)
* [x] metadata extraction
* [x] bounding box calculation (Robust parser implemented for SVG paths handling relative/absolute commands and exponential notation)

## Phase 2 — Interaction System

Deliverables:

* [x] Action classes
* [x] manifest generator
* [x] tooltip system (Shadow DOM encapsulated)
* [x] hit detection

## Phase 3 — Frontend Runtime

Deliverables:

* [x] JS runtime
* [x] resize handling
* [x] drill-down transitions (SVG loading & chart rebuilding fixed)
* [x] event system (Full Streamlit callback sync)

## Phase 4 — Streamlit Integration

Deliverables:

* [x] Streamlit component (V2 API)
* [x] example apps
* dynamic updates

## Phase 5 — Configuration & CLI

Deliverables:

* [x] Configuration Engine (JSON/dict parsing)
* [x] CLI tool
* [x] Sivo Declarative Orchestrator
* pip packaging
* documentation
* example gallery

---

# 19. Testing Strategy

### Unit Tests

* SVG parsing
* transform flattening
* metadata generation

### Integration Tests

* runtime interaction
* tooltip rendering
* drill-down navigation

### Security Tests

* HTML sanitization
* iframe sandboxing

### Performance Tests

Goal:

* <50ms interaction latency
* 200+ paths without slowdown

---

# 20. Documentation

Documentation will include:

* Quickstart guide
* API reference
* SVG preparation guidelines
* Streamlit examples
* troubleshooting guide

---

# 21. Packaging and Distribution

The project will be distributed via:

```
pip install sivo
```

Assets include:

* Python package
* JS runtime bundle
* CLI tool
* example datasets

---

# 22. Example Use Cases

### Smart Buildings

Interactive building diagrams showing occupancy and sensor data.

### Factory Monitoring

Machines displayed as SVG elements updating status in real time.

### Infrastructure Maps

Power grids, pipelines, and network systems.

### Educational Diagrams

Biology, anatomy, engineering schematics.

---

# 23. Success Criteria

Version 1 of SIVO is considered successful when:

* Developers can convert an SVG to an interactive asset in under 10 minutes.
* Streamlit dashboards can embed SIVO graphics easily.
* The system handles real-world SVG complexity.
* Interactions remain responsive with hundreds of paths.

---

# 24. Future Enhancements

Future versions may include:

* Interactive SVG editor
* visual mapping GUI
* real-time websocket updates
* automatic path labeling
* path morph animations

---

# 25. Summary

**SIVO (SVG Interactive Vector Objects)** provides a robust framework for transforming static SVG designs into interactive data-driven interfaces using Python. By combining SVG normalization, Python-defined interaction logic, and Streamlit integration, SIVO enables developers to build powerful visual interfaces without complex frontend engineering.

The system prioritizes reliability, accessibility, and simplicity while remaining extensible for advanced visualization needs.

# 26. Next Steps

### Phase 1: Debugging & Security Audit

**1. Critical Vulnerability: XML External Entity (XXE) Injection (Completed)**
*   **Location:** `src/sivo/svg/parser.py`, Lines 9-14
*   **Assessment:** The application parses SVG (XML) files using `lxml.etree.parse()` without disabling network access or entity resolution. This exposes the application to XXE injection vulnerabilities, potentially allowing attackers to read local files, conduct Server-Side Request Forgery (SSRF) attacks, or cause Denial of Service (DoS) if malicious or untrusted SVGs are uploaded and processed.
*   **Proposed Solution:**
    ```python
    def __init__(self, filepath_or_string: str, is_file: bool = True):
        # Explicitly secure the parser against XXE
        parser = etree.XMLParser(resolve_entities=False, no_network=True)

        if is_file:
            with open(filepath_or_string, 'rb') as f:
                self.tree = etree.parse(f, parser=parser)
            self.root = self.tree.getroot()
        else:
            self.root = etree.fromstring(filepath_or_string.encode('utf-8'), parser=parser)
            self.tree = etree.ElementTree(self.root)
    ```
*   **Trade-off:** Disabling external entities improves security immensely but may break unusual legacy SVG files that legitimately rely on external entities. This does not change the API contract.

**2. Security Risk: Cross-Site Scripting (XSS) via DOM Injection (Completed)**
*   **Location:** `src/sivo/runtime/templates/echarts.html`, Lines 117-124
*   **Assessment:** The JS runtime injects user-defined HTML content (`action.content`) into the DOM via `infoContent.innerHTML = htmlContent;`. Even though it is encapsulated in a Shadow DOM, this is still vulnerable to XSS if the HTML configuration originates from untrusted sources (e.g., `<img src="x" onerror="alert(1)">`).
*   **Proposed Solution:**
    ```javascript
    // Introduce a lightweight client-side sanitizer
    function sanitizeHTML(str) {
        var temp = document.createElement('div');
        temp.innerHTML = str;
        var scripts = temp.getElementsByTagName('script');
        for (var i = scripts.length - 1; i >= 0; i--) {
            scripts[i].parentNode.removeChild(scripts[i]);
        }
        // Iterate and remove inline event handlers (on*)
        var allElements = temp.getElementsByTagName("*");
        for (var i = 0, len = allElements.length; i < len; i++) {
            var el = allElements[i];
            for (var j = el.attributes.length - 1; j >= 0; j--) {
                if (el.attributes[j].name.toLowerCase().startsWith('on')) {
                    el.removeAttribute(el.attributes[j].name);
                }
            }
        }
        return temp.innerHTML;
    }

    if (hasInteraction && htmlContent) {
        infoContent.innerHTML = sanitizeHTML(htmlContent);
        infoPanel.classList.add('active');
    }
    ```
*   **Trade-off:** Adds minor processing overhead on the frontend and strips out legitimately intended scripts, slightly reducing functionality if developers wanted executable code inside tooltips.

**3. Logical Error: Misaligned Coordinate Parsing (Completed)**
*   **Location:** `src/sivo/svg/metadata.py`, Lines 62-63
*   **Assessment:** When calculating the bounding box for `polygon` or `polyline`, the code assumes the `points` array will always contain an even number of coordinates after regex parsing. If an SVG contains a malformed points string (e.g., an odd number of numbers), `xs` and `ys` will misalign, leading to mathematically skewed bounding box calculations.
*   **Proposed Solution:**
    ```python
        elif tag_name in ['polygon', 'polyline']:
            points_str = elem.get('points', '')
            coords = [float(p) for p in re.findall(r'[-+]?(?:\d*\.\d+|\d+)', points_str)]
            if len(coords) < 2:
                return None

            # Ensure an even number of coordinates to prevent misalignment
            if len(coords) % 2 != 0:
                coords = coords[:-1]

            xs = coords[0::2]
            ys = coords[1::2]
            return [min(xs), min(ys), max(xs), max(ys)]
    ```
*   **Trade-off:** Dropping a trailing orphaned coordinate changes strict parsing behavior in favor of fault tolerance. It ensures the application won't crash or generate corrupted spatial metadata.

---

### Phase 2: Refactoring & Optimization

**1. Performance: O(n) Mapping Bottleneck (Completed)**
*   **Location:** `src/sivo/core/infographic.py`, Lines 77-83 (`map` method)
*   **Assessment:** The `map` method performs a linear search `O(n)` over `self.elements` every time an element is mapped. When loading from a JSON configuration containing `m` mappings, this results in `O(n * m)` complexity, severely bottlenecking performance for complex SVGs with thousands of elements.
*   **Proposed Solution:**
    ```python
    # Inside __init__, build an O(1) lookup map
    def __init__(self, parser: SVGParser):
        self.parser = parser
        self.elements = self.parser.process_elements()
        self.mappings: Dict[str, InteractionMapping] = {}
        self._element_lookup: Dict[str, dict] = {}

        for elem in self.elements:
            self.mappings[elem['name']] = InteractionMapping(id=elem['id'])
            self._element_lookup[elem['id']] = elem
            self._element_lookup[elem['name']] = elem

    # Inside the map method, replace the loop:
    def map(self, element_id: str, ...):
        target_elem = self._element_lookup.get(element_id)
        if not target_elem:
            raise ValueError(f"Element with id/name '{element_id}' not found in SVG.")

        elem_name = target_elem['name']
        mapping = self.mappings[elem_name]
        # ... logic continues
    ```
*   **Trade-off:** Slightly increases memory usage due to the `_element_lookup` dictionary, but vastly improves computational speed from `O(n)` to `O(1)` per mapped element.

**2. Readability & Maintenance: Monolithic Logic (Completed)**
*   **Location:** `src/sivo/svg/metadata.py`, Lines 68-185 (`calculate_path_bbox` method)
*   **Assessment:** `calculate_path_bbox` is a massive, deeply nested function handling multiple SVG path commands within a single monolithic `while` loop. This violates the Single Responsibility Principle, making it difficult to maintain, read, or write targeted unit tests for specific SVG commands.
*   **Proposed Solution:**
    ```python
    class PathBBoxCalculator:
        def __init__(self):
            self.min_x = self.min_y = float('inf')
            self.max_x = self.max_y = float('-inf')
            self.curr_x = self.curr_y = 0.0

        def update_bounds(self, *coords):
            for i in range(0, len(coords), 2):
                x, y = coords[i], coords[i+1]
                self.min_x, self.max_x = min(self.min_x, x), max(self.max_x, x)
                self.min_y, self.max_y = min(self.min_y, y), max(self.max_y, y)

        def handle_M(self, x, y, is_relative):
            if is_relative:
                x += self.curr_x
                y += self.curr_y
            self.curr_x, self.curr_y = x, y
            self.update_bounds(x, y)

        # ... other handlers (handle_L, handle_C, etc.) ...

    def calculate_path_bbox(d_str: str) -> Optional[List[float]]:
        # Tokenize and pass to PathBBoxCalculator instance
        pass
    ```
*   **Trade-off:** Refactoring to a class or a dispatcher model introduces slight function call overhead, but drastically improves readability, maintainability, and testing isolation.

**3. Optimization: Arbitrary Cycle Prevention (Completed)**
*   **Location:** `src/sivo/svg/normalizer.py`, Lines 69-79 (`resolve_use_tags` method)
*   **Assessment:** The cycle detection logic for SVG `<use>` references relies on an arbitrary depth counter (`depth > 20`). This heuristic approach wastes CPU cycles on deep, legitimately nested trees while failing to explicitly catch true circular dependencies in an optimized manner.
*   **Proposed Solution:**
    ```python
    # Pass a specific visited_ids set alongside the queue items
    initial_uses = [(u, set()) for u in self.root.xpath('.//svg:use', namespaces=self.namespaces)]
    queue = collections.deque(initial_uses)

    while queue:
        use_elem, visited = queue.popleft()
        # ... fetch href ...
        ref_id = href[1:]

        if ref_id in visited:
            parent.remove(use_elem) # Cycle detected
            continue

        new_visited = visited.copy()
        new_visited.add(ref_id)

        # ... clone logic ...

        for new_use in new_uses:
            queue.append((new_use, new_visited))
    ```
*   **Trade-off:** Memory overhead increases marginally because each queue item maintains its own set of visited IDs. However, it provides guaranteed mathematical loop prevention.

---

### Phase 3: Strategic Expansion

**1. Programmatic Zoom & Pan API**
*   **Utility:** Currently, the ECharts implementation allows manual user panning (`roam: true`). Exposing an API method (e.g., `sivo_app.zoom_to("element_id")`) that calculates the target's metadata `bbox` and triggers ECharts' `dispatchAction` to automatically focus and center on a specific SVG region would be highly valuable for guided storytelling or presentation flows.

**2. Bi-directional Streamlit State Synchronization**
*   **Utility:** SIVO can send click callbacks to Streamlit via the V2 component, but it currently lacks a way for Streamlit to update the SVG state *without* initiating a full backend re-render. Implementing a JS frontend listener that accepts state mutations from Streamlit (e.g., changing colors dynamically based on live data feeds) would make the infographics truly reactive and real-time.

**3. HTML/DOM Overlay Positioning System**
*   **Utility:** Allow developers to define custom HTML overlays (like React-style tooltips or floating charts) that are absolutely positioned *over* specific SVG coordinates, derived from the Python bounding box metadata. This enables rich annotations and complex UI components that live outside the strict ECharts `<canvas>` bounds, significantly enhancing the visual capabilities of the framework.
