import sivo
import json
import traceback
import js

config = json.loads(js.window.builderConfigJson)

try:
    template_path = config.get('template')
    custom_svg = config.get('customSvg')
    bg_image = config.get('bgImage')

    # Load base template or blank or custom svg
    if custom_svg:
        try:
            # check if it's a url or a file path in idbfs
            if custom_svg.startswith('http'):
                 app = sivo.Sivo.from_svg(custom_svg)
            elif custom_svg.startswith('<svg'):
                 app = sivo.Sivo.from_string(custom_svg)
            else:
                 with open(custom_svg, 'r') as f:
                     app = sivo.Sivo.from_string(f.read())
        except Exception as e:
            app = sivo.Sivo.from_string(f'<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg"><text x="20" y="40">Error loading custom SVG {custom_svg}: {str(e)}</text></svg>')
    elif template_path == 'blank' or not template_path:
        app = sivo.Sivo.from_string('<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="#f8fafc"/></svg>')
    else:
        try:
            app = sivo.Sivo.from_template(template_path)
        except Exception as e:
            app = sivo.Sivo.from_string(f'<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg"><text x="20" y="40">Error loading template {template_path}: {str(e)}</text></svg>')

    # Apply Canvas Settings
    if bg_image:
         app.background_image_url = bg_image

    # Highlight Elements CSS Injection
    if config.get('highlightElements'):
         app.custom_css += "\\n svg [id] { fill: rgba(150, 150, 255, 0.2) !important; stroke: rgba(100, 100, 255, 0.5) !important; }"

    # Apply Element Configurations
    elements = config.get('elements', {})
    for el_id, el_cfg in elements.items():
        theme = sivo.ThemeOverride(
            color=el_cfg.get('fill'),
            hover_color=el_cfg.get('hover')
        )

        kwargs = {
            'theme_override': theme
        }

        if el_cfg.get('tooltip'):
            kwargs['html'] = el_cfg['tooltip']

        # Tooltip Z-Index Enforcement is handled by injecting custom CSS
        if el_cfg.get('enforceZIndex'):
            app.custom_css += "\\n.echarts-tooltip { z-index: 9999 !important; }"

        if el_cfg.get('selectiveHover') == False:
            # Prevent hover effects
            theme.hover_color = el_cfg.get('fill')

        # Actions
        click_cb = el_cfg.get('clickCallback')
        if click_cb == 'zoom':
            kwargs['zoom_to'] = el_id
        elif click_cb == 'toggle_image':
            kwargs['toggle_image'] = {
                'image_urls': [url.strip() for url in el_cfg.get('toggleImageUrls', '').split(',') if url.strip()],
                'target_id': el_id
            }
        elif click_cb == 'footnote':
            kwargs['footnote'] = el_cfg.get('footnoteText', '')

        app.map(el_id, **kwargs)

    html_output = app.to_html(build_js=False)
except Exception as main_e:
    html_output = f'<div style="color:red;"><pre>{traceback.format_exc()}</pre></div>'

html_output
