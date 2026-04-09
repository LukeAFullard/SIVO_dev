---
Last Updated: 2026-04-09
SIVO Version: 0.1.0
---

# H-02: Getting Started Tutorial

Welcome to SIVO! This guide will walk you through the process of turning a static SVG file into an interactive web application from scratch. We will cover installation, loading your first SVG, adding interactivity, and viewing the result.

## 1. Prerequisites

Before starting, make sure you have Python 3.8 or newer installed. It's recommended to set up a virtual environment for your project:

```bash
# Create a virtual environment (do this in your terminal)
# python -m venv venv

# Activate it
# On Windows:
# venv\Scripts\activate
# On macOS/Linux:
# source venv/bin/activate
```

You'll also need a basic SVG file. You can download one, export one from a tool like Figma or Illustrator, or create a simple one:

```xml
<!-- Save this as diagram.svg -->
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <rect id="node_A" x="50" y="50" width="100" height="100" fill="#cccccc" />
</svg>
```

Ensure the elements you want to interact with have an `id` attribute (like `id="node_A"` in the example above).

## 2. Installation and Setup

Install the SIVO framework using `pip`:

```bash
pip install sivo
```

To verify the installation, you can run a quick check in your terminal:

```bash
python -c "import sivo; print(sivo.__version__)"
```

*(Note: In the current version 0.1.0, this should execute without errors if installed correctly.)*

## 3. Loading an SVG

SIVO needs to read your SVG file to begin working its magic. There are a few ways to do this, but the most common is using `Sivo.from_svg()`.

Create a Python script named `app.py`:

```python
from sivo import Sivo

# Load the SVG file
sivo_app = Sivo.from_svg("diagram.svg")
```

Alternatively, if you already have the SVG content as a string in memory, you can use `Sivo.from_string()`:

```python
svg_content = '<svg width="200" height="200"><rect id="node_A" width="100" height="100"/></svg>'
sivo_app = Sivo.from_string(svg_content)
```

## 4. Your First Interaction

The core of SIVO's power lies in the `.map()` method. You use it to connect Python configurations to the `id` of an SVG element. Let's add a hover color and a tooltip to our rectangle.

Add the following to your `app.py`:

```python
from sivo import Sivo

# 1. Initialize Sivo from the SVG
sivo_app = Sivo.from_svg("diagram.svg")

# 2. Map interactions to an element
sivo_app.map(
    element_id="node_A",
    color="#ff0000",           # Changes the static color to red
    hover_color="#00ff00",     # Changes color to green when hovered
    tooltip="This is Node A!"  # Displays a tooltip on hover
)

# 3. Export the result to a standalone HTML file
sivo_app.to_html("output.html")
```

## 5. Viewing the Output

Run your Python script:

```bash
python app.py
```

This will generate a file named `output.html` in the same directory.

Open `output.html` in your web browser. You don't need a server to view it; SIVO's zero-backend architecture means the generated HTML contains all the necessary HTML, CSS, and JavaScript (powered by ECharts under the hood) to render the interactive map.

Hover over the rectangle—you should see it turn green and display "This is Node A!".

## 6. Next Steps

Congratulations! You've built your first interactive SVG application with SIVO.

From here, you can explore more advanced features:
- **[Core Concepts](../guides/core-concepts.md)**: Understand the architecture and how Python objects translate to frontend elements.
- **[Styling and Layout](../guides/styling-and-layout.md)**: Learn how to control the look and feel of your interactive maps.
- **[Visual Gallery](../examples/gallery.md)**: See what's possible with SIVO and grab some inspiration.
