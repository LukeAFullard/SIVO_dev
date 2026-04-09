---
Last Updated: 2026-04-09
SIVO Version: 0.1.0
---

# A-06: Security & Sanitization Protocols

This document outlines the strict security rules and sanitization protocols within the SIVO repository. These guidelines are crucial for AI agents to ensure they do not generate unsafe code.

## 1. Cross-Site Scripting (XSS) Prevention

### DOMPurify is Mandatory
- In SIVO frontend templates (`echarts.html`, `dashboard_blocks.html`), all dynamic assignments to `.innerHTML` MUST be wrapped with `window.DOMPurify.sanitize()`. This is non-negotiable for mitigating XSS vulnerabilities.
- The `DOMPurify` library script is included unconditionally in the `<head>` of HTML templates.

### Fail-Closed Fallback
- Always include a fail-closed or escaped fallback mechanism in case the DOMPurify library fails to load (e.g., due to network issues or restrictive CSPs).
- Example secure JS Snippet:
  ```javascript
  let cleanHTML = window.DOMPurify ? window.DOMPurify.sanitize(dirtyHTML) : dirtyHTML.replace(/</g, "&lt;").replace(/>/g, "&gt;");
  element.innerHTML = cleanHTML;
  ```

## 2. Template Variable Escaping

### Python-Side Sanitization
- The JSON configuration payload is injected into JavaScript runtime templates as `viewsData` (`{{ views_data | safe }}`).
- The Python backend handles basic sanitization during serialization (in `src/sivo/runtime/bundle_generator.py`) by replacing `<`, `>`, and `&` to prevent XSS breakout from the JS scope.

### Dynamic CSS Injection
- When dynamically injecting CSS strings into SIVO templates (e.g., `panel_css`), the input MUST be sanitized.
- Escape HTML brackets and closing tags (e.g., replacing `</style>`, `<`, and `>` with `\3C/style\3E`, `\3C`, and `\3E`) to prevent CSS-based HTML breakout vulnerabilities.

## 3. Content-Security-Policy (CSP)

SIVO implements strict CSP meta tags in its HTML bundle templates to harden frontend execution.
- Scripts are restricted.
- Objects are blocked entirely: `object-src 'none'`.
- Safe sources are defined for images and external connections.
- Ensure any generated code requiring external assets aligns with these CSP constraints.

## 4. Server-Side Request Forgery (SSRF) Mitigations

When SIVO fetches external resources (e.g., in `Sivo.fetch_image_base64`), strict validations are in place to prevent SSRF:
- URLs are explicitly parsed.
- Permitted schemes are limited to `http` or `https` (blocking `file://` protocols).
- Requests to localhost (`127.0.0.1`, `localhost`) and standard internal IP ranges (`10.x.x.x`, `192.168.x.x`, `172.16.x.x` - `172.31.x.x`) are explicitly blocked.

## 5. Path Traversal Protection

### Local File Loading
- In `from_svg` and `embed_svg` methods, paths are resolved using `os.path.abspath`.
- Paths containing `..` strings are explicitly rejected prior to opening files to mitigate Path Traversal.

### Local Server Security
- The `sivo annotate` HTTP server (`AnnotatorHandler`) overrides `translate_path`.
- It ensures the fully resolved real path (`os.path.realpath`) falls strictly within the current working directory by verifying `os.path.commonpath([real_base, real_path]) == real_base`.
- This protects against out-of-workspace symlink access and prefix confusion vulnerabilities.
- Additionally, the server securely binds to `127.0.0.1` by default (not `0.0.0.0`) to prevent unintended exposure on the local network.

## 6. XML External Entity (XXE) Prevention

SIVO protects against XXE vulnerabilities when parsing SVG files.
- `src/sivo/svg/parser.py` uses `etree.XMLParser(resolve_entities=False, no_network=True)`.
- Instantiation methods explicitly validate file existence and string integrity before parsing to handle malformed inputs gracefully.
