import json

with open("examples/features/add_card_custom_svg/output.html", "r") as f:
    content = f.read()

start = content.find('var viewsData = {')
if start != -1:
    end = content.find('};', start)
    json_str = content[start+16:end+1]
    data = json.loads(json_str)
    svg = data['default_view']['svg_string']

    from xml.etree import ElementTree as ET
    try:
        root = ET.fromstring(svg)
        for elem in root.iter():
            if elem.tag.endswith('text'):
                print(f"Found text: {elem.text} -> x={elem.attrib.get('x')}, y={elem.attrib.get('y')}")
    except Exception as e:
        print(f"Error parsing SVG: {e}")
