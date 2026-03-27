import os

def insert_zoom_logic(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    zoom_logic = """
                        } else if (action.action_type === 'zoom') {
                            var startZoom = chart.getOption().geo[0].zoom || 1.0;
                            var startCenter = chart.getOption().geo[0].center || ['50%', '50%'];

                            var targetZoom = action.zoom_level;
                            var targetCenter = action.center;

                            if (action.target_bbox) {
                                var bboxMinX = action.target_bbox[0];
                                var bboxMinY = action.target_bbox[1];
                                var bboxMaxX = action.target_bbox[2];
                                var bboxMaxY = action.target_bbox[3];
                                var bboxWidth = bboxMaxX - bboxMinX;
                                var bboxHeight = bboxMaxY - bboxMinY;

                                var geoModel = chart.getModel().getComponent('geo', 0);
                                if (geoModel && geoModel.coordinateSystem && geoModel.coordinateSystem.getBoundingRect) {
                                    var rect = geoModel.coordinateSystem.getBoundingRect();
                                    var fullWidth = rect.width;
                                    var fullHeight = rect.height;

                                    var sizeRatioStr = action.zoom_to_size || "90%";
                                    var sizeRatio = parseFloat(sizeRatioStr.replace('%', '')) / 100.0;

                                    var cw = chart.getWidth();
                                    var ch = chart.getHeight();
                                    var fitScale = Math.min(cw / fullWidth, ch / fullHeight);

                                    var shapeWAtZ1 = bboxWidth * fitScale;
                                    var shapeHAtZ1 = bboxHeight * fitScale;

                                    var screenScaleX = cw / shapeWAtZ1;
                                    var screenScaleY = ch / shapeHAtZ1;

                                    targetZoom = Math.min(screenScaleX, screenScaleY) * sizeRatio;
                                }
                            }

                            var startTime = performance.now();
                            var duration = action.duration_ms || 500;

                            function animateZoom(time) {
                                var progress = Math.min((time - startTime) / duration, 1.0);
                                var easeProgress = progress < 0.5 ? 4 * progress * progress * progress : 1 - Math.pow(-2 * progress + 2, 3) / 2;

                                var currentZ = startZoom + (targetZoom - startZoom) * easeProgress;
                                var currentCX = startCenter[0] + (targetCenter[0] - startCenter[0]) * easeProgress;
                                var currentCY = startCenter[1] + (targetCenter[1] - startCenter[1]) * easeProgress;

                                chart.setOption({ geo: [{ center: [currentCX, currentCY], zoom: currentZ }] });

                                if (progress < 1.0) {
                                    requestAnimationFrame(animateZoom);
                                }
                            }
                            requestAnimationFrame(animateZoom);
"""
    search_str = "                        } else if (action.action_type === 'drilldown' && action.target_svg) {"

    if search_str in content and "'zoom'" not in content:
        content = content.replace(search_str, zoom_logic + search_str)
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Updated {filepath}")
    else:
        print(f"Skipped {filepath} (Already updated or target not found)")

for root, _, files in os.walk('src/sivo/templates/dashboards/'):
    for file in files:
        if file.endswith('.html'):
            insert_zoom_logic(os.path.join(root, file))
