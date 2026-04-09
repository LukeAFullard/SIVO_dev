---
Last Updated: 2026-04-09
SIVO Version: 1.0.0
---

# A-03: SVG Engine Internals Plan

Explanation of the src/sivo/svg/ logic for AI-assisted path generation.

## Table of Contents

1. **SVG Parsing with lxml**
   - `src/sivo/svg/parser.py` implementation details.
   - XXE vulnerability protection (`etree.XMLParser(resolve_entities=False, no_network=True)`).
2. **Node Manipulation Constraints**
   - How ECharts/ZRender interprets SVG.
   - The `<text>` tag ID issue and SIVO's `name` attribute workaround.
3. **Programmatic Card Generation (`src/sivo/svg/card_generator.py`)**
   - Bounding box calculations.
   - `auto_shrink_font` mathematical logic for scaling text.
   - Example Python implementation detail:
     ```python
     # Concept used in card generation
     def calculate_width_at_y(radius, y_offset):
         # Math to prevent text overflow in circular cards
         pass
     ```
4. **Path Sanitization**
   - Removing `<script>` tags from imported SVGs.
