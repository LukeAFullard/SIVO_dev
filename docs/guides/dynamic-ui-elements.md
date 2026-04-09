---
Last Updated: 2026-04-09
SIVO Version: 1.0.0
---

# H-16: Dynamic UI Elements Guide Plan

Programmatically adding UI layers: cards, progress bars, markers, image overlays, and scalable text.

## Table of Contents

1. **Introduction to UI Elements**
   - Injecting dynamic elements into an existing SVG canvas.
2. **Cards and Text**
   - Using `add_card()` for contextual information panels.
   - Injecting auto-scaling text with `add_scalable_text()` and `fill_template_zone()`.
3. **Overlays and Markers**
   - Injecting custom HTML overlays (`add_overlay()`).
   - Pinning markers (`add_marker()`).
4. **Images and Clipping**
   - Adding images (`add_image_overlay()`).
   - Masking and clipping with `clip_html_to_shape()` and `clip_image_to_shape()`.
5. **Progress Bars**
   - Injecting visual indicators with `add_scalable_progress_bar()`.
