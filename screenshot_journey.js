const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    viewport: { width: 1200, height: 800 },
    deviceScaleFactor: 2,
  });
  const page = await context.newPage();
  const fileUrl = 'file://' + path.resolve('examples/52_customer_journey_flow/customer_journey.html');
  console.log('Navigating to', fileUrl);
  await page.goto(fileUrl, { waitUntil: 'networkidle' });
  await page.screenshot({ path: 'screenshot_journey.png', fullPage: true });
  await browser.close();
})();
