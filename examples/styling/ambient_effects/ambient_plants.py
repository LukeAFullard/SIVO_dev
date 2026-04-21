import os
from sivo import Sivo

def main():
    svg_content = """<svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="sunsetGrad" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stop-color="#FF7F50"/>
          <stop offset="50%" stop-color="#FFD700"/>
          <stop offset="100%" stop-color="#FFEC8B"/>
        </linearGradient>
        <linearGradient id="groundGrad" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stop-color="#556B2F"/>
          <stop offset="100%" stop-color="#2F4F4F"/>
        </linearGradient>
      </defs>

      <!-- Sunset Sky -->
      <rect width="800" height="400" fill="url(#sunsetGrad)"/>

      <!-- Sun -->
      <circle cx="400" cy="350" r="100" fill="#FF4500" opacity="0.9"/>

      <!-- Ground -->
      <rect x="0" y="400" width="800" height="200" fill="url(#groundGrad)"/>

      <!-- Distant Mountains -->
      <path d="M-50,450 L100,250 L300,450 Z" fill="#8B4513" opacity="0.6"/>
      <path d="M200,450 L400,200 L650,450 Z" fill="#A0522D" opacity="0.5"/>
      <path d="M500,450 L650,300 L850,450 Z" fill="#8B4513" opacity="0.7"/>

      <!-- Tree Trunks and Silhouettes (Foreground) -->
      <rect x="150" y="300" width="20" height="150" fill="#3E2723"/>
      <path d="M160,350 Q120,250 140,200 Q180,280 160,350 Z" fill="#3E2723"/>

      <rect x="600" y="250" width="30" height="200" fill="#3E2723"/>
      <path d="M615,300 Q660,200 680,150 Q600,220 615,300 Z" fill="#3E2723"/>
      <path d="M615,320 Q550,220 530,170 Q590,240 615,320 Z" fill="#3E2723"/>

    </svg>"""

    app = Sivo.from_string(
        svg_content,
        ambient_effect="plants",
        ambient_speed=2.0,
        title="Ambient Plants Effect",
        subtitle="With speed multiplier 2.0 (Sunset Silhouette)",
        transparent_template_lines=True,
        default_panel_position="none", # Explicitly declaring none
        disable_panel=True             # Since this example is non-interactive, panel is disabled
    )

    output_file = os.path.join(os.path.dirname(__file__), 'ambient_plants.html')
    app.to_html(output_file)
    print(f"Saved {output_file}")

if __name__ == "__main__":
    main()
