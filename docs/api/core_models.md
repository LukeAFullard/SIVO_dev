---
Last Updated: 2026-04-09
SIVO Version: 0.1.0
---

# Core Models API Reference

This document serves as an index and brief reference for every major class located in the `src/sivo/core/` directory. For detailed parameters and methods, please follow the links to the dedicated documentation files.

## High-Level APIs

These classes form the primary interfaces for users building applications with SIVO.

*   **`Sivo`** (`src/sivo/core/sivo.py`)
    *   The primary orchestrator class for interacting with a single SVG file or template.
    *   **Detailed Reference:** [Sivo Class Reference](sivo_class.md)
*   **`Infographic`** (`src/sivo/core/infographic.py`)
    *   The underlying core class that manages the SVG state, data bindings, and action mappings for a single `Sivo` instance.
    *   **Detailed Reference:** [Infographic Reference](infographic_api.md)
*   **`SivoDashboard`** (`src/sivo/core/dashboard.py`)
    *   Manages a responsive, multi-block CSS grid layout that can contain multiple `Sivo` instances and raw HTML blocks.
    *   **Detailed Reference:** [Dashboard & Project Reference](dashboard_project_api.md)
*   **`SivoProject`** (`src/sivo/core/project.py`)
    *   Manages multiple `Sivo` instances (views) to create multi-level, navigable applications via drilldowns without requiring a multi-block grid.
    *   **Detailed Reference:** [Dashboard & Project Reference](dashboard_project_api.md)

## Pydantic Models

SIVO uses Pydantic heavily to validate and structure the declarative configurations passed to the frontend runtime.

### Actions (`src/sivo/core/actions.py`)

These models define interactive behaviors bound to SVG elements. All actions inherit from `BaseAction`.

*   **`TooltipAction`**: Displays text or HTML on hover.
*   **`DrillDownAction`**: Navigates to a secondary view.
*   **`CallbackAction`**: Dispatches a custom JavaScript event on click.
*   **`URLAction`**: Opens a web link.
*   **`InteractionMapping`**: The container model that holds all assigned actions and visual overrides for a specific SVG element.
*   *(And many others: `VideoAction`, `AudioAction`, `FormAction`, `CompareAction`, etc.)*

**Detailed Reference:** [Actions Reference](actions_reference.md)

### Configurations (`src/sivo/core/config.py`)

These models define project-wide settings and data binding definitions.

*   **`ProjectConfig`**: Top-level configuration schema for defining a SIVO project from JSON/YAML.
*   **`ElementConfig`**: Represents a single element's declarative mappings within a project configuration.
*   **`DataBindingConfig`**: Specifies how quantitative data maps to element colors.
*   **`LiveBindingConfig`**: Configures WebSocket connections for live canvas updates.
*   **`ApiBindingConfig`**: Configures API polling.
*   **`ScrollytellingStepConfig` & `TourStepConfig`**: Models for narrative-driven presentations.
*   *(And others: `HexbinConfig`, `DotDensityConfig`, `ProportionalSymbolConfig`, etc.)*

**Detailed Reference:** [Config Reference](config_reference.md)
