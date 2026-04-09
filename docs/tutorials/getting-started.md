---
Last Updated: 2026-04-09
SIVO Version: 1.0.0
---

# H-02: Getting Started Tutorial Plan

Step-by-step guide from pip install to rendering your first interactive SVG.

## Table of Contents

1. **Prerequisites**
   - Setting up a virtual environment.
   - Obtaining an initial SVG file.
2. **Installation and Setup**
   - `pip install sivo`
   - Checking installation.
3. **Loading an SVG**
   - Using `Sivo.from_svg()`
   - Using `Sivo.from_string()`
4. **Your First Interaction**
   - Adding a hover color and a tooltip.
   - Example snippet:
     ```python
     from sivo import Sivo
     sivo = Sivo.from_svg("diagram.svg")
     sivo.map(
         element_id="node_A",
         hover_color="#ff0000",
         tooltip="This is Node A"
     )
     sivo.save("output.html")
     ```
5. **Viewing the Output**
   - Opening the generated HTML file in a browser.
   - Understanding the zero-backend architecture.
6. **Next Steps**
   - Links to Core Concepts and Styling Guides.
