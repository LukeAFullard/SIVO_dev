# SIVO Codebase Review & Audit Report

## Phase 1: Debugging & Security Audit

**1. Security Risk: Cross-Site Scripting (XSS) via Inline JSON Serialization**
* **Location:** `src/sivo/runtime/bundle_generator.py`, Lines 131-132
* **Assessment:** The application injects Python objects directly into an inline JavaScript variable using `json.dumps(formatted_views)` inside a Jinja template. If any tooltips, custom HTML content, or string parameters contain the `</script>` string, it will break out of the script context and execute arbitrary JavaScript, bypassing the shadow DOM sanitization completely. This is a classic XSS vulnerability when mixing JSON inside HTML `<script>` blocks.
* **Proposed Solution:**
  ```python
  html_output = template.render(
      views_data=json.dumps(formatted_views).replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026"),
      initial_view=json.dumps(initial_view).replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026"),
      custom_css=custom_css,
      custom_js=custom_js
  )
  ```
* **Trade-off:** This change introduces negligible string processing overhead but is imperative to secure against XSS. It does not alter the API contract.

**2. Logical Error: Dropping Exponential Numbers in Polygon Coordinates**
* **Location:** `src/sivo/svg/metadata.py`, Line 46
* **Assessment:** While path parsing (`parse_coord` and `calculate_path_bbox`) accounts for exponential coordinate formats, the polygon/polyline parsing uses a simpler regex `r'[-+]?(?:\d*\.\d+|\d+)'` which completely truncates exponents (e.g. `1e3` becomes `1`), resulting in distorted or microscopic bounding boxes for polygons rendered by design software exporting exponential notation.
* **Proposed Solution:**
  ```python
          elif tag_name in ['polygon', 'polyline']:
              points_str = elem.get('points', '')
              # Extract all numbers from points string, accounting for exponential notation
              coords = [float(p) for p in re.findall(r'[-+]?(?:\d*\.\d+|\d+)(?:[eE][-+]?\d+)?', points_str)]
              if len(coords) < 2:
                  return None
  ```
* **Trade-off:** Minor regex performance hit due to an extra optional non-capturing group.

## Phase 2: Refactoring & Optimization

**1. Modularity: Type Safety in Pydantic Action Models**
* **Location:** `src/sivo/core/actions.py`
* **Assessment:** The `InteractionMapping` class uses `actions: list[BaseAction]`. However, due to Pydantic's serialization mechanisms, using a base class without a discriminator can cause attributes of inherited classes to be stripped out during `.model_dump()`.
* **Proposed Solution:**
  Change the type to a Discriminated Union:
  ```python
  from typing import Union, Annotated
  ActionType = Annotated[Union[TooltipAction, URLAction, DrillDownAction, CallbackAction, HoverCallbackAction], Field(discriminator='action_type')]
  class InteractionMapping(BaseModel):
      id: str
      actions: list[ActionType] = Field(default_factory=list)
  ```
* **Trade-off:** Requires explicit declaration of all possible subclass action types but massively improves Pydantic's schema validation, serialization, and typing support.

## Phase 3: Strategic Expansion

**1. Data-Driven Theming (Choropleth Generation)**
* **Proposal:** Introduce an integration allowing developers to pass a Pandas DataFrame mapping element IDs to numerical values alongside a color scale (e.g., `matplotlib.colormaps` or simple linear interpolation).
* **Utility:** Automates the creation of heatmaps or geographic density maps without forcing the user to manually compute `map(id, color=...)` in a loop.

**2. Auto-Generated Interactive Legends**
* **Proposal:** Generate a color scale legend automatically when `apply_choropleth` is called, displaying the `min_color` and `max_color` alongside their corresponding minimum and maximum values.
* **Utility:** Saves developers from manually writing HTML overlays to explain heatmap scales on their infographics.

**3. Animation API**
* **Proposal:** Introduce an `animation` parameter to SIVO's mapping API, appending standard CSS keyframes (e.g. `pulse`, `fade`) to mapped elements.
* **Utility:** Provides an easy way to highlight critical statuses or active elements on an interactive map.

**4. Built-in Zoom UI Controls**
* **Proposal:** Update the `echarts.html` template to include visible `[ + ]`, `[ - ]`, and `[ Reset ]` buttons overlaying the canvas, providing explicit controls for zooming and panning the map via ECharts API.
* **Utility:** Explicit zoom controls greatly improve the user experience for users who lack scroll wheels or on devices with touchpads.

**5. Dynamic Annotations & Markers**
* **Proposal:** Add an `add_marker` convenience API in Sivo that drops an HTML overlay pin/marker exactly at the computed bounding box center of an SVG element.
* **Utility:** Allows developers to programmatically drop markers ("📍 You are here", etc.) on SVGs dynamically without editing the SVG payload manually.
