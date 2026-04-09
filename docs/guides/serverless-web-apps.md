---
Last Updated: $(date +%Y-%m-%d)
SIVO Version: 1.0.0
---

# H-11: Serverless Web Apps Guide Plan

Guide on using SIVO with Pyodide and WebAssembly for 100% serverless apps.

## Table of Contents

1. **Introduction**
   - Concept of running Python in the browser using Pyodide.
2. **Architecture**
   - How SIVO uses Pyodide, Emscripten IDBFS, and iframes.
3. **Setting up Pyodide**
   - Loading Pyodide.
   - Initializing virtual file system.
4. **Deploying without a Server**
   - Embedding `annotator.html`.
   - Handling browser security policies (CORS).
