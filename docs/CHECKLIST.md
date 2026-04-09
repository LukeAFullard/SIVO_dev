---
Last Updated: 2026-04-09
SIVO Version: 0.1.0
---

# SIVO Documentation Progress Checklist

Below is the detailed checklist to track the development of the SIVO documentation suite.

## 🟢 Pillar 1: Human-Centric Documentation (The "Learning" Path)
*Focus: Readability, Tutorials, and Mental Models.*

| Status | Task ID | Documentation Component | Description / Requirements |
|---|---|---|---|
| [x] | H-01 | `docs/README.md` (Project Hub) | High-level value prop, installation, and "Quick Start" visual gallery. |
| [x] | H-02 | `docs/tutorials/getting-started.md` | Step-by-step guide from pip install to rendering your first interactive SVG. |
| [x] | H-03 | `docs/guides/core-concepts.md` | Explaining the "Bridge": How Python objects become interactive frontend elements. |
| [x] | H-04 | `docs/guides/styling-and-layout.md` | Comprehensive guide on SVG attributes, CSS injection, and layout containers. |
| [x] | H-05 | `docs/guides/interactivity-events.md` | How to use Python callbacks, tooltips, and click events. Include JS snippets. |
| [x] | H-06 | `docs/guides/drilldowns-state.md` | Managing the viewHistory stack and multi-level data dashboards. |
| [x] | H-07 | `docs/examples/gallery.md` | A curated list of .py scripts with corresponding screenshots/descriptions. |
| [x] | H-08 | `docs/reference/troubleshooting.md` | Common errors (e.g., Pydantic validation failures, SVG path clipping). |
| [x] | H-09 | `docs/guides/dashboards.md` | Building multi-block interactive dashboards with CSS Grid Builder. |
| [x] | H-10 | `docs/guides/streamlit-integration.md` | How to use SIVO inside Streamlit applications. |
| [x] | H-11 | `docs/guides/serverless-web-apps.md` | Guide on using SIVO with Pyodide and WebAssembly for 100% serverless apps. |
| [x] | H-12 | `docs/guides/cli-tools.md` | Using SIVO's command-line interface for init, validation, export, and annotation. |
| [x] | H-13 | `docs/guides/charts-and-graphs.md` | Guide on embedding native ECharts (bar, line, pie, scatter, etc.) into SIVO maps. |
| [ ] | H-14 | `docs/guides/advanced-mapping.md` | Guide on advanced thematic mapping: choropleths, hexbins, dot density, flow maps, and geocoding via Mapbox/Google. |
| [ ] | H-15 | `docs/guides/live-data-and-animations.md` | Connecting SIVO to live API endpoints, WebSockets, and timeline animations. |
| [ ] | H-16 | `docs/guides/dynamic-ui-elements.md` | Programmatically adding UI layers: cards, progress bars, markers, image overlays, and scalable text. |
| [ ] | H-17 | `docs/guides/scrollytelling-and-tours.md` | Building narrative-driven data presentations using `bind_scrollytelling` and `bind_tour`. |
| [ ] | H-18 | `docs/guides/built-in-templates.md` | Guide on using the built-in aspect-ratio based SVG templates (1_1, 16_10, 3_2, etc.) and filling zones. |
| [ ] | H-19 | `docs/guides/multimedia-advanced-actions.md` | Using Video, Audio, CycleState, Explode, and other advanced actions. |
| [ ] | H-20 | `docs/guides/security-and-offline.md` | Best practices for CSP, DOMPurify, running offline, and mitigating vulnerabilities. |
| [ ] | H-21 | `docs/guides/accessibility.md` | Best practices for making SIVO maps and dashboards accessible (WCAG, ARIA, high contrast). |
| [ ] | H-22 | `docs/guides/external-integrations.md` | Guide on integrating external services (Ecommerce, BI tools, Replit, Forms). |
| [ ] | H-23 | `docs/guides/multi-view-projects.md` | Organizing complex applications with `SivoProject` and multiple interconnected views. |
| [ ] | H-24 | `docs/guides/infographics.md` | Building static and dynamic data visualizations using the `Infographic` class. |

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
| [ ] | A-07 | `docs/ai/testing-guidelines.md` | Testing strategies for Playwright and WASM/Pyodide constraints for AI test generation. |

## 🟠 Pillar 3: Technical API Reference (Common Foundation)
*Focus: Complete functional coverage of the codebase.*

| Status | Task ID | Documentation Component | Description / Requirements |
|---|---|---|---|
| [ ] | T-01 | `docs/api/sivo_class.md` | Comprehensive API reference for the main `Sivo` class (`src/sivo/core/sivo.py`). |
| [ ] | T-01a| `docs/api/actions_reference.md` | Complete reference for all action models (e.g., TooltipAction, VideoAction) in `src/sivo/core/actions.py`. |
| [ ] | T-01b| `docs/api/config_reference.md` | Complete reference for all configuration models (e.g., HexbinConfig, LiveBindingConfig) in `src/sivo/core/config.py`. |
| [ ] | T-01c| `docs/api/dashboard_project_api.md` | API reference for `SivoDashboard` and `SivoProject` classes. |
| [ ] | T-01d| `docs/api/infographic_api.md` | API reference for the `Infographic` class (`src/sivo/core/infographic.py`). |
| [ ] | T-01e| `docs/api/core_models.md` | Reference for every class in src/sivo/core/. |
| [ ] | T-02 | `docs/api/svg_processor.md` | Reference for path manipulation, coordinate transforms, and lxml integration. |
| [ ] | T-03 | `docs/api/template_engine.md` | Documentation for Jinja2 templates and how data is injected into HTML/JS. |
| [ ] | T-04 | `docs/api/export_formats.md` | Specs for PDF (jsPDF), Image, and JSON exports. |
| [ ] | T-05 | `docs/api/streamlit_component.md` | API Reference for Streamlit SIVO component. |
| [ ] | T-06 | `docs/api/cli_reference.md` | API Reference for SIVO command line tools. |
| [ ] | T-07 | `docs/api/template_catalog.md` | Comprehensive list and reference of all provided SVG templates. |
| [ ] | T-08 | `docs/api/developer_contributing.md` | Guidelines for running tests (pytest, Playwright) and managing dependencies. |
| [ ] | T-09 | `docs/api/annotator_server.md` | API and architecture reference for the local Annotator HTTP server (`src/sivo/cli/tools/annotator.py`). |

## 🛠️ Documentation Infrastructure Tasks

* [ ] **Cross-Linking:** Ensure all AI docs link to Human tutorials for context and vice-versa.
* [ ] **Validation:** Run a "Link Checker" to ensure no broken relative paths between .md files.
* [ ] **Snippet Testing:** Verify that every code snippet in the docs runs against the current SIVO version.
* [x] **Version Header:** Every file should include a Last Updated and SIVO Version metadata header. (Implemented in plans)
