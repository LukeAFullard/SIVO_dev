import re

with open("src/sivo/runtime/templates/echarts.html", "r") as f:
    content = f.read()

subitem_css = """
        .sivo-nav-subitem {
            padding: 8px 20px 8px 40px;
            color: #475569;
            text-decoration: none;
            font-size: 13px;
            font-weight: 400;
            cursor: pointer;
            transition: background 0.2s ease, color 0.2s ease;
        }
        .sivo-nav-subitem:hover {
            background: #f1f5f9;
            color: #0f172a;
        }
        body.sivo-theme-dark .sivo-nav-subitem {
            color: #94a3b8;
        }
        body.sivo-theme-dark .sivo-nav-subitem:hover {
            background: #334155;
            color: #f8fafc;
        }
        .sivo-nav-header {
            padding: 10px 20px 5px 20px;
            color: #64748b;
            font-size: 12px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }
        body.sivo-theme-dark .sivo-nav-header {
            color: #64748b;
        }
"""

content = content.replace("        /* Dark Theme Support */", subitem_css + "        /* Dark Theme Support */")


sublink_js = """
                // Helper to create link elements
                function createLink(item, isSub) {
                    var el = document.createElement(item.url || item.view_id ? 'a' : 'div');
                    el.className = isSub ? 'sivo-nav-subitem' : (item.url || item.view_id ? 'sivo-nav-item' : 'sivo-nav-header');
                    el.innerText = item.label;
                    if (item.url) {
                        el.href = item.url;
                        el.target = item.target || '_self';
                    } else if (item.view_id) {
                        el.onclick = function(e) {
                            e.preventDefault();
                            renderView(item.view_id);
                            menu.classList.remove('active');
                        };
                    }
                    return el;
                }

                // Populate items
                view.navigation_menu.forEach(function(item) {
                    menu.appendChild(createLink(item, false));
                    if (item.sublinks && item.sublinks.length > 0) {
                        item.sublinks.forEach(function(sub) {
                            menu.appendChild(createLink(sub, true));
                        });
                    }
                });
"""

old_js = """                // Populate items
                view.navigation_menu.forEach(function(item) {
                    var el = document.createElement('a');
                    el.className = 'sivo-nav-item';
                    el.innerText = item.label;
                    if (item.url) {
                        el.href = item.url;
                        el.target = item.target || '_self';
                    } else if (item.view_id) {
                        el.onclick = function(e) {
                            e.preventDefault();
                            renderView(item.view_id);
                            menu.classList.remove('active');
                        };
                    }
                    menu.appendChild(el);
                });"""

content = content.replace(old_js, sublink_js)

with open("src/sivo/runtime/templates/echarts.html", "w") as f:
    f.write(content)
