import os
import json
from typing import Dict, Optional, List
from jinja2 import Environment, FileSystemLoader, select_autoescape

from .bundle_generator import format_views_data, determine_dependencies

def generate_dashboard_blocks_html(views_data: Dict[str, Dict], html_blocks: Dict[str, str], details_panels: Dict[str, Dict], metrics_panels: Dict[str, Dict], layout_order: List[Dict[str, str]], title: str, columns: int = 3, template: str = "default", desktop_grid: Optional[str] = None, mobile_grid: Optional[str] = None, background_image_url: Optional[str] = None, background_image_opacity: float = 1.0, background_image_size: str = "cover", gap: str = "1.5rem", mobile_gap: Optional[str] = None, width: str = "100%", mobile_width: str = "100%", theme: str = "light", navigation_menu: Optional[List[Dict[str, str]]] = None, navigation_menu_position: str = 'top-right', output_path: Optional[str] = None, custom_css: Optional[str] = None, custom_js: Optional[str] = None, data_tables: Dict[str, Dict] = None, tabs_blocks: Dict[str, Dict] = None) -> str:
    import warnings
    if template != "default":
        warnings.warn(f"Dashboard templates are deprecated. The '{template}' template parameter is ignored in favor of the modular CSS Grid Builder layout.", DeprecationWarning)

    # Force using standard template
    template_dir = os.path.join(os.path.dirname(__file__), 'templates')
    template_file = 'dashboard_blocks.html'


    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template_obj = env.get_template(template_file)

    # We reuse the processing from bundle_generator by running `views_data` through the same structurer

    mobile_grid_cols = None
    if mobile_grid:
        first_line = mobile_grid.strip().split('\n')[0].replace('"', '').replace("'", "")
        mobile_grid_cols = len([x for x in first_line.split() if x.strip()])

    formatted_views = format_views_data(views_data)
    deps = determine_dependencies(formatted_views)

    # If there's a details panel, we need marked for markdown processing
    if details_panels:
        deps['marked'] = True

    # Fetch custom theme CSS if applicable
    if theme not in ["light", "dark"]:
        from ..core.sivo import Sivo
        theme_css = Sivo.get_theme_css(theme)
        if theme_css:
            # Note: We append it to a separate custom_css variable to pass to Jinja
            custom_css_payload = theme_css + "\n" + (custom_css or "")
        else:
            custom_css_payload = custom_css
    else:
        custom_css_payload = custom_css

    html_output = template_obj.render(
        custom_css=custom_css_payload,
        views_data=json.dumps(formatted_views, separators=(',', ':')).replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026"),
        layout_order=layout_order,
        html_blocks=html_blocks,
        details_panels=details_panels,
        metrics_panels=metrics_panels,
        data_tables=data_tables,
        tabs_blocks=tabs_blocks,
        title=title,
        columns=columns,
        desktop_grid=desktop_grid,
        mobile_grid=mobile_grid,
        mobile_grid_cols=mobile_grid_cols,
        background_image_url=background_image_url, background_image_opacity=background_image_opacity, background_image_size=background_image_size,
        gap=gap, mobile_gap=mobile_gap, width=width, mobile_width=mobile_width,
        theme=theme,
        navigation_menu=navigation_menu,
        navigation_menu_position=navigation_menu_position,
        custom_js=custom_js,
        **deps
    )

    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_output)

    return html_output
