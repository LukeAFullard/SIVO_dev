import re

file_path = "tests/e2e/test_a11y_ux.py"
with open(file_path, "r") as f:
    content = f.read()

content = content.replace("page.keyboard.press(\"ArrowRight\")", "page.keyboard.press(\"Tab\")")
content = content.replace("page.keyboard.press(\"ArrowLeft\")", "page.keyboard.press(\"Shift+Tab\")")

with open(file_path, "w") as f:
    f.write(content)
