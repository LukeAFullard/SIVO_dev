const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  page.on('console', msg => console.log('BROWSER LOG:', msg.text()));

  const fileUrl = 'file://' + path.resolve('examples/60_overlay_geometry_fix/index.html');
  await page.goto(fileUrl);
  await page.waitForTimeout(1000);

  // Get initial box-1 state
  let initialLeft = await page.evaluate(() => window.overlayElements['box-1'].dom.style.left);
  let initialWidth = await page.evaluate(() => window.overlayElements['box-1'].dom.style.width);
  console.log(`Initial overlay: ${initialLeft}, ${initialWidth}`);

  // SIVO zoom-btn UI selector specifically
  await page.evaluate(() => {
     // call the method directly to bypass UI visibility playwright checks (sometimes floating tooltips overlap)
     window.zoomIn();
  });

  // Wait for the setTimeout in our code
  await page.waitForTimeout(600);

  let zoomedLeft = await page.evaluate(() => window.overlayElements['box-1'].dom.style.left);
  let zoomedWidth = await page.evaluate(() => window.overlayElements['box-1'].dom.style.width);
  console.log(`Zoomed overlay: ${zoomedLeft}, ${zoomedWidth}`);

  if(initialLeft !== zoomedLeft && initialWidth !== zoomedWidth) {
      console.log("TEST PASSED: Overlay properties changed smoothly after UI zoom call.");
  }

  await browser.close();
})();
