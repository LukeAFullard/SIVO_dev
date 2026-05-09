import re

with open("examples/web_app/src/annotator.js", "r") as f:
    text = f.read()

matches = re.finditer(r"updateShapeList\(\)", text)
for m in matches:
    start = max(0, m.start() - 200)
    end = min(len(text), m.end() + 200)
    print(f"--- MATCH AT {m.start()} ---")
    print(text[start:end])
