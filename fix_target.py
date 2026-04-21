import re

with open("src/sivo/runtime/templates/echarts.html", "r") as f:
    content = f.read()

content = content.replace('''                    if (item.url) {
                        el.href = item.url;
                        if (item.url.startsWith('http')) {
                            el.target = '_blank';
                        }
                    } else if (item.view_id) {''', '''                    if (item.url) {
                        el.href = item.url;
                        el.target = item.target || '_self';
                    } else if (item.view_id) {''')

with open("src/sivo/runtime/templates/echarts.html", "w") as f:
    f.write(content)


with open("src/sivo/runtime/templates/dashboard_blocks.html", "r") as f:
    content = f.read()

content = content.replace('''<a class="sivo-nav-item" href="{{ item.url }}" {% if item.url.startswith('http') %}target="_blank"{% endif %}>{{ item.label }}</a>''', '''<a class="sivo-nav-item" href="{{ item.url }}" target="{{ item.target | default('_self') }}">{{ item.label }}</a>''')

with open("src/sivo/runtime/templates/dashboard_blocks.html", "w") as f:
    f.write(content)
