import re

with open("index.html", "r") as f:
    html = f.read()

# Add CSS animations for ambient backgrounds
css_anim = """
      /* Ambient Animations */
      .bg-gradient-radial {
        animation: breathe-radial 8s ease-in-out infinite both;
      }
      .bg-gradient-top {
        animation: breathe-top 10s ease-in-out infinite both;
      }
      @keyframes breathe-radial {
        0%, 100% { transform: scale(1); opacity: 0.8; }
        50% { transform: scale(1.2); opacity: 1; }
      }
      @keyframes breathe-top {
        0%, 100% { opacity: 0.6; transform: translateY(0); }
        50% { opacity: 1; transform: translateY(50px); }
      }
"""
html = html.replace("/* Captions Container */", css_anim + "      /* Captions Container */")

# Fix scene timings
html = re.sub(r'<div id="scene1".*?></div>', '<div id="scene1" class="clip safe-zone" data-start="0" data-duration="6.2" data-track-index="4" data-composition-id="scene1" data-composition-src="compositions/scene1.html"></div>', html)
html = re.sub(r'<div id="scene2".*?></div>', '<div id="scene2" class="clip safe-zone" data-start="6.2" data-duration="7.8" data-track-index="4" data-composition-id="scene2" data-composition-src="compositions/scene2.html"></div>', html)
html = re.sub(r'<div id="scene3".*?></div>', '<div id="scene3" class="clip safe-zone" data-start="14.0" data-duration="12.2" data-track-index="4" data-composition-id="scene3" data-composition-src="compositions/scene3.html"></div>', html)
html = re.sub(r'<div id="scene4".*?></div>', '<div id="scene4" class="clip safe-zone" data-start="26.2" data-duration="14.0" data-track-index="4" data-composition-id="scene4" data-composition-src="compositions/scene4.html"></div>', html)
html = re.sub(r'<div id="scene5".*?></div>', '<div id="scene5" class="clip safe-zone" data-start="40.2" data-duration="10.1" data-track-index="4" data-composition-id="scene5" data-composition-src="compositions/scene5.html"></div>', html)
html = re.sub(r'<div id="scene6".*?></div>', '<div id="scene6" class="clip safe-zone" data-start="50.3" data-duration="2.7" data-track-index="4" data-composition-id="scene6" data-composition-src="compositions/scene6.html"></div>', html)

with open("index.html", "w") as f:
    f.write(html)
