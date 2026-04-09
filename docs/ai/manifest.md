---
Last Updated: 2026-04-09
SIVO Version: 1.0.0
---

# A-01: AI Agent Manifest Plan

A 'Map' for AI agents to understand the repository structure and entry points.

## Table of Contents

1. **Repository Overview for Agents**
   - Goal: Quickly orient the LLM on where code lives.
2. **Directory Structure & Roles**
   - `src/sivo/core/`: Python API and models.
   - `src/sivo/svg/`: Parsers, manipulators, card generation.
   - `src/sivo/runtime/`: Bundler logic and HTML/JS templates.
3. **Key Architectural Constraints**
   - 100% Serverless execution.
   - Strict Pydantic models.
   - Jinja2 data injection logic.
4. **Important Files to Analyze First**
   - `src/sivo/core/infographic.py`: Main `Sivo` class entry point.
   - `src/sivo/runtime/bundle_generator.py`: Where Python meets HTML.
   - `src/sivo/runtime/templates/echarts.html`: The core JS runtime engine.
5. **Cross-References**
   - Links to Technical API docs (`docs/api/`).
