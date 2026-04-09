---
Last Updated: $(date +%Y-%m-%d)
SIVO Version: 1.0.0
---

# H-20: Security and Offline Deployment Plan

Best practices for CSP, DOMPurify, running offline, and mitigating vulnerabilities.

## Table of Contents

1. **Introduction**
   - SIVO's zero-backend architecture and security principles.
2. **Cross-Site Scripting (XSS) Prevention**
   - How `DOMPurify` is used in SIVO templates.
   - Handling fail-closed states.
3. **Content Security Policy (CSP)**
   - Hardening the HTML bundle headers.
4. **Offline Capabilities**
   - How to embed templates for offline usage without triggering CORS errors via `file:///`.
