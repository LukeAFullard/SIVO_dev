---
Last Updated: 2026-04-09
SIVO Version: 0.1.0
---

# Security and Offline Deployment Guide

SIVO is designed with a zero-backend architecture, meaning all data and rendering logic run entirely on the client side. While this provides excellent scalability and ease of deployment, it requires strict adherence to client-side security best practices. This guide details how SIVO handles Cross-Site Scripting (XSS), Content Security Policy (CSP), and how to safely deploy SIVO offline.

## 1. Introduction

SIVO's architecture takes Python configurations and compiles them into static HTML/JS bundles.
Security in SIVO is built around three core principles:
1. **Sanitization:** Never trust dynamically injected data.
2. **Restriction:** Use CSP to tightly control what resources the browser can load or execute.
3. **Graceful Degradation:** Fail closed if security libraries are unavailable.

## 2. Cross-Site Scripting (XSS) Prevention

XSS is the most significant risk when injecting dynamic content (like user-provided labels or tooltips) into a web page. SIVO employs multiple layers of defense:

### Backend Serialization

When compiling the HTML bundle (`src/sivo/runtime/bundle_generator.py`), the JSON payload injected into the templates is natively sanitized. Characters that could break out of a `<script>` tag or JSON string (`<`, `>`, and `&`) are explicitly replaced with their unicode string escapes (`\u003c`, `\u003e`, `\u0026`).

### Client-Side DOM Sanitization (`DOMPurify`)

In SIVO's frontend templates (e.g., `echarts.html`, `dashboard_blocks.html`), **all dynamic assignments to `.innerHTML` must be wrapped with `window.DOMPurify.sanitize()`**.

To guarantee this protection is always active:
- The `DOMPurify` library script is included unconditionally in the `<head>` of all HTML templates.
- If the `DOMPurify` library fails to load (e.g., due to a network error in an offline environment without bundled assets), SIVO implements a fail-closed or escaped fallback.

**Example Fallback:**
```javascript
const safeHTML = window.DOMPurify
    ? window.DOMPurify.sanitize(userInput)
    : userInput.replace(/</g, "&lt;").replace(/>/g, "&gt;");

element.innerHTML = safeHTML;
```

### CSS Injection Protection

When dynamically injecting CSS strings (e.g., `panel_css` configurations), the input is sanitized by escaping HTML brackets and closing tags to prevent CSS-based HTML breakout vulnerabilities.

## 3. Content Security Policy (CSP)

To harden frontend execution, SIVO's HTML bundle templates implement a strict Content Security Policy (CSP) via a `<meta>` tag.

A standard SIVO CSP restricts scripts to trusted sources, explicitly blocks the use of plugins (`object-src 'none'`), and controls where images and network connections can be made.

```html
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net; style-src 'self' 'unsafe-inline'; img-src 'self' data: https:; connect-src 'self' https:; object-src 'none';">
```

*Note: Depending on the external services you integrate (like live data polling or map tiles), you may need to adjust the CSP in your specific deployment, but you should never weaken it unnecessarily.*

## 4. Server-Side Request Forgery (SSRF) Prevention

During compilation or offline processing, if SIVO needs to fetch external resources (e.g., `Sivo.fetch_image_base64`), it protects against SSRF vulnerabilities by:
- Enforcing `http` or `https` schemes (explicitly blocking local file access via `file://`).
- Parsing URLs to block requests to `localhost` and standard internal IP ranges (10.x.x.x, 192.168.x.x, 172.16.x.x - 172.31.x.x).

## 5. Offline Capabilities

Because SIVO generates static HTML bundles, these files can be opened directly in a browser without a web server.

### Running Offline Safely

When opening an HTML file directly from the filesystem (using the `file:///` protocol), browsers enforce strict security restrictions that can trigger CORS errors, particularly when loading local JSON files or external scripts.

To build an entirely offline SIVO application:
1. **Bundle Assets:** Ensure all required libraries (ECharts, DOMPurify) are either downloaded locally and referenced via relative paths, or use SIVO's inline bundling options if available.
2. **Inline Data:** Avoid fetching data via `fetch('data.json')` in offline mode. Instead, inject the data directly into the SIVO Python configuration before compilation, so it is hardcoded into the `window.SivoData` object.
3. **Use a Local Server:** The easiest way to develop and view SIVO bundles locally without `file:///` protocol issues is to use SIVO's built-in annotator server or a simple Python HTTP server:
   ```bash
   python -m http.server 8000
   ```
