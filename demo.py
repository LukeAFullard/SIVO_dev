from sivo import SivoDashboard, Sivo
dashboard = SivoDashboard(title="Test Navigation Menu", navigation_menu=[{"label": "Home", "url": "#"}, {"label": "About", "url": "#"}])
dashboard.add_text_block("text_block", "Hello this is a test. We should be able to scroll to see the fixed navigation menu.")
for i in range(10):
    dashboard.add_text_block(f"text_block_{i}", "Placeholder text " * 100)
with open("index.html", "w") as f:
    f.write(dashboard.to_html())
