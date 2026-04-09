---
Last Updated: 2026-04-09
SIVO Version: 1.0.0
---

# H-01: README.md (Project Hub) Documentation Plan

High-level value prop, installation, and 'Quick Start' visual gallery.

## Table of Contents

1. **Introduction to SIVO**
   - What is SIVO? (SVG Interactive Vector Objects)
   - Key Value Proposition (100% serverless, declarative Python API, AI-friendly)
2. **Installation**
   - Requirements (Python 3.8+)
   - `pip install sivo`
3. **Quick Start: Hello World**
   - Creating your first interactive SVG map.
   - Example Python snippet:
     ```python
     from sivo import Sivo
     # Quick start example
     sivo = Sivo.from_svg("map.svg")
     sivo.map("region1", color="blue", tooltip="Hello Region 1")
     sivo.save("interactive_map.html")
     ```
4. **Visual Gallery & Use Cases**
   - Screenshots of dashboards, interactive diagrams, and geocoded maps.
   - Link to `docs/examples/gallery.md`
5. **Project Architecture Map**
   - Brief diagram of Python core vs. JS runtime.
   - Links to AI docs (`docs/ai/manifest.md`) and Technical API (`docs/api/core_models.md`).
6. **Contributing & Community**
   - License (MIT)
   - Issue tracker and PR guidelines.
