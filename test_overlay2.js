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
     for (const [id, overlayObj] of Object.entries(window.overlayElements)) {
         let el = overlayObj.dom;
         console.log(`Live Overlay ${id} width: ${el.style.width} height: ${el.style.height}`);
     }
  });

  await browser.close();
})();
