const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1200, height: 800 } });
  await page.goto('file://' + process.cwd() + '/examples/51_saas_metrics_dashboard/saas_dashboard.html');
  await page.waitForTimeout(2000);
  await page.screenshot({ path: 'screenshot_saas.png' });
  await browser.close();
})();
