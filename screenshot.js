const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1200, height: 800 } });
  await page.goto('file://' + process.cwd() + '/examples/50_climate_change_infographic/climate_change_dashboard.html');
  // wait for render
  await page.waitForTimeout(2000);
  await page.screenshot({ path: 'screenshot.png' });
  await browser.close();
})();
