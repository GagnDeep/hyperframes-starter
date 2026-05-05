# 1M+ Context Window in LLMs: Explainer Video Script

## Style Guide
- **Visual Style**: Swiss Pulse (from visual-styles.md)
  - **Mood**: Clinical, precise.
  - **Colors**: Primary `#1a1a1a`, On-Primary `#ffffff`, Accent `#0066FF`.
  - **Typography**: Helvetica Neue (Headline/Stat), Inter (Label/Body).
  - **Motion**: High energy, `expo.out` entry, grid-locked, snaps to a 12-column grid.

## Scene Breakdown & Timing

### Scene 1: The Context Window Evolution (0s - 4s)
- **Concept**: Show how fast context windows grew.
- **Visuals**:
  - Dark grey `#1a1a1a` background with subtle grid lines.
  - Giant text "4K" in the center. (t=0s)
  - Swiftly scales down as the text increments rapidly: "32K" (t=1s), "128K" (t=2s), then "1,000,000+" (t=3s) fills the screen.
  - A small document icon appears at 4K, multiplies to a huge stack at 1M+.
- **Voiceover/Text**: "We went from reading a few pages..." -> "...to digesting entire libraries in one prompt."

### Scene 2: The KV Cache Bottleneck (4s - 10s)
- **Concept**: Why is 1M context hard? The KV Cache.
- **Visuals**:
  - Split screen or centralized block.
  - A block labeled "Keys & Values" starts filling up rapidly as tokens process.
  - A red warning line appears: "VRAM LIMIT".
  - Text: "Every token remembers the past."
  - The bar bursts or stops at the limit.
- **Voiceover/Text**: "But storing the history of every token takes massive memory. The KV cache bottleneck."

### Scene 3: The Solution - RingAttention (10s - 16s)
- **Concept**: How we solve the bottleneck. Blockwise compute / RingAttention.
- **Visuals**:
  - The giant KV Cache block breaks into 4 smaller, manageable blocks.
  - 4 "GPU" icons appear.
  - The blocks pass between the GPUs in a circular/ring motion.
  - Accent blue `#0066FF` highlights the active block being processed.
- **Voiceover/Text**: "The fix? RingAttention. We split the massive attention matrix into blocks and pass them around GPUs in a ring."

### Scene 4: Outcome (16s - 20s)
- **Concept**: Conclusion. Full document understanding.
- **Visuals**:
  - The blocks merge back together into a glowing blue ring.
  - The ring expands to frame the text: "1M+ Context: Infinite Recall."
  - Smooth fade out.
- **Voiceover/Text**: "The result? Near-infinite recall without crashing memory."
