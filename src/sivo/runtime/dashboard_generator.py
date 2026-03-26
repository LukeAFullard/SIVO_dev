import os
import json
from typing import Dict, Optional, List
from jinja2 import Environment, FileSystemLoader, select_autoescape

from .bundle_generator import format_views_data

def generate_dashboard_blocks_html(views_data: Dict[str, Dict], html_blocks: Dict[str, str], details_panels: Dict[str, Dict], metrics_panels: Dict[str, Dict], layout_order: List[Dict[str, str]], title: str, columns: int = 3, template: str = "default", output_path: Optional[str] = None, custom_js: Optional[str] = None) -> str:
    if template == "default":
        template_dir = os.path.join(os.path.dirname(__file__), 'templates')
        template_file = 'dashboard_blocks.html'
    else:
        template_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates', 'dashboards')
        template_file = f'{template}.html'
        if not os.path.exists(os.path.join(template_dir, template_file)):
            raise FileNotFoundError(f"Dashboard template '{template}' not found in {template_dir}.")

    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template_obj = env.get_template(template_file)

    # We reuse the processing from bundle_generator by running `views_data` through the same structurer
    formatted_views = format_views_data(views_data)

    html_output = template_obj.render(
        views_data=json.dumps(formatted_views).replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026"),
        layout_order=layout_order,
        html_blocks=html_blocks,
        details_panels=details_panels,
        metrics_panels=metrics_panels,
        title=title,
        columns=columns,
        custom_js=custom_js
    )

    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_output)

    return html_output
