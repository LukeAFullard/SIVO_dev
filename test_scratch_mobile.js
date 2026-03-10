const { chromium, devices } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const context = await browser.newContext(devices['iPhone 13']);
  const page = await context.newPage();

  await page.setContent(`
    <!DOCTYPE html>
    <html>
    <head>
    <style>
      #scratch {
        width: 100vw;
        height: 100vh;
        background: red;
      }
    </style>
    </head>
    <body style="margin: 0; padding: 0;">
    <canvas id="scratch"></canvas>
    <script>
      const canvas = document.getElementById('scratch');
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
      const ctx = canvas.getContext('2d');
      ctx.fillStyle = 'gray';
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      let isDrawing = false;
      const draw = (e) => {
        if (!isDrawing) return;
        // e.preventDefault(); // What happens if we don't preventDefault?
        const touch = e.touches ? e.touches[0] : e;
        ctx.globalCompositeOperation = 'destination-out';
        ctx.beginPath();
        ctx.arc(touch.clientX, touch.clientY, 30, 0, Math.PI * 2);
        ctx.fill();
      };

      canvas.addEventListener('mousedown', () => isDrawing = true);
      canvas.addEventListener('mousemove', draw);
      canvas.addEventListener('mouseup', () => isDrawing = false);
      canvas.addEventListener('touchstart', (e) => { isDrawing = true; draw(e); }, { passive: false });
      canvas.addEventListener('touchmove', (e) => { draw(e); }, { passive: false });
      canvas.addEventListener('touchend', () => isDrawing = false);
    </script>
    </body>
    </html>
  `);

  await page.waitForTimeout(1000);

  // Simulate touch scroll
  await page.touchscreen.tap(100, 100);
  await page.mouse.move(100, 100);
  await page.mouse.down();
  await page.mouse.move(100, 300, { steps: 10 });
  await page.mouse.up();

  await page.screenshot({ path: 'scratch_mobile_test.png' });
  await browser.close();
})();
