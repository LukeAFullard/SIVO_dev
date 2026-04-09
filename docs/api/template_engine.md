---
Last Updated: 2026-04-09
SIVO Version: 1.0.0
---

# T-03: Template Engine API Reference Plan

Documentation for Jinja2 templates and how data is injected into HTML/JS.

## Table of Contents

1. **Bundle Generator (`src/sivo/runtime/bundle_generator.py`)**
   - `generate_html_bundle()`: Parameters and return types.
   - The JSON sanitization pipeline for injection.
2. **Jinja2 Template Context**
   - Variables exposed to templates (e.g., `sivo_json`, `svg_content`, `global_css`).
3. **Template Directory Structure (`src/sivo/runtime/templates/`)**
   - `echarts.html`: Single-view runtime template.
   - `dashboard_blocks.html`: Multi-block layout template.
   - Differences in data injection requirements for each.
