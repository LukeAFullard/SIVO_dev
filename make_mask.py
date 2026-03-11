import base64
from PIL import Image, ImageDraw

# Create a 400x400 transparent image
img = Image.new('RGBA', (400, 400), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Draw a large black circle in the middle
draw.ellipse((50, 50, 350, 350), fill='black')

img.save('large_mask.png')

with open('large_mask.png', 'rb') as f:
    b64_str = base64.b64encode(f.read()).decode('utf-8')

print(f"data:image/png;base64,{b64_str}")
