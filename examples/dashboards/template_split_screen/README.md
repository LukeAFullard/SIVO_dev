# Split Screen Template Example

This example demonstrates how to use the `split_screen.html` dashboard template. The template provides a dual-pane layout that is perfect for side-by-side comparisons of maps or charts.

## Usage

```python
from sivo.core.dashboard import SivoDashboard
# ...
dashboard = SivoDashboard(title="Comparison Dashboard", columns=2, template="split_screen")
dashboard.add_sivo_block("left_view", left_map, slot="left")
dashboard.add_sivo_block("right_view", right_map, slot="right")
```
