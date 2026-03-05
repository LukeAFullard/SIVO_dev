import os
import json
from typing import Dict, Optional
from jinja2 import Environment, FileSystemLoader, select_autoescape

def generate_echarts_html(svg_string: str, mappings: Dict, overlays: Dict, output_path: Optional[str] = None, custom_css: Optional[str] = None, custom_js: Optional[str] = None) -> str:
    template_dir = os.path.join(os.path.dirname(__file__), 'templates')
    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('echarts.html')

    echarts_data = []
    actions_manifest = {}

    for name, mapping in mappings.items():
        data_item = {
            'name': name,
            'value': 1,
        }

        element_actions = []

        # Process Actions
        for action in mapping.actions:
            element_actions.append(action.model_dump())
            if action.action_type == "tooltip" and action.title:
                data_item['tooltip'] = action.title

        if element_actions:
            actions_manifest[name] = element_actions

        # Process Theme
        item_style = {}
        if mapping.theme.color:
            item_style['areaColor'] = mapping.theme.color
        if mapping.theme.border_color:
            item_style['borderColor'] = mapping.theme.border_color
        if mapping.theme.border_width is not None:
            item_style['borderWidth'] = mapping.theme.border_width

        if item_style:
            data_item['itemStyle'] = item_style

        emphasis_style = {}
        if mapping.theme.hover_color:
            emphasis_style['areaColor'] = mapping.theme.hover_color

        if mapping.theme.glow:
            emphasis_style['shadowBlur'] = 15
            emphasis_style['shadowColor'] = mapping.theme.hover_color if mapping.theme.hover_color else 'rgba(0, 0, 0, 0.5)'
            emphasis_style['shadowOffsetX'] = 0
            emphasis_style['shadowOffsetY'] = 0

        if emphasis_style:
            data_item['emphasis'] = {'itemStyle': emphasis_style}

        echarts_data.append(data_item)

    html_output = template.render(
        svg_string=json.dumps(svg_string),
        echarts_data=json.dumps(echarts_data),
        actions_manifest=json.dumps(actions_manifest),
        overlays=json.dumps(overlays),
        custom_css=custom_css,
        custom_js=custom_js
    )

    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_output)

    return html_output
