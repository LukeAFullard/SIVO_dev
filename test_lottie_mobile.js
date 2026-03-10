const { chromium, devices } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const context = await browser.newContext(devices['iPhone 13']);
  const page = await context.newPage();

  await page.route('**/*', route => route.continue());

  page.on('console', msg => console.log('PAGE LOG:', msg.text()));
  page.on('pageerror', error => console.log('PAGE ERROR:', error.message));

  await page.setContent(`
    <!DOCTYPE html>
    <html>
    <head>
    <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/dompurify/3.0.6/purify.min.js"></script>
    </head>
    <body>
    <div id="container" style="border: 1px solid black; width: 100%; height: 400px;"></div>
    <script>
    const config = {
        ADD_TAGS: ['form', 'input', 'textarea', 'button', 'lottie-player'],
        ADD_ATTR: ['onsubmit', 'required', 'type', 'name', 'src', 'background', 'speed', 'style', 'loop', 'autoplay', 'min', 'max', 'value'],
        CUSTOM_ELEMENT_HANDLING: {
            tagNameCheck: (tagName) => tagName.match(/-/),
            attributeNameCheck: (attr) => attr.match(/-/),
            allowCustomizedBuiltInElements: true,
        }
    };
    // Use a working Lottie JSON file from lottiefiles.
    const html = '<lottie-player src="https://lottie.host/81bd98b9-e1ce-4277-bc63-bd433dc5eaf5/V7Q2lS2qJj.json" background="transparent" speed="1" style="width: 100%; height: 300px; display: block;" loop autoplay></lottie-player>';

    document.getElementById('container').innerHTML = DOMPurify.sanitize(html, config);
    </script>
    </body>
    </html>
  `);

  await page.waitForTimeout(3000);
  await page.screenshot({ path: 'lottie_mobile_test6.png' });
  await browser.close();
})();
