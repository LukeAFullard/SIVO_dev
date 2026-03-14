const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  page.on('console', msg => console.log('BROWSER LOG:', msg.text()));
  const fileUrl = 'file://' + path.resolve('examples/60_overlay_geometry_fix/index.html');
  await page.goto(fileUrl);
  await page.waitForTimeout(1000);

  await page.evaluate(() => {
     let chart = window.myChart;

     // Is it centering exactly in the path? Let's check where the SVG path actually draws on screen
     // compared to the overlay positioning.
     let b1 = document.querySelector('svg [id="box-1"]');
     if (b1) {
         let r = b1.getBoundingClientRect();
         console.log(`SVG 'box-1' real screen rect: center [${r.left + r.width/2}, ${r.top + r.height/2}]`);
     }
  });

  await browser.close();
})();
