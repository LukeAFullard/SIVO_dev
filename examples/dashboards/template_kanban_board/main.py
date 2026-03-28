import os
from sivo import Sivo, SivoDashboard

def main():
    # Helper to generate simple task cards
    def create_task_card(task_id, title, color):
        svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200">
            <rect id="bg" width="300" height="200" fill="#ffffff" rx="8" />
            <rect width="10" height="200" fill="{color}" rx="4" />
            <text x="30" y="40" font-family="sans-serif" font-size="20" font-weight="bold" fill="#1e293b">{title}</text>
            <text x="30" y="80" font-family="sans-serif" font-size="14" fill="#64748b">ID: {task_id}</text>
            <circle cx="260" cy="160" r="16" fill="#e2e8f0" />
            <text x="260" y="165" font-family="sans-serif" font-size="12" fill="#475569" text-anchor="middle">JD</text>
        </svg>"""
        return Sivo.from_string(svg, theme="light", layout_size="95%")

    # Create task cards
    task1 = create_task_card("T-101", "Design API", "#3b82f6")
    task2 = create_task_card("T-102", "Setup Database", "#3b82f6")
    task3 = create_task_card("T-103", "Implement Auth", "#f59e0b")
    task4 = create_task_card("T-104", "Deploy to Staging", "#10b981")

    # Interactive elements on tasks
    task1.map("bg", hover_color="#f8fafc", tooltip="<b>T-101</b><br/>Design REST API endpoints.")
    task2.map("bg", hover_color="#f8fafc", tooltip="<b>T-102</b><br/>Setup PostgreSQL schemas.")
    task3.map("bg", hover_color="#f8fafc", tooltip="<b>T-103</b><br/>Implement OAuth2 flow.")
    task4.map("bg", hover_color="#f8fafc", tooltip="<b>T-104</b><br/>Deploy using GitHub Actions.")

    # Assemble Dashboard using 'kanban_board' template
    dashboard = SivoDashboard(title="Project Sprint Board", columns=3)
    dashboard.set_grid_layout(
        desktop='''
    "to_do1 in_progress done review"
    "to_do2 in_progress done review"
        ''',
        mobile='''
    "to_do1"
    "to_do2"
    "in_progress"
    "done"
    "review"
        '''
    )

    # Assign blocks to different "lanes" using the 'slot' parameter
    dashboard.add_sivo_block("task_api", task1, grid_area="to_do1")
    dashboard.add_sivo_block("task_db", task2, grid_area="to_do2")

    dashboard.add_sivo_block("task_auth", task3, grid_area="in_progress")

    dashboard.add_sivo_block("task_deploy", task4, grid_area="done")

    # Export
    output_file = os.path.join(os.path.dirname(__file__), "output.html")
    dashboard.to_html(output_file)
    print(f"Successfully generated dashboard: {output_file}")


if __name__ == "__main__":
    main()
