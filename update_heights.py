import os
import re

def get_chart_height(html_path):
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
            match = re.search(r'height":(\d+)', content)
            if match:
                return int(match.group(1))
    except Exception as e:
        print(f"Error reading {html_path}: {e}")
    return None

def process_popup(md_path, html_dir):
    try:
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find the iframe src to get the corresponding chart file
        match = re.search(r'<iframe src="(results/[^"]+)"', content)
        if match:
            chart_file = match.group(1).replace('%20', ' ')
            chart_path = os.path.join(html_dir, chart_file.split('/')[-1])

            height = get_chart_height(chart_path)
            if height:
                # Add a bit of padding to the height to avoid scrollbars
                new_height = height + 50
                new_content = re.sub(r'height="\d+px"', f'height="{new_height}px"', content)

                with open(md_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {md_path} height to {new_height}px")
    except Exception as e:
        print(f"Error processing {md_path}: {e}")

base_dir = "examples/mysite/title_page/subpage/water/science/fmu/manawatū"
md_dir = os.path.join(base_dir, "md")
html_dir = os.path.join(base_dir, "results")

for root, _, files in os.walk(md_dir):
    for file in files:
        if file.endswith("popup.md"):
            md_path = os.path.join(root, file)
            process_popup(md_path, html_dir)
