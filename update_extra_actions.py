import os

def inject_extra_actions(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    extra_actions_logic = """
                        } else if (action.action_type === 'confetti') {
                            if (typeof confetti === 'function') {
                                var x = 0.5, y = 0.5;
                                if (params.event && params.event.event) {
                                    var e = params.event.event;
                                    var clientX = e.clientX;
                                    var clientY = e.clientY;

                                    if (clientX === undefined && e.changedTouches && e.changedTouches.length > 0) {
                                        clientX = e.changedTouches[0].clientX;
                                        clientY = e.changedTouches[0].clientY;
                                    } else if (clientX === undefined && e.touches && e.touches.length > 0) {
                                        clientX = e.touches[0].clientX;
                                        clientY = e.touches[0].clientY;
                                    }

                                    if (clientX !== undefined && clientY !== undefined) {
                                        x = clientX / window.innerWidth;
                                        y = clientY / window.innerHeight;
                                    }
                                }
                                confetti({
                                    particleCount: action.particle_count || 100,
                                    spread: action.spread || 70,
                                    origin: { x: x, y: y },
                                    zIndex: 10000
                                });
                            }
                        } else if (action.action_type === 'callback') {
                            console.log('Triggering callback:', action.event_name, action.payload);
                            window.parent.postMessage({
                                type: 'sivo_click',
                                payload: {
                                    element_id: params.name,
                                    event_name: action.event_name,
                                    data: action.payload || {}
                                }
                            }, '*');
"""
    search_str = "                        } else if (action.action_type === 'drilldown' && action.target_svg) {"

    if search_str in content and "'confetti'" not in content:
        content = content.replace(search_str, extra_actions_logic + search_str)
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Updated extra actions in {filepath}")
    else:
        print(f"Skipped {filepath} (Already updated or target not found)")


def inject_default_click(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    default_click_logic = """
                if (!elementActions || !elementActions.find(a => a.action_type === 'callback')) {
                    window.parent.postMessage({
                        type: 'sivo_click',
                        payload: {
                            element_id: params.name,
                            event_name: 'click',
                            data: {}
                        }
                    }, '*');
                }
"""
    search_str = "                if ((panelPosition === 'right' || panelPosition === 'overlay') && tooltipContent) {"

    if search_str in content and "'sivo_click'" not in content:
        content = content.replace(search_str, default_click_logic + "\n" + search_str)
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Updated default click in {filepath}")
    else:
        print(f"Skipped default click in {filepath} (Already updated or target not found)")


def add_confetti_script(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    confetti_script = """    <script src="https://cdn.jsdelivr.net/npm/echarts@5.5.0/dist/echarts.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.2/dist/confetti.browser.min.js"></script>"""
    search_str = "    <script src=\"https://cdn.jsdelivr.net/npm/echarts@5.5.0/dist/echarts.min.js\"></script>"

    if search_str in content and "canvas-confetti" not in content:
        content = content.replace(search_str, confetti_script)
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Added confetti script in {filepath}")
    else:
        print(f"Skipped confetti script in {filepath} (Already updated or target not found)")


for root, _, files in os.walk('src/sivo/templates/dashboards/'):
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            inject_extra_actions(path)
            inject_default_click(path)
            add_confetti_script(path)
