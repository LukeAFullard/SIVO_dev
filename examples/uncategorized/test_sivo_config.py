import os
import sys

# Ensure SIVO is importable from src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from sivo.core.infographic import Infographic

def run():
    config_path = os.path.join(os.path.dirname(__file__), "project.json")
    print(f"Loading configuration from {config_path}...")

    # Load from the config file directly
    sivo_instance = Infographic.from_config(config_path)

    output_path = os.path.join(os.path.dirname(__file__), "config_output.html")
    print(f"Exporting HTML to {output_path}...")
    sivo_instance.to_echarts_html(output_path)

    print("Done! Open examples/config_output.html in your browser.")

if __name__ == "__main__":
    run()
