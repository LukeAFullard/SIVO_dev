import streamlit as st
from typing import Optional, Any
import html

from sivo.core.sivo import Sivo

from typing import Optional, Any, Dict

def sivo_component(
    sivo_app: Sivo,
    key: Optional[str] = None,
    custom_css: Optional[str] = None,
    custom_js: Optional[str] = None,
    zoom_to: Optional[str] = None,
    dynamic_colors: Optional[Dict[str, str]] = None
) -> Any:
    """
    Renders a SIVO Infographic inside a Streamlit application using a V2 custom component.

    Args:
        sivo_app (Sivo): The SIVO orchestrator instance to render.
        key (str, optional): An optional key that uniquely identifies this component.
        custom_css (str, optional): Optional CSS string to inject into the component.
        custom_js (str, optional): Optional JS string to inject into the component.
        zoom_to (str, optional): An SVG element ID to zoom to programmatically.
        dynamic_colors (dict, optional): A dictionary of element_id: color hex mapping to update colors without full re-render.

    Returns:
        Any: The value returned by the Streamlit component (e.g. click/hover events).
    """
    # Generate the interactive HTML bundle
    html_content = sivo_app.to_html(custom_css=custom_css, custom_js=custom_js)

    # Pass the data payload including commands like zoom
    zoom_center = sivo_app.get_element_center(zoom_to) if zoom_to else None

    payload = {
        "html_content": html_content,
        "zoom_to": zoom_to,
        "zoom_center": zoom_center,
        "dynamic_colors": dynamic_colors or {}
    }

    # Mount the component, passing the full payload as data
    return _sivo_v2_component(data=payload, key=key)

# Define HTML and JS for the custom component
_COMPONENT_HTML = """
<iframe id="sivo-iframe" style="width: 100%; height: 600px; border: none;"></iframe>
"""

_COMPONENT_JS = """
export default function(component) {
    const { data, setTriggerValue, parentElement } = component;
    const iframe = parentElement.querySelector('#sivo-iframe');

    // We only want to populate the iframe's HTML once or when it explicitly changes,
    // to avoid full re-renders when only sending a command like zoom_to.

    // Store the last rendered HTML to prevent flickering
    if (!iframe.dataset.renderedHtml || iframe.dataset.renderedHtml !== data.html_content) {
        const doc = iframe.contentWindow.document;
        doc.open();
        doc.write(data.html_content);
        doc.close();
        iframe.dataset.renderedHtml = data.html_content;
    }

    // Send programmatic commands (e.g., zoom_to, dynamic_colors) into the iframe
    // We use setTimeout to ensure the iframe content has loaded before sending the message.
    setTimeout(() => {
        if (data.zoom_to) {
            iframe.contentWindow.postMessage({
                type: 'sivo_command',
                payload: {
                    command: 'zoom_to',
                    element_id: data.zoom_to,
                    zoom_center: data.zoom_center,
                    zoom: 2
                }
            }, '*');
        }

        if (data.dynamic_colors && Object.keys(data.dynamic_colors).length > 0) {
            iframe.contentWindow.postMessage({
                type: 'sivo_command',
                payload: {
                    command: 'update_colors',
                    colors: data.dynamic_colors
                }
            }, '*');
        }
    }, 500);

    // We can listen for messages from the iframe to support callbacks to Streamlit
    // Ensure we don't attach multiple event listeners if the component re-renders
    if (!window.sivoListenerAttached) {
        window.addEventListener('message', function(event) {
            if (event.data && (event.data.type === 'sivo_click' || event.data.type === 'sivo_hover')) {
                setTriggerValue(event.data.payload);
            }
        });
        window.sivoListenerAttached = true;
    }
}
"""

# Register the component once at the module level to avoid re-registration warnings
_sivo_v2_component = st.components.v2.component(
    "sivo_renderer",
    html=_COMPONENT_HTML,
    js=_COMPONENT_JS,
    isolate_styles=True
)
