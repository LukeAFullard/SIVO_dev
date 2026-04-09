---
Last Updated: 2026-04-09
SIVO Version: 0.1.0
---

# A-05: State Machine & Transition Spec

This document details the formal logic of the SIVO view state machine, interactive state tracking, and state transitions to ensure accurate code generation for AI agents.

## 1. The View Navigation State Machine

SIVO applications, particularly those utilizing the `SivoProject` for multi-level data dashboards, rely on a view navigation stack to manage state transitions between different views.

### `viewHistory` Array Structure and Logic
- The core state mechanism for view navigation is the `viewHistory` array.
- When transitioning to a new view (e.g., via a `DrillDownAction`), the current view ID is pushed onto the `viewHistory` stack.
- The stack operates on a standard push/pop LIFO (Last-In, First-Out) model.
- Example structure: `["main_view", "regional_view", "city_view"]`

### Push/Pop Transitions
- **Forward Navigation (Push):** When the user triggers a drill-down, `viewHistory.push(currentViewId)` is executed before updating the canvas.
- **Backward Navigation (Pop):** When the user clicks the "Back" button, `viewHistory.pop()` retrieves the previous view ID, which is then rendered. The back button's visibility is tied to `viewHistory.length > 0`.

## 2. State Restoration on Navigation

When navigating backward in SIVO's frontend templates (`echarts.html`), it is crucial to explicitly reset the ECharts canvas state.
- Dispatch a `'restore'` action to ECharts to clear pan and zoom states.
- Revert `zoom` and `layoutSize` properties in the series configuration.
- Failure to do this results in the previous view inheriting the transform state of the deeper view.

## 3. Interactive State Tracking

Certain interactions require maintaining state across clicks without triggering full view transitions.

### Toggle Image State Mechanics
- The `ToggleImageAction` cycles through a list of images on an element.
- This is typically tracked via a global or closure-scoped state dictionary, e.g., `window.sivoToggleImageState`.
- Example logic flow:
  ```javascript
  // Pseudocode for toggle image state logic
  let currentStateIdx = window.sivoToggleImageState[elementId] || 0;
  let nextStateIdx = (currentStateIdx + 1) % urls.length;
  window.sivoToggleImageState[elementId] = nextStateIdx;
  ```

### Note on `cycle_state`
- While `toggle_image` is implemented, a generic `cycle_state` feature (for mutating text labels or background area colors iteratively) is currently designated as a future enhancement and is not yet implemented. Do not generate code assuming `cycle_state` is a valid action.

## 4. Performance Implications

When generating JavaScript code for SIVO runtime interactions:
- **Avoid `setInterval` for UI updates.** Continuous polling or intervals can lead to memory leaks and UI stuttering, especially in complex SVG renderings.
- Use event-driven updates (e.g., clicking, hovering) or `requestAnimationFrame` for smooth animations where absolutely necessary.
- Clean up any event listeners or timeouts when elements are unmounted or views change.

## Drilldowns and State

For managing history stacks and multi-level data dashboards, refer to the [Drilldowns and State](../guides/drilldowns-state.md) guide.
