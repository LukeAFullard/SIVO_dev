from sivo import Sivo
import os

svg = '''<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <rect width="400" height="400" fill="#f8fafc" />
    <circle id="circle1" cx="100" cy="200" r="80" fill="#3b82f6" />
    <text x="100" y="200" font-family="sans-serif" font-size="14" fill="#fff" text-anchor="middle" pointer-events="none">None</text>
    <circle id="circle2" cx="300" cy="200" r="80" fill="#ef4444" />
    <text x="300" y="200" font-family="sans-serif" font-size="14" fill="#fff" text-anchor="middle" pointer-events="none">Right Panel</text>
    <text x="200" y="50" font-family="sans-serif" font-size="16" fill="#333" text-anchor="middle" pointer-events="none">Test: panel_position="none"</text>
    <text x="200" y="350" font-family="sans-serif" font-size="12" fill="#666" text-anchor="middle" pointer-events="none">1. Click Red to open. 2. Click Blue to close.</text>
</svg>'''

map = Sivo.from_string(svg, theme="light")
map.map("circle1", html="<h2>This should NOT appear in a sidebar!</h2>", panel_position="none")
map.map("circle2", html="<h2>This is the right sidebar</h2><p>Clicking the blue circle should close this.</p>", panel_position="right")

map.to_html('test_panel_position.html')
print("Generated test_panel_position.html")
