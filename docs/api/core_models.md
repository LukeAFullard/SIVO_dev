---
Last Updated: 2026-04-09
SIVO Version: 1.0.0
---

# T-01: Core Models API Reference Plan

Reference for every class in src/sivo/core/.

## Table of Contents

1. **`Sivo` Main Class (`src/sivo/core/infographic.py`)**
   - `__init__` arguments.
   - `from_svg()`, `from_string()` factory methods.
   - `map()` method parameters and usage.
   - `add_view()`, `add_card()` signatures.
   - `save()`, `to_html()` methods.
2. **Pydantic Data Models (`src/sivo/core/models.py`)**
   - Detailed specification of all configuration models.
   - `SivoConfig`, `ViewConfig`, `ElementConfig`.
   - Interaction Action models (`CycleStateAction`, etc.).
3. **Internal Helpers**
   - Utility functions used within the core logic.
