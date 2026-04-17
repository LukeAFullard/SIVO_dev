import sivo
import json
import traceback
import js
import gc

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
    gs = config.get("globalSettings", {})
    if gs.get("theme"): app.theme = gs["theme"]
    if gs.get("ambient_effect"): app.ambient_effect = gs["ambient_effect"]
    if gs.get("default_panel_position"): app.default_panel_position = gs["default_panel_position"]
    if gs.get("background_image_url"): app.background_image_url = gs["background_image_url"]
    if gs.get("svg_background_image_url"): app.svg_background_image_url = gs["svg_background_image_url"]
    if gs.get("border_image_url"): app.border_image_url = gs["border_image_url"]
    if bg_image:
         app.background_image_url = bg_image


    # Phase 5: Global Controls
    if config.get("ctrlZoomUi") is False:
        app.lock_zoom_out = True
    if config.get("ctrlMinimap"):
        app.add_minimap()
    if config.get("ctrlZoomClick") is False:
        pass # Handle in elements or natively if possible, currently SIVO doesn't strictly have a global disable zoom on click unless lock_zoom_out is true, but we'll leave it
    if config.get("ctrlDrawing"):
        app.enable_drawing_tools = True
    if config.get("ctrlBrush"):
        app.enable_brush_selection = True
    if config.get("ctrlSearch"):
        app.enable_search = True
    if config.get("ctrlLayerToggle"):
        app.add_layer_toggle(config.get("ctrlLayerToggle"), label="Toggle Layer")

    # Phase 6: Geocoding & Export Globals
    if config.get("geocodeEnable"):
        app.enable_geocoder = True
        if config.get("geocodeProvider"):
            app.geocode_provider = config.get("geocodeProvider")
        if config.get("geocodeApiKey"):
            app.geocode_api_key = config.get("geocodeApiKey")

    if config.get("exportWatermark"):
        app.watermark = config.get("exportWatermark")
    if config.get("exportAttribution"):
        app.attribution = config.get("exportAttribution")

    # Highlight Elements CSS Injection
    if config.get('highlightElements'):
         app.custom_css += "\\n svg [id] { fill: rgba(150, 150, 255, 0.2) !important; stroke: rgba(100, 100, 255, 0.5) !important; cursor: pointer; transition: all 0.2s; }"
         app.custom_css += "\\n svg [id]:hover { fill: rgba(100, 100, 255, 0.4) !important; stroke: rgba(50, 50, 255, 0.8) !important; }"

    active_element_id = config.get('activeElementId')
    if active_element_id:
        app.custom_css += f"\\n svg #{active_element_id} {{ stroke: #ef4444 !important; stroke-width: 3px !important; stroke-dasharray: 5,5; animation: dash 1s linear infinite; }}"
        app.custom_css += "\\n @keyframes dash { to { stroke-dashoffset: -10; } }"

    # Phase 4: Data Binding (Advanced Maps)
    data_file = config.get("dataFile")
    data_map_type = config.get("dataMapType", "choropleth")

    data_id_col = config.get("dataIdCol", "id")
    data_value_col = config.get("dataValueCol", "value")
    data_base_col = config.get("dataBaseCol", "value1")
    data_alpha_col = config.get("dataAlphaCol", "value2")
    data_x_col = config.get("dataXCol", "x")
    data_y_col = config.get("dataYCol", "y")
    data_origin_col = config.get("dataOriginCol", "origin")
    data_dest_col = config.get("dataDestCol", "destination")

    if data_file:
        try:
            import pandas as pd
            # Use IDBFS mount path
            df = pd.read_csv(f"/sivo_workspace/{data_file}")

            if data_map_type == "choropleth" and data_id_col in df.columns and data_value_col in df.columns:
                df[data_value_col] = pd.to_numeric(df[data_value_col], errors='coerce')
                data_map = dict(zip(df[data_id_col].astype(str), df[data_value_col]))
                app.apply_choropleth(data_map, min_color="#e2e8f0", max_color="#3b82f6")

            elif data_map_type == "categorical" and data_id_col in df.columns and data_value_col in df.columns:
                data_map = dict(zip(df[data_id_col].astype(str), df[data_value_col].astype(str)))
                app.apply_categorical_map(data_map)

            elif data_map_type == "value_by_alpha" and data_id_col in df.columns and data_base_col in df.columns and data_alpha_col in df.columns:
                df[data_base_col] = pd.to_numeric(df[data_base_col], errors='coerce')
                df[data_alpha_col] = pd.to_numeric(df[data_alpha_col], errors='coerce')
                base_map = dict(zip(df[data_id_col].astype(str), df[data_base_col]))
                alpha_map = dict(zip(df[data_id_col].astype(str), df[data_alpha_col]))
                app.apply_value_by_alpha(base_map, alpha_map)

            elif data_map_type == "hexbin" and data_x_col in df.columns and data_y_col in df.columns:
                df[data_x_col] = pd.to_numeric(df[data_x_col], errors='coerce')
                df[data_y_col] = pd.to_numeric(df[data_y_col], errors='coerce')
                points = df[[data_x_col, data_y_col]].dropna().values.tolist()
                app.apply_hexbin(points)

            elif data_map_type == "dot_density" and data_id_col in df.columns and data_value_col in df.columns:
                df[data_value_col] = pd.to_numeric(df[data_value_col], errors='coerce')
                data_map = dict(zip(df[data_id_col].astype(str), df[data_value_col]))
                app.apply_dot_density(data_map)

            elif data_map_type == "proportional_symbols" and data_id_col in df.columns and data_value_col in df.columns:
                df[data_value_col] = pd.to_numeric(df[data_value_col], errors='coerce')
                data_map = dict(zip(df[data_id_col].astype(str), df[data_value_col]))
                app.apply_proportional_symbols(data_map)

            elif data_map_type == "spike_map" and data_id_col in df.columns and data_value_col in df.columns:
                df[data_value_col] = pd.to_numeric(df[data_value_col], errors='coerce')
                data_map = dict(zip(df[data_id_col].astype(str), df[data_value_col]))
                app.apply_spike_map(data_map)

            elif data_map_type == "flow_map" and data_origin_col in df.columns and data_dest_col in df.columns and data_value_col in df.columns:
                df[data_value_col] = pd.to_numeric(df[data_value_col], errors='coerce')
                data_list = []
                for _, row in df.iterrows():
                    data_list.append({
                        "origin": str(row[data_origin_col]),
                        "destination": str(row[data_dest_col]),
                        "value": float(row[data_value_col]) if not pd.isna(row[data_value_col]) else 0.0
                    })
                app.apply_flow_map(data_list)

        except Exception as e:
            error_msg = json.dumps(f"Error loading data file {data_file}: {str(e)}")
            app.custom_js += f"if(window.parent && window.parent.showToast) {{ window.parent.showToast({error_msg}, 'error'); }}"

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


    # Phase 4: Live Binding
    live_ws_url = config.get("liveWsUrl")
    live_ws_topic = config.get("liveWsTopic")
    if live_ws_url and live_ws_topic:
        app.bind_live(live_ws_url, live_ws_topic)

    live_api_url = config.get("liveApiUrl")
    if live_api_url:
        live_api_interval = config.get("liveApiInterval")
        interval_ms = int(live_api_interval) if live_api_interval else 5000
        live_api_path = config.get("liveApiPath")
        app.bind_api(live_api_url, polling_interval_ms=interval_ms, data_path=live_api_path if live_api_path else None)

    timeline_csv = config.get("timelineCsvFile")
    if timeline_csv:
        try:
            import pandas as pd
            import io
            with open(f"/sivo_workspace/{timeline_csv}", 'r') as f:
                df = pd.read_csv(io.StringIO(f.read()))

            time_col = config.get("timelineTimeCol", "date")
            map_type = config.get("timelineMapType", "choropleth")

            if time_col in df.columns:
                 # Standardize to list of dicts for simple mapping
                 timeline_data = df.to_dict(orient="records")
                 app.bind_timeline(timeline_data, time_column=time_col, map_type=map_type)
        except Exception as e:
            error_msg = json.dumps(str(e))
            app.custom_js += f"if(window.parent && window.parent.showToast) {{ window.parent.showToast({error_msg}, 'error'); }}"

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


        # Integrations
        for t in ['document', 'map_location', 'ecommerce', 'rich_media', 'bi', 'external_form', 'form', 'social', 'replit']:
            if el_cfg.get(t):
                kwargs[t] = {'url': el_cfg[t]}

        # A11y & Media
        if el_cfg.get('marker'): kwargs['marker'] = el_cfg['marker']
        if el_cfg.get('video'): kwargs['video'] = el_cfg['video']
        if el_cfg.get('audio'): kwargs['audio'] = el_cfg['audio']
        if el_cfg.get('markdown'): kwargs['markdown'] = el_cfg['markdown']
        if el_cfg.get('gallery'): kwargs['gallery'] = el_cfg['gallery']
        if el_cfg.get('embed_svg'): kwargs['embed_svg'] = el_cfg['embed_svg']
        if el_cfg.get('lottie'): kwargs['lottie'] = el_cfg['lottie']
        if el_cfg.get('morph_to_path'): kwargs['morph_to_path'] = el_cfg['morph_to_path']
        if el_cfg.get('transform'): kwargs['transform'] = el_cfg['transform']
        if el_cfg.get('explode'): kwargs['explode'] = True
        if el_cfg.get('confetti'): kwargs['confetti'] = True
        if el_cfg.get('loading'): kwargs['loading'] = True
        if el_cfg.get('zoom_to'): kwargs['zoom_to'] = el_cfg['zoom_to']

        fetch_url = el_cfg.get('fetchUrl')
        if fetch_url:
            kwargs['fetch_url'] = fetch_url
            fetch_data_path = el_cfg.get('fetchDataPath')
            if fetch_data_path:
                kwargs['fetch_data_path'] = fetch_data_path


        # Phase 5: Regions & Overlays
        fill_zone = el_cfg.get('fillZone')
        if fill_zone:
            app.fill_template_zone(el_id, fill_zone)

        clip_html = el_cfg.get('clipHtml')
        if clip_html:
            app.clip_html_to_shape(el_id, clip_html)

        shape_type = el_cfg.get('shapeType')
        if shape_type and shape_type != 'none':
            if shape_type == 'circle':
                app.add_shape('circle', cx=100, cy=100, r=50, id=el_id + "_shape", fill="red")
            elif shape_type == 'rect':
                app.add_shape('rect', x=100, y=100, width=100, height=50, id=el_id + "_shape", fill="blue")
            elif shape_type == 'text':
                app.add_shape('text', x=100, y=100, text_content="Sample Text", id=el_id + "_shape", fill="black")

        abs_img = el_cfg.get('absoluteImageUrl')
        if abs_img:
            app.add_image_overlay(el_id, abs_img)

        scratchoff = el_cfg.get('scratchoff')
        if scratchoff:
            app.map(el_id, scratchoff=sivo.ScratchoffConfig()) # Requires applying scratchoff config

        # Phase 6: Drill-Through (Multi-View preview representation)
        # Note: In preview, this might just register as a click callback to show it's linked
        drill_view_id = el_cfg.get('drillThroughViewId')
        if drill_view_id:
            # Tell SIVO to use real page transitions for this element ID when clicked
            kwargs['drill_through_target'] = drill_view_id

            # Add simple tooltip if none
            if 'html' not in kwargs:
                kwargs['html'] = f"Click to drill through to view: {drill_view_id}"

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
            data_file = config.get("dataFile")
            data_id_col = config.get("dataIdCol", "id")
            data_value_col = config.get("dataValueCol", "value")
            graph_title = el_cfg.get("graphTitle")

            if data_file:
                try:
                    import pandas as pd
                    df = pd.read_csv(f"/sivo_workspace/{data_file}")

                    if data_id_col in df.columns and data_value_col in df.columns:
                        df_clean = df.dropna(subset=[data_id_col, data_value_col]).copy()
                        df_clean[data_value_col] = pd.to_numeric(df_clean[data_value_col], errors='coerce')
                        df_clean = df_clean.dropna(subset=[data_value_col])

                        if not df_clean.empty:
                            names = df_clean[data_id_col].astype(str).tolist()
                            values = df_clean[data_value_col].tolist()

                            chart_config = {}
                            if graph_title:
                                chart_config["title"] = {"text": graph_title}

                            if graph_type == "bar":
                                chart_config.update({"x": names, "y": values})
                                kwargs["bar_chart"] = chart_config
                            elif graph_type == "line":
                                chart_config.update({"x": names, "y": values})
                                kwargs["line_chart"] = chart_config
                            elif graph_type == "pie":
                                chart_config.update({"data": [{"name": str(n), "value": float(v)} for n, v in zip(names, values)]})
                                kwargs["pie_chart"] = chart_config
                            elif graph_type == "scatter":
                                # For scatter, use values as Y, and index as X if no other metric is provided,
                                # but real data is preferred.
                                chart_config.update({"data": [[i, v] for i, v in enumerate(values)]})
                                kwargs["scatter_chart"] = chart_config
                            elif graph_type == "boxplot":
                                chart_config.update({"data": [values]})
                                kwargs["boxplot_chart"] = chart_config
                            elif graph_type == "candlestick":
                                # Assume data is provided as Open, Close, Lowest, Highest
                                # if additional columns exist, otherwise fallback to simple calculation
                                # Since we only mapped one `data_value_col`, we will try to find others or use an educated guess from DataFrame
                                # for real candlestick mapping. If the user only provided one column, we duplicate it but it's real data.
                                candle_data = []
                                open_col = data_value_col
                                close_col = [c for c in df.columns if 'close' in c.lower()]
                                low_col = [c for c in df.columns if 'low' in c.lower()]
                                high_col = [c for c in df.columns if 'high' in c.lower()]

                                for idx, row in df_clean.iterrows():
                                    op = float(row[open_col]) if not pd.isna(row[open_col]) else 0
                                    cl = float(row[close_col[0]]) if close_col and not pd.isna(row[close_col[0]]) else op
                                    lo = float(row[low_col[0]]) if low_col and not pd.isna(row[low_col[0]]) else min(op, cl)
                                    hi = float(row[high_col[0]]) if high_col and not pd.isna(row[high_col[0]]) else max(op, cl)
                                    candle_data.append([op, cl, lo, hi])

                                chart_config.update({"x": names, "y": candle_data})
                                kwargs["candlestick_chart"] = chart_config
                            elif graph_type == "heatmap":
                                # For a heatmap we typically need 3 dimensions (X, Y, Value).
                                # Use ID col for X, other numeric columns for Y
                                numeric_cols = df_clean.select_dtypes(include=['number']).columns.tolist()
                                if data_value_col in numeric_cols:
                                    numeric_cols.remove(data_value_col)
                                numeric_cols.insert(0, data_value_col) # Ensure primary value col is first

                                heatmap_data = []
                                y_axis_names = numeric_cols[:5] # limit to 5 categories to prevent overflow

                                for x_idx, row in df_clean.iterrows():
                                    # the actual index in the `names` list
                                    actual_x_idx = list(df_clean.index).index(x_idx)
                                    for y_idx, col in enumerate(y_axis_names):
                                        val = float(row[col]) if pd.notna(row[col]) else 0
                                        heatmap_data.append([actual_x_idx, y_idx, val])

                                chart_config.update({"x_axis": names, "y_axis": y_axis_names, "data": heatmap_data})
                                kwargs["heatmap_chart"] = chart_config

                        else:
                            error_msg = json.dumps(f"No valid numeric data found in column '{data_value_col}'.")
                            app.custom_js += f"if(window.parent && window.parent.showToast) {{ window.parent.showToast({error_msg}, 'warning'); }}"
                    else:
                        error_msg = json.dumps(f"Columns '{data_id_col}' or '{data_value_col}' not found in {data_file}.")
                        app.custom_js += f"if(window.parent && window.parent.showToast) {{ window.parent.showToast({error_msg}, 'warning'); }}"
                except Exception as e:
                    error_msg = json.dumps(f"Error parsing {data_file} for graphing: {str(e)}")
                    app.custom_js += f"if(window.parent && window.parent.showToast) {{ window.parent.showToast({error_msg}, 'error'); }}"

        app.map(el_id, **kwargs)


    # Phase 5: Connections
    connections = config.get("connections", [])
    for conn in connections:
        app.add_connection(conn["from"], conn["to"], animate=True)


    # Phase 5: Timeline
    timeline_steps = config.get("timelineSteps", [])
    if timeline_steps:
        for step in timeline_steps:
            target_id = step.get("targetId")
            app.add_scrollytelling_step(
                element_id=target_id if target_id else None,
                html_content=f"<h3>{step.get('title', '')}</h3><p>{step.get('content', '')}</p>"
            )

        presentation_autoplay = config.get("presentationAutoplay")
        presentation_progress = config.get("presentationProgress")
        presentation_laser = config.get("presentationLaser")
        presentation_notes = config.get("presentationNotes")

        if presentation_autoplay:
            try:
                app.presentation_autoplay_ms = int(presentation_autoplay)
            except:
                pass
        if presentation_progress:
            app.presentation_progress = True
        if presentation_laser:
            app.presentation_laser = True
        if presentation_notes:
            app.presentation_speaker_notes_element = presentation_notes

    # Apply Custom CSS / JS to the final output
    gs = config.get("globalSettings", {})
    to_html_kwargs = {"build_js": False}

    if gs.get("custom_css"):
        to_html_kwargs["custom_css"] = gs["custom_css"]
    if gs.get("custom_js"):
        to_html_kwargs["custom_js"] = gs["custom_js"]

    dashboard_blocks = config.get("dashboardBlocks", [])
    export_e2e = config.get("exportE2e")

    # In SIVO, enable_e2e_testing is typically passed when rendering or generating a project structure.
    # To demonstrate this in the builder without crashing preview, we configure the project instance if drill-through is used,
    # or append a runtime script block. But natively we should enable it on the `app` instance if supported, or project.

    if export_e2e:
        to_html_kwargs["enable_e2e_testing"] = True

    if dashboard_blocks:
        dashboard = sivo.SivoDashboard(app, theme="light")
        for block in dashboard_blocks:
            title = block.get("title", "Metric")
            value = block.get("value", "0")
            dashboard.add_html_block(f"<h3>{title}</h3><h2>{value}</h2>")
        html_output = dashboard.to_html(**to_html_kwargs)
    else:
        # Check if there are drill-through elements, and if so, use SivoProject for the preview
        # so drill through links correctly generate SivoProject HTML
        has_drill = any(el.get("drillThroughViewId") for el in elements.values())
        if has_drill:
            project = sivo.SivoProject(initial_view_id="main")
            project.add_view("main", app)
            # Add proper fallback views for the drill through targets to prevent 404s in preview
            for el_id, el in elements.items():
                if el.get("drillThroughViewId"):
                    target_view = el.get("drillThroughViewId")
                    # Try to load the target view if it's an uploaded SVG file in the workspace
                    try:
                        with open(f"/sivo_workspace/{target_view}", 'r') as f:
                            target_app = sivo.Sivo.from_string(f.read())

                        target_app.custom_js += "if(window.parent && window.parent.showToast) { window.parent.showToast('Drill-through target loaded', 'success'); }"
                    except Exception as e:
                        # Graceful fallback without hardcoded dummy SVG
                        target_app = sivo.Sivo() # Start with empty sivo app
                        error_msg = json.dumps(f"Target View '{target_view}' not found or invalid SVG.")
                        target_app.custom_js += f"if(window.parent && window.parent.showToast) {{ window.parent.showToast({error_msg}, 'error'); }}"

                    # Back link logic so users can return
                    target_app.custom_js += """
                        document.addEventListener("DOMContentLoaded", () => {
                             let backBtn = document.createElement("button");
                             backBtn.innerText = "Back to Main Map";
                             backBtn.style.position = "absolute";
                             backBtn.style.top = "10px";
                             backBtn.style.left = "10px";
                             backBtn.style.zIndex = "9999";
                             backBtn.style.padding = "5px 10px";
                             backBtn.style.backgroundColor = "#fff";
                             backBtn.style.border = "1px solid #ccc";
                             backBtn.style.borderRadius = "4px";
                             backBtn.style.cursor = "pointer";
                             backBtn.onclick = () => window.location.hash = "#main";
                             document.body.appendChild(backBtn);
                        });
                    """

                    try:
                        project.add_view(target_view, target_app)
                    except:
                        pass # View already added
            html_output = project.to_html(**to_html_kwargs)
        else:
            html_output = app.to_html(**to_html_kwargs)

except Exception as main_e:
    html_output = f'<div style="color:red;"><pre>{traceback.format_exc()}</pre></div>'

# Memory profiling/cleanup: explicitly delete large objects and force garbage collection
# This prevents memory leaks across successive preview generations in the browser
try:
    if 'app' in locals():
        del app
    if 'dashboard' in locals():
        del dashboard
    if 'project' in locals():
        del project
    if 'target_app' in locals():
        del target_app
except:
    pass

gc.collect()

html_output
