from sivo import Sivo, ProjectConfig, ElementConfig

svg = """<svg viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg" style="background-color: #f4f4f9;">
    <!-- Background styling to look like a simple presentation slide -->
    <text x="200" y="40" font-family="sans-serif" font-size="24" font-weight="bold" fill="#333" text-anchor="middle">SIVO Presentation Mode</text>
    <text x="200" y="60" font-family="sans-serif" font-size="14" fill="#666" text-anchor="middle">Use Left/Right arrow keys to step through the boxes</text>

    <!-- Interactive Elements -->
    <g id="step1" transform="translate(50, 100)">
        <rect width="60" height="60" rx="8" fill="#3b82f6" />
        <text x="30" y="35" font-family="sans-serif" font-size="18" fill="white" font-weight="bold" text-anchor="middle">1</text>
    </g>

    <g id="step2" transform="translate(170, 100)">
        <rect width="60" height="60" rx="8" fill="#10b981" />
        <text x="30" y="35" font-family="sans-serif" font-size="18" fill="white" font-weight="bold" text-anchor="middle">2</text>
    </g>

    <g id="step3" transform="translate(290, 100)">
        <rect width="60" height="60" rx="8" fill="#f59e0b" />
        <text x="30" y="35" font-family="sans-serif" font-size="18" fill="white" font-weight="bold" text-anchor="middle">3</text>
    </g>
</svg>"""

config = ProjectConfig(
    svg_file="none",
    title="Keyboard Presentation Example",
    subtitle="Demonstrates the presentation_order parameter",
    presentation_order=["step1", "step2", "step3"],
    disable_zoom_controls=True,  # Disable manual zoom controls for a cleaner presentation feel
    mappings={
        "step1": ElementConfig(
            html="<h3>Step 1: Introduction</h3><p>This is the first step in our presentation. We zoomed in on the blue box.</p>",
            zoom_on_click=True,
            zoom_level=2.5,
            panel_position="right",
            hover_color="#2563eb"
        ),
        "step2": ElementConfig(
            html="<h3>Step 2: Details</h3><p>Now we have moved to the second step (green box) simply by pressing the Right Arrow key.</p>",
            zoom_on_click=True,
            zoom_level=2.5,
            panel_position="right",
            hover_color="#059669"
        ),
        "step3": ElementConfig(
            html="<h3>Step 3: Conclusion</h3><p>And finally, the third step. Press Left Arrow to go back.</p>",
            zoom_on_click=True,
            zoom_level=2.5,
            panel_position="right",
            hover_color="#d97706"
        )
    }
)

# Some keys in ProjectConfig don't map directly to Sivo.from_string's kwargs
exclude_keys = {"svg_file", "mappings", "connections", "data_binding", "timeline_binding", "live_binding", "api_binding", "scrollytelling", "tour", "layer_toggles", "scratchoff", "proportional_symbols", "spike_map", "hexbin", "dot_density"}
conf_dict = config.model_dump(exclude=exclude_keys, exclude_unset=True)
app = Sivo.from_string(svg, **conf_dict)

for elem_id, elem_conf in config.mappings.items():
    app.map(elem_id, **elem_conf.model_dump(exclude_none=True, exclude_unset=True))

app.to_html("examples/advanced/presentation_mode.html")
print("Saved presentation_mode.html to examples/advanced/.")