---
Last Updated: 2026-04-09
SIVO Version: 1.0.0
---

# H-03: Core Concepts Plan

Explaining the 'Bridge': How Python objects become interactive frontend elements.

## Table of Contents

1. **The SIVO Philosophy**
   - Declarative data-binding to SVG shapes.
   - No backend required.
2. **The Lifecycle of a SIVO Object**
   - **Step 1: Ingestion** - Parsing SVG via lxml.
   - **Step 2: Configuration** - Building Pydantic `SivoConfig` state.
   - **Step 3: Bundling** - Compiling Jinja2 templates (`bundle_generator.py`).
   - **Step 4: Runtime** - Rendering in the browser with ECharts.
3. **Pydantic Model Integration**
   - How Python types map to JS logic.
   - Example mapping model:
     ```python
     class ElementConfig(BaseModel):
         id: str
         tooltip: Optional[str] = None
         hover_color: Optional[str] = None
         # Strict validation prevents malformed configs
         model_config = ConfigDict(extra="forbid")
     ```
4. **State Management in Python vs JS**
   - Static generation vs. runtime interactions (like `cycle_state`).
5. **Sanitization and Security boundary**
   - Mentioning DOMPurify and safe HTML injection.
