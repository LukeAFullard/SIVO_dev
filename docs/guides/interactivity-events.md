---
Last Updated: 2026-04-09
SIVO Version: 1.0.0
---

# H-05: Interactivity & Events Guide Plan

How to use Python callbacks, tooltips, and click events. Include JS snippets.

## Table of Contents

1. **Tooltips and Hover Effects**
   - Basic `tooltip=...` usage.
   - Advanced tooltip formatting.
2. **Click Events & The Sidebar Panel**
   - Enabling the sidebar (`panel_position="right"`).
   - Injecting HTML content on click.
3. **Dynamic State Transitions (`cycle_state`)**
   - Updating multiple properties on click.
   - Example Python snippet:
     ```python
     sivo.map(
         "button1",
         cycle_state=[
             {"target_id": {"color": "green", "text": "ON"}},
             {"target_id": {"color": "red", "text": "OFF"}}
         ]
     )
     ```
4. **Audio Playback on Event**
   - Triggering audio and handling browser autoplay policies.
   - JS Snippet reference:
     ```javascript
     // Internal SIVO runtime handling audio
     audio.play().catch(e => console.warn('Autoplay blocked:', e));
     ```
5. **Form Events and External Callbacks**
   - Integrating with external JS systems or iframe parents.
