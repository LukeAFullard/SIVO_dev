from sivo import Sivo
from sivo.core.config import ProjectConfig

def main():
    svg_str = """
    <svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg">
        <rect id="background" width="800" height="600" fill="#1e293b"/>
        <text id="title" x="400" y="50" font-family="sans-serif" font-size="24" fill="white" text-anchor="middle">Global Rollout</text>
        <circle id="node1" cx="200" cy="300" r="50" fill="transparent"/>
        <circle id="node2" cx="400" cy="300" r="50" fill="transparent"/>
        <circle id="node3" cx="600" cy="300" r="50" fill="transparent"/>
    </svg>
    """
    app = Sivo.from_string(svg_str)

    # Map sequential fades
    app.map("node1", color="#3b82f6", fade_in=True, fade_start_time_ms=0, fade_duration_ms=2000)
    app.map("node2", color="#10b981", fade_in=True, fade_start_time_ms=1000, fade_duration_ms=2000)
    app.map("node3", color="#f59e0b", fade_pulse=True, fade_start_time_ms=2000, fade_duration_ms=3000)

    # Save standalone
    app.to_html("examples/advanced/33_fade_in/fade_in_infographic.html")

if __name__ == "__main__":
    main()
