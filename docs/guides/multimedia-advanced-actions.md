---
Last Updated: 2026-04-09
SIVO Version: 0.1.0
---

# Multimedia & Advanced Actions Guide

SIVO provides a suite of advanced actions that allow you to embed rich multimedia and create dramatic visual transitions within your interactive SVG maps. This guide covers how to use video, audio, image toggling, and explosion effects to build highly engaging experiences.

## 1. Introduction

Advanced actions in SIVO go beyond basic tooltips and links. They allow your SVGs to:
- Play sound effects or narration.
- Open embedded video players.
- Dynamically toggle visual states (e.g., cycling through different background images).
- Create dramatic UI transitions by morphing or "exploding" into new layouts.

These actions are defined in `src/sivo/core/actions.py` and are attached to SVG elements using `sivo.map()`.

## 2. Multimedia Integration

### Adding Audio Playback (`AudioAction`)

The `AudioAction` allows you to trigger audio playback when a user interacts with an SVG element.

*Note: Modern browsers have strict autoplay policies. SIVO handles this internally by ensuring that audio playback triggered by a user click is wrapped with a `.catch()` block to gracefully handle any promise rejections.*

```python
from sivo.core.sivo import Sivo
from sivo.core.actions import AudioAction

sivo = Sivo.from_svg("map.svg")

sivo.map(
    element_id="play_button",
    actions=[
        AudioAction(audio_url="https://example.com/sound.mp3")
    ]
)
```

### Embedding Video (`VideoAction`)

The `VideoAction` displays a video embed (such as a YouTube iframe) in SIVO's info panel or a designated modal, depending on your template's configuration.

```python
from sivo.core.actions import VideoAction

sivo.map(
    element_id="cinema_icon",
    actions=[
        VideoAction(video_url="https://www.youtube.com/embed/dQw4w9WgXcQ")
    ]
)
```

## 3. Interactive Visual Effects

### Toggling Images (`ToggleImageAction`)

While some systems use a `cycle_state` feature, SIVO implements dynamic state transitions (like cycling through images on click) using the `ToggleImageAction`. (Note: A dedicated `cycle_state` feature is planned as a future enhancement).

This action changes the background image of the targeted SVG element, cycling through a list of URLs each time it is triggered.

```python
from sivo.core.actions import ToggleImageAction

sivo.map(
    element_id="status_indicator",
    actions=[
        ToggleImageAction(
            image_urls=[
                "https://example.com/state_red.png",
                "https://example.com/state_yellow.png",
                "https://example.com/state_green.png"
            ]
        )
    ]
)
```

### Dramatic UI Transitions (`ExplodeAction`)

The `ExplodeAction` is a powerful visual effect that dramatically transitions the UI by exploding the clicked element into a new, stylized grid or hex SVG layout.

```python
from sivo.core.actions import ExplodeAction

sivo.map(
    element_id="data_cluster",
    actions=[
        ExplodeAction(
            target_svg="expanded_cluster_view.svg",
            duration_ms=1000
        )
    ]
)
```

By combining these advanced actions, you can transform a static map into a dynamic, multimedia-rich application without writing custom frontend code.
