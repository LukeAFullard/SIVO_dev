# Footnotes

## Description
Demonstrates the use of SIVO for footnotes.

## Relevant Code
```python
sivo_app.map(
    element_id="point1",
    tooltip="Red Data Point",
    footnote="This figure excludes data from Alaska and Hawaii due to reporting differences. Source: U.S. Census Bureau 2023.",
    footnote_title="Methodology Note"
)
sivo_app.map(
    element_id="point2",
    tooltip="Green Data Point",
    footnote="Estimated values based on predictive modeling. Margin of error &plusmn; 4%.",
    footnote_title="Estimation Disclaimer"
)
sivo_app.to_html(output_path)
```
