---
Last Updated: 2026-04-09
SIVO Version: 1.0.0
---

# H-07: Example Gallery Plan

A curated list of .py scripts with corresponding screenshots/descriptions.

## Table of Contents

1. **Gallery Overview**
   - How to run these examples locally.
2. **Example 1: Interactive US Map**
   - Description: A geocoded map highlighting state data.
   - Link to source code / Snippet:
     ```python
     sivo = Sivo.from_svg("us_map.svg")
     sivo.map("CA", color="#ffcc00", tooltip="California: 39M")
     ```
3. **Example 2: IT Infrastructure Diagram**
   - Description: Network topology with drilldowns into server racks.
4. **Example 3: Serverless Dashboard**
   - Description: Multi-block dashboard using `dashboard_blocks.html`.
5. **Example 4: Image Toggling & Media**
   - Description: Using `toggle_image` to switch states in a home automation SVG.
6. **Running the Examples**
   - `python run_examples.py` instructions.
