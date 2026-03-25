import os
import json
from typing import Dict, Optional, List
from jinja2 import Environment, FileSystemLoader, select_autoescape

def generate_dashboard_blocks_html(views_data: Dict[str, Dict], html_blocks: Dict[str, str], details_panels: Dict[str, Dict], metrics_panels: Dict[str, Dict], layout_order: List[Dict[str, str]], title: str, output_path: Optional[str] = None, custom_js: Optional[str] = None) -> str:
    template_dir = os.path.join(os.path.dirname(__file__), 'templates')
    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('dashboard_blocks.html')

    # We reuse the processing from bundle_generator by running `views_data` through the same structurer
    formatted_views = {}

    for view_id, view_obj in views_data.items():
        echarts_data = []
        actions_manifest = {}

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

            if mapping_dict.get('draggable'):
                data_item['draggable'] = True

            if mapping_dict.get('context_menu'):
                data_item['context_menu'] = mapping_dict['context_menu']

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

                if "action_type" not in act_dict:
                    if hasattr(action, "action_type"):
                        act_dict["action_type"] = action.action_type
                    elif hasattr(action, "__class__"):
                        act_dict["action_type"] = action.__class__.__name__.lower().replace('action', '')

                if hasattr(action, 'url') and "url" not in act_dict: act_dict["url"] = action.url
                if hasattr(action, 'video_url') and "video_url" not in act_dict: act_dict["video_url"] = action.video_url
                if hasattr(action, 'target_svg') and "target_svg" not in act_dict: act_dict["target_svg"] = action.target_svg
                if hasattr(action, 'transition') and "transition" not in act_dict: act_dict["transition"] = action.transition
                if hasattr(action, 'target') and "target" not in act_dict: act_dict["target"] = action.target
                if hasattr(action, 'repl_url') and "repl_url" not in act_dict: act_dict["repl_url"] = action.repl_url
                if hasattr(action, 'content') and "content" not in act_dict: act_dict["content"] = action.content
                if hasattr(action, 'event_name') and "event_name" not in act_dict: act_dict["event_name"] = action.event_name
                if hasattr(action, 'payload') and "payload" not in act_dict: act_dict["payload"] = action.payload
                if hasattr(action, 'provider') and "provider" not in act_dict: act_dict["provider"] = action.provider
                if hasattr(action, 'option') and "option" not in act_dict: act_dict["option"] = action.option
                if hasattr(action, 'height') and "height" not in act_dict: act_dict["height"] = action.height
                if hasattr(action, 'completion_html') and "completion_html" not in act_dict: act_dict["completion_html"] = action.completion_html
                if hasattr(action, 'completion_color') and "completion_color" not in act_dict: act_dict["completion_color"] = action.completion_color
                if hasattr(action, 'center') and "center" not in act_dict: act_dict["center"] = action.center
                if hasattr(action, 'zoom_level') and "zoom_level" not in act_dict: act_dict["zoom_level"] = action.zoom_level
                if hasattr(action, 'panel_position') and "panel_position" not in act_dict: act_dict["panel_position"] = action.panel_position
                if hasattr(action, 'map_name') and "map_name" not in act_dict: act_dict["map_name"] = action.map_name
                if hasattr(action, 'map_data') and "map_data" not in act_dict: act_dict["map_data"] = action.map_data

                element_actions.append(act_dict)

            mapping_dict['actions'] = element_actions
            processed_element_actions = []

            for action in element_actions:
                processed_element_actions.append(action)
                if action.get('action_type') == "tooltip" and action.get('title'):
                    data_item['tooltip'] = action['title']

            if processed_element_actions:
                actions_manifest[name] = processed_element_actions

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

            if theme.get('fill_gradient'):
                grad = theme['fill_gradient']
                if grad.get('type') == 'radial':
                    item_style['areaColor'] = {
                        'type': 'radial',
                        'x': grad.get('x', 0.5), 'y': grad.get('y', 0.5), 'r': grad.get('r', 0.5),
                        'colorStops': grad.get('stops', []),
                        'global': grad.get('global', False)
                    }
                else:
                    item_style['areaColor'] = {
                        'type': 'linear',
                        'x': grad.get('x', 0), 'y': grad.get('y', 0), 'x2': grad.get('x2', 0), 'y2': grad.get('y2', 1),
                        'colorStops': grad.get('stops', []),
                        'global': grad.get('global', False)
                    }

            if view_obj.get("render_mode", "canvas") == "svg":
                if theme.get('morph_to_path') or theme.get('filter') or theme.get('clip_path') or theme.get('mask') or theme.get('transform') or mapping_dict.get('draggable'):
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

        safe_mappings = {}
        for m_name, mapping in mappings.items():
            if hasattr(mapping, "model_dump"):
                safe_mappings[m_name] = mapping.model_dump()
            elif hasattr(mapping, "dict"):
                safe_mappings[m_name] = mapping.dict()
            elif isinstance(mapping, dict):
                safe_mappings[m_name] = mapping.copy()
            else:
                safe_mappings[m_name] = dict(mapping)

        view_dict = {
            "svg_string": view_obj["svg_string"],
            "echarts_data": echarts_data,
            "actions_manifest": actions_manifest,
            "overlays": view_obj["overlays"],
            "connections": view_obj.get("connections", []),
            "default_panel_position": view_obj.get("default_panel_position", "right"),
            "disable_panel": view_obj.get("disable_panel", False),
            "panel_width": view_obj.get("panel_width", None),
            "panel_height": view_obj.get("panel_height", None),
            "disable_resizer": view_obj.get("disable_resizer", False),
            "disable_tooltips": view_obj.get("disable_tooltips", False),
            "disable_zoom_controls": view_obj.get("disable_zoom_controls", False),
            "lock_scroll_bounds": view_obj.get("lock_scroll_bounds", True),
            "presentation_order": view_obj.get("presentation_order", None),
            "lock_zoom_out": view_obj.get("lock_zoom_out", False),
            "layout_size": view_obj.get("layout_size", None),
            "starting_zoom": view_obj.get("starting_zoom", 1.0),
            "lock_canvas": view_obj.get("lock_canvas", False),
            "render_mode": view_obj.get("render_mode", "canvas"),
            "enable_minimap": view_obj.get("enable_minimap", False),
            "enable_export": view_obj.get("enable_export", False),
            "fade_unselected": view_obj.get("fade_unselected", False),
            "theme": view_obj.get("theme", "light"),
            "enable_search": view_obj.get("enable_search", False),
            "enable_geocoder": view_obj.get("enable_geocoder", False),
            "geocode_provider": view_obj.get("geocode_provider", "nominatim"),
            "geocode_api_key": view_obj.get("geocode_api_key", None),
            "watermark": view_obj.get("watermark", None),
            "enable_brush_selection": view_obj.get("enable_brush_selection", False),
            "title": view_obj.get("title", None),
            "subtitle": view_obj.get("subtitle", None),
            "attribution": view_obj.get("attribution", None),
            "enable_fullscreen": view_obj.get("enable_fullscreen", False),
            "enable_share": view_obj.get("enable_share", False),
            "enable_data_download": view_obj.get("enable_data_download", False),
            "enable_drawing_tools": view_obj.get("enable_drawing_tools", False),
            "ambient_effect": view_obj.get("ambient_effect", None),
            "ambient_speed": view_obj.get("ambient_speed", 1.0),
            "bounding_coords": view_obj.get("bounding_coords", None),
            "graphic": view_obj.get("graphic", None),
            "border_image_url": view_obj.get("border_image_url", None),
            "border_image_position": view_obj.get("border_image_position", "all"),
            "border_image_width": view_obj.get("border_image_width", "10%"),
            "border_image_opacity": view_obj.get("border_image_opacity", 1.0),
            "border_image_grayscale": view_obj.get("border_image_grayscale", False),
            "background_image_url": view_obj.get("background_image_url", None),
            "background_image_opacity": view_obj.get("background_image_opacity", 1.0),
            "background_image_grayscale": view_obj.get("background_image_grayscale", False),
            "mappings": safe_mappings
        }

        formatted_views[view_id] = view_dict

    html_output = template.render(
        views_data=json.dumps(formatted_views).replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026"),
        layout_order=layout_order,
        html_blocks=html_blocks,
        details_panels=details_panels,
        metrics_panels=metrics_panels,
        title=title,
        custom_js=custom_js
    )

    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_output)

    return html_output
