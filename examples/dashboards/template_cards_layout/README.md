# Cards Layout Template Example

This example demonstrates how to use the `cards_layout.html` dashboard template. The template provides a responsive, grid-based layout where dashboard components are presented as standalone cards.

## Usage

```python
from sivo.core.dashboard import SivoDashboard
# ...
dashboard = SivoDashboard(title="Modular Cards Dashboard", template="cards_layout")
dashboard.add_sivo_block("geographic_overview", map_view, col_span=2)
```
