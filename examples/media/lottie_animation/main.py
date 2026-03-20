import os
from sivo import Sivo

def main():
    svg_path = os.path.join(os.path.dirname(__file__), "..", "01_hello_world", "sample.svg")

    sivo_app = Sivo.from_svg(svg_path, title="Lottie Animation Embed")

    sivo_app.map(
        "river",
        tooltip="Cafeteria",
        lottie={
            "lottie_url": "https://assets3.lottiefiles.com/packages/lf20_UJNc2t.json", # A sample lottie
            "loop": True,
            "autoplay": True
        },
        html="<p>Enjoy a nice hot cup of coffee at our cafeteria.</p>"
    )

    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    sivo_app.to_html(output_path)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    main()