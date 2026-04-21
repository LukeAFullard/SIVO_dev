# Professional Styling

This example demonstrates how to apply advanced, professional styling to SIVO interactive elements. Specifically, it showcases how to inject a custom CSS theme that targets SIVO's `#info-panel` UI component, giving it a sleek, dark glassmorphism aesthetic.

### What is being tested/showcased:
- **Custom CSS Injection**: Passing a large block of custom CSS to `sivo_app.to_html(..., custom_css=professional_css)` to overwrite the default SIVO panel styles.
- **Glassmorphism UI**: Using CSS attributes like `backdrop-filter: blur(16px)` and semi-transparent `rgba` backgrounds on SIVO UI elements (`#info-panel`, `.close-btn`, etc.).
- **Panel Position**: Utilizing the `panel_position` argument (set to `"right"`) in `sivo_app.map()` so that the side panel opens up to reveal the content. (By default, it is set to `"none"`, so no side panel would appear without specifying it).
- **Inline Status Badges**: Injecting structured HTML with CSS classes (like `<span class="status-badge">`) within the `html` parameter of `sivo_app.map()` to create beautiful data tooltips.
- **Hover Glows and Colors**: Passing `glow=True` and specific highlight hex colors (`color`, `hover_color`) to make elements 'pop' upon interaction.

### Related Code Bits

**Defining the CSS Theme:**
```python
professional_css = """
/* Sleek Glassmorphism Info Panel */
#info-panel {
    background: rgba(15, 23, 42, 0.85) !important;
    backdrop-filter: blur(16px);
    color: #f8fafc !important;
    /* ... */
}
"""
```

**Injecting CSS into the App Build:**
```python
sivo_app.to_html(output_path, custom_css=professional_css)
```

**Mapping the Elements with Content and Panel Position:**
```python
sivo_app.map(
    element_id="server-alpha",
    tooltip="Server Alpha Details",
    html="""
    <h3>Server Alpha</h3>
    <span class="status-badge">● Online</span>
    <p>This server handles primary database routing...</p>
    """,
    panel_position="right",  # Ensure the panel opens
    color="#bae6fd",
    hover_color="#7dd3fc",
    glow=True
)
```

## Running the Example
```bash
python3 main.py
```
After running, open the generated `output.html` in your web browser and click on "Server Alpha" or "Server Beta" to see the professionally styled side panel.