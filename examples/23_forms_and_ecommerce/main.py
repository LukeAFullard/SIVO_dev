import os
from sivo import Sivo

def main():
    # 1. Initialize Sivo with our SVG
    base_dir = os.path.dirname(os.path.abspath(__file__))
    svg_path = os.path.join(base_dir, "sample.svg")

    app = Sivo.from_svg(svg_path)

    # 2. Map Ecommerce action (e.g., Stripe Payment Link) to product1
    app.map(
        "product1",
        tooltip="Buy Now",
        html="<h3>Special Product</h3><p>Price: $99.99</p>",
        ecommerce={
            "provider": "stripe",
            "checkout_url": "https://buy.stripe.com/test_abcdefg"
        }
    )

    # 3. Map External Form (e.g., Typeform) to survey1
    app.map(
        "survey1",
        tooltip="Take our Survey",
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
