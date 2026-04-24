from sivo import SivoDashboard, Sivo
from sivo.core.config import ProjectConfig

def main():
    svg_str1 = """
    <svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
        <rect id="bg1" width="400" height="400" fill="#0f172a"/>
        <circle id="c1" cx="200" cy="200" r="100" fill="transparent"/>
    </svg>
    """

    svg_str2 = """
    <svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
        <rect id="bg2" width="400" height="400" fill="#0f172a"/>
        <circle id="c2" cx="200" cy="200" r="100" fill="transparent"/>
    </svg>
    """

    app1 = Sivo.from_string(svg_str1)
    app1.map("c1", color="#3b82f6", fade_in=True, fade_start_time_ms=500, fade_duration_ms=2000)

    app2 = Sivo.from_string(svg_str2)
    app2.map("c2", color="#ef4444", fade_pulse=True, fade_start_time_ms=1000, fade_duration_ms=3000)

    dash = SivoDashboard("Animated Dashboard")
    dash.add_sivo_block("app1", app1)
    dash.add_sivo_block("app2", app2)

    dash.to_html("examples/advanced/34_dashboard_fade_in/dashboard_fade.html")

if __name__ == "__main__":
    main()
