const fs = require('fs');

const transcript = JSON.parse(fs.readFileSync('transcript.json', 'utf8'));

let scriptContent = `
      // Subtitles GSAP Timeline
      const subTl = gsap.timeline();
      const captionText = document.getElementById("caption-text");

      const words = ${JSON.stringify(transcript.map(w => ({ text: w.text, start: w.start, end: w.end })))};

      words.forEach((word) => {
        subTl.set(captionText, { innerHTML: word.text }, word.start);
      });
      subTl.to(captionText, { opacity: 1, duration: 0.2 }, words[0].start);
      subTl.set(captionText, { innerHTML: "" }, words[words.length - 1].end);

      tl.add(subTl, 0);
`;
fs.writeFileSync('generated_script.txt', scriptContent);
