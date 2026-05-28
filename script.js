const terminalLines = [
  "System.init(User.REDWOLF);",
  "Loading Elite Architect Profile...",
  "> Deploying Infrastructure...",
  "> Status: <span class='status-online'>ONLINE</span>"
];

if (typeof document !== 'undefined') {
  document.addEventListener("DOMContentLoaded", () => {
    const terminalContainer = document.getElementById("terminal-content");
    let lineIndex = 0;

    function typeTerminalLine(lineText, container, callback) {
      const lineEl = document.createElement("div");
      lineEl.className = "terminal-line";
      container.appendChild(lineEl);

      let charIndex = 0;
      const isHtml = lineText.includes("<span");
      
      if (isHtml) {
        const baseText = lineText.split("<span")[0];
        const spanContent = "ONLINE";
        
        function typeBase() {
          if (charIndex < baseText.length) {
            lineEl.textContent += baseText.charAt(charIndex++);
            setTimeout(typeBase, 40);
          } else {
            const span = document.createElement("span");
            span.className = "status-online";
            lineEl.appendChild(span);
            let spanCharIndex = 0;
            
            function typeSpan() {
              if (spanCharIndex < spanContent.length) {
                span.textContent += spanContent.charAt(spanCharIndex++);
                setTimeout(typeSpan, 40);
              } else {
                callback();
              }
            }
            typeSpan();
          }
        }
        typeBase();
      } else {
        function typeRegular() {
          if (charIndex < lineText.length) {
            lineEl.textContent += lineText.charAt(charIndex++);
            setTimeout(typeRegular, 40);
          } else {
            callback();
          }
        }
        typeRegular();
      }
    }

    function startAnimation() {
      if (lineIndex < terminalLines.length) {
        typeTerminalLine(terminalLines[lineIndex], terminalContainer, () => {
          lineIndex++;
          setTimeout(startAnimation, 400);
        });
      }
    }

    // Clear existing content and start
    if (terminalContainer) {
      terminalContainer.innerHTML = "";
      startAnimation();
    }
  });
}

if (typeof module !== 'undefined') {
  module.exports = { terminalLines };
}
