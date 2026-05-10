import re

with open("src/sivo/runtime/templates/dashboard_blocks.html", "r") as f:
    content = f.read()

# Notice the overlay logic changed in the replacement script
# It used to say:
# overlay.id = 'sivo-geocoder-overlay-result';
# Let's see if that was deleted or changed by looking at the diff or checking the actual content now
