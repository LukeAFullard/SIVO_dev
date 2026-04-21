# Forms Integration Example

This example demonstrates how to integrate native HTML forms within a SIVO application using the `form_fields` argument of the `Sivo.map()` method.

## Purpose

The `forms` example shows how you can bind a form overlay to an SVG element click. In this example, when the user clicks the "play_button" element, a side panel slides open from the left containing a form. The form allows users to enter text inputs (e.g., name, issue description). Upon submission, a customized event (`form_submit_event`) is emitted which can be captured by parent applications or embedded backends (e.g., Streamlit).

## Code Walkthrough

```python
import os
from sivo import Sivo

def main():
    svg_path = os.path.join(os.path.dirname(__file__), "sample.svg")

    # Initialize the Sivo app from an SVG
    sivo_app = Sivo.from_svg(svg_path)

    # Click the shape to open a native HTML form in the panel.
    # Submission emits a 'sivo_click' event to the parent window (e.g. Streamlit backend)
    sivo_app.map(
        element_id="play_button",
        tooltip="Click to report an issue",
        form_fields=[
            {"name": "username", "label": "Your Name", "type": "text"},
            {"name": "issue", "label": "Describe the Issue", "type": "textarea"}
        ],
        form_submit_event="issue_reported",
        panel_position="left",
        hover_color="#cc0000",
        glow=True
    )

    # Export the configured application to HTML
    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    sivo_app.to_html(output_path)
    print(f"Exported Form interactive HTML to {output_path}")

if __name__ == "__main__":
    main()
```

### Key Elements

- **`form_fields`**: A list of dictionaries defining the fields to be included in the form. Here we have a text input for a name and a textarea for an issue description.
- **`form_submit_event`**: Specifies the name of the event to be emitted when the form is submitted. In this case, it emits an `issue_reported` event.
- **`panel_position`**: Since the default panel position is `'none'`, setting it to `'left'` is crucial to render the HTML form side panel smoothly.
- **`glow`** and **`hover_color`**: Provide visual feedback when interacting with the SVG target.

## Backend Integration

Please note that this is a **frontend-only** example. The SIVO engine itself does not manage databases or backend API requests.

When a user completes and submits the form, the SIVO interactive app emits the custom DOM event (in this case, `issue_reported`) via standard `window.parent.postMessage` and custom DOM events.

To process the data, your host application (such as a Streamlit backend, a React wrapper, or vanilla Javascript) must listen for this event, extract the form payload, and route the data to your actual backend logic or database.

## Running the Example

Simply execute the `main.py` script to generate `output.html`.
```bash
python main.py
```
After doing so, you can open `output.html` in your browser. Hover over the play button to see the tooltip, click it to see the side-panel pop open on the left, and try interacting with the generated form.
