import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from sivo import Sivo

svg_string = """
<svg viewBox="0 0 500 200" xmlns="http://www.w3.org/2000/svg">
  <!-- Twitter Logo -->
  <g id="btn_twitter" transform="translate(10, 10)">
    <rect width="80" height="80" rx="15" fill="#1DA1F2"/>
    <path d="M56 31c-1.4 1-3.1 1.6-4.8 1.9 1.8-1 3.1-2.6 3.8-4.6-1.5.9-3.2 1.5-5 1.9-1.5-1.5-3.6-2.5-5.9-2.5-4.5 0-8.2 3.7-8.2 8.2 0 .6.1 1.3.2 1.9-6.8-.3-12.8-3.6-16.8-8.5-.7 1.2-1.1 2.6-1.1 4.1 0 2.8 1.4 5.4 3.6 6.9-1.3 0-2.6-.4-3.7-1v.1c0 4 2.8 7.3 6.6 8.1-.7.2-1.4.3-2.1.3-.5 0-1 0-1.5-.1 1 3.3 4.1 5.6 7.7 5.7-2.8 2.2-6.3 3.5-10.2 3.5-.7 0-1.3 0-1.9-.1 3.6 2.3 8 3.7 12.6 3.7 15.2 0 23.5-12.6 23.5-23.5v-1.1c1.7-1.2 3.1-2.6 4.2-4.3-1.5.7-3.1 1.1-4.8 1.3 1.8-1.2 3-2.9 3.6-5z" fill="white"/>
  </g>

  <!-- Instagram Logo -->
  <g id="btn_insta" transform="translate(110, 10)">
    <rect width="80" height="80" rx="15" fill="#C13584"/>
    <path d="M40 25c-8.3 0-15 6.7-15 15s6.7 15 15 15 15-6.7 15-15-6.7-15-15-15zm0 24.5c-5.2 0-9.5-4.3-9.5-9.5S34.8 30.5 40 30.5 49.5 34.8 49.5 40 45.2 49.5 40 49.5zm9.8-19.3c-2 0-3.6-1.6-3.6-3.6s1.6-3.6 3.6-3.6 3.6 1.6 3.6 3.6-1.6 3.6-3.6 3.6zM60 40c0-6.1-.1-12.1-.4-18.1-.3-6.5-5.2-11.4-11.7-11.7C41.9 9.9 35.9 9.8 29.8 9.8s-12.1.1-18.1.4c-6.5.3-11.4 5.2-11.7 11.7C-.1 27.9-.2 33.9-.2 40s.1 12.1.4 18.1c.3 6.5 5.2 11.4 11.7 11.7 6.1.3 12.1.4 18.1.4s12.1-.1 18.1-.4c6.5-.3 11.4-5.2 11.7-11.7.3-6 .4-12 .4-18.1zM54 53.6c-1.3 3.3-3.8 5.8-7.1 7.1-4.9 1.9-16.5 1.5-26.9 1.5-10.4 0-22 .4-26.9-1.5-3.3-1.3-5.8-3.8-7.1-7.1-1.9-4.9-1.5-16.5-1.5-26.9 0-10.4-.4-22 1.5-26.9 1.3-3.3 3.8-5.8 7.1-7.1C18-.2 29.6.2 40 .2c10.4 0 22-.4 26.9 1.5 3.3 1.3 5.8 3.8 7.1 7.1 1.9 4.9 1.5 16.5 1.5 26.9 0 10.4.4 22-1.5 26.9z" fill="white" transform="scale(0.8) translate(10, 10)"/>
  </g>

  <!-- TikTok Logo -->
  <g id="btn_tiktok" transform="translate(210, 10)">
    <rect width="80" height="80" rx="15" fill="#000000"/>
    <path d="M47.7 21v14.1c4.5 0 8.5 2.1 11.3 5.4V26.4c-2.8-1-5.9-1.5-9.1-1.5v-3.9zm-13.6 0v27.2c0 3.7-3 6.8-6.8 6.8s-6.8-3-6.8-6.8 3-6.8 6.8-6.8c1.3 0 2.5.4 3.5 1.1v-6.9c-1.1-.6-2.3-1-3.5-1-7.5 0-13.6 6.1-13.6 13.6s6.1 13.6 13.6 13.6 13.6-6.1 13.6-13.6V21H34.1z" fill="white" transform="scale(1.2) translate(12, 10)"/>
  </g>

  <!-- Facebook Logo -->
  <g id="btn_fb" transform="translate(310, 10)">
    <rect width="80" height="80" rx="15" fill="#4267B2"/>
    <path d="M50 20h-7c-5.5 0-10 4.5-10 10v6h-7v8h7v26h10V44h8l1-8h-9v-4c0-2.2 1.8-4 4-4h5v-8z" fill="white" transform="scale(1.2) translate(3, 3)"/>
  </g>
</svg>
"""

sivo_app = Sivo.from_string(svg_string)

# We use valid post URLs that actually exist for the demo
# Setting default_color directly overrides ECharts' gray default, making the buttons look "proper" from the start.
sivo_app.map("btn_twitter", social={"provider": "twitter", "url": "https://twitter.com/OpenAI/status/1758231365825700200"}, tooltip="Twitter Embed", hover_color="#0d8bd9", color="#1da1f2")
sivo_app.map("btn_insta", social={"provider": "instagram", "url": "https://www.instagram.com/p/C0f9W5aIxtA/"}, tooltip="Instagram Embed", hover_color="#a0296e", color="#c13584")
sivo_app.map("btn_tiktok", social={"provider": "tiktok", "url": "https://www.tiktok.com/@tiktok/video/7106594312293371179"}, tooltip="TikTok Embed", hover_color="#111111", color="#333333")
sivo_app.map("btn_fb", social={"provider": "facebook", "url": "https://www.facebook.com/20531316728/posts/10154009990506729/"}, tooltip="Facebook Embed", hover_color="#365899", color="#4267b2")

sivo_app.to_html("examples/9_social_embeds/output.html")
print("Social embeds test generated at examples/9_social_embeds/output.html")
