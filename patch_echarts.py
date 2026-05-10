import re

with open("src/sivo/runtime/templates/echarts.html", "r") as f:
    content = f.read()

search_str = """                                            // Ensure previous element is restored
                                            if (window.sivoGeocoderPulsedNodes) {
                                                window.sivoGeocoderPulsedNodes.forEach(function(n) {
                                                    n.classList.remove('sivo-anim-fade-pulse-highlight');
                                                });
                                            }
                                            window.sivoGeocoderPulsedNodes = [];

                                            var possibleNames = [val];
                                            if (val.indexOf(' ') !== -1) possibleNames.push(val.replace(/ /g, '_'));

                                            // Pulse via CSS animation on the underlying SVG DOM nodes
                                            possibleNames.forEach(function(n) {
                                                document.querySelectorAll(`[id="${n}"], [name="${n}"]`).forEach(function(node) {
                                                    node.classList.add('sivo-anim-fade-pulse-highlight');
                                                    window.sivoGeocoderPulsedNodes.push(node);
                                                });
                                            });

                                            // Ensure styles are added once
                                            if (!document.getElementById('sivo-geocoder-pulse-style')) {
                                                var styleEl = document.createElement('style');
                                                styleEl.id = 'sivo-geocoder-pulse-style';
                                                styleEl.innerHTML = `
                                                @keyframes sivo-highlight-pulse {
                                                    0% { opacity: 0.4; }
                                                    50% { opacity: 1.0; }
                                                    100% { opacity: 0.4; }
                                                }
                                                .sivo-anim-fade-pulse-highlight {
                                                    animation: sivo-highlight-pulse 2s infinite ease-in-out !important;
                                                }`;
                                                document.head.appendChild(styleEl);
                                            }"""

replace_str = """                                            if (window.sivoGeocoderPulseInterval) {
                                                clearInterval(window.sivoGeocoderPulseInterval);
                                                window.sivoGeocoderPulseInterval = null;
                                            }

                                            if (window.sivoGeocoderPulsedNames) {
                                                try {
                                                    var opts = myChart.getOption();
                                                    if (opts && opts.series && opts.series[0] && opts.series[0].data) {
                                                        var restoreData = [];
                                                        window.sivoGeocoderPulsedNames.forEach(function(pn) {
                                                            var existingItem = opts.series[0].data.find(function(d) { return d.name === pn; });
                                                            if (existingItem) {
                                                                var newItem = JSON.parse(JSON.stringify(existingItem));
                                                                if (newItem.itemStyle) newItem.itemStyle.opacity = 1.0;
                                                                if (newItem.emphasis && newItem.emphasis.itemStyle) newItem.emphasis.itemStyle.opacity = 1.0;
                                                                if (newItem.select && newItem.select.itemStyle) newItem.select.itemStyle.opacity = 1.0;
                                                                restoreData.push(newItem);
                                                            }
                                                        });
                                                        if (restoreData.length > 0) {
                                                            myChart.setOption({ animation: false, series: [{ data: restoreData }] });
                                                        }
                                                    }
                                                } catch (e) {}
                                            }

                                            var possibleNames = [val];
                                            if (val.indexOf(' ') !== -1) possibleNames.push(val.replace(/ /g, '_'));
                                            window.sivoGeocoderPulsedNames = possibleNames;

                                            var startTime = Date.now();
                                            window.sivoGeocoderPulseInterval = setInterval(function() {
                                                var elapsed = Date.now() - startTime;
                                                var progress = (elapsed % 2000) / 2000;
                                                var opacity = 0.4 + 0.6 * (0.5 - 0.5 * Math.cos(progress * Math.PI * 2));

                                                try {
                                                    var opts = myChart.getOption();
                                                    if (opts && opts.series && opts.series[0] && opts.series[0].data) {
                                                        var updateData = [];
                                                        window.sivoGeocoderPulsedNames.forEach(function(pn) {
                                                            var existingItem = opts.series[0].data.find(function(d) { return d.name === pn; });
                                                            if (existingItem) {
                                                                var newItem = JSON.parse(JSON.stringify(existingItem));
                                                                if (!newItem.itemStyle) newItem.itemStyle = {};
                                                                newItem.itemStyle.opacity = opacity;

                                                                if (!newItem.emphasis) newItem.emphasis = {};
                                                                if (!newItem.emphasis.itemStyle) newItem.emphasis.itemStyle = {};
                                                                newItem.emphasis.itemStyle.opacity = opacity;

                                                                if (!newItem.select) newItem.select = {};
                                                                if (!newItem.select.itemStyle) newItem.select.itemStyle = {};
                                                                newItem.select.itemStyle.opacity = opacity;

                                                                updateData.push(newItem);
                                                            }
                                                        });
                                                        if (updateData.length > 0) {
                                                            myChart.setOption({ animation: false, series: [{ data: updateData }] });
                                                        }
                                                    }
                                                } catch (e) {}
                                            }, 100);"""

content = content.replace(search_str, replace_str)

search_not_found = """                                    if (window.sivoGeocoderPulsedNodes) {
                                        window.sivoGeocoderPulsedNodes.forEach(function(n) {
                                            n.classList.remove('sivo-anim-fade-pulse-highlight');
                                        });
                                        window.sivoGeocoderPulsedNodes = [];
                                    }"""

replace_not_found = """                                    if (window.sivoGeocoderPulseInterval) {
                                        clearInterval(window.sivoGeocoderPulseInterval);
                                        window.sivoGeocoderPulseInterval = null;
                                    }

                                    if (window.sivoGeocoderPulsedNames) {
                                        try {
                                            var opts = myChart.getOption();
                                            if (opts && opts.series && opts.series[0] && opts.series[0].data) {
                                                var restoreData = [];
                                                window.sivoGeocoderPulsedNames.forEach(function(pn) {
                                                    var existingItem = opts.series[0].data.find(function(d) { return d.name === pn; });
                                                    if (existingItem) {
                                                        var newItem = JSON.parse(JSON.stringify(existingItem));
                                                        if (newItem.itemStyle) newItem.itemStyle.opacity = 1.0;
                                                        if (newItem.emphasis && newItem.emphasis.itemStyle) newItem.emphasis.itemStyle.opacity = 1.0;
                                                        if (newItem.select && newItem.select.itemStyle) newItem.select.itemStyle.opacity = 1.0;
                                                        restoreData.push(newItem);
                                                    }
                                                });
                                                if (restoreData.length > 0) {
                                                    myChart.setOption({ animation: false, series: [{ data: restoreData }] });
                                                }
                                            }
                                        } catch (e) {}
                                        window.sivoGeocoderPulsedNames = [];
                                    }"""

content = content.replace(search_not_found, replace_not_found)

with open("src/sivo/runtime/templates/echarts.html", "w") as f:
    f.write(content)
