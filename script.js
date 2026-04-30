document.addEventListener("DOMContentLoaded", () => {
  const lines = [
    "Full‑Stack Engineer 🚀",
    "Software Engineering @ BCU 🎓",
    "AI • Automation • Cyberpunk Dev",
  ];
  const speed = 75,
    pauseBetween = 1500;
  let lineIndex = 0,
    charIndex = 0;

  const typingEl = document.querySelector(".typing");
  const cursorEl = document.createElement("span");
  cursorEl.classList.add("cursor");
  typingEl.after(cursorEl);

  function typeLine() {
    if (charIndex < lines[lineIndex].length) {
      typingEl.textContent += lines[lineIndex].charAt(charIndex++);
      setTimeout(typeLine, speed);
    } else {
      setTimeout(() => eraseLine(), pauseBetween);
    }
  }

  function eraseLine() {
    if (charIndex > 0) {
      typingEl.textContent = lines[lineIndex].slice(0, --charIndex);
      setTimeout(eraseLine, speed / 2);
    } else {
      lineIndex = (lineIndex + 1) % lines.length;
      setTimeout(typeLine, speed);
    }
  }

  function blinkCursor() {
    cursorEl.classList.toggle("inactive");
  }

  setInterval(blinkCursor, 500);
  typeLine();
});
