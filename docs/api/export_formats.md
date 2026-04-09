---
Last Updated: 2026-04-09
SIVO Version: 1.0.0
---

# T-04: Export Formats API Reference Plan

Specs for PDF (jsPDF), Image, and JSON exports.

## Table of Contents

1. **HTML Export (`sivo.save()`)**
   - Structure of the standalone HTML file.
2. **Image Export**
   - Client-side canvas exporting via ECharts `getDataURL()`.
   - Server-side screenshotting approaches (if applicable, referencing Playwright scripts).
3. **JSON State Serialization**
   - How `annotator.html` exports and imports project state.
   - Structure of the saved JSON project file.
4. **Future/Planned Formats**
   - jsPDF integration specs.
