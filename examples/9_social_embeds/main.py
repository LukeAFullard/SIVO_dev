import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from sivo import Sivo

svg_string = """
<svg viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect id="btn_twitter" x="10" y="10" width="100" height="50" fill="#1DA1F2"/>
  <rect id="btn_insta" x="120" y="10" width="100" height="50" fill="#C13584"/>
  <rect id="btn_tiktok" x="230" y="10" width="100" height="50" fill="#000000"/>
  <rect id="btn_fb" x="10" y="70" width="100" height="50" fill="#4267B2"/>
</svg>
"""

sivo_app = Sivo.from_string(svg_string)

sivo_app.map("btn_twitter", social={"provider": "twitter", "url": "https://x.com/OpenAI/status/1758231365825700200"})
sivo_app.map("btn_insta", social={"provider": "instagram", "url": "https://www.instagram.com/p/C3fL7t8LkQc/"})
sivo_app.map("btn_tiktok", social={"provider": "tiktok", "url": "https://www.tiktok.com/@tiktok/video/7328904576136056106"})
sivo_app.map("btn_fb", social={"provider": "facebook", "url": "https://www.facebook.com/zuck/posts/pfbid0259eAijz6kK2v2R9fUuYv3wT9qL5qH7N7tCq6R8jY1Y1Y1Y1Y1Y1Y1Y1Y1Y1Y1Y1l"})

sivo_app.to_html("examples/9_social_embeds/output.html")
print("Social embeds test generated at examples/9_social_embeds/output.html")
