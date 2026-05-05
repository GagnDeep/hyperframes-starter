# Plan: Tokenization Explainer Reel

## 1. Project Setup
- We need to create the basic composition `index.html`.
- Theme: deep ink-blue background (`#0A0A1A`), gradient accents (cyan `#00F0FF`, indigo `#6366F1`, rose `#F43F5E`, yellow `#FBBF24`, mint `#34D399`).
- Fonts: Inter (body/words) and JetBrains Mono (token IDs/numbers).
- Format: 1080x1920 (9:16), 60fps. Duration ~53 seconds (from narration transcript).
- We already have `assets/narration.wav` and `transcript.json`.

## 2. Audio & Captions
- Add `<audio>` for `narration.wav`.
- The video needs burned-in captions, following the audio timing.
- Will create a caption rendering logic using GSAP timeline mapping to `transcript.json`.
- Caption text big, phone-readable (42-52px minimum, headlines 96-132px).

## 3. Scenes & Visuals (The "Pill" Motif)
- Visual motif: Tokens are colored, rounded pills (`border-radius: 9999px`, padding, colored background/border).
- **Scene 1 (0-6s):** Hook. "Ask any AI to count the R's in strawberry..."
  - Show "strawberry" text. Show ChatGPT-like incorrect answers ("two").
- **Scene 2 (6-18s):** Reveal.
  - "They don't actually see letters. They see tokens."
  - Animate "strawberry" breaking apart into `[straw]` and `[berry]` pills.
  - Show short words becoming one token, long words into pieces, emojis into tokens.
- **Scene 3 (18-28s):** Byte-pair encoding.
  - Letters merging into common pairs.
- **Scene 4 (28-40s):** Language Tax.
  - Show "hello" vs Hindi/Korean.
  - Hindi/Korean expanding into many token pills.
- **Scene 5 (40-50s):** Callback to Strawberry.
  - Show `[straw]` and `[berry]` again. Highlight the R's inside the "berry" pill, showing the model can't look inside.
- **Scene 6 (50-53s):** Outro. "You speak words. It hears tokens."

## 4. Animation implementation
- Use GSAP for primary timeline.
- Use Anime.js for secondary animation (staggered token pills splitting).
- Use `css-animations` for ambient backgrounds (e.g. slow breathing radial gradients).

## 5. Build and Verify
- Implement all HTML, CSS, JS in `index.html`.
- Run `npm run check` (`hyperframes lint`, `validate`, `inspect`).
- Fix any layout overflows or contrast issues.

## 6. Pre-commit & Render
- Call `pre_commit_instructions` and follow steps.
- Run `npm run render -- --fps 60 --quality high --output reel.mp4`
- Submit branch.
