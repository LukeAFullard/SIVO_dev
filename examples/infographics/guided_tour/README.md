# Guided Tour Example

This example demonstrates how to create a step-by-step guided tour of an interactive SVG vector object using SIVO. Guided tours are useful for onboarding users or explaining different parts of an infographic or dashboard in a sequence.

## Overview

The script `main.py` defines a simple interactive map of a museum with three rooms: an Art Gallery, a Cafe, and a Gift Shop. It maps interaction content to each room, and configures a guided tour that walks the user through them.

### Key Features Showcased
- `Sivo.from_string()`: Loading an SVG vector map directly from a Python string.
- `sivo_app.map()`: Adding interactive content (`html`) to each mapped element, which is displayed in the side panel when the element is clicked.
- `sivo_app.bind_tour()`: Binding a sequence of steps to the application.
  - Each step defines HTML `content` explaining the step.
  - Optionally configures an element ID to `zoom_to` and a `zoom_level`.
  - Optionally configures `show_tooltips` to automatically trigger interactions for certain elements during the step.

## Relevant Code

```python
# Map interactive panels for elements
sivo_app.map("gallery", html="<h2>Main Art Gallery</h2><p>Featuring modern artists.</p>")
sivo_app.map("cafe", html="<h2>Museum Cafe</h2><p>Coffee and pastries.</p>")
sivo_app.map("giftshop", html="<h2>Gift Shop</h2><p>Souvenirs and books.</p>")

# Define Guided Tour Steps
steps = [
    {
        "content": "<h3>Welcome to the Museum Tour</h3><p>We'll guide you through the main exhibits. Click <b>Next</b> to begin.</p>",
    },
    {
        "content": "<h3>1. Art Gallery</h3><p>First stop: the main exhibition hall.</p>",
        "zoom_to": "gallery",
        "zoom_level": 2.5,
        "show_tooltips": ["gallery"]
    },
    # ... more steps
]

# Bind the tour
sivo_app.bind_tour(steps)
```

## Running the Example

Run the `main.py` script to regenerate the interactive HTML output:

```bash
PYTHONPATH=src python examples/infographics/guided_tour/main.py
```

This will output `guided_tour.html` in the current directory, which you can open in your web browser to interact with the tour.
