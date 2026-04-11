import os
from sivo import Sivo, SivoDashboard

# --- 1. Base Sivo Registration Map ---
map_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
    <rect id="bg" width="800" height="600" fill="#f1f5f9" />
    <circle id="event_nyc" cx="200" cy="300" r="80" fill="#3b82f6" />
    <circle id="event_ldn" cx="600" cy="300" r="80" fill="#f59e0b" />
    <text x="200" y="420" font-family="sans-serif" font-size="20" fill="#333" pointer-events="none" text-anchor="middle">New York Summit</text>
    <text x="600" y="420" font-family="sans-serif" font-size="20" fill="#333" pointer-events="none" text-anchor="middle">London Expo</text>
</svg>"""

# Using default_panel_position="none" because the dashboard uses a Details Panel layout block
sivo_map = Sivo.from_string(map_svg, theme="light", title="Global Developer Events", default_panel_position="none")

# --- 2. Advanced Feature: Rich External Integrations via HTML Block ---
# We can use SivoDashboard's `add_html_block` to embed fully functional third-party widgets,
# like a live Typeform, a Calendly scheduler, a Stripe checkout, or a Google Form.
# In this case, we embed a standard registration iframe that sits alongside the map.

registration_form_html = """
<div style="height: 100%; display: flex; flex-direction: column;">
    <h3 style="color: #1e293b; margin-top: 0;">Register Your Attendance</h3>
    <p style="color: #64748b;">Select an event on the map to view schedule details, then fill out the form below to secure your spot.</p>

    <!-- This is a placeholder for a real iframe, e.g., src="https://docs.google.com/forms/..." -->
    <div style="flex: 1; background: #e2e8f0; border-radius: 8px; display: flex; align-items: center; justify-content: center; min-height: 400px;">
        <span style="color: #64748b; font-family: monospace;">[ iframe src="https://your-registration-form-url" ]</span>
    </div>
</div>
"""

# Map standard click behaviors for the details panel
sivo_map.map(
    "event_nyc",
    hover_color="#2563eb",
    glow=True,
    html="<h4>New York Schedule</h4><ul><li>09:00 AM - Keynote</li><li>11:00 AM - AI Workshops</li><li>02:00 PM - Networking</li></ul>",
)

sivo_map.map(
    "event_ldn",
    hover_color="#d97706",
    glow=True,
    html="<h4>London Schedule</h4><ul><li>10:00 AM - Opening Ceremony</li><li>12:00 PM - Fintech Panel</li><li>03:00 PM - Happy Hour</li></ul>",
)

# --- 3. Assemble the Integration Dashboard ---
dashboard = SivoDashboard(title="Event Registration Portal")

# The CSS grid automatically arranges the map on the left...
dashboard.add_sivo_block("event_map", sivo_map)

# ...the interactive schedule details panel in the middle...
dashboard.add_details_panel("schedule", title="Event Schedule", placeholder="Click an event to view the agenda.")

# ...and the external registration form on the right.
dashboard.add_html_block("registration", registration_form_html)

# Export the dashboard
output_file = os.path.join(os.path.dirname(__file__), "output.html")
dashboard.to_html(output_file)

print(f"Successfully generated integration dashboard: {output_file}")
