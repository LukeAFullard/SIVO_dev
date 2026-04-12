const fs = require('fs');
const jsdom = require('jsdom');
const { JSDOM } = jsdom;
const virtualConsole = new jsdom.VirtualConsole();
virtualConsole.on("log", (message) => {
  console.log("LOG:", message);
});
virtualConsole.on("error", (message) => {
  console.error("ERROR:", message);
});
const html = fs.readFileSync('fix_minimap.html', 'utf8');
const dom = new JSDOM(html, { runScripts: "dangerously", virtualConsole });
