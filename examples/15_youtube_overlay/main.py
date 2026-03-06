import os
from sivo import Sivo

def main():
    svg_path = os.path.join(os.path.dirname(__file__), "sample.svg")

    sivo_app = Sivo.from_svg(svg_path)

    # We map a callback event to the play button
    # The default HTML sanitizer (DOMPurify) strips <iframe> tags, so we use a custom JS modal
    # to overlay the YouTube video perfectly on top of the SIVO canvas.

    sivo_app.map(
        element_id="play_button",
        tooltip="Click to watch video",
        callback_event="open_youtube_modal",
        hover_color="#CC0000",
        glow=True
    )

    sivo_app.map(
        element_id="play_icon",
        tooltip="Click to watch video",
        callback_event="open_youtube_modal",
        hover_color="#f0f0f0",
        glow=True
    )

    custom_css = """
    #youtube-modal {
        display: none;
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(0, 0, 0, 0.8);
        z-index: 9999;
        justify-content: center;
        align-items: center;
        backdrop-filter: blur(5px);
    }
    #youtube-modal.active {
        display: flex;
    }
    .modal-content {
        position: relative;
        width: 80%;
        max-width: 800px;
        background: #000;
        border-radius: 8px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.5);
        overflow: hidden;
    }
    .close-btn {
        position: absolute;
        top: -40px;
        right: 0;
        color: white;
        font-size: 30px;
        font-weight: bold;
        cursor: pointer;
    }
    .video-container {
        position: relative;
        padding-bottom: 56.25%; /* 16:9 Aspect Ratio */
        height: 0;
    }
    .video-container iframe {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
    }
    """

    custom_js = """
    // Create the modal container dynamically
    var modalHTML = `
    <div id="youtube-modal">
        <div style="position: relative; width: 80%; max-width: 800px;">
            <span class="close-btn" id="close-modal">&times;</span>
            <div class="modal-content">
                <div class="video-container" id="video-wrapper">
                    <!-- Iframe injected on click to avoid autoplaying immediately -->
                </div>
            </div>
        </div>
    </div>
    `;
    document.body.insertAdjacentHTML('beforeend', modalHTML);

    var modal = document.getElementById('youtube-modal');
    var closeBtn = document.getElementById('close-modal');
    var videoWrapper = document.getElementById('video-wrapper');

    // Listen for the custom SIVO callback event
    window.addEventListener('message', function(event) {
        if (event.data && event.data.type === 'sivo_click') {
            var payload = event.data.payload;
            if (payload.event_name === 'open_youtube_modal') {
                // Inject iframe when opened
                videoWrapper.innerHTML = `<iframe src="https://www.youtube.com/embed/dQw4w9WgXcQ?autoplay=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>`;
                modal.classList.add('active');
            }
        }
    });

    // Close modal logic
    function closeModal() {
        modal.classList.remove('active');
        videoWrapper.innerHTML = ''; // Stop video playback
    }

    closeBtn.addEventListener('click', closeModal);
    modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            closeModal();
        }
    });
    """

    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    sivo_app.to_html(output_path, custom_css=custom_css, custom_js=custom_js)
    print(f"Exported interactive HTML with YouTube overlay to {output_path}")

if __name__ == "__main__":
    main()
