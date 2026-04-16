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
         app.custom_css += "\\n svg [id] { fill: rgba(150, 150, 255, 0.2) !important; stroke: rgba(100, 100, 255, 0.5) !important; cursor: pointer; transition: all 0.2s; }"
         app.custom_css += "\\n svg [id]:hover { fill: rgba(100, 100, 255, 0.4) !important; stroke: rgba(50, 50, 255, 0.8) !important; }"

    active_element_id = config.get('activeElementId')
    if active_element_id:
        app.custom_css += f"\\n svg #{active_element_id} {{ stroke: #ef4444 !important; stroke-width: 3px !important; stroke-dasharray: 5,5; animation: dash 1s linear infinite; }}"
        app.custom_css += "\\n @keyframes dash { to { stroke-dashoffset: -10; } }"

    # Click-to-select logic: Inject a custom script to listen for clicks on elements with IDs
    app.custom_js += """
    document.addEventListener('DOMContentLoaded', () => {
        const svgElement = document.querySelector('svg');
        if (!svgElement) return;

        svgElement.addEventListener('click', (e) => {
            // Find the closest element with an ID within the SVG
            let target = e.target;
            while (target && target !== svgElement) {
                if (target.id) {
                    window.parent.postMessage({ type: 'sivo_element_clicked', id: target.id }, '*');
                    e.preventDefault();
                    e.stopPropagation();
                    return;
                }
                target = target.parentNode;
            }
        });
    });
    """


    # Phase 3: Data Binding (Choropleth)
    data_file = config.get("dataFile")
    data_id_col = config.get("dataIdCol", "id")
    data_value_col = config.get("dataValueCol", "value")

    if data_file:
        try:
            import pandas as pd
            # Use IDBFS mount path
            df = pd.read_csv(f"/sivo_workspace/{data_file}")
            # If specified columns exist, apply choropleth
            if data_id_col in df.columns and data_value_col in df.columns:
                data_map = dict(zip(df[data_id_col].astype(str), df[data_value_col]))
                app.apply_choropleth(data_map, min_color="#e2e8f0", max_color="#3b82f6")
        except Exception as e:
            error_msg = json.dumps(f"Error loading data file {data_file}: {str(e)}")
            app.custom_js += f"console.error({error_msg});"

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

        hover_cb = el_cfg.get('hoverCallback')
        if hover_cb and hover_cb != 'none':
            kwargs['hover_callback_event'] = hover_cb
            kwargs['hover_callback_payload'] = {"element": el_id, "action": hover_cb}


        graph_type = el_cfg.get("graphType")
        if graph_type and graph_type != "none":
            # Real implementation using parsed CSV logic
            data_file = config.get("dataFile")
            data_id_col = config.get("dataIdCol", "id")
            data_value_col = config.get("dataValueCol", "value")
            if data_file:
                try:
                    import pandas as pd
                    df = pd.read_csv(f"/sivo_workspace/{data_file}")
                    # If columns exist
                    if data_id_col in df.columns and data_value_col in df.columns:
                        # Extract data for this particular element or generally
                        # Since we want to show a graph, let's plot the top 5 values for bar/pie or a trend
                        # Coerce values to numeric first
                        df[data_value_col] = pd.to_numeric(df[data_value_col], errors='coerce')
                        top_df = df.nlargest(5, data_value_col)
                        names = top_df[data_id_col].astype(str).tolist()
                        values = top_df[data_value_col].tolist()
                        if graph_type == "bar":
                            kwargs["bar_chart"] = {"x": names, "y": values}
                        elif graph_type == "line":
                            kwargs["line_chart"] = {"x": names, "y": values}
                        elif graph_type == "pie":
                            kwargs["pie_chart"] = {"data": [{"name": str(n), "value": float(v)} for n, v in zip(names, values)]}
                except Exception as e:
                    pass

        app.map(el_id, **kwargs)


    dashboard_blocks = config.get("dashboardBlocks", [])
    if dashboard_blocks:
        dashboard = sivo.SivoDashboard(app, theme="light")
        for block in dashboard_blocks:
            title = block.get("title", "Metric")
            value = block.get("value", "0")
            dashboard.add_html_block(f"<h3>{title}</h3><h2>{value}</h2>")
        html_output = dashboard.to_html(build_js=False)
    else:
        html_output = app.to_html(build_js=False)

except Exception as main_e:
    html_output = f'<div style="color:red;"><pre>{traceback.format_exc()}</pre></div>'

html_output
