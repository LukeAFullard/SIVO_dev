import re

with open('examples/mysite/title_page/subpage/water/science/fmu/manawatū/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('src=\\"results/Chart_Visual%20Clarity.html\\"', 'src=\\"./results/Chart_Visual%20Clarity.html\\"')
content = content.replace('src="results/Chart_Visual%20Clarity.html"', 'src="./results/Chart_Visual%20Clarity.html"')

with open('examples/mysite/title_page/subpage/water/science/fmu/manawatū/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
