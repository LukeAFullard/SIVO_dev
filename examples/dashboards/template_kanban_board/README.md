# Kanban Board Dashboard Template

This example demonstrates how to use the `kanban_board` HTML template to create a multi-lane layout in `SivoDashboard`.

## Key Concepts

- **Lanes via Slots**: The template groups blocks based on their assigned `slot` string. Each unique slot becomes a vertical "lane" (e.g., "to_do", "in_progress", "done").
- **Fixed Dimensions**: Kanban cards typically have fixed proportions. The CSS in the template is adjusted to ensure consistent card heights and a horizontally scrollable container if lanes overflow.

## Running the Example

Run the script directly:
```bash
python main.py
```
This will generate an `output.html` file in the same directory.
