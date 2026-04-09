# SIVO Documentation Progress Checklist

Below is the detailed checklist to track the development of the SIVO documentation suite.

## 🟢 Pillar 1: Human-Centric Documentation (The "Learning" Path)
*Focus: Readability, Tutorials, and Mental Models.*

| Status | Task ID | Documentation Component | Description / Requirements |
|---|---|---|---|
| [ ] | H-01 | `docs/README.md` (Project Hub) | High-level value prop, installation, and "Quick Start" visual gallery. |
| [ ] | H-02 | `docs/tutorials/getting-started.md` | Step-by-step guide from pip install to rendering your first interactive SVG. |
| [ ] | H-03 | `docs/guides/core-concepts.md` | Explaining the "Bridge": How Python objects become interactive frontend elements. |
| [ ] | H-04 | `docs/guides/styling-and-layout.md` | Comprehensive guide on SVG attributes, CSS injection, and layout containers. |
| [ ] | H-05 | `docs/guides/interactivity-events.md` | How to use Python callbacks, tooltips, and click events. Include JS snippets. |
| [ ] | H-06 | `docs/guides/drilldowns-state.md` | Managing the viewHistory stack and multi-level data dashboards. |
| [ ] | H-07 | `docs/examples/gallery.md` | A curated list of .py scripts with corresponding screenshots/descriptions. |
| [ ] | H-08 | `docs/reference/troubleshooting.md` | Common errors (e.g., Pydantic validation failures, SVG path clipping). |
| [ ] | H-09 | `docs/guides/dashboards.md` | Building multi-block interactive dashboards with CSS Grid Builder. |
| [ ] | H-10 | `docs/guides/streamlit-integration.md` | How to use SIVO inside Streamlit applications. |
| [ ] | H-11 | `docs/guides/serverless-web-apps.md` | Guide on using SIVO with Pyodide and WebAssembly for 100% serverless apps. |
| [ ] | H-12 | `docs/guides/cli-tools.md` | Using SIVO's command-line interface for init, validation, export, and annotation. |
| [ ] | H-13 | `docs/guides/charts-and-graphs.md` | Guide on embedding native ECharts (bar, line, pie, scatter, etc.) into SIVO maps. |
| [ ] | H-14 | `docs/guides/advanced-mapping.md` | Guide on advanced thematic mapping: choropleths, hexbins, dot density, and flow maps. |
| [ ] | H-15 | `docs/guides/live-data-and-animations.md` | Connecting SIVO to live API endpoints, WebSockets, and timeline animations. |
| [ ] | H-16 | `docs/guides/dynamic-ui-elements.md` | Programmatically adding UI layers: cards, progress bars, markers, image overlays, and scalable text. |
| [ ] | H-17 | `docs/guides/scrollytelling-and-tours.md` | Building narrative-driven data presentations using `bind_scrollytelling` and `bind_tour`. |

## 🔵 Pillar 2: AI-Agent Documentation (The "Context" Path)
*Focus: Schema definitions, API signatures, and prompt-injection readiness.*

| Status | Task ID | Documentation Component | Description / Requirements |
|---|---|---|---|
| [ ] | A-01 | `docs/ai/manifest.md` | A "Map" for AI agents to understand the repository structure and entry points. |
| [ ] | A-02 | `docs/ai/schema-reference.md` | Deep dive into Pydantic models; detailed I/O for bundle_generator.py. |
| [ ] | A-03 | `docs/ai/svg-logic-internals.md` | Explanation of the src/sivo/svg/ logic for AI-assisted path generation. |
| [ ] | A-04 | `docs/ai/runtime-api.md` | Detailed technical spec of the JS runtime (echarts.html, dashboard_blocks.html). |
| [ ] | A-05 | `docs/ai/state-machine-spec.md` | Formal logic of the viewHistory and state transitions for code-gen accuracy. |
| [ ] | A-06 | `docs/ai/security-protocols.md` | Strict rules on DOMPurify usage and sanitization to ensure AI doesn't generate unsafe code. |

## 🟠 Pillar 3: Technical API Reference (Common Foundation)
*Focus: Complete functional coverage of the codebase.*

| Status | Task ID | Documentation Component | Description / Requirements |
|---|---|---|---|
| [ ] | T-01 | `docs/api/core_models.md` | Reference for every class in src/sivo/core/. |
| [ ] | T-02 | `docs/api/svg_processor.md` | Reference for path manipulation, coordinate transforms, and lxml integration. |
| [ ] | T-03 | `docs/api/template_engine.md` | Documentation for Jinja2 templates and how data is injected into HTML/JS. |
| [ ] | T-04 | `docs/api/export_formats.md` | Specs for PDF (jsPDF), Image, and JSON exports. |
| [ ] | T-05 | `docs/api/streamlit_component.md` | API Reference for Streamlit SIVO component. |
| [ ] | T-06 | `docs/api/cli_reference.md` | API Reference for SIVO command line tools. |

## 🛠️ Documentation Infrastructure Tasks

* [ ] **Cross-Linking:** Ensure all AI docs link to Human tutorials for context and vice-versa.
* [ ] **Validation:** Run a "Link Checker" to ensure no broken relative paths between .md files.
* [ ] **Snippet Testing:** Verify that every code snippet in the docs runs against the current SIVO version.
* [x] **Version Header:** Every file should include a Last Updated and SIVO Version metadata header. (Implemented in plans)
