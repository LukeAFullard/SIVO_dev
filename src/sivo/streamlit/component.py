import streamlit as st
from typing import Optional, Any
import html

from sivo.core.infographic import Infographic

def sivo_component(infographic: Infographic, key: Optional[str] = None) -> Any:
    """
    Renders a SIVO Infographic inside a Streamlit application using a V2 custom component.

    Args:
        infographic (Infographic): The SIVO Infographic instance to render.
        key (str, optional): An optional key that uniquely identifies this component.

    Returns:
        Any: The value returned by the Streamlit component (e.g. click events).
    """
    # Generate the interactive HTML bundle
    html_content = infographic.to_echarts_html()

    # The V2 component requires us to pass the HTML (either as string or file path).
    # Since we dynamically generate the HTML bundle including ECharts and SVG mapping logic,
    # we can pass it via the `html` parameter. However, the `html` parameter for V2 components
    # usually expects inner HTML. Since our bundle generates a full HTML document (or large snippet),
    # an iframe-based approach or passing a container div via `html` and populating it via `js` is standard.
    # We will use an iframe-like approach by injecting our HTML string into a component.

    # Alternatively, the easiest way to render arbitrary HTML with scripts in Streamlit is `st.components.v1.html`,
    # but the instructions strictly require `st.components.v2.component`.
    # A V2 component accepts `html`, `css`, `js`.

    # We can create a base wrapper HTML that will inject the payload.
    # Or simply provide the generated HTML string directly.
    # The V2 component documentation says: "Raw HTML. This doesn't require any <html>, <head>, or <body> tags; just provide the inner HTML."

    # We will provide a simple container and execute a JavaScript block to inject the actual HTML or create an iframe.
    # Because `to_echarts_html()` generates a full HTML document, placing it inside an iframe is the safest way
    # to avoid CSS/JS conflicts with Streamlit.

    # Let's create an iframe in the component's HTML, and use JavaScript to populate it.

    # Mount the component, passing the full HTML string as data
    return _sivo_v2_component(data=html_content, key=key)

# Define HTML and JS for the custom component
_COMPONENT_HTML = """
<iframe id="sivo-iframe" style="width: 100%; height: 600px; border: none;"></iframe>
"""

_COMPONENT_JS = """
export default function(component) {
    const { data, setTriggerValue, parentElement } = component;
    const iframe = parentElement.querySelector('#sivo-iframe');

    // Populate the iframe with the generated HTML
    const doc = iframe.contentWindow.document;
    doc.open();
    doc.write(data);
    doc.close();

    // We can listen for messages from the iframe to support callbacks to Streamlit
    window.addEventListener('message', function(event) {
        if (event.data && event.data.type === 'sivo_click') {
            setTriggerValue(event.data.payload);
        }
    });
}
"""

# Register the component once at the module level to avoid re-registration warnings
_sivo_v2_component = st.components.v2.component(
    "sivo_renderer",
    html=_COMPONENT_HTML,
    js=_COMPONENT_JS,
    isolate_styles=True
)
