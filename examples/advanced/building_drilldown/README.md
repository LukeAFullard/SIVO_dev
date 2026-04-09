# Building Drilldown

## Description
1. Level 1: Building -> Drill down to Floorplan 2. Level 2: Floorplan -> Drill down to Room A Let's map Room B to something simple 3. Level 3: Inside Room A Assemble into a multi-view project

## Relevant Code
```python
    building_app = Sivo.from_svg(building_svg_path)
    floorplan_app = Sivo.from_svg(floorplan_svg_path)
    room_app = Sivo.from_svg(room_svg_path)
```
