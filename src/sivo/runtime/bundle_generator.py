import os
import json
from typing import Dict, Optional
from jinja2 import Environment, FileSystemLoader, select_autoescape

def generate_echarts_html(views_data: Dict[str, Dict], initial_view: str, output_path: Optional[str] = None, custom_css: Optional[str] = None, custom_js: Optional[str] = None) -> str:
    template_dir = os.path.join(os.path.dirname(__file__), 'templates')
    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('echarts.html')

    # Re-structure the views data to format echarts Data and actionsManifest directly for the JS side
    formatted_views = {}

    for view_id, view_obj in views_data.items():
        echarts_data = []
        actions_manifest = {}

        # In a single view, mappings was a Dict[str, InteractionMapping]
        # In SivoProject, mappings is already dumped to a dictionary. We must process both.
        # Check if the mapping is an instance of BaseModel or dict.
        mappings = view_obj["mappings"]

        for name, mapping in mappings.items():
            if hasattr(mapping, "model_dump"):
                mapping_dict = mapping.model_dump()
            elif hasattr(mapping, "dict"):
                mapping_dict = mapping.dict()
            elif isinstance(mapping, dict):
                mapping_dict = mapping.copy()
            else:
                mapping_dict = dict(mapping)

            data_item = {
                'name': name,
                'value': 1,
            }
            if mapping_dict.get('open_by_default'):
                data_item['open_by_default'] = True

            element_actions = []
            actions_list = mapping_dict.get('actions', [])

            for action in actions_list:
                if hasattr(action, "model_dump"):
                    act_dict = action.model_dump()
                elif hasattr(action, "dict"):
                    act_dict = action.dict()
                elif isinstance(action, dict):
                    act_dict = action.copy()
                else:
                    act_dict = dict(action)

                # Check for action_type correctly handling 'url' vs URLAction
                if "action_type" not in act_dict:
                    if hasattr(action, "action_type"):
                        act_dict["action_type"] = action.action_type
                    elif hasattr(action, "__class__"):
                        act_dict["action_type"] = action.__class__.__name__.lower().replace('action', '')

                # If it's a URLAction or DrillDownAction, it might be stored directly without being serialized properly by the dict dump if using nested Pydantic
                if hasattr(action, 'url') and "url" not in act_dict: act_dict["url"] = action.url
                if hasattr(action, 'video_url') and "video_url" not in act_dict: act_dict["video_url"] = action.video_url
                if hasattr(action, 'target_svg') and "target_svg" not in act_dict: act_dict["target_svg"] = action.target_svg
                if hasattr(action, 'target') and "target" not in act_dict: act_dict["target"] = action.target
                if hasattr(action, 'repl_url') and "repl_url" not in act_dict: act_dict["repl_url"] = action.repl_url
                if hasattr(action, 'content') and "content" not in act_dict: act_dict["content"] = action.content
                if hasattr(action, 'event_name') and "event_name" not in act_dict: act_dict["event_name"] = action.event_name
                if hasattr(action, 'payload') and "payload" not in act_dict: act_dict["payload"] = action.payload
                if hasattr(action, 'provider') and "provider" not in act_dict: act_dict["provider"] = action.provider
                if hasattr(action, 'option') and "option" not in act_dict: act_dict["option"] = action.option
                if hasattr(action, 'height') and "height" not in act_dict: act_dict["height"] = action.height
                if hasattr(action, 'center') and "center" not in act_dict: act_dict["center"] = action.center
                if hasattr(action, 'zoom_level') and "zoom_level" not in act_dict: act_dict["zoom_level"] = action.zoom_level
                if hasattr(action, 'panel_position') and "panel_position" not in act_dict: act_dict["panel_position"] = action.panel_position

                element_actions.append(act_dict)

            mapping_dict['actions'] = element_actions

            processed_element_actions = []

            # Process Actions for Echarts
            for action in element_actions:
                processed_element_actions.append(action)
                if action.get('action_type') == "tooltip" and action.get('title'):
                    data_item['tooltip'] = action['title']

            if processed_element_actions:
                actions_manifest[name] = processed_element_actions

            # Process Theme
            theme = mapping_dict.get('theme', {})
            if hasattr(theme, "model_dump"):
                theme = theme.model_dump()
            elif hasattr(theme, "dict"):
                theme = theme.dict()
            elif not isinstance(theme, dict):
                theme = dict(theme)

            item_style = {}
            if theme.get('color'):
                item_style['areaColor'] = theme['color']
            if theme.get('border_color'):
                item_style['borderColor'] = theme['border_color']
            if theme.get('border_width') is not None:
                item_style['borderWidth'] = theme['border_width']

            if theme.get('animation'):
                data_item['animation_class'] = theme.get('animation')

            if theme.get('morph_to_path'):
                data_item['morph_to_path'] = theme.get('morph_to_path')

            if theme.get('morph_duration_ms') is not None:
                data_item['morph_duration_ms'] = theme.get('morph_duration_ms')

            if theme.get('filter'):
                data_item['filter'] = theme.get('filter')

            if theme.get('morph_to_path') or theme.get('filter'):
                # When relying on native SVG overlay (morph or filter), we hide the underlying ECharts shape
                item_style['opacity'] = 0

            if item_style:
                data_item['itemStyle'] = item_style

            emphasis_style = {}
            if theme.get('hover_color'):
                emphasis_style['areaColor'] = theme['hover_color']

            if theme.get('glow'):
                emphasis_style['shadowBlur'] = 15
                emphasis_style['shadowColor'] = theme.get('hover_color') if theme.get('hover_color') else 'rgba(0, 0, 0, 0.5)'
                emphasis_style['shadowOffsetX'] = 0
                emphasis_style['shadowOffsetY'] = 0

            if emphasis_style:
                data_item['emphasis'] = {'itemStyle': emphasis_style}

            echarts_data.append(data_item)

        view_dict = {
            "svg_string": view_obj["svg_string"],
            "echarts_data": echarts_data,
            "actions_manifest": actions_manifest,
            "overlays": view_obj.get("overlays", {}),
            "connections": view_obj.get("connections", []),
            "path_labels": view_obj.get("path_labels", []),
            "lock_zoom_out": view_obj.get("lock_zoom_out", False),
            "render_mode": view_obj.get("render_mode", "echarts")
        }
        if "data_binding" in view_obj:
            view_dict["data_binding"] = view_obj["data_binding"]

        formatted_views[view_id] = view_dict

    # Check for locally bundled JS
    build_js = False
    bundled_js_content = ""
    # Assuming any view with build_js flag active should trigger it globally
    # In Sivo core, build_js flag is on the Infographic. We can infer it if a 'dist/sivo.min.js' exists locally.
    if os.path.exists("dist/sivo.min.js"):
        build_js = True
        with open("dist/sivo.min.js", "r", encoding="utf-8") as f:
            bundled_js_content = f.read()

    html_output = template.render(
        views_data=json.dumps(formatted_views).replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026"),
        initial_view=json.dumps(initial_view).replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026"),
        custom_css=custom_css,
        custom_js=custom_js,
        build_js=build_js,
        bundled_js_content=bundled_js_content
    )

    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_output)

    return html_output
