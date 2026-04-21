# Forms & E-commerce Integration Example

This example demonstrates how to integrate external interactive forms (e.g., Typeform) and E-commerce checkout flows (e.g., Stripe Payment Links) directly into your SIVO SVG elements. These embeddings can be displayed contextually within a sliding side panel upon clicking the mapped SVG paths.

## What is being tested/demonstrated
*   **External Forms (`external_form`)**: Integrating an external form provider using a provided URL.
*   **E-commerce integration (`ecommerce`)**: Embedding a payment/checkout provider into SIVO.
*   **Overlay/Side Panel (`panel_position="right"`)**: Setting the position where the external content frame will be displayed upon user interaction with the elements.

## Relevant Code Snippets

```python
import os
from sivo import Sivo

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    svg_path = os.path.join(base_dir, "sample.svg")

    app = Sivo.from_svg(svg_path)

    # Map Ecommerce action (e.g., Stripe Payment Link) to product1
    # with a side panel sliding from the right.
    app.map(
        "product1",
        tooltip="Buy Now",
        html="<h3>Special Product</h3><p>Price: $99.99</p>",
        panel_position="right",
        ecommerce={
            "provider": "stripe",
            "checkout_url": "https://buy.stripe.com/test_abcdefg"
        }
    )

    # Map External Form (e.g., Typeform) to survey1
    # also rendered in a right side panel.
    app.map(
        "survey1",
        tooltip="Take our Survey",
        panel_position="right",
        external_form={
            "provider": "typeform",
            "form_url": "https://form.typeform.com/to/demo_form"
        }
    )

    # Export to HTML
    output_path = os.path.join(base_dir, "interactive_forms_ecommerce.html")
    app.to_html(output_path)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    main()
```

## Steps
1. Run the script using `python main.py`
2. Open the resulting `interactive_forms_ecommerce.html` in your web browser.
3. Click on the first element (e.g., `product1`) to see the e-commerce side panel slide in.
4. Click on the second element (e.g., `survey1`) to see the external form slide in.
