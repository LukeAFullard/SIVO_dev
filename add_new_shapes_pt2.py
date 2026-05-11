import sys

filename = "src/sivo/core/infographic.py"
with open(filename, "r") as f:
    content = f.read()

search = """        elif shape == "koura":
            # Stylized crayfish shape (body and claws)
            x, y, w, h = abs_left, abs_top, abs_width, abs_height
            # Body curve
            path_d = f"M {x+w*0.1},{y+h*0.5} C {x+w*0.3},{y+h*0.1} {x+w*0.7},{y+h*0.3} {x+w*0.8},{y+h*0.5} "
            path_d += f"C {x+w*0.7},{y+h*0.7} {x+w*0.3},{y+h*0.9} {x+w*0.1},{y+h*0.5} Z "
            # Top claw
            path_d += f"M {x+w*0.7},{y+h*0.3} C {x+w*0.8},{y+h*0.1} {x+w},{y+h*0.1} {x+w*0.9},{y+h*0.3} C {x+w*0.85},{y+h*0.4} {x+w*0.8},{y+h*0.35} {x+w*0.7},{y+h*0.3} Z "
            # Bottom claw
            path_d += f"M {x+w*0.7},{y+h*0.7} C {x+w*0.8},{y+h*0.9} {x+w},{y+h*0.9} {x+w*0.9},{y+h*0.7} C {x+w*0.85},{y+h*0.6} {x+w*0.8},{y+h*0.65} {x+w*0.7},{y+h*0.7} Z"
            shape_attrs.update({"d": path_d})
            shape_attrs["fill-rule"] = "evenodd"
            etree.SubElement(group, "path", shape_attrs)"""

replace = """        elif shape == "koura":
            # Stylized crayfish shape (body and claws)
            x, y, w, h = abs_left, abs_top, abs_width, abs_height
            # Body curve
            path_d = f"M {x+w*0.1},{y+h*0.5} C {x+w*0.3},{y+h*0.1} {x+w*0.7},{y+h*0.3} {x+w*0.8},{y+h*0.5} "
            path_d += f"C {x+w*0.7},{y+h*0.7} {x+w*0.3},{y+h*0.9} {x+w*0.1},{y+h*0.5} Z "
            # Top claw
            path_d += f"M {x+w*0.7},{y+h*0.3} C {x+w*0.8},{y+h*0.1} {x+w},{y+h*0.1} {x+w*0.9},{y+h*0.3} C {x+w*0.85},{y+h*0.4} {x+w*0.8},{y+h*0.35} {x+w*0.7},{y+h*0.3} Z "
            # Bottom claw
            path_d += f"M {x+w*0.7},{y+h*0.7} C {x+w*0.8},{y+h*0.9} {x+w},{y+h*0.9} {x+w*0.9},{y+h*0.7} C {x+w*0.85},{y+h*0.6} {x+w*0.8},{y+h*0.65} {x+w*0.7},{y+h*0.7} Z"
            shape_attrs.update({"d": path_d})
            shape_attrs["fill-rule"] = "evenodd"
            etree.SubElement(group, "path", shape_attrs)
        elif shape == "tap_splash":
            x, y, w, h = abs_left, abs_top, abs_width, abs_height
            # Tap nozzle on top left, splashing water into bottom right bowl
            path_d = f"M {x},{y} L {x+w*0.3},{y} L {x+w*0.3},{y+h*0.2} L {x+w*0.1},{y+h*0.2} Z " # Tap
            # Splash / Puddle
            path_d += f"M {x+w*0.2},{y+h*0.2} C {x+w*0.2},{y+h*0.5} {x},{y+h*0.6} {x+w*0.1},{y+h*0.8} "
            path_d += f"C {x+w*0.1},{y+h} {x+w*0.9},{y+h} {x+w*0.9},{y+h*0.8} "
            path_d += f"C {x+w},{y+h*0.6} {x+w*0.8},{y+h*0.4} {x+w*0.6},{y+h*0.5} "
            path_d += f"C {x+w*0.4},{y+h*0.6} {x+w*0.3},{y+h*0.5} {x+w*0.3},{y+h*0.2} Z"
            shape_attrs.update({"d": path_d})
            shape_attrs["fill-rule"] = "evenodd"
            etree.SubElement(group, "path", shape_attrs)
        elif shape == "mobile_phone":
            x, y, w, h = abs_left, abs_top, abs_width, abs_height
            try: r_val = float(rx)
            except (ValueError, TypeError): r_val = min(w, h) * 0.1
            shape_attrs.update({"x": str(x), "y": str(y), "width": str(w), "height": str(h), "rx": str(r_val), "ry": str(r_val)})
            etree.SubElement(group, "rect", shape_attrs)
            # Add screen inner line to make it look like a phone
            screen_attrs = {"x": str(x + w*0.05), "y": str(y + h*0.05), "width": str(w*0.9), "height": str(h*0.8), "rx": str(r_val*0.5), "fill": "none", "stroke": shape_attrs.get("stroke", "#000"), "stroke-width": str(float(shape_attrs.get("stroke-width", "1").replace("px", "")) * 0.5)}
            etree.SubElement(group, "rect", screen_attrs)
            # Add home button
            btn_attrs = {"cx": str(x + w/2), "cy": str(y + h*0.925), "r": str(min(w, h)*0.04), "fill": "none", "stroke": shape_attrs.get("stroke", "#000")}
            etree.SubElement(group, "circle", btn_attrs)
        elif shape == "internet":
            # Cloud/Network node shape
            x, y, w, h = abs_left, abs_top, abs_width, abs_height
            path_d = f"M {x+w*0.2},{y+h*0.6} C {x},{y+h*0.6} {x},{y+h*0.3} {x+w*0.2},{y+h*0.3} "
            path_d += f"C {x+w*0.3},{y} {x+w*0.7},{y} {x+w*0.8},{y+h*0.3} "
            path_d += f"C {x+w},{y+h*0.3} {x+w},{y+h*0.6} {x+w*0.8},{y+h*0.6} Z"
            shape_attrs.update({"d": path_d})
            etree.SubElement(group, "path", shape_attrs)
        elif shape == "globe":
            x, y, w, h = abs_left, abs_top, abs_width, abs_height
            r = min(w, h) / 2
            cx = x + w / 2
            cy = y + h / 2
            # Base circle
            shape_attrs.update({"cx": str(cx), "cy": str(cy), "r": str(r)})
            etree.SubElement(group, "circle", shape_attrs)
            # Lat/Long lines
            line_color = shape_attrs.get("stroke", "#000")
            line_w = str(float(shape_attrs.get("stroke-width", "1").replace("px", "")) * 0.5)
            # Equator
            etree.SubElement(group, "line", x1=str(cx-r), y1=str(cy), x2=str(cx+r), y2=str(cy), stroke=line_color, **{"stroke-width": line_w})
            # Prime Meridian
            etree.SubElement(group, "line", x1=str(cx), y1=str(cy-r), x2=str(cx), y2=str(cy+r), stroke=line_color, **{"stroke-width": line_w})
            # Ellipses for lat/long
            etree.SubElement(group, "ellipse", cx=str(cx), cy=str(cy), rx=str(r*0.5), ry=str(r), fill="none", stroke=line_color, **{"stroke-width": line_w})
            etree.SubElement(group, "ellipse", cx=str(cx), cy=str(cy), rx=str(r), ry=str(r*0.5), fill="none", stroke=line_color, **{"stroke-width": line_w})"""

content = content.replace(search, replace)
with open(filename, "w") as f:
    f.write(content)
