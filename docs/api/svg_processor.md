---
Last Updated: 2026-04-09
SIVO Version: 1.0.0
---

# T-02: SVG Processor API Reference Plan

Reference for path manipulation, coordinate transforms, and lxml integration.

## Table of Contents

1. **SVG Parsing Utilities (`src/sivo/svg/parser.py`)**
   - `load_svg_tree()`: Safe parsing logic.
   - `extract_element_by_id()`: Node retrieval.
2. **Coordinate & Transform Handlers**
   - Functions for dealing with SVG coordinate space.
   - Bounding box extraction logic used for card placement.
3. **Card Generator Module (`src/sivo/svg/card_generator.py`)**
   - `generate_card_svg()`: Full signature and shape options ('rect', 'circle', 'pill', etc.).
   - Text scaling utilities.
4. **Security Filters**
   - Node sanitization functions applied during processing.
