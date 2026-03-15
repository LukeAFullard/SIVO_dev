const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1200, height: 800 } });
  await page.goto('file://' + process.cwd() + '/examples/49_template_styles/dark_mode_styled.html');
  await page.waitForTimeout(2000);
  await page.screenshot({ path: 'screenshot_dark_mode.png' });
  await browser.close();
})();
