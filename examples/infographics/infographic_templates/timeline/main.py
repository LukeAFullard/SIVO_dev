from sivo import Sivo
import os

# Build the Timeline Infographic using the new from_template method
timeline = Sivo.from_template("other/timeline", default_panel_position="none")

header_html2 = """
<div style="text-align: center; width: 100%; height: 100%; display: flex; flex-direction: column; justify-content: center; align-items: center; box-sizing: border-box; padding: 5%; container-type: inline-size;">
    <h1 style="margin: 0; color: #1e293b; font-family: sans-serif; font-size: clamp(12px, 3.5cqw, 32px);">Project Milestone History</h1>
    <p style="margin: 5px 0 0 0; color: #64748b; font-family: sans-serif; font-size: clamp(8px, 1.5cqw, 16px);">Key events over the last two years</p>
</div>
"""
timeline.add_overlay("header_area", header_html2)

# Add text overlays to timeline nodes
for i, date in enumerate(["Q1 2023", "Q3 2023", "Q1 2024", "Q4 2024"], 1):
    html = f"""
    <div style="text-align: center; width: 100%; height: 100%; display: flex; flex-direction: column; justify-content: center; align-items: center; box-sizing: border-box; padding: 10%; container-type: inline-size; pointer-events: none;">
        <h3 style="margin: 0; color: #3b82f6; font-family: sans-serif; font-size: clamp(12px, 5cqw, 20px);">{date}</h3>
        <p style="margin: 5px 0 10px 0; color: #475569; font-family: sans-serif; font-size: clamp(8px, 3.5cqw, 14px);">Milestone {i}: Project Phase {i} Launch</p>
        <button style="padding: 5px 15px; border: none; background: #e2e8f0; border-radius: 4px; cursor: pointer; font-size: clamp(8px, 3cqw, 14px); pointer-events: auto;" onclick="window.triggerElementClick('node_{i}_card')">View Details</button>
    </div>
    """
    timeline.add_overlay(f"node_{i}_card", html)

    # Map interactivity to the node dot
    timeline.map(
        element_id=f"node_{i}_dot",
        panel_position="right",
        html=f"<h3>{date} Details</h3><p>Extensive details for milestone phase {i}...</p><p>Resources allocated: {i*50}h</p>",
        hover_color="#60a5fa",
        glow=True
    )
    # Also make the card interactive
    timeline.map(
        element_id=f"node_{i}_card",
        panel_position="right",
        html=f"<h3>{date} Details</h3><p>Extensive details for milestone phase {i}...</p>",
        hover_color="#f8fafc"
    )

timeline.to_html(os.path.join(os.path.dirname(__file__), "output.html"))
print("Generated output.html")
