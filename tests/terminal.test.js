const { terminalLines } = require('../script.js');

test('terminal lines match the new Elite Architect branding', () => {
  expect(terminalLines).toContain("System.init(User.REDWOLF);");
  expect(terminalLines).toContain("Loading Elite Architect Profile...");
});
