---
Last Updated: 2026-04-09
SIVO Version: 1.0.0
---

# A-06: Security & Sanitization Protocols Plan

Strict rules on DOMPurify usage and sanitization to ensure AI doesn't generate unsafe code.

## Table of Contents

1. **Cross-Site Scripting (XSS) Prevention**
   - Mandatory usage of `window.DOMPurify.sanitize()` for `.innerHTML` injections.
   - Fail-closed fallback mechanisms.
   - Example secure JS Snippet:
     ```javascript
     let cleanHTML = window.DOMPurify ? window.DOMPurify.sanitize(dirtyHTML) : dirtyHTML.replace(/</g, "&lt;");
     element.innerHTML = cleanHTML;
     ```
2. **Template Variable Escaping**
   - Escaping `<`, `>`, and `&` in Python before JSON injection (`bundle_generator.py`).
   - Handling CSS string escaping (`C/styleE`).
3. **Content-Security-Policy (CSP)**
   - Understanding SIVO's CSP headers in generated HTML.
4. **Server-Side Request Forgery (SSRF) Mitigations**
   - Logic in `Sivo.fetch_image_base64` blocking localhost and internal IP fetches.
5. **Path Traversal Protection**
   - Safe path resolution in `from_svg` and local servers (e.g., `os.path.commonpath`).
