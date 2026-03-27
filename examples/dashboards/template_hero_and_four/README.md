# Hero and Four Template Example

This example demonstrates how to use the `hero_and_four.html` dashboard template. The template provides a 2-column layout where the left column contains a single large "hero" component (enforced to be a square aspect ratio), and the right column contains a 2x2 grid of smaller components (also forming a square in total).

## Usage

```python
from sivo.core.dashboard import SivoDashboard
# ...
dashboard = SivoDashboard(title="Executive Summary", template="hero_and_four")
# Adding to the large left column
dashboard.add_sivo_block("primary_focus", main_map, slot="hero")
# Adding to the 2x2 right grid (no slot specified)
dashboard.add_metrics_panel("q1_metrics", title="Revenue", metrics=["revenue", "growth"])
# ... add 3 more blocks
```
