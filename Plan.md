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

## Infographic Class

Primary user-facing API.

```python
from sivo import Infographic

inf = Infographic.from_svg("campus.svg")

inf.map(
    "buildingA",
    tooltip="<h3>Building A</h3>",
    drill_to="buildingA.svg"
)
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
from sivo import Infographic

inf = Infographic.from_svg("factory.svg")

inf.map("machineA", tooltip="Machine A")

st.sivo(inf)
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
    infographic.py
    actions.py
    manifest.py

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
* [ ] metadata extraction
* [ ] bounding box calculation

## Phase 2 — Interaction System

Deliverables:

* Action classes
* manifest generator
* tooltip system
* hit detection

## Phase 3 — Frontend Runtime

Deliverables:

* JS runtime
* resize handling
* drill-down transitions
* event system

## Phase 4 — Streamlit Integration

Deliverables:

* Streamlit component
* example apps
* dynamic updates

## Phase 5 — CLI & Packaging

Deliverables:

* CLI tool
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
