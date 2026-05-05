import re

def write_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)

# Scene 1: Must have motion and a readable hook word in first 1.5 seconds. Reset local timeline to 0.
scene1 = """<div data-composition-id="scene1" data-width="800" data-height="1040">
<div class="center-flex" style="color: white; font-family: Inter;">
  <div id="s1-word" class="display" style="opacity: 0;">strawberry</div>
  <div id="s1-answer" class="body-text" style="opacity: 0; color: #F43F5E; margin-top: 40px; font-weight: 600;">
    AI: There are <span style="font-family: 'JetBrains Mono'; font-weight: 700; color: #FFF;">2</span> R's.
  </div>
</div>
<script>
  window.__timelines = window.__timelines || {};
  const tl = gsap.timeline({ paused: true });

  // Audio: "Ask any AI to count the R's in strawberry..." (0 to ~3s). Need motion AND hook word in first 1.5s
  tl.fromTo("#s1-word", { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: 0.6, ease: "power2.out" }, 0.2);

  // "...Watch what happens. It confidently says two." (3s to ~5.6s)
  tl.fromTo("#s1-answer", { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: 0.6, ease: "power2.out" }, 2.0);

  // Exit at ~6s (6.2s total scene duration)
  tl.to(["#s1-word", "#s1-answer"], { opacity: 0, y: -40, duration: 0.5, stagger: 0.1, ease: "power2.in" }, 5.5);

  window.__timelines["scene1"] = tl;
</script>
</div>"""
write_file("compositions/scene1.html", scene1)


# Scene 2: Reset timeline to 0. Use 45ms stagger for anime.js. Fix GSAP mapping.
scene2 = """<div data-composition-id="scene2" data-width="800" data-height="1040">
<div class="center-flex" style="color: white;">
  <div id="s2-strawberry" class="display" style="opacity: 0;">strawberry</div>
  <div id="s2-tokens" style="position: absolute; display: flex; gap: 20px;">
    <div class="token-pill pill-indigo" style="opacity: 0; transform: scale(0.5);">[straw]</div>
    <div class="token-pill pill-rose" style="opacity: 0; transform: scale(0.5);">[berry]</div>
  </div>
</div>
<script>
  window.__timelines = window.__timelines || {};
  const tl = gsap.timeline({ paused: true });

  // "Why do the smartest models fumble spelling and math? It's because they don't actually see letters."
  tl.fromTo("#s2-strawberry", { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: 0.8, ease: "power2.out" }, 0.5);

  // "They see tokens." (around 4.9 local time)
  tl.to("#s2-strawberry", { opacity: 0, scale: 1.1, duration: 0.4 }, 4.7);

  const s2Tokens = document.querySelectorAll('#s2-tokens .token-pill');
  if (typeof anime !== 'undefined') {
    const anim = anime({
      targets: s2Tokens,
      scale: [0.5, 1],
      opacity: [0, 1],
      translateX: [-50, 0],
      rotate: [-10, 0],
      duration: 800,
      delay: anime.stagger(45),
      easing: 'easeOutElastic(1, .8)',
      autoplay: false
    });
    window.__hfAnime = window.__hfAnime || [];
    window.__hfAnime.push(anim);
  }

  // We DO need to drive the container visibility if needed, but Anime.js handles the items.
  // Wait, the reviewer said: "the Anime.js animation is completely disjointed from the GSAP timeline and will play invisibly before its GSAP-controlled container actually appears."
  // And "We bind anime play to GSAP timeline position" was WRONG according to skill.md.
  // Actually, HyperFrames adapter seeks Anime.js globally!
  // To delay an Anime.js animation so it starts at local t=4.9s, we MUST use a timeline or delay relative to the composition.
  // The Anime.js adapter seeks based on the *composition's local time*.
  // So we should add a baseline `delay` of 4900ms to the Anime.js animation.
</script>
</div>"""
# Let's fix Anime.js delay to match local time.
scene2 = scene2.replace("delay: anime.stagger(45),", "delay: anime.stagger(45, {start: 4900}),")
scene2 += """
<script>
  // Exit around 7s
  tl.to("#s2-tokens", { opacity: 0, y: -40, duration: 0.5, ease: "power2.in" }, 7.0);
  window.__timelines["scene2"] = tl;
</script>
"""
write_file("compositions/scene2.html", scene2)

# Scene 3: Reset local timeline to 0. (Original global start was 14.0, duration 12.2)
scene3 = """<div data-composition-id="scene3" data-width="800" data-height="1040">
<div class="center-flex" style="color: white; width: 800px;">
  <div id="s3-short" style="display: flex; align-items: center; justify-content: space-between; width: 100%; opacity: 0; margin-bottom: 20px;">
    <div class="body-text">"the"</div>
    <div class="token-pill pill-mint" style="font-size: 40px; padding: 12px 24px;">[the]</div>
  </div>

  <div id="s3-long" style="display: flex; align-items: center; justify-content: space-between; width: 100%; opacity: 0; margin-bottom: 20px;">
    <div class="body-text">"indivisible"</div>
    <div style="display: flex; gap: 10px;">
      <div class="token-pill pill-cyan" style="font-size: 30px; padding: 12px 16px;">[ind]</div>
      <div class="token-pill pill-indigo" style="font-size: 30px; padding: 12px 16px;">[ivis]</div>
      <div class="token-pill pill-rose" style="font-size: 30px; padding: 12px 16px;">[ible]</div>
    </div>
  </div>

  <div id="s3-emoji" style="display: flex; align-items: center; justify-content: space-between; width: 100%; opacity: 0;">
    <div class="display">🚀</div>
    <div class="token-pill pill-yellow" style="font-size: 40px; padding: 12px 24px;">[🚀]</div>
  </div>
</div>
<script>
  window.__timelines = window.__timelines || {};
  const tl = gsap.timeline({ paused: true });

  // "Short words are one token." (Local time 0.3)
  tl.fromTo("#s3-short", { opacity: 0, x: 20 }, { opacity: 1, x: 0, duration: 0.6, ease: "power2.out" }, 0.3);

  // "Long words get chopped into pieces." (Local time 2.5)
  tl.fromTo("#s3-long", { opacity: 0, x: 20 }, { opacity: 1, x: 0, duration: 0.6, ease: "power2.out" }, 2.5);

  // "Even emojis are their own tokens." (Local time 4.8)
  tl.fromTo("#s3-emoji", { opacity: 0, x: 20 }, { opacity: 1, x: 0, duration: 0.6, ease: "power2.out" }, 4.8);

  // Exit around 11.0
  tl.to(["#s3-short", "#s3-long", "#s3-emoji"], { opacity: 0, x: -40, duration: 0.5, stagger: 0.1, ease: "power2.in" }, 11.0);

  window.__timelines["scene3"] = tl;
</script>
</div>"""
write_file("compositions/scene3.html", scene3)

# Scene 4: Reset local timeline to 0. (Original global start was 26.2, duration 14.0)
scene4 = """<div data-composition-id="scene4" data-width="800" data-height="1040">
<div class="center-flex" style="color: white; width: 800px;">
  <div id="s4-english" style="display: flex; flex-direction: column; align-items: center; opacity: 0; margin-bottom: 60px;">
    <div class="body-text" style="color: #34D399; margin-bottom: 20px;">English</div>
    <div class="token-pill pill-mint">hello</div>
  </div>

  <div id="s4-hindi" style="display: flex; flex-direction: column; align-items: center; opacity: 0;">
    <div class="body-text" style="color: #F43F5E; margin-bottom: 20px;">Hindi (नमस्ते)</div>
    <div style="display: flex; gap: 10px;">
      <div class="token-pill pill-rose" style="font-size: 40px; padding: 12px 24px;">[न]</div>
      <div class="token-pill pill-indigo" style="font-size: 40px; padding: 12px 24px;">[म]</div>
      <div class="token-pill pill-cyan" style="font-size: 40px; padding: 12px 24px;">[स]</div>
      <div class="token-pill pill-yellow" style="font-size: 40px; padding: 12px 24px;">[ते]</div>
    </div>
  </div>
</div>
<script>
  window.__timelines = window.__timelines || {};
  const tl = gsap.timeline({ paused: true });

  // "If you say hello in English, that's one cheap token." (Local time: 2.5)
  tl.fromTo("#s4-english", { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: 0.6, ease: "power2.out" }, 2.5);

  // "But translating that exact same meaning into Hindi or Korean, that costs three times as many tokens." (Local time: 7.3)
  tl.fromTo("#s4-hindi", { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: 0.6, ease: "power2.out" }, 7.3);

  // Exit around 13.0
  tl.to(["#s4-english", "#s4-hindi"], { opacity: 0, y: -40, duration: 0.5, stagger: 0.1, ease: "power2.in" }, 13.0);

  window.__timelines["scene4"] = tl;
</script>
</div>"""
write_file("compositions/scene4.html", scene4)

# Scene 5: Reset local timeline to 0. (Original global start was 40.2, duration 10.1)
scene5 = """<div data-composition-id="scene5" data-width="800" data-height="1040">
<div class="center-flex" style="color: white;">
  <div id="s5-tokens" style="display: flex; gap: 20px; opacity: 0;">
    <div class="token-pill pill-indigo" style="opacity: 0.5;">[straw]</div>
    <div id="s5-berry" class="token-pill pill-rose">[be<span id="s5-r1" style="color: #00F0FF; transition: all 0.3s;">r</span><span id="s5-r2" style="color: #00F0FF; transition: all 0.3s;">r</span>y]</div>
  </div>
</div>
<script>
  window.__timelines = window.__timelines || {};
  const tl = gsap.timeline({ paused: true });

  // "So back to our strawberry... It sees the token straw and the token berry." (Local time: 1.3)
  tl.fromTo("#s5-tokens", { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: 0.8, ease: "power2.out" }, 1.3);

  // "The R's were hidden inside the chunks the whole time." (Local time: 6.3)
  tl.to(["#s5-r1", "#s5-r2"], { color: "#FFF", scale: 1.5, duration: 0.4, stagger: 0.1, yoyo: true, repeat: 1 }, 6.3);

  // Exit around 9.5
  tl.to("#s5-tokens", { opacity: 0, scale: 0.9, duration: 0.5, ease: "power2.in" }, 9.5);

  window.__timelines["scene5"] = tl;
</script>
</div>"""
write_file("compositions/scene5.html", scene5)

# Scene 6: Reset local timeline to 0. (Original global start was 50.3, duration 2.7)
scene6 = """<div data-composition-id="scene6" data-width="800" data-height="1040">
<div class="center-flex" style="color: white;">
  <div id="s6-words" class="display" style="opacity: 0; margin-bottom: 40px;">Words.</div>
  <div id="s6-tokens" class="display mono" style="opacity: 0; color: #00F0FF;">[Tokens]</div>
</div>
<script>
  window.__timelines = window.__timelines || {};
  const tl = gsap.timeline({ paused: true });

  // "You speak words." (Local time 0.2)
  tl.fromTo("#s6-words", { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: 0.6, ease: "power2.out" }, 0.2);

  // "It hears tokens." (Local time 1.4)
  tl.fromTo("#s6-tokens", { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: 0.6, ease: "power2.out" }, 1.4);

  window.__timelines["scene6"] = tl;
</script>
</div>"""
write_file("compositions/scene6.html", scene6)
