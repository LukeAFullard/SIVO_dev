import os
from sivo import Sivo

svg_path = os.path.join(os.path.dirname(__file__), '../../src/sivo/templates/other/timeline_9_nodes_template.svg')
app = Sivo.from_svg(svg_path)

# Data for 9 nodes representing a modern tech timeline
timeline_data = [
    {"year": "1990", "title": "The Dawn of the Web", "desc": "Tim Berners-Lee creates the first web browser and server. The foundation of modern internet infrastructure is laid, connecting the first servers across the globe."},
    {"year": "1995", "title": "The Dot-Com Boom", "desc": "The commercialization of the internet accelerates. New protocols and scripting languages like JavaScript emerge, making web pages dynamic for the first time."},
    {"year": "2000", "title": "The Mobile Era Begins", "desc": "Initial steps into mobile computing. Early smartphones start providing internet access, albeit slowly, shifting the focus towards portability."},
    {"year": "2005", "title": "Web 2.0 & Social Media", "desc": "The web becomes a two-way street. Users start generating content on massive scales, leading to the rise of social networks and global connectivity."},
    {"year": "2010", "title": "The Cloud Computing Revolution", "desc": "Infrastructure moves from on-premise to the cloud. Massive data centers allow seamless scaling for applications, transforming how businesses operate."},
    {"year": "2015", "title": "The Rise of Machine Learning", "desc": "Deep learning architectures achieve breakthrough performance in image and speech recognition. The integration of AI into consumer products becomes commonplace."},
    {"year": "2020", "title": "The Remote Work Shift", "desc": "A global catalyst accelerates digital transformation. Cloud communication, collaborative software, and distributed architectures become essential to modern work."},
    {"year": "2023", "title": "The Generative AI Boom", "desc": "Large Language Models reach unprecedented capabilities. AI assists in writing code, creating art, and solving complex reasoning tasks, revolutionizing human-computer interaction."},
    {"year": "2025", "title": "The Autonomous Future", "desc": "AI agents begin performing complex, multi-step workflows independently. The internet evolves into a highly personalized and automated digital ecosystem."}
]

# Configure Header
app.add_scalable_text(
    target_id="header_area",
    text="The Evolution of the Digital Age",
    font_size="40%",
    font_weight="bold",
    color="#1e293b",
    align="center",
    vertical_align="middle"
)

# Prepare scrollytelling steps
steps = [
    {
        "content": "<h1>Welcome to the Digital Timeline</h1><p>Scroll down to journey through the pivotal moments of the digital age. From the birth of the web to the rise of autonomous AI, each node represents a massive leap forward in technology.</p><p>As you scroll, the view will zoom into each specific era. You can also click any node on the timeline to jump to that part of the story.</p>",
        "zoom_to": "header_area",
        "zoom_level": 1.2,
        "colors": {
            "node_1_dot": "#ffffff", "node_2_dot": "#ffffff", "node_3_dot": "#ffffff",
            "node_4_dot": "#ffffff", "node_5_dot": "#ffffff", "node_6_dot": "#ffffff",
            "node_7_dot": "#ffffff", "node_8_dot": "#ffffff", "node_9_dot": "#ffffff"
        }
    }
]

for i, data in enumerate(timeline_data):
    node_id = i + 1
    dot_id = f"node_{node_id}_dot"
    card_id = f"node_{node_id}_card"

    # Fill the template zone for the card
    app.fill_template_zone(
        element_id=card_id,
        text=f"{data['year']}\n{data['title']}",
        font_size="25%",
        font_weight="bold",
        color="#1e293b",
        align="center",
        vertical_align="middle"
    )

    app.map(
        element_id=dot_id,
        tooltip=data["title"],
        hover_color="#3b82f6"
    )
    app.map(
        element_id=card_id,
        tooltip=data["desc"],
        hover_color="#f8fafc"
    )

    # Create the scrollytelling step
    # Highlight the current node dot
    step_colors = {f"node_{j}_dot": "#ffffff" for j in range(1, 10)}
    step_colors[dot_id] = "#3b82f6"

    steps.append({
        "content": f"<h2>{data['year']}: {data['title']}</h2><p>{data['desc']}</p><p>This era redefined how we interact with technology and set the stage for the next major leap in innovation. The rapid advancement during this period led to unprecedented global connectivity and computational power.</p>",
        "zoom_to": dot_id,
        "zoom_level": 2.5,
        "colors": step_colors,
        "show_tooltips": [dot_id]
    })

# Add a concluding step
steps.append({
    "content": "<h1>Conclusion</h1><p>The journey from a static web to an intelligent, autonomous digital ecosystem took less than four decades. The future promises even more rapid acceleration. Thank you for exploring the timeline.</p>",
    "zoom_to": "header_area",
    "zoom_level": 1.0,
    "colors": {f"node_{j}_dot": "#ffffff" for j in range(1, 10)}
})

# Bind scrollytelling
app.bind_scrollytelling(steps)

output_path = os.path.join(os.path.dirname(__file__), "scrollytelling_timeline.html")

# Render HTML and inject custom JS to scroll the narrative on click
html_content = app.to_html()

# Inject click-to-scroll logic
custom_js = r"""
<script>
    // Add an event listener to ECharts once it's initialized
    setTimeout(function() {
        if (typeof myChart !== 'undefined') {
            myChart.on('click', function(params) {
                if (params.name) {
                    // Extract node number from 'node_1_dot' or 'node_1_card'
                    var match = params.name.match(/node_(\d+)_(dot|card)/);
                    if (match) {
                        var nodeIndex = parseInt(match[1]);
                        var container = document.getElementById('scrollytelling-container');
                        if (container) {
                            var step = container.querySelector('.scrolly-step[data-index="' + nodeIndex + '"]');
                            if (step) {
                                step.scrollIntoView({ behavior: 'smooth', block: 'center' });
                            }
                        }
                    }
                }
            });
        }
    }, 1000); // give echarts a second to boot up
</script>
"""

# Insert right before the closing body tag
html_content = html_content.replace('</body>', f'{custom_js}\n</body>')

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Generated {output_path}")
