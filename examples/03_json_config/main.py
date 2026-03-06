import os
from sivo import Sivo

def main():
    config_path = os.path.join(os.path.dirname(__file__), "config.json")

    # Generate the app from declarative config
    sivo_app = Sivo.from_config(config_path)

    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    sivo_app.to_html(output_path)
    print(f"Exported interactive HTML to {output_path}")

if __name__ == "__main__":
    main()
