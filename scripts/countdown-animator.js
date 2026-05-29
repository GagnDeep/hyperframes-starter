// Reusable countdown animation logic
window.createCountdownAnimation = function(tl, wrapperId, startNum, duration) {
  const timePerNum = duration / startNum;
  const wrapper = document.getElementById(wrapperId);

  if (!wrapper) return;

  // Create number elements
  for (let i = startNum; i > 0; i--) {
    const el = document.createElement("div");
    el.className = "count-number";
    el.id = `count-num-${i}`;
    el.textContent = i;
    wrapper.appendChild(el);

    const startTime = (startNum - i) * timePerNum;

    // Animate each number
    tl.fromTo(`#count-num-${i}`,
      { scale: 0.5, opacity: 0 },
      { scale: 1, opacity: 1, duration: 0.4, ease: "back.out(1.5)" },
      startTime
    );

    tl.to(`#count-num-${i}`,
      { scale: 1.5, opacity: 0, duration: 0.4, ease: "power2.in" },
      startTime + timePerNum - 0.4
    );

    // Audio-reactive pulse glow on each beat
    tl.fromTo("#ring-1",
      { scale: 0.8, opacity: 0.8, borderWidth: "16px", filter: "drop-shadow(0 0 10px var(--color-brand))" },
      { scale: 1.4, opacity: 0, borderWidth: "0px", filter: "drop-shadow(0 0 40px var(--color-brand))", duration: timePerNum, ease: "power2.out" },
      startTime
    );
  }
};
