import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from sivo import Sivo

svg_string = """
<svg viewBox="0 0 800 300" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Authentic Instagram Gradient -->
    <linearGradient id="instaGrad" x1="0%" y1="100%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#f09433" />
      <stop offset="25%" stop-color="#e6683c" />
      <stop offset="50%" stop-color="#dc2743" />
      <stop offset="75%" stop-color="#cc2366" />
      <stop offset="100%" stop-color="#bc1888" />
    </linearGradient>
    <filter id="shadow" x="-10%" y="-10%" width="130%" height="130%">
      <feDropShadow dx="0" dy="8" stdDeviation="6" flood-color="#000000" flood-opacity="0.12"/>
    </filter>
  </defs>

  <rect width="800" height="300" fill="#f8fafc" rx="20" />

  <text x="400" y="55" font-family="system-ui, -apple-system, sans-serif" font-size="30" font-weight="700" fill="#1e293b" text-anchor="middle">Social Media Integrations</text>
  <text x="400" y="85" font-family="system-ui, -apple-system, sans-serif" font-size="16" font-weight="400" fill="#64748b" text-anchor="middle">Click the interactive buttons below to embed content directly into the canvas side panel.</text>

  <!-- Wikipedia Icon Group -->
  <g transform="translate(100, 120)" filter="url(#shadow)">
    <!-- iOS squircle styling -->
    <rect width="120" height="120" rx="28" fill="#ffffff" />
    <!-- Authentic Wikipedia "W" Path -->
    <g transform="translate(30, 30) scale(0.6)">
      <path d="M78.683 0h-30.82l-9.158 59.489-13.628-59.489h-24.966l33.259 100h20.732l10.87-44.593 11.237 44.593h20.573l34.408-100h-24.878l-14.498 57.51-13.131-57.51zm21.317 0h-25.044l13.131 57.51-1.393 5.485c-.48 1.884-.816 3.82-1.002 5.795l14.308-68.79z" fill="#000000"/>
    </g>
    <!-- Invisible hitbox for SIVO interactions -->
    <rect id="btn_wiki" width="120" height="120" rx="28" fill="transparent" opacity="0" style="cursor:pointer;" />
  </g>

  <!-- Instagram Logo Group -->
  <g transform="translate(260, 120)" filter="url(#shadow)">
    <rect width="120" height="120" rx="28" fill="url(#instaGrad)"/>
    <!-- Authentic Instagram SVG Path -->
    <g transform="translate(30, 30) scale(0.6)">
      <path d="M50 8.6c13.4 0 15 .1 20.3.3 4.9.2 7.6 1 9.4 1.7 2.4.9 4.1 2 5.9 3.8 1.8 1.8 2.9 3.5 3.8 5.9.7 1.8 1.5 4.5 1.7 9.4.2 5.3.3 6.9.3 20.3s-.1 15-.3 20.3c-.2 4.9-1 7.6-1.7 9.4-.9 2.4-2 4.1-3.8 5.9-1.8 1.8-3.5 2.9-5.9 3.8-1.8.7-4.5 1.5-9.4 1.7-5.3.2-6.9.3-20.3.3s-15-.1-20.3-.3c-4.9-.2-7.6-1-9.4-1.7-2.4-.9-4.1-2-5.9-3.8-1.8-1.8-2.9-3.5-3.8-5.9-.7-1.8-1.5-4.5-1.7-9.4-.2-5.3-.3-6.9-.3-20.3s.1-15 .3-20.3c.2-4.9 1-7.6 1.7-9.4.9-2.4 2-4.1 3.8-5.9 1.8-1.8 3.5-2.9 5.9-3.8 1.8-.7 4.5-1.5 9.4-1.7 5.3-.2 6.9-.3 20.3-.3m0-8.6C36.4 0 34.7.1 29.4.3c-5.3.2-8.9 1-12.1 2.2-3.3 1.3-6.1 3.1-8.9 5.9s-4.6 5.6-5.9 8.9C1.3 20.5.5 24.1.3 29.4.1 34.7 0 36.4 0 50s.1 15.3.3 20.6c.2 5.3 1 8.9 2.2 12.1 1.3 3.3 3.1 6.1 5.9 8.9s5.6 4.6 8.9 5.9c3.2 1.2 6.8 2 12.1 2.2 5.3.2 7 .3 20.6.3s15.3-.1 20.6-.3c5.3-.2 8.9-1 12.1-2.2 3.3-1.3 6.1-3.1 8.9-5.9s4.6-5.6 5.9-8.9c1.2-3.2 2-6.8 2.2-12.1.2-5.3.3-7 .3-20.6s-.1-15.3-.3-20.6c-.2-5.3-1-8.9-2.2-12.1-1.3-3.3-3.1-6.1-5.9-8.9s-5.6-4.6-8.9-5.9C89.5 1.3 85.9.5 80.6.3 75.3.1 73.6 0 50 0z" fill="#ffffff"/>
      <path d="M50 24.3c-14.2 0-25.7 11.5-25.7 25.7S35.8 75.7 50 75.7 75.7 64.2 75.7 50 64.2 24.3 50 24.3zm0 42.8c-9.4 0-17.1-7.7-17.1-17.1S40.6 32.9 50 32.9 67.1 40.6 67.1 50 59.4 67.1 50 67.1z" fill="#ffffff"/>
      <circle cx="76.7" cy="23.3" r="5.7" fill="#ffffff"/>
    </g>
    <!-- Invisible hitbox for SIVO interactions -->
    <rect id="btn_insta" width="120" height="120" rx="28" fill="transparent" opacity="0" style="cursor:pointer;" />
  </g>

  <!-- TikTok Logo Group -->
  <g transform="translate(420, 120)" filter="url(#shadow)">
    <rect width="120" height="120" rx="28" fill="#000000"/>
    <!-- Authentic TikTok Path -->
    <g transform="translate(30, 30) scale(0.6)">
      <path d="M54.1 0h-16v65.6c0 8.3-6.7 15.1-15.1 15.1-8.3 0-15.1-6.7-15.1-15.1s6.7-15.1 15.1-15.1c1.5 0 2.9.2 4.3.6v-16c-1.4-.2-2.8-.3-4.3-.3-17.1 0-31.1 13.9-31.1 31.1S26 96.9 43.1 96.9s31.1-13.9 31.1-31.1V31.5c7.3 5.4 16.4 8.7 26.2 8.7V24c-11.4 0-21.4-5.2-26.2-13.3V0h-.1z" fill="#ffffff"/>
      <path d="M54.1 0v10.8c4.8 8.1 14.8 13.3 26.2 13.3V8.1c-10.7 0-19.8-5.3-25.2-13.4l-.1-.2v5.5z" fill="#fe2c55"/>
      <path d="M22.9 56.1c-1.4-.4-2.8-.6-4.3-.6-8.3 0-15.1 6.7-15.1 15.1s6.7 15.1 15.1 15.1 15.1-6.7 15.1-15.1v-3.7l-2.4 1c-4.4 1.8-9.3 2.8-14.4 2.8v-16c1.4.2 2.8.5 4.1 1.1l1.9.8.1-1.1v.6z" fill="#00f2fe"/>
    </g>
    <!-- Invisible hitbox for SIVO interactions -->
    <rect id="btn_tiktok" width="120" height="120" rx="28" fill="transparent" opacity="0" style="cursor:pointer;" />
  </g>

  <!-- Website Iframe Logo Group -->
  <g transform="translate(580, 120)" filter="url(#shadow)">
    <rect width="120" height="120" rx="28" fill="#3b82f6"/>
    <!-- Authentic generic globe/website icon -->
    <g transform="translate(30, 30) scale(0.6)">
      <path d="M50 0C22.4 0 0 22.4 0 50s22.4 50 50 50 50-22.4 50-50S77.6 0 50 0zm0 8.3c8.7 0 16.2 10.9 20.3 25.8H29.7C33.8 19.2 41.3 8.3 50 8.3zM8.3 50c0-6 .1-11.7.3-17.2h19.5c-.2 5.5-.3 11.2-.3 17.2 0 6 .1 11.7.3 17.2H8.6c-.2-5.5-.3-11.2-.3-17.2zm41.7 41.7c-8.7 0-16.2-10.9-20.3-25.8h40.6C66.2 80.8 58.7 91.7 50 91.7zm22-30.3H28.1c.1-3.8.2-7.6.2-11.4 0-3.8-.1-7.6-.2-11.4h43.8c.1 3.8.2 7.6.2 11.4 0 3.8-.1 7.6-.2 11.4zm1.5-17.1h19.5c.2 5.5.3 11.2.3 17.2 0 6-.1 11.7-.3 17.2H71.8c.2-5.5.3-11.2.3-17.2 0-6-.1-11.7-.3-17.2z" fill="#ffffff"/>
    </g>
    <!-- Invisible hitbox for SIVO interactions -->
    <rect id="btn_web" width="120" height="120" rx="28" fill="transparent" opacity="0" style="cursor:pointer;" />
  </g>
</svg>
"""

sivo_app = Sivo.from_string(svg_string)

# We use robust, highly-available URLs for the demo
sivo_app.map(
    "btn_wiki",
    social={"provider": "wikipedia", "url": "https://en.wikipedia.org/wiki/Python_(programming_language)"},
    tooltip="Wikipedia API Fetch",
    panel_position="right",
    color="transparent",
    hover_color="rgba(255, 255, 255, 0.2)"
)

sivo_app.map(
    "btn_insta",
    social={"provider": "instagram", "url": "https://www.instagram.com/p/B_X_yR_A4rV/"},
    tooltip="Instagram Embed",
    panel_position="right",
    color="transparent",
    hover_color="rgba(255, 255, 255, 0.2)"
)

sivo_app.map(
    "btn_tiktok",
    social={"provider": "tiktok", "url": "https://www.tiktok.com/@scout2015/video/6718335390845095173"},
    tooltip="TikTok Embed",
    panel_position="right",
    color="transparent",
    hover_color="rgba(255, 255, 255, 0.2)"
)

sivo_app.map(
    "btn_web",
    social={"provider": "website", "url": "https://example.com"},
    tooltip="Generic Website Embed",
    panel_position="right",
    color="transparent",
    hover_color="rgba(255, 255, 255, 0.2)"
)

output_path = os.path.join(os.path.dirname(__file__), "output.html")
sivo_app.to_html(output_path)
print(f"Social embeds test generated at {output_path}")
