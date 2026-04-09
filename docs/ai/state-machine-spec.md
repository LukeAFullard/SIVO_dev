---
Last Updated: 2026-04-09
SIVO Version: 1.0.0
---

# A-05: State Machine & Transition Spec Plan

Formal logic of the viewHistory and state transitions for code-gen accuracy.

## Table of Contents

1. **The View Navigation State Machine**
   - `viewHistory` array structure and logic.
   - Push/Pop transitions.
2. **State Restoration on Navigation**
   - Restoring ECharts canvas state (zoom/pan) via `'restore'` actions.
3. **Interactive State Tracking**
   - `window.sivoToggleImageState` object logic.
   - `cycle_state` mutation mechanics (e.g., updating `<text>` labels vs. background area colors).
   - Example logic flow:
     ```javascript
     // Pseudocode for toggle image state logic
     let currentStateIdx = window.sivoToggleImageState[elementId] || 0;
     let nextStateIdx = (currentStateIdx + 1) % urls.length;
     window.sivoToggleImageState[elementId] = nextStateIdx;
     ```
4. **Performance Implications**
   - Why SIVO avoids `setInterval` for UI updates to prevent memory leaks.
