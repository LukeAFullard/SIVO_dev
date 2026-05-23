import sys

with open("examples/mysite/title_page/subpage/air/science/generate_dashboard.py", "r") as f:
    content = f.read()

content = content.replace("if taihape_last_exc_date and taihape_exc_val > 0:", "if taihape_last_exc_date:")

with open("examples/mysite/title_page/subpage/air/science/generate_dashboard.py", "w") as f:
    f.write(content)
