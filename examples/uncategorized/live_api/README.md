# SIVO Live API Example

This example demonstrates how to use the `bind_api` feature in SIVO to dynamically update SVG element properties over time using a live polling endpoint.

## What is being shown
- Setting an initial state for an element (`status_dot`) using `sivo_app.map()`.
- Using `sivo_app.bind_api()` to connect the visualization to a mock API URL (represented by a Data URI).
- The SIVO frontend bundle will automatically poll this endpoint every 3000ms. When the data payload is parsed, the frontend dynamically updates the mapped color and tooltip of the targeted SVG element without refreshing the page.

## Key Code Snippets

```python
# Bind the mock API endpoint with a 3-second delay to show the "before" and "after" state
sivo_app.bind_api(
    url=mock_api_url,
    polling_interval_ms=3000,
    method="GET"
)
```

## Running the example
To run the example and generate the HTML output:
```bash
python live_api.py
```
Open the generated `live_api_example.html` in your browser. Wait for 3 seconds, and observe the gray "status dot" turn green and update its tooltip text as it receives data from the mock API.
