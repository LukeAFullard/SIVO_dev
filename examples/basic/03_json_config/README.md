# 03 JSON Config

This example demonstrates how to configure a SIVO application declaratively using a JSON configuration file instead of mapping elements programmatically via Python.

### Key Code

```python
# Generate the app from declarative config
sivo_app = Sivo.from_config(config_path)
```

In `config.json`:
```json
{
  "view": {
    "svg_path": "sample.svg"
  },
  "elements": [
    {
      "id": "sun",
      "tooltip": "The Sun (from config)",
      "color": "gold"
    }
  ]
}
```
