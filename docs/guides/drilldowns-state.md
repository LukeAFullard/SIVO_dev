---
Last Updated: 2026-04-09
SIVO Version: 1.0.0
---

# H-06: Drilldowns & State Management Plan

Managing the viewHistory stack and multi-level data dashboards.

## Table of Contents

1. **Understanding Drilldowns**
   - What is a drilldown view? (Navigating from a parent SVG to a child SVG/View).
2. **Configuring Multiple Views**
   - Adding secondary views using `Sivo.add_view()`.
   - Linking elements to views.
3. **The `viewHistory` Stack**
   - How SIVO manages navigation state in JavaScript.
   - Back button visibility logic.
   - Example JS context snippet:
     ```javascript
     // ECharts event handler for drilldown
     if (params.data.view) {
         viewHistory.push(currentViewId);
         renderView(params.data.view);
         updateBackButton();
     }
     ```
4. **State Restoration**
   - Resetting pan, zoom, and transforms on back navigation.
   - Firing ECharts `restore` actions.
5. **Complex Multi-Level Dashboards**
   - Structuring data for deep drilldowns.
