---
Last Updated: 2026-04-09
SIVO Version: 0.1.0
---

# External Integrations with SIVO

SIVO is designed to be highly embeddable and flexible, allowing you to integrate your interactive maps and dashboards into various external ecosystems such as E-commerce platforms, Business Intelligence (BI) tools, low-code builders, and generic web frameworks.

## 1. Web Integration (iframes)

The simplest way to integrate a SIVO output into an external platform is via an HTML `iframe`. SIVO compiles down to a single, standalone HTML file that has zero external server dependencies (other than optionally loading CDNs for ECharts or Mapbox).

### Exporting for the Web

First, export your SIVO instance to HTML:

```python
sivo.to_html("my_sivo_map.html")
```

### Embedding via iframe

Upload `my_sivo_map.html` to any static hosting provider (e.g., AWS S3, GitHub Pages, Vercel) and embed it:

```html
<iframe src="https://my-domain.com/my_sivo_map.html"
        width="100%"
        height="600px"
        style="border:none;">
</iframe>
```

This method is universally supported by CMS platforms (WordPress, Webflow), no-code builders (Bubble, Framer), and standard web apps.

## 2. E-commerce Integration

SIVO can act as an interactive visual storefront. You can bind SIVO elements to external URLs to route users to product pages or add items to their cart.

### Linking to Product Pages

Use the `url` and `url_target` parameters in `sivo.map()` to link specific regions or elements directly to a checkout or product details page:

```python
sivo.map(
    element_id="premium_ticket_zone",
    color="#FFD700",
    url="https://store.example.com/checkout?item=premium",
    url_target="_top"  # Use _top to break out of iframes if necessary
)
```

## 3. Business Intelligence (BI) Tools

For BI tools (like Tableau, PowerBI, or Metabase), SIVO can serve as a custom visual component.

- **Tableau:** You can use Tableau's Web Page object to embed a SIVO iframe.
- **PowerBI:** You can embed SIVO using the HTML Content visual or by building a custom visual wrapper around SIVO's exported HTML.

## 4. WebAssembly and Serverless Environments (Pyodide / Replit)

SIVO is compatible with Pyodide and WebAssembly, enabling you to run the SIVO Python configuration logic directly in the browser without a backend server.

This is particularly useful for platforms like **Replit** or JupyterLite, where you want to dynamically build maps based on user input solely on the client-side. See the [Serverless Web Apps Guide](serverless-web-apps.md) for detailed instructions.

## 5. Forms and External APIs

Using SIVO's live data bindings, you can create two-way interactions with external forms and APIs.

For instance, you could configure SIVO to poll an external API endpoint to visually update a map based on live form submissions from Google Forms or Typeform.

```python
from sivo.core.config import ApiBindingConfig

api_config = ApiBindingConfig(
    endpoint="https://api.example.com/live-survey-results",
    poll_interval=5000,  # Poll every 5 seconds
    data_path="results.geodata",
    key_field="region_id",
    value_field="vote_count"
)

sivo.bind_api(api_config)
```

This allows SIVO to reflect data gathered from external systems in real-time.

## Conclusion

Because SIVO outputs pure HTML/JS/CSS without relying on a proprietary runtime server, its integration footprint is extremely lightweight. Whether you are embedding via an iframe or using live data bindings, SIVO seamlessly adapts to your existing tech stack.
