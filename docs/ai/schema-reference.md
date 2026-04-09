---
Last Updated: 2026-04-09
SIVO Version: 1.0.0
---

# A-02: Pydantic Schema Reference Plan

Deep dive into Pydantic models; detailed I/O for bundle_generator.py.

## Table of Contents

1. **Core Configuration Models (`src/sivo/core/models.py`)**
   - `SivoConfig`, `ViewConfig`, `ElementConfig`.
   - Explanation of `model_config = ConfigDict(extra="forbid")` and its impact on generated kwargs.
2. **Action Models**
   - Schema for `cycle_state` actions.
   - Schema for `toggle_image` actions.
   - Example Schema Snippet:
     ```python
     class ToggleImageAction(BaseModel):
         image_urls: List[str]
         target_id: Optional[str] = None
         secondary_target_id: Optional[str] = None
         secondary_htmls: Optional[List[str]] = None
     ```
3. **Data Serialization for JS Bundle**
   - How models are converted to dicts in `bundle_generator.py`.
   - Handling `try...except` for corrupt mapping data.
4. **Agent Generation Guidelines**
   - Rules for LLMs when generating configurations to ensure they pass strict validation.
