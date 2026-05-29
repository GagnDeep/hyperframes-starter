// Reusable CTA button pulse animation logic
window.createCtaPulseAnimation = function(tl, ctaSelector, startTime, durationOutro) {
  const pulseCycleDuration = 1.6; // 0.8s * 2 (yoyo)
  const availableTimeForPulse = durationOutro - startTime;
  const pulseRepeats = Math.floor(availableTimeForPulse / pulseCycleDuration) - 1;
  const actualRepeats = Math.max(0, pulseRepeats); // ensure no negative repeats

  tl.to(ctaSelector,
    { scale: 1.05, duration: 0.8, yoyo: true, repeat: actualRepeats, ease: "sine.inOut" },
    startTime
  );

  return actualRepeats; // return so caller knows how long it runs safely
};
