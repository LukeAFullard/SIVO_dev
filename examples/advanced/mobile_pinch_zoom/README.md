# Mobile Pinch Zoom

## Description
Ensure PYTHONPATH is set so sivo module can be found

## Relevant Code
```python
    app = Sivo.from_string('<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><rect id="box" x="10" y="10" width="80" height="80" fill="lightblue"/></svg>')
    app.map("box", html="<h2>Pinch to zoom!</h2><p>Try it on mobile.</p>", hover_color="lightgreen")
    html_content = app.to_html()
```
