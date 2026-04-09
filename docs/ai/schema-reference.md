---
Last Updated: 2026-04-09
SIVO Version: 0.1.0
---

# A-02: Pydantic Schema Reference

This document provides a deep dive into the Pydantic models used by SIVO, detailing how configuration and actions are structured, validated, and serialized for the frontend Javascript engine.

## 1. Core Configuration Models

The primary configuration models are located in `src/sivo/core/config.py`. SIVO uses strict validation to ensure that the data passed from Python exactly matches what the frontend Javascript expects.

*   **`SivoConfig`**: The root configuration object that holds all views and global settings.
*   **`ViewConfig`**: Represents a single interactive SVG canvas. It contains mappings and references to the raw SVG data.
*   **`ElementConfig`**: Represents the styling and interactive state mapped to a specific SVG element (e.g., an SVG `<path>` ID).

### Strict Validation Strategy (`model_config`)

All core SIVO Pydantic models utilize:

```python
model_config = ConfigDict(extra="forbid")
```

**Impact for Agents:**
When programmatically generating configuration dictionaries or kwargs for SIVO objects, you *must not* include undocumented or hallucinated arguments. If an argument is not explicitly defined in the Pydantic model (e.g., in `config.py` or `actions.py`), SIVO will crash immediately during instantiation with a validation error.

## 2. Action Models

Interactive behaviors are defined in `src/sivo/core/actions.py` as discrete Pydantic models. These are attached to an `ElementConfig`.

### `ToggleImageAction`

This action handles dynamic state transitions like cycling through images when a user clicks an SVG element.

*Note: The older concept of `cycle_state` is deprecated/unimplemented and agents should use `toggle_image` for state cycling.*

```python
class ToggleImageAction(BaseModel):
    image_urls: List[str]
    target_id: Optional[str] = None
    secondary_target_id: Optional[str] = None
    secondary_htmls: Optional[List[str]] = None

    model_config = ConfigDict(extra="forbid")
```

### Other Common Actions

*   **`DrillDownAction`**: Handles multi-level dashboards by linking an element to another registered view (`target_svg`).
*   **`TooltipAction`**: Displays hover text or HTML.
*   **`ClickAction`**: Triggers a JS callback event or payload.

*For full details on every action, inspect `src/sivo/core/actions.py`.*

## 3. Data Serialization for JS Bundle

The conversion from Python Pydantic models to Javascript occurs in `src/sivo/runtime/bundle_generator.py`.

### The `try...except` Serialization Block

When SIVO serializes mapping dictionaries, it wraps the process in a robust `try...except` block:

```python
for view_id, view in config.views.items():
    safe_mappings = {}
    for elem_id, elem_config in view.mappings.items():
        try:
            safe_mappings[elem_id] = elem_config.model_dump(exclude_none=True)
        except Exception as e:
            logger.warning(f"Failed to serialize mapping for {elem_id}: {e}")
            continue
    # ... bundle creation continues
```

**Impact for Agents:**
If malformed data or unexpected types somehow bypass initial Pydantic validation (e.g., through direct dict manipulation), the bundler will skip the corrupted mapping and log a warning rather than crashing the entire HTML bundle generation process. This ensures maximum resilience.

## 4. Agent Generation Guidelines

1.  **Always use defined Actions:** When configuring an element's interactivity via `sivo.map()`, use the explicit kwargs mapped to actions (e.g., `tooltip`, `drilldown_target`, `toggle_image_urls`). Do not invent parameters.
2.  **No `cycle_state`:** Remember that `cycle_state` is not a valid action. Use `toggle_image` for state cycles.
3.  **Inspect Source Files:** If unsure about a parameter name, read `src/sivo/core/config.py` or `src/sivo/core/actions.py` directly using your file reading tools. The Pydantic definitions are the ultimate source of truth.
