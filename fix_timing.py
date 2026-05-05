import re

with open("index.html", "r") as f:
    html = f.read()

# Fix track indices to avoid exact overlaps
html = re.sub(r'<div id="scene1" class="clip safe-zone" data-start="0" data-duration="6\.2" data-track-index="4"', '<div id="scene1" class="clip safe-zone" data-start="0" data-duration="6.2" data-track-index="4"', html)
html = re.sub(r'<div id="scene2" class="clip safe-zone" data-start="6\.2" data-duration="7\.8" data-track-index="4"', '<div id="scene2" class="clip safe-zone" data-start="6.2" data-duration="7.8" data-track-index="5"', html)
html = re.sub(r'<div id="scene3" class="clip safe-zone" data-start="14\.0" data-duration="12\.2" data-track-index="4"', '<div id="scene3" class="clip safe-zone" data-start="14.0" data-duration="12.2" data-track-index="4"', html)
html = re.sub(r'<div id="scene4" class="clip safe-zone" data-start="26\.2" data-duration="14\.0" data-track-index="4"', '<div id="scene4" class="clip safe-zone" data-start="26.2" data-duration="14.0" data-track-index="5"', html)
html = re.sub(r'<div id="scene5" class="clip safe-zone" data-start="40\.2" data-duration="10\.1" data-track-index="4"', '<div id="scene5" class="clip safe-zone" data-start="40.2" data-duration="10.1" data-track-index="4"', html)
html = re.sub(r'<div id="scene6" class="clip safe-zone" data-start="50\.3" data-duration="2\.7" data-track-index="4"', '<div id="scene6" class="clip safe-zone" data-start="50.3" data-duration="2.7" data-track-index="5"', html)

with open("index.html", "w") as f:
    f.write(html)
