import re
with open("src/sivo/runtime/templates/echarts.html", "r") as f:
    html = f.read()

# Let's see how click is handled
print(re.findall(r'window\.triggerElementClick\s*=\s*function.*?\n(.*?)function ', html, re.DOTALL | re.IGNORECASE)[:1])
