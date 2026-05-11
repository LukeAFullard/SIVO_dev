import sys

filename = "src/sivo/core/infographic.py"
with open(filename, "r") as f:
    content = f.read()

search_padding = """        if is_centered or shape in ["fish", "eel", "koura"] or shape.startswith("speech_bubble_"):
            if shape == "speech_bubble_left":
                text_x = abs_left + (abs_width + min(abs_width, abs_height) * 0.15) / 2
            elif shape == "speech_bubble_right":
                text_x = abs_left + (abs_width - min(abs_width, abs_height) * 0.15) / 2
            else:
                text_x = abs_left + abs_width / 2
            text_anchor = "middle"
        else:
            text_x = abs_left + padding_x"""

replace_padding = """        if is_centered or shape in ["fish", "eel", "koura", "mobile_phone", "internet", "globe", "tap_splash"] or shape.startswith("speech_bubble_"):
            if shape == "speech_bubble_left":
                text_x = abs_left + (abs_width + min(abs_width, abs_height) * 0.15) / 2
            elif shape == "speech_bubble_right":
                text_x = abs_left + (abs_width - min(abs_width, abs_height) * 0.15) / 2
            elif shape == "tap_splash":
                # Splashes pool to the right side
                text_x = abs_left + abs_width * 0.55
            else:
                text_x = abs_left + abs_width / 2
            text_anchor = "middle"
        else:
            text_x = abs_left + padding_x"""

content = content.replace(search_padding, replace_padding)

search_width = """            elif shape in ["fish", "koura"]:
                # The text should be bounded heavily within the central body
                return abs_width * 0.5
            elif shape == "eel":
                # Eels are skinny, so text must be very restricted
                return abs_width * 0.3
            else:
                return abs_width - (padding_x * 2)"""

replace_width = """            elif shape in ["fish", "koura"]:
                # The text should be bounded heavily within the central body
                return abs_width * 0.5
            elif shape == "eel":
                # Eels are skinny, so text must be very restricted
                return abs_width * 0.3
            elif shape == "mobile_phone":
                return abs_width * 0.8
            elif shape == "internet":
                return abs_width * 0.7
            elif shape == "globe":
                # Match circular bounds roughly
                cy = abs_top + abs_height / 2
                r = min(abs_width, abs_height) / 2
                dy = abs(y_pos - cy)
                if dy >= r: return 0
                import math
                return 2 * math.sqrt(r**2 - dy**2) * 0.75
            elif shape == "tap_splash":
                # Bounded text into the splash puddle
                if y_pos < abs_top + abs_height * 0.3:
                    return 0 # In the tap nozzle, no text
                return abs_width * 0.6
            else:
                return abs_width - (padding_x * 2)"""

content = content.replace(search_width, replace_width)

search_max_y = """        if shape == "speech_bubble_bottom":
            max_y_limit -= min(abs_width, abs_height) * 0.15
        elif shape in ["fish", "eel", "koura"]:
            max_y_limit = abs_top + abs_height * 0.75 # heavily limit y drop"""

replace_max_y = """        if shape == "speech_bubble_bottom":
            max_y_limit -= min(abs_width, abs_height) * 0.15
        elif shape in ["fish", "eel", "koura"]:
            max_y_limit = abs_top + abs_height * 0.75 # heavily limit y drop
        elif shape == "mobile_phone":
            max_y_limit = abs_top + abs_height * 0.85 # Avoid home button
        elif shape == "internet":
            max_y_limit = abs_top + abs_height * 0.55 # Cloud bounds
        elif shape == "tap_splash":
            # Force text to start lower down, in the splash puddle
            if not title_above:
                padding_y = abs_height * 0.5"""

content = content.replace(search_max_y, replace_max_y)

with open(filename, "w") as f:
    f.write(content)
