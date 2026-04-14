        const imageUpload = document.getElementById('image-upload');
        const canvas = document.getElementById('draw-canvas');
        const ctx = canvas.getContext('2d');
        const container = document.getElementById('canvas-container');
        const toolsDiv = document.getElementById('tools');
        const setupInstructions = document.getElementById('setup-instructions');
        const toolInstructions = document.getElementById('tool-instructions');
        const shapeList = document.getElementById('shape-list');

        const toolSelectBtn = document.getElementById('tool-select');
        const toolPolyBtn = document.getElementById('tool-poly');
        const toolRectBtn = document.getElementById('tool-rect');
        const toolEllipseBtn = document.getElementById('tool-ellipse');
        const toolFreehandBtn = document.getElementById('tool-freehand');
        const toolMagicBtn = document.getElementById('tool-magic');
        const toolSamBtn = document.getElementById('tool-sam');
        const magicOptionsDiv = document.getElementById('magic-wand-options');
        const samOptionsDiv = document.getElementById('sam-options');
        const samModelSelect = document.getElementById('sam-model-select');
        const samApplyBtn = document.getElementById('sam-apply-btn');
        const samAcceptBtn = document.getElementById('sam-accept-btn');

        samApplyBtn.addEventListener('click', () => {
            if (currentTool === 'sam' && isSamReady && isImageEmbedded && currentSamPoints.length > 0) {
                canvas.style.cursor = 'wait';
                const pList = currentSamPoints.map(p => ({x: p.x, y: p.y}));
                const lList = currentSamPoints.map(p => p.label);
                samWorker.postMessage({ type: 'segment', points: pList, labels: lList });
            }
        });

        const samClearBtn = document.getElementById('sam-clear-btn');
        if (samClearBtn) {
            samClearBtn.addEventListener('click', () => {
                currentSamPoints = [];
                currentSamPreview = null;
                if (samAcceptBtn) samAcceptBtn.disabled = true;
                redraw();
            });
        }

        if (samAcceptBtn) {
            samAcceptBtn.addEventListener('click', () => {
                if (currentTool === 'sam' && currentSamPreview) {
                    addShape('poly', null, [...currentSamPreview.points], null);
                    currentSamPoints = [];
                    currentSamPreview = null;
                    samAcceptBtn.disabled = true;
                    redraw();
                }
            });
        }

        samModelSelect.addEventListener('change', () => {
            if (toolSamBtn.classList.contains('tool-active')) {
                // If SAM is active, re-initialize worker immediately on change
                initSamWorker();
            }
        });

        const samLoadingDiv = document.getElementById('sam-loading');
        const samStatusText = document.getElementById('sam-status-text');
        const samProgressContainer = document.getElementById('sam-progress-container');
        const samProgressBar = document.getElementById('sam-progress-bar');
        const magicToleranceInput = document.getElementById('magic-tolerance');
        const magicToleranceVal = document.getElementById('tolerance-val');
        const toolColorInput = document.getElementById('tool-color');
        const btnUndo = document.getElementById('btn-undo');
        const btnRedo = document.getElementById('btn-redo');

        magicToleranceInput.addEventListener('input', (e) => {
            magicToleranceVal.innerText = e.target.value;
        });

        toolColorInput.addEventListener('input', () => {
            redraw(); // Update live colors
        });

        const exportBtn = document.getElementById('export-btn');

        const saveProjectBtn = document.getElementById('save-project-btn');
        const loadProjectBtn = document.getElementById('load-project-btn');
        const loadProjectFile = document.getElementById('load-project-file');

        const exportModal = document.getElementById('export-modal');
        const closeModalBtn = document.getElementById('close-modal');
        const downloadSvgBtn = document.getElementById('download-svg-btn');
        const saveIdbfsBtn = document.getElementById('save-idbfs-btn');
        const saveFilenameInput = document.getElementById('save-filename');
        const svgOutputArea = document.getElementById('svg-output');

        const zoomInBtn = document.getElementById('zoom-in-btn');
        const zoomOutBtn = document.getElementById('zoom-out-btn');
        const zoomResetBtn = document.getElementById('zoom-reset-btn');

        let shapes = []; // { id: string, type: 'poly'|'rect'|'ellipse', points: [{x,y}], rect: {x,y,w,h}, ellipse: {cx, cy, rx, ry} }
        let currentPath = [];
        let isDrawing = false;
        let currentTool = 'poly'; // 'select' or 'poly' or 'rect' or 'ellipse' or 'freehand' or 'magic'
        let startPoint = null;
        let tempEndPoint = null;

        let imgWidth = 0;
        let imgHeight = 0;
        let shapeCounter = 1;

        // Selection & Transformation State
        let selectedShapeIndices = new Set();
        let clipboard = [];
        let isDraggingShape = false;
        let isDraggingHandle = false;
        let selectedHandleIndex = -1; // -1 means none
        let lastDragPoint = null;

        // SAM Active State
        let currentSamPoints = []; // [{x, y, label: 1 or 0}]
        let currentSamPreview = null; // { points: [{x, y}] }

        let transformScale = 1.0;
        let transformPanX = 0;
        let transformPanY = 0;
        let isPanning = false;
        let isSpacePressed = false;
        let lastPanPoint = null;

        // Undo / Redo History State
        let historyStack = [];
        let historyIndex = -1;

        // Image data cache for Magic Wand
        let imageDataCache = null;
        const hiddenCanvas = document.createElement('canvas');
        const hiddenCtx = hiddenCanvas.getContext('2d', { willReadFrequently: true });

        const bgImage = new Image(); // Create image object manually, not tied to DOM

        // --- SAM Worker Setup ---
        let samWorker = null;
        let isSamReady = false;
        let isImageEmbedded = false;
        let currentModelId = null;

        function initSamWorker() {
            const selectedModelId = samModelSelect.value;
            if (samWorker && currentModelId === selectedModelId) return;

            if (samWorker) {
                samWorker.terminate();
                samWorker = null;
                isSamReady = false;
                isImageEmbedded = false;
            }

            currentModelId = selectedModelId;

            samLoadingDiv.style.display = 'block';
            samStatusText.innerText = "Initializing AI Model...";
            toolSamBtn.disabled = true;

            const workerCode = `
                import { env, SamModel, AutoProcessor, RawImage, Tensor } from 'https://cdn.jsdelivr.net/npm/@xenova/transformers@2.14.0';

                // Configure environments
                env.allowLocalModels = false;
                env.useBrowserCache = false;

                let model = null;
                let processor = null;
                let image_embeddings = null;
                let original_image_size = null;

                async function initModel(model_id) {
                    try {
                        model = await SamModel.from_pretrained(model_id, {
                            quantized: true,
                            progress_callback: (data) => {
                                if (data.status !== 'done') {
                                    postMessage({ type: 'progress', message: \`Downloading \${data.file || 'model'} (\${Math.round(data.progress || 0)}%)\` });
                                }
                            }
                        });
                        processor = await AutoProcessor.from_pretrained(model_id, {
                            progress_callback: (data) => {
                                if (data.status !== 'done') {
                                    postMessage({ type: 'progress', message: \`Downloading \${data.file || 'processor'} (\${Math.round(data.progress || 0)}%)\` });
                                }
                            }
                        });
                        postMessage({ type: 'ready' });
                    } catch (e) {
                        postMessage({ type: 'error', message: e.toString() });
                    }
                }

                self.onmessage = async (e) => {
                    if (e.data.type === 'init') {
                        initModel(e.data.model_id);
                    }
                    else if (e.data.type === 'embed') {
                        if (!model || !processor) return;
                        try {
                            const { imageSrc } = e.data;
                            postMessage({ type: 'progress', message: 'Embedding image...' });

                            const image = await RawImage.fromURL(imageSrc);
                            original_image_size = [image.height, image.width];

                            const inputs = await processor(image);
                            image_embeddings = await model.get_image_embeddings(inputs);
                            // We explicitly save reshaped_input_sizes to use in segment
                            self.reshaped_input_sizes = inputs.reshaped_input_sizes;

                            postMessage({ type: 'embedded', original_sizes: [original_image_size], reshaped_input_sizes: inputs.reshaped_input_sizes });
                        } catch (err) {
                            postMessage({ type: 'error', message: err.toString() });
                        }
                    }
                                        else if (e.data.type === 'segment') {
                        if (!model || !processor || !image_embeddings) return;
                        try {
                            const { points, labels } = e.data;

                            // Scale points to 256x256 space which is what the model uses for inputs
                            // We don't scale it here as the processor handles it or we might need manual scaling
                            // based on how transformers.js SAM is implemented.
                            // In Xenova SAM demo, they scale the [0,1] coordinates by reshaped_input_sizes
                            // But here we get world coordinates. Let's convert to [0,1] first.
                            // Convert world coordinates to [0,1] then to reshaped size
                            const reshaped = (self.reshaped_input_sizes && self.reshaped_input_sizes[0]) || [image_embeddings.image_embeddings.dims[2] * 16, image_embeddings.image_embeddings.dims[3] * 16];
                            const pts = points.map(p => {
                                const normX = p.x / original_image_size[1];
                                const normY = p.y / original_image_size[0];
                                return [normX * reshaped[1], normY * reshaped[0]];
                            });

                            // Manual Tensor creation (like xenova demo)
                            const input_points = new Tensor(
                                'float32',
                                pts.flat(Infinity),
                                [1, 1, pts.length, 2],
                            );

                            // Labels also need to be BigInt for int64 Tensor!
                            const BigIntLabels = labels.map(x => BigInt(x));
                            const input_labels = new Tensor(
                                'int64',
                                BigIntLabels.flat(Infinity),
                                [1, 1, labels.length],
                            );

                            const outputs = await model({
                                ...image_embeddings,
                                input_points,
                                input_labels,
                            });

                            // Post-process the masks
                            // self.reshaped_input_sizes was saved during embed!
                            const reshaped_sizes = self.reshaped_input_sizes || [[image_embeddings.image_embeddings.dims[2] * 16, image_embeddings.image_embeddings.dims[3] * 16]];
                            const masks = await processor.post_process_masks(
                                outputs.pred_masks,
                                [original_image_size],
                                reshaped_sizes
                            );

                            // The post-processed mask matches the original image dimensions exactly
                            const finalMask = masks[0][0]; // Tensor of shape [3, h, w]

                            // Select best mask using iou_scores
                            const scores = outputs.iou_scores.data;
                            let bestIndex = 0;
                            for (let i = 1; i < scores.length; ++i) {
                                if (scores[i] > scores[bestIndex]) {
                                    bestIndex = i;
                                }
                            }

                            const numMasks = scores.length;
                            const maskData = finalMask.data;
                            const mw = finalMask.dims[2];
                            const mh = finalMask.dims[1];
                            const binaryMask = new Uint8Array(mw * mh);

                            for (let i = 0; i < mw * mh; ++i) {
                                binaryMask[i] = maskData[bestIndex * mw * mh + i] > 0.0 ? 1 : 0;
                            }

                            postMessage({ type: 'segmented', mask: binaryMask, w: mw, h: mh, origW: original_image_size[1], origH: original_image_size[0] });
                        } catch (err) {
                            postMessage({ type: 'error', message: err.toString() });
                        }
                    }  };
            `;

            const dataUri = 'data:text/javascript;charset=utf-8,' + encodeURIComponent(workerCode);
            samWorker = new Worker(dataUri, { type: 'module' });

            samWorker.onmessage = (e) => {
                if (e.data.type === 'ready') {
                    isSamReady = true;
                    samProgressContainer.style.display = 'none';
                    samProgressBar.style.width = '0%';
                    // If an image was loaded before SAM was ready, embed it now
                    if (bgImage.src && !isImageEmbedded) {
                        embedImageForSam();
                    } else {
                        samLoadingDiv.style.display = 'none';
                        toolSamBtn.disabled = false;
                    }
                } else if (e.data.type === 'progress') {
                    samStatusText.innerText = e.data.message;
                    if (e.data.progress !== undefined) {
                        samProgressContainer.style.display = 'block';
                        samProgressBar.style.width = e.data.progress + '%';
                    }
                } else if (e.data.type === 'embedded') {
                    isImageEmbedded = true;
                    samLoadingDiv.style.display = 'none';
                    samProgressContainer.style.display = 'none';
                    toolSamBtn.disabled = false;
                } else if (e.data.type === 'segmented') {
                    handleSamSegmentation(e.data.mask, e.data.w, e.data.h, e.data.origW, e.data.origH);
                } else if (e.data.type === 'error') {
                    console.error("SAM Worker Error:", e.data.message);
                    samStatusText.innerText = "SAM Error";
                    samProgressContainer.style.display = 'none';
                    setTimeout(() => { samLoadingDiv.style.display = 'none'; }, 3000);
                }
            };

            samWorker.postMessage({ type: 'init', model_id: currentModelId });
        }

        function embedImageForSam() {
            if (!isSamReady || !bgImage.src) return;
            samLoadingDiv.style.display = 'block';
            samStatusText.innerText = "Computing Image Embedding...";
            toolSamBtn.disabled = true;
            samWorker.postMessage({ type: 'embed', imageSrc: bgImage.src });
        }

        function handleSamSegmentation(maskArray, w, h, origW, origH) {
            canvas.style.cursor = 'crosshair';

            // Fast extraction logic using existing Moore-Neighborhood trace
            const rawPath = traceContour(maskArray, w, h);
            if (rawPath && rawPath.length > 2) {
                const simplified = simplifyPath(rawPath, 2.0);

                // Scale back up to original image dimensions if necessary
                // Sometimes w and h are exactly origW and origH because of post_process_masks
                // but if not, we handle it here.
                const scaleX = origW / w;
                const scaleY = origH / h;
                const scaledPoints = simplified.map(p => ({ x: p.x * scaleX, y: p.y * scaleY }));

                currentSamPreview = { points: scaledPoints };
            } else {
                currentSamPreview = null;
            }
            if (samAcceptBtn) {
                samAcceptBtn.disabled = !currentSamPreview;
            }
            redraw();
        }

        // --- Undo / Redo History System ---
        function saveState() {
            // Drop any history after the current index if we branched
            if (historyIndex < historyStack.length - 1) {
                historyStack = historyStack.slice(0, historyIndex + 1);
            }

            // Deep copy shapes array
            const state = JSON.parse(JSON.stringify(shapes));
            historyStack.push(state);

            // Limit stack to 50 states to save memory
            if (historyStack.length > 50) {
                historyStack.shift();
            } else {
                historyIndex++;
            }
            updateHistoryButtons();
        }

        function undo() {
            if (historyIndex > 0) {
                historyIndex--;
                shapes = JSON.parse(JSON.stringify(historyStack[historyIndex]));

                // Clear selection if the shape was deleted in this past state
                const newSel = new Set(); selectedShapeIndices.forEach(i => {if (i < shapes.length) newSel.add(i);}); selectedShapeIndices = newSel;

                updateShapeList();
                redraw();
                updateHistoryButtons();
            } else if (historyIndex === 0) {
                // Revert to empty state (before first drawing)
                historyIndex = -1;
                shapes = [];
                selectedShapeIndices.clear();
                updateShapeList();
                redraw();
                updateHistoryButtons();
            }
        }

        function redo() {
            if (historyIndex < historyStack.length - 1) {
                historyIndex++;
                shapes = JSON.parse(JSON.stringify(historyStack[historyIndex]));
                updateShapeList();
                redraw();
                updateHistoryButtons();
            }
        }

        function updateHistoryButtons() {
            btnUndo.disabled = historyIndex < 0;
            btnRedo.disabled = historyIndex >= historyStack.length - 1;
        }

        btnUndo.addEventListener('click', undo);
        btnRedo.addEventListener('click', redo);


        // --- Image Loading ---
        function handleImageLoad(src, preserveShapes = false) {
            const img = new Image();
            img.onload = () => {
                imgWidth = img.width;
                imgHeight = img.height;

                canvas.width = window.innerWidth - 300; // minus sidebar
                canvas.height = window.innerHeight;

                // Center the image initially
                transformScale = Math.min((canvas.width - 100) / imgWidth, (canvas.height - 100) / imgHeight);
                if (transformScale > 1) transformScale = 1;
                transformPanX = (canvas.width - (imgWidth * transformScale)) / 2;
                transformPanY = (canvas.height - (imgHeight * transformScale)) / 2;

                container.style.display = 'block';
                toolsDiv.style.display = 'block';
                setupInstructions.style.display = 'none';

                // Cache image data for magic wand
                hiddenCanvas.width = imgWidth;
                hiddenCanvas.height = imgHeight;
                hiddenCtx.drawImage(img, 0, 0);
                imageDataCache = hiddenCtx.getImageData(0, 0, imgWidth, imgHeight);

                if (!preserveShapes) {
                    shapes = [];
                }

                updateShapeList();
                redraw();

                // Reset SAM embedding state for new image
                isImageEmbedded = false;

                // Only embed if SAM was already loaded and active from a previous image
                if (samWorker && isSamReady) {
                    embedImageForSam();
                }
            };
            bgImage.src = src; // Trigger redraw updates inside onload when image naturally loads
            img.src = src;
        }

        imageUpload.addEventListener('change', (e) => {
            const file = e.target.files[0];
            if (!file) return;

            const reader = new FileReader();
            reader.onload = (event) => {
                handleImageLoad(event.target.result, false);
            };
            reader.readAsDataURL(file);
        });

        // Resize canvas when window resizes
        window.addEventListener('resize', () => {
            if (imgWidth > 0) {
                canvas.width = window.innerWidth - 300;
                canvas.height = window.innerHeight;
                redraw();
            }
        });

        // --- Tool Selection ---
        function setTool(tool) {
            currentTool = tool;
            toolSelectBtn.classList.remove('tool-active');
            toolPolyBtn.classList.remove('tool-active');
            toolRectBtn.classList.remove('tool-active');
            toolEllipseBtn.classList.remove('tool-active');
            toolFreehandBtn.classList.remove('tool-active');
            toolMagicBtn.classList.remove('tool-active');
            toolSamBtn.classList.remove('tool-active');
            magicOptionsDiv.style.display = 'none';
            samOptionsDiv.style.display = 'none';

            if (tool === 'select') {
                toolSelectBtn.classList.add('tool-active');
                toolInstructions.innerHTML = "Click a shape to select it. Drag to move it.";
            } else if (tool === 'poly') {
                toolPolyBtn.classList.add('tool-active');
                toolInstructions.innerHTML = "Click to add points. Press <strong>Enter</strong> or click the first point to complete the polygon. Press <strong>Esc</strong> to cancel.";
            } else if (tool === 'rect') {
                toolRectBtn.classList.add('tool-active');
                toolInstructions.innerHTML = "Click and drag to create a rectangle.";
            } else if (tool === 'ellipse') {
                toolEllipseBtn.classList.add('tool-active');
                toolInstructions.innerHTML = "Click and drag to draw an ellipse. Hold Shift for a perfect circle.";
            } else if (tool === 'freehand') {
                toolFreehandBtn.classList.add('tool-active');
                toolInstructions.innerHTML = "Click and drag freely to draw a path. Release to close it. The path is automatically smoothed.";
            } else if (tool === 'magic') {
                toolMagicBtn.classList.add('tool-active');
                magicOptionsDiv.style.display = 'block';
                toolInstructions.innerHTML = "Click any solid colored area in the image. The tool will auto-detect the edges and generate a polygon.";
            } else if (tool === 'sam') {
                toolSamBtn.classList.add('tool-active');
                samOptionsDiv.style.display = 'block';
                toolInstructions.innerHTML = "<strong>Left Click</strong> to include. <strong>Right Click</strong> to exclude. Click <strong>Generate Mask</strong> then <strong>Accept Shape</strong> to complete.";

                // Lazy-load SAM Worker when tool is clicked
                if (!samWorker) {
                    initSamWorker();
                } else if (isSamReady && !isImageEmbedded) {
                    embedImageForSam();
                }
            }

            // Reset state
            currentPath = [];
            currentSamPoints = [];
            currentSamPreview = null;
            if (samAcceptBtn) samAcceptBtn.disabled = true;
            isDrawing = false;
            startPoint = null;
            selectedShapeIndices.clear();
            redraw();
        }

        toolSelectBtn.addEventListener('click', () => setTool('select'));
        toolPolyBtn.addEventListener('click', () => setTool('poly'));
        toolRectBtn.addEventListener('click', () => setTool('rect'));
        toolEllipseBtn.addEventListener('click', () => setTool('ellipse'));
        toolFreehandBtn.addEventListener('click', () => setTool('freehand'));
        toolMagicBtn.addEventListener('click', () => setTool('magic'));
        toolSamBtn.addEventListener('click', () => setTool('sam'));

        // --- Douglas-Peucker Algorithm for Path Simplification ---
        function getSqDist(p1, p2) {
            const dx = p1.x - p2.x, dy = p1.y - p2.y;
            return dx * dx + dy * dy;
        }

        function getSqSegDist(p, p1, p2) {
            let x = p1.x, y = p1.y, dx = p2.x - x, dy = p2.y - y;
            if (dx !== 0 || dy !== 0) {
                const t = ((p.x - x) * dx + (p.y - y) * dy) / (dx * dx + dy * dy);
                if (t > 1) {
                    x = p2.x; y = p2.y;
                } else if (t > 0) {
                    x += dx * t; y += dy * t;
                }
            }
            dx = p.x - x; dy = p.y - y;
            return dx * dx + dy * dy;
        }

        function simplifyDPStep(points, first, last, sqTolerance, simplified) {
            let maxSqDist = sqTolerance;
            let index;
            for (let i = first + 1; i < last; i++) {
                const sqDist = getSqSegDist(points[i], points[first], points[last]);
                if (sqDist > maxSqDist) {
                    index = i; maxSqDist = sqDist;
                }
            }
            if (maxSqDist > sqTolerance) {
                if (index - first > 1) simplifyDPStep(points, first, index, sqTolerance, simplified);
                simplified.push(points[index]);
                if (last - index > 1) simplifyDPStep(points, index, last, sqTolerance, simplified);
            }
        }

        function simplifyPath(points, tolerance) {
            if (points.length <= 2) return points;
            const sqTolerance = tolerance !== undefined ? tolerance * tolerance : 1;
            const simplified = [points[0]];
            simplifyDPStep(points, 0, points.length - 1, sqTolerance, simplified);
            simplified.push(points[points.length - 1]);
            return simplified;
        }

        // --- Magic Wand Algorithm ---
        function magicWand(startX, startY, tolerance) {
            if (!imageDataCache) return;
            const imgData = imageDataCache.data;
            const w = imgWidth;
            const h = imgHeight;

            startX = Math.round(startX);
            startY = Math.round(startY);
            if (startX < 0 || startX >= w || startY < 0 || startY >= h) return;

            const startIndex = (startY * w + startX) * 4;
            const r = imgData[startIndex];
            const g = imgData[startIndex + 1];
            const b = imgData[startIndex + 2];
            const a = imgData[startIndex + 3];

            // Boolean mask of filled pixels
            const mask = new Uint8Array(w * h);
            const stack = [[startX, startY]];

            function colorMatch(idx) {
                const tr = imgData[idx];
                const tg = imgData[idx + 1];
                const tb = imgData[idx + 2];
                const ta = imgData[idx + 3];
                // Simple Euclidean distance in RGB space
                const dist = Math.sqrt((r-tr)*(r-tr) + (g-tg)*(g-tg) + (b-tb)*(b-tb));
                // Scale distance to 0-100 range roughly (max dist is ~441)
                return (dist / 4.41) <= tolerance;
            }

            // Flood fill using 1D index array for stack to save memory
            // mask states: 0 = unvisited, 1 = matched/filled, 2 = visited/unmatched
            const stack1D = [startY * w + startX];

            while (stack1D.length > 0) {
                const idx = stack1D.pop();

                if (mask[idx]) continue; // Already visited (1 or 2)

                const pixelIdx = idx * 4;
                if (!colorMatch(pixelIdx)) {
                    mask[idx] = 2; // Visited but no match
                    continue;
                }

                mask[idx] = 1; // Filled

                const y = Math.floor(idx / w);
                const x = idx % w;

                if (x > 0 && !mask[idx - 1]) stack1D.push(idx - 1);
                if (x < w - 1 && !mask[idx + 1]) stack1D.push(idx + 1);
                if (y > 0 && !mask[idx - w]) stack1D.push(idx - w);
                if (y < h - 1 && !mask[idx + w]) stack1D.push(idx + w);
            }

            // --- Marching Squares / Contour Tracing to extract Path ---
            return traceContour(mask, w, h);
        }

        function traceContour(mask, w, h) {
            // Find a starting pixel
            let startX = -1, startY = -1;
            for (let y = 0; y < h; y++) {
                for (let x = 0; x < w; x++) {
                    if (mask[y * w + x] === 1) { // Explicitly check for 1 (filled) not just truthy (could be 2)
                        startX = x; startY = y; break;
                    }
                }
                if (startX !== -1) break;
            }
            if (startX === -1) return [];

            const path = [];
            let cx = startX, cy = startY;

            // Directions: 0=E, 1=SE, 2=S, 3=SW, 4=W, 5=NW, 6=N, 7=NE (Clockwise)
            const dx = [1, 1, 0, -1, -1, -1, 0, 1];
            const dy = [0, 1, 1, 1, 0, -1, -1, -1];
            let dir = 7; // Initial search direction

            path.push({x: cx, y: cy});

            // Moore Neighborhood Tracing
            let pointsFound = 0;
            const MAX_POINTS = 10000; // safety breaker

            while (pointsFound < MAX_POINTS) {
                let found = false;
                // Check 8 neighbors counter-clockwise starting from the previous background pixel
                for (let i = 0; i < 8; i++) {
                    const ndir = (dir + i) % 8;
                    const nx = cx + dx[ndir];
                    const ny = cy + dy[ndir];

                    if (nx >= 0 && nx < w && ny >= 0 && ny < h && mask[ny * w + nx] === 1) { // Explicitly check for 1
                        cx = nx; cy = ny;
                        path.push({x: cx, y: cy});
                        // Backtrack by 2 to find the next boundary pixel
                        dir = (ndir + 5) % 8;
                        found = true;
                        pointsFound++;
                        break;
                    }
                }

                // If we're back at the start, contour is closed
                if (cx === startX && cy === startY) break;
                if (!found) break; // Isolated pixel
            }

            return path;
        }

        // --- Coordinate Transformation Helpers ---
        function getMouseWorldPos(e) {
            const rect = canvas.getBoundingClientRect();
            // Get raw screen coords relative to canvas
            const screenX = (e.clientX - rect.left) * (canvas.width / rect.width);
            const screenY = (e.clientY - rect.top) * (canvas.height / rect.height);
            // Translate to world coords
            const worldX = (screenX - transformPanX) / transformScale;
            const worldY = (screenY - transformPanY) / transformScale;
            return { x: worldX, y: worldY, screenX, screenY };
        }

        // --- Ray Casting for Hit Testing ---
        function pointInPolygon(point, vs) {
            let x = point.x, y = point.y;
            let inside = false;
            for (let i = 0, j = vs.length - 1; i < vs.length; j = i++) {
                let xi = vs[i].x, yi = vs[i].y;
                let xj = vs[j].x, yj = vs[j].y;
                let intersect = ((yi > y) != (yj > y)) && (x < (xj - xi) * (y - yi) / (yj - yi) + xi);
                if (intersect) inside = !inside;
            }
            return inside;
        }

        // --- Handle Hit Testing ---
        function getHandleAtPoint(point, shape) {
            const handleSize = 8 / transformScale;
            const hs = handleSize / 2;

            const check = (hx, hy, idx) => {
                if (point.x >= hx - hs && point.x <= hx + hs && point.y >= hy - hs && point.y <= hy + hs) {
                    return idx;
                }
                return -1;
            };

            if (shape.type === 'rect') {
                const {x, y, w, h} = shape.rect;
                // 4 corners: TL=0, TR=1, BR=2, BL=3
                let hIdx = check(x, y, 0); if (hIdx !== -1) return hIdx;
                hIdx = check(x + w, y, 1); if (hIdx !== -1) return hIdx;
                hIdx = check(x + w, y + h, 2); if (hIdx !== -1) return hIdx;
                hIdx = check(x, y + h, 3); if (hIdx !== -1) return hIdx;
            } else if (shape.type === 'ellipse') {
                const {cx, cy, rx, ry} = shape.ellipse;
                // 4 cardinal points: T=0, R=1, B=2, L=3
                let hIdx = check(cx, cy - ry, 0); if (hIdx !== -1) return hIdx;
                hIdx = check(cx + rx, cy, 1); if (hIdx !== -1) return hIdx;
                hIdx = check(cx, cy + ry, 2); if (hIdx !== -1) return hIdx;
                hIdx = check(cx - rx, cy, 3); if (hIdx !== -1) return hIdx;
            } else if (shape.type === 'poly') {
                for (let i = 0; i < shape.points.length; i++) {
                    const hIdx = check(shape.points[i].x, shape.points[i].y, i);
                    if (hIdx !== -1) return hIdx;
                }
            }
            return -1;
        }

        function getShapeAtPoint(point) {
            // Check in reverse order so we hit the top-most shape first
            for (let i = shapes.length - 1; i >= 0; i--) {
                const shape = shapes[i];
                if (shape.type === 'rect') {
                    if (point.x >= shape.rect.x && point.x <= shape.rect.x + shape.rect.w &&
                        point.y >= shape.rect.y && point.y <= shape.rect.y + shape.rect.h) {
                        return i;
                    }
                } else if (shape.type === 'ellipse') {
                    // (x-cx)^2 / rx^2 + (y-cy)^2 / ry^2 <= 1
                    const dx = point.x - shape.ellipse.cx;
                    const dy = point.y - shape.ellipse.cy;
                    const val = (dx * dx) / (shape.ellipse.rx * shape.ellipse.rx) + (dy * dy) / (shape.ellipse.ry * shape.ellipse.ry);
                    if (val <= 1.0) {
                        return i;
                    }
                } else if (shape.type === 'poly') {
                    if (pointInPolygon(point, shape.points)) {
                        return i;
                    }
                }
            }
            return -1;
        }

        // Prevent default context menu on canvas for right clicks
        canvas.addEventListener('contextmenu', e => e.preventDefault());

        // --- Keyboard Events for Panning ---
        window.addEventListener('keydown', (e) => {
            if (e.code === 'Space' && !isSpacePressed) {
                isSpacePressed = true;
                canvas.style.cursor = 'grab';
                e.preventDefault(); // prevent scrolling
            }
        });

        window.addEventListener('keyup', (e) => {
            if (e.code === 'Space') {
                isSpacePressed = false;
                isPanning = false;
                canvas.style.cursor = currentTool === 'select' ? 'default' : 'crosshair';
            }
        });

        // --- Mouse Events for Drawing / Panning / Editing ---
        canvas.addEventListener('mousedown', (e) => {
            const { x, y, screenX, screenY } = getMouseWorldPos(e);

            // Panning Logic
            if (isSpacePressed || e.button === 1) { // Middle click or Space+Drag
                isPanning = true;
                lastPanPoint = { x: screenX, y: screenY };
                canvas.style.cursor = 'grabbing';
                e.preventDefault();
                return;
            }

            // Normal Tools
            if (currentTool === 'select') {
                if (selectedShapeIndices.size === 1) {
                    const singleIdx = Array.from(selectedShapeIndices)[0];
                    const handleIdx = getHandleAtPoint({x, y}, shapes[singleIdx]);
                    if (handleIdx !== -1) {
                        isDraggingHandle = true;
                        selectedHandleIndex = handleIdx;
                        return; // Done
                    }
                }

                const hoverIdx = getShapeAtPoint({x, y});
                if (hoverIdx !== -1) {
                    if (e.shiftKey) {
                        if (selectedShapeIndices.has(hoverIdx)) selectedShapeIndices.delete(hoverIdx);
                        else selectedShapeIndices.add(hoverIdx);
                    } else {
                        if (!selectedShapeIndices.has(hoverIdx)) {
                            selectedShapeIndices.clear();
                            selectedShapeIndices.add(hoverIdx);
                        }
                    }
                    isDraggingShape = true;
                    lastDragPoint = {x, y};
                } else {
                    if (!e.shiftKey) selectedShapeIndices.clear();
                }
                redraw();
                return;
            }

            if (currentTool === 'poly') {
                // If clicking near the first point to close
                if (currentPath.length > 2) {
                    const firstPt = currentPath[0];
                    const dist = Math.hypot(firstPt.x - x, firstPt.y - y);
                    if (dist < 10) {
                        finishPolygon();
                        return;
                    }
                }
                currentPath.push({x, y});
                redraw();
            }
            else if (currentTool === 'rect' || currentTool === 'ellipse') {
                isDrawing = true;
                startPoint = {x, y};
                tempEndPoint = {x, y};
            }
            else if (currentTool === 'freehand') {
                isDrawing = true;
                currentPath = [{x, y}];
                redraw();
            }
            else if (currentTool === 'magic') {
                const tol = parseInt(magicToleranceInput.value, 10);
                canvas.style.cursor = 'wait';

                // Use setTimeout to allow UI to update cursor before heavy work
                setTimeout(() => {
                    const rawPath = magicWand(x, y, tol);
                    if (rawPath && rawPath.length > 2) {
                        // Simplify the extremely dense pixel path
                        const simplified = simplifyPath(rawPath, 2.0);
                        addShape('poly', null, simplified, null);
                    }
                    canvas.style.cursor = 'crosshair';
                    redraw();
                }, 10);
            }
            else if (currentTool === 'sam' && isSamReady && isImageEmbedded) {
                // Ignore left/right clicks for tools other than select or specific logic, but handle SAM right clicks here
                if (e.button === 0) {
                    currentSamPoints.push({ x, y, label: 1 }); // Positive point
                } else if (e.button === 2) {
                    currentSamPoints.push({ x, y, label: 0 }); // Negative point
                }

                // Just update the points visually, do not trigger model
                redraw();
            }
        });

        canvas.addEventListener('mousemove', (e) => {
            const { x, y, screenX, screenY } = getMouseWorldPos(e);

            if (isPanning && lastPanPoint) {
                const dx = screenX - lastPanPoint.x;
                const dy = screenY - lastPanPoint.y;
                transformPanX += dx;
                transformPanY += dy;
                lastPanPoint = { x: screenX, y: screenY };
                redraw();
                return;
            }

            if (currentTool === 'select') {
                if (isDraggingHandle && selectedShapeIndices.size === 1 && selectedHandleIndex !== -1) {
                    const shape = shapes[Array.from(selectedShapeIndices)[0]];
                    if (shape.type === 'poly') {
                        shape.points[selectedHandleIndex] = {x, y};
                    } else if (shape.type === 'rect') {
                        const {x: sx, y: sy, w: sw, h: sh} = shape.rect;
                        if (selectedHandleIndex === 0) { // TL
                            shape.rect.w = sw + (sx - x);
                            shape.rect.h = sh + (sy - y);
                            shape.rect.x = x;
                            shape.rect.y = y;
                        } else if (selectedHandleIndex === 1) { // TR
                            shape.rect.w = x - sx;
                            shape.rect.h = sh + (sy - y);
                            shape.rect.y = y;
                        } else if (selectedHandleIndex === 2) { // BR
                            shape.rect.w = x - sx;
                            shape.rect.h = y - sy;
                        } else if (selectedHandleIndex === 3) { // BL
                            shape.rect.w = sw + (sx - x);
                            shape.rect.h = y - sy;
                            shape.rect.x = x;
                        }
                        // Enforce positive width/height to avoid inversion bugs
                        if (shape.rect.w < 1) shape.rect.w = 1;
                        if (shape.rect.h < 1) shape.rect.h = 1;

                    } else if (shape.type === 'ellipse') {
                        const {cx, cy} = shape.ellipse;
                        if (selectedHandleIndex === 0 || selectedHandleIndex === 2) { // T or B
                            shape.ellipse.ry = Math.abs(cy - y);
                        } else if (selectedHandleIndex === 1 || selectedHandleIndex === 3) { // R or L
                            shape.ellipse.rx = Math.abs(cx - x);
                        }
                    }
                    redraw();
                } else if (isDraggingShape && selectedShapeIndices.size > 0 && lastDragPoint) {
                    const dx = x - lastDragPoint.x;
                    const dy = y - lastDragPoint.y;

                    selectedShapeIndices.forEach(idx => {
                        const shape = shapes[idx];
                        if (shape.type === 'rect') {
                            shape.rect.x += dx;
                            shape.rect.y += dy;
                        } else if (shape.type === 'ellipse') {
                            shape.ellipse.cx += dx;
                            shape.ellipse.cy += dy;
                        } else if (shape.type === 'poly') {
                            shape.points.forEach(p => { p.x += dx; p.y += dy; });
                        }
                    });

                    lastDragPoint = { x, y };
                    redraw();
                } else {
                    // Hover effect
                    let cursor = 'default';
                    if (selectedShapeIndices.size === 1) {
                        const hIdx = getHandleAtPoint({x, y}, shapes[Array.from(selectedShapeIndices)[0]]);
                        if (hIdx !== -1) cursor = 'crosshair';
                    }
                    if (cursor === 'default') {
                        const hoverIdx = getShapeAtPoint({x, y});
                        if (hoverIdx !== -1) cursor = 'move';
                    }
                    canvas.style.cursor = cursor;
                }
                return;
            }

            if (currentTool === 'poly' && currentPath.length > 0) {
                tempEndPoint = {x, y};
                redraw();
            }
            else if ((currentTool === 'rect' || currentTool === 'ellipse') && isDrawing) {
                tempEndPoint = {x, y};

                // If shift is held, constrain ellipse to perfect circle
                if (currentTool === 'ellipse' && e.shiftKey) {
                    const dx = tempEndPoint.x - startPoint.x;
                    const dy = tempEndPoint.y - startPoint.y;
                    const radius = Math.max(Math.abs(dx), Math.abs(dy));
                    tempEndPoint.x = startPoint.x + Math.sign(dx) * radius;
                    tempEndPoint.y = startPoint.y + Math.sign(dy) * radius;
                }

                redraw();
            }
            else if (currentTool === 'freehand' && isDrawing) {
                currentPath.push({x, y});
                redraw();
            }
        });

        canvas.addEventListener('mouseup', (e) => {
            if (isPanning) {
                isPanning = false;
                canvas.style.cursor = currentTool === 'select' ? 'default' : 'crosshair';
                return;
            }
            if (currentTool === 'select') {
                if (isDraggingHandle) {
                    isDraggingHandle = false;
                    selectedHandleIndex = -1;
                    saveState();
                } else if (isDraggingShape) {
                    isDraggingShape = false;
                    lastDragPoint = null;
                    saveState();
                }
                return;
            }

            if (isDrawing && (currentTool === 'rect' || currentTool === 'ellipse')) {
                isDrawing = false;

                if (currentTool === 'rect') {
                    const rectBounds = {
                        x: Math.min(startPoint.x, tempEndPoint.x),
                        y: Math.min(startPoint.y, tempEndPoint.y),
                        w: Math.abs(tempEndPoint.x - startPoint.x),
                        h: Math.abs(tempEndPoint.y - startPoint.y)
                    };

                    if (rectBounds.w > 5 && rectBounds.h > 5) {
                        addShape('rect', rectBounds, null, null);
                    }
                } else if (currentTool === 'ellipse') {
                    // Start point is center, tempEndPoint is edge
                    // OR start point is corner, tempEndPoint is opposite corner
                    // Let's go with start->temp = bounding box for consistency with rect
                    const rx = Math.abs(tempEndPoint.x - startPoint.x) / 2;
                    const ry = Math.abs(tempEndPoint.y - startPoint.y) / 2;
                    const cx = Math.min(startPoint.x, tempEndPoint.x) + rx;
                    const cy = Math.min(startPoint.y, tempEndPoint.y) + ry;

                    if (rx > 2 && ry > 2) {
                        addShape('ellipse', null, null, {cx, cy, rx, ry});
                    }
                }

                startPoint = null;
                tempEndPoint = null;
                redraw();
            }
            else if (currentTool === 'freehand' && isDrawing) {
                isDrawing = false;
                if (currentPath.length > 2) {
                    // Simplify the path so it's not a million points
                    const simplified = simplifyPath(currentPath, 2.0); // 2.0 tolerance works well for freehand
                    addShape('poly', null, simplified, null);
                }
                currentPath = [];
                redraw();
            }
        });

        // --- Zooming Event (Mouse Wheel) ---
        canvas.addEventListener('wheel', (e) => {
            e.preventDefault();
            const rect = canvas.getBoundingClientRect();
            const screenX = (e.clientX - rect.left) * (canvas.width / rect.width);
            const screenY = (e.clientY - rect.top) * (canvas.height / rect.height);

            // Compute world position before zoom
            const worldX = (screenX - transformPanX) / transformScale;
            const worldY = (screenY - transformPanY) / transformScale;

            const zoomSpeed = 0.1;
            if (e.deltaY < 0) {
                transformScale *= (1 + zoomSpeed);
            } else {
                transformScale *= (1 - zoomSpeed);
            }
            transformScale = Math.max(0.1, Math.min(transformScale, 10)); // Clamp scale

            // Adjust pan to keep the world position under the mouse
            transformPanX = screenX - worldX * transformScale;
            transformPanY = screenY - worldY * transformScale;

            redraw();
        }, { passive: false });

        // --- Zoom Buttons ---
        function applyZoomCenter(factor) {
            const rect = canvas.getBoundingClientRect();
            const screenX = rect.width / 2;
            const screenY = rect.height / 2;

            const worldX = (screenX - transformPanX) / transformScale;
            const worldY = (screenY - transformPanY) / transformScale;

            transformScale *= factor;
            transformScale = Math.max(0.1, Math.min(transformScale, 10));

            transformPanX = screenX - worldX * transformScale;
            transformPanY = screenY - worldY * transformScale;
            redraw();
        }

        zoomInBtn.addEventListener('click', () => applyZoomCenter(1.2));
        zoomOutBtn.addEventListener('click', () => applyZoomCenter(0.8));
        zoomResetBtn.addEventListener('click', () => {
            const rect = canvas.getBoundingClientRect();
            const scaleX = rect.width / imgWidth;
            const scaleY = rect.height / imgHeight;
            transformScale = Math.min(scaleX, scaleY) * 0.95;

            const renderW = imgWidth * transformScale;
            const renderH = imgHeight * transformScale;
            transformPanX = (rect.width - renderW) / 2;
            transformPanY = (rect.height - renderH) / 2;
            redraw();
        });

        // --- Keyboard Events ---
        window.addEventListener('keydown', (e) => {
            // Ignore keystrokes if typing in an input
            if (e.target.tagName.toLowerCase() === 'input' && e.target.type === 'text') return;

            if (e.code === 'Space' && !isSpacePressed) {
                isSpacePressed = true;
                canvas.style.cursor = 'grab';
                e.preventDefault(); // prevent scrolling
            }
            if (e.key === 'Escape') {
                currentPath = [];
                isDrawing = false;
                startPoint = null;
                redraw();
            } else if (e.key === 'Enter') {
                if (currentTool === 'poly' && currentPath.length > 2) {
                    finishPolygon();
                } else if (currentTool === 'sam' && currentSamPreview) {
                    // Finalize SAM Shape
                    addShape('poly', null, [...currentSamPreview.points], null);
                    currentSamPoints = [];
                    currentSamPreview = null;
                    redraw();
                }
            }

            // Undo / Redo Shortcuts
            if (e.ctrlKey || e.metaKey) {
                if (e.key === 'z') {
                    if (currentTool === 'sam' && currentSamPoints.length > 0) {
                        currentSamPoints.pop();
                        redraw();
                    } else if (e.shiftKey) {
                        redo();
                    } else {
                        undo();
                    }
                    e.preventDefault();
                } else if (e.key === 'y') {
                    redo();
                    e.preventDefault();
                } else if (e.key === 'c') {
                    if (selectedShapeIndices.size > 0) {
                        clipboard = Array.from(selectedShapeIndices).map(idx => JSON.parse(JSON.stringify(shapes[idx])));
                        e.preventDefault();
                    }
                } else if (e.key === 'v') {
                    if (clipboard.length > 0) {
                        selectedShapeIndices.clear();
                        const newClipboard = [];
                        clipboard.forEach(shape => {
                            // Offset paste slightly
                            if (shape.type === 'rect') { shape.rect.x += 20; shape.rect.y += 20; }
                            else if (shape.type === 'ellipse') { shape.ellipse.cx += 20; shape.ellipse.cy += 20; }
                            else if (shape.type === 'poly') { shape.points.forEach(p => { p.x += 20; p.y += 20; }); }

                            shape.id = "shape_" + shapeCounter++;
                            shapes.push(shape);
                            selectedShapeIndices.add(shapes.length - 1);
                            newClipboard.push(JSON.parse(JSON.stringify(shape)));
                        });
                        clipboard = newClipboard; // update for subsequent pastes
                        updateShapeList();
                        redraw();
                        saveState();
                        e.preventDefault();
                    }
                }
            }

            if (e.key === 'Delete' || e.key === 'Backspace') {
                if (selectedShapeIndices.size > 0) {
                    const indices = Array.from(selectedShapeIndices).sort((a,b) => b - a); // descending
                    indices.forEach(idx => shapes.splice(idx, 1));
                    selectedShapeIndices.clear();
                    updateShapeList();
                    redraw();
                    saveState();
                    e.preventDefault();
                }
            }
        });

        function finishPolygon() {
            addShape('poly', null, [...currentPath]);
            currentPath = [];
            tempEndPoint = null;
            redraw();
        }

        // --- Shape Management ---
        function addShape(type, rectBounds, pathPoints, ellipseData) {
            const id = `region_${shapeCounter++}`;
            shapes.push({ id, type, rect: rectBounds, points: pathPoints, ellipse: ellipseData });
            updateShapeList();
            saveState();
        }

        function removeShape(index) {
            shapes.splice(index, 1);
            if (selectedShapeIndices.has(index)) {
                selectedShapeIndices.delete(index);
                isDraggingShape = false;
                isDraggingHandle = false;
                selectedHandleIndex = -1;
            }
            const newSel = new Set();
            selectedShapeIndices.forEach(idx => {
                if (idx > index) newSel.add(idx - 1);
                else newSel.add(idx);
            });
            selectedShapeIndices = newSel;
            updateShapeList();
            redraw();
            saveState();
        }

        function updateShapeId(index, newId) {
            shapes[index].id = newId;
            saveState();
        }

        function updateShapeList() {
            shapeList.innerHTML = '';
            shapes.forEach((shape, index) => {
                const li = document.createElement('li');
                li.className = 'shape-item';
                if (selectedShapeIndices.has(index)) {
                    li.style.borderLeft = '3px solid #3b82f6';
                }

                const input = document.createElement('input');
                input.type = 'text';
                input.value = shape.id;
                input.addEventListener('change', (e) => updateShapeId(index, e.target.value));

                const delBtn = document.createElement('button');
                delBtn.innerText = 'Delete';
                delBtn.addEventListener('click', () => removeShape(index));

                li.appendChild(input);
                li.appendChild(delBtn);
                shapeList.appendChild(li);
            });
        }

        // --- Color Helper ---
        function hexToRgb(hex, alpha) {
            let r = 0, g = 0, b = 0;
            // 3 digits
            if (hex.length == 4) {
                r = "0x" + hex[1] + hex[1];
                g = "0x" + hex[2] + hex[2];
                b = "0x" + hex[3] + hex[3];
            // 6 digits
            } else if (hex.length == 7) {
                r = "0x" + hex[1] + hex[2];
                g = "0x" + hex[3] + hex[4];
                b = "0x" + hex[5] + hex[6];
            }
            return `rgba(${+r}, ${+g}, ${+b}, ${alpha})`;
        }

        // --- Drawing Canvas ---
        function redraw() {
            // Clear entire actual canvas
            ctx.setTransform(1, 0, 0, 1, 0, 0);
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            // Apply Zoom/Pan Transform
            ctx.setTransform(transformScale, 0, 0, transformScale, transformPanX, transformPanY);

            // Draw Background Image
            if (bgImage.src) {
                ctx.drawImage(bgImage, 0, 0, imgWidth, imgHeight);
            }

            const baseColorHex = toolColorInput.value || '#3b82f6';
            const baseColorFill = hexToRgb(baseColorHex, 0.3);
            const activeColorFill = hexToRgb(baseColorHex, 0.5);

            // Draw committed shapes
            shapes.forEach((shape, idx) => {
                const isSelected = selectedShapeIndices.has(idx);
                ctx.fillStyle = isSelected ? activeColorFill : baseColorFill;
                ctx.strokeStyle = baseColorHex;
                ctx.lineWidth = isSelected ? 3 / transformScale : 2 / transformScale;

                ctx.beginPath();
                if (shape.type === 'rect') {
                    ctx.rect(shape.rect.x, shape.rect.y, shape.rect.w, shape.rect.h);
                } else if (shape.type === 'ellipse') {
                    ctx.ellipse(shape.ellipse.cx, shape.ellipse.cy, shape.ellipse.rx, shape.ellipse.ry, 0, 0, 2 * Math.PI);
                } else if (shape.type === 'poly') {
                    ctx.moveTo(shape.points[0].x, shape.points[0].y);
                    for (let i = 1; i < shape.points.length; i++) {
                        ctx.lineTo(shape.points[i].x, shape.points[i].y);
                    }
                    ctx.closePath();
                }
                ctx.fill();
                ctx.stroke();

                // Draw Edit Handles if selected
                if (isSelected && selectedShapeIndices.size === 1) {
                    const handleSize = 8 / transformScale;
                    const hs = handleSize / 2;
                    ctx.fillStyle = '#ffffff';
                    ctx.strokeStyle = '#ef4444';
                    ctx.lineWidth = 2 / transformScale;

                    const drawHandle = (hx, hy) => {
                        ctx.beginPath();
                        ctx.rect(hx - hs, hy - hs, handleSize, handleSize);
                        ctx.fill();
                        ctx.stroke();
                    };

                    if (shape.type === 'rect') {
                        const {x, y, w, h} = shape.rect;
                        drawHandle(x, y); // TL
                        drawHandle(x + w, y); // TR
                        drawHandle(x + w, y + h); // BR
                        drawHandle(x, y + h); // BL
                    } else if (shape.type === 'ellipse') {
                        const {cx, cy, rx, ry} = shape.ellipse;
                        drawHandle(cx, cy - ry); // T
                        drawHandle(cx + rx, cy); // R
                        drawHandle(cx, cy + ry); // B
                        drawHandle(cx - rx, cy); // L
                    } else if (shape.type === 'poly') {
                        shape.points.forEach(p => drawHandle(p.x, p.y));
                    }
                }
            });

            // Draw current path/rect in progress
            const markerSize = 6 / transformScale;
            const tempColorHex = '#10b981';
            const tempColorFill = hexToRgb(tempColorHex, 0.3);

            if (currentTool === 'poly' && currentPath.length > 0) {
                ctx.strokeStyle = tempColorHex;
                ctx.lineWidth = 2 / transformScale;
                ctx.beginPath();
                ctx.moveTo(currentPath[0].x, currentPath[0].y);
                for (let i = 1; i < currentPath.length; i++) {
                    ctx.lineTo(currentPath[i].x, currentPath[i].y);
                    ctx.fillStyle = tempColorHex;
                    ctx.fillRect(currentPath[i].x - (markerSize/2), currentPath[i].y - (markerSize/2), markerSize, markerSize);
                }
                if (tempEndPoint) {
                    ctx.lineTo(tempEndPoint.x, tempEndPoint.y);
                }
                ctx.stroke();

                // Draw start point larger
                ctx.fillStyle = '#ef4444';
                ctx.fillRect(currentPath[0].x - (markerSize), currentPath[0].y - (markerSize), markerSize*2, markerSize*2);
            }
            else if (currentTool === 'rect' && isDrawing && startPoint && tempEndPoint) {
                ctx.strokeStyle = tempColorHex;
                ctx.lineWidth = 2 / transformScale;
                ctx.fillStyle = tempColorFill;
                const w = tempEndPoint.x - startPoint.x;
                const h = tempEndPoint.y - startPoint.y;
                ctx.fillRect(startPoint.x, startPoint.y, w, h);
                ctx.strokeRect(startPoint.x, startPoint.y, w, h);
            }
            else if (currentTool === 'ellipse' && isDrawing && startPoint && tempEndPoint) {
                ctx.strokeStyle = tempColorHex;
                ctx.lineWidth = 2 / transformScale;
                ctx.fillStyle = tempColorFill;

                const rx = Math.abs(tempEndPoint.x - startPoint.x) / 2;
                const ry = Math.abs(tempEndPoint.y - startPoint.y) / 2;
                const cx = Math.min(startPoint.x, tempEndPoint.x) + rx;
                const cy = Math.min(startPoint.y, tempEndPoint.y) + ry;

                ctx.beginPath();
                ctx.ellipse(cx, cy, rx, ry, 0, 0, 2 * Math.PI);
                ctx.fill();
                ctx.stroke();
            }

            // Draw SAM Preview and Prompts
            if (currentTool === 'sam') {
                if (currentSamPreview && currentSamPreview.points.length > 0) {
                    ctx.strokeStyle = '#4f46e5';
                    ctx.fillStyle = 'rgba(79, 70, 229, 0.3)';
                    ctx.lineWidth = 2 / transformScale;
                    ctx.beginPath();
                    ctx.moveTo(currentSamPreview.points[0].x, currentSamPreview.points[0].y);
                    for (let i = 1; i < currentSamPreview.points.length; i++) {
                        ctx.lineTo(currentSamPreview.points[i].x, currentSamPreview.points[i].y);
                    }
                    ctx.closePath();
                    ctx.fill();
                    ctx.stroke();
                }

                currentSamPoints.forEach(p => {
                    ctx.fillStyle = p.label === 1 ? '#10b981' : '#ef4444';
                    ctx.beginPath();
                    ctx.arc(p.x, p.y, markerSize, 0, 2 * Math.PI);
                    ctx.fill();

                    // Add outline for visibility
                    ctx.strokeStyle = '#ffffff';
                    ctx.lineWidth = 1 / transformScale;
                    ctx.stroke();
                });
            }

            // Reset transform for UI rendering if any
            ctx.setTransform(1, 0, 0, 1, 0, 0);
        }

        // --- Export ---
        function generateSVG() {
            let svgStr = `<svg viewBox="0 0 ${imgWidth} ${imgHeight}" xmlns="http://www.w3.org/2000/svg">\n`;

            // Generate a background rect that matches the image dimensions exactly.
            // This ensures the viewBox scales correctly, and gives the user an anchor for app.add_svg_background_image()
            svgStr += `    <!-- Background anchor for add_svg_background_image -->\n`;
            svgStr += `    <rect id="background" x="0" y="0" width="${imgWidth}" height="${imgHeight}" fill="transparent" pointer-events="none" />\n\n`;

            shapes.forEach(shape => {
                // Ensure IDs are safe for SVG/XML
                const safeId = shape.id.replace(/[^a-zA-Z0-9_\-]/g, '_');

                if (shape.type === 'rect') {
                    svgStr += `    <rect id="${safeId}" fill="transparent" x="${shape.rect.x.toFixed(1)}" y="${shape.rect.y.toFixed(1)}" width="${shape.rect.w.toFixed(1)}" height="${shape.rect.h.toFixed(1)}" />\n`;
                } else if (shape.type === 'ellipse') {
                    svgStr += `    <ellipse id="${safeId}" fill="transparent" cx="${shape.ellipse.cx.toFixed(1)}" cy="${shape.ellipse.cy.toFixed(1)}" rx="${shape.ellipse.rx.toFixed(1)}" ry="${shape.ellipse.ry.toFixed(1)}" />\n`;
                } else if (shape.type === 'poly') {
                    let d = `M${shape.points[0].x.toFixed(1)},${shape.points[0].y.toFixed(1)}`;
                    for (let i = 1; i < shape.points.length; i++) {
                        d += ` L${shape.points[i].x.toFixed(1)},${shape.points[i].y.toFixed(1)}`;
                    }
                    d += ' Z';
                    svgStr += `    <path id="${safeId}" fill="transparent" d="${d}" />\n`;
                }
            });

            svgStr += `</svg>`;
            return svgStr;
        }

        exportBtn.addEventListener('click', () => {
            const svgContent = generateSVG();
            svgOutputArea.value = svgContent;

            // Check pyodide availability each time modal opens since it might have loaded
            const pyodideInstance = getPyodideInstance();
            if (pyodideInstance && pyodideInstance.FS) {
                saveIdbfsBtn.style.display = 'inline-block';
            } else {
                saveIdbfsBtn.style.display = 'none';
            }

            exportModal.style.display = 'flex';
        });

        closeModalBtn.addEventListener('click', () => {
            exportModal.style.display = 'none';
        });

        downloadSvgBtn.addEventListener('click', () => {
            const svgContent = svgOutputArea.value;
            const blob = new Blob([svgContent], { type: 'image/svg+xml' });
            const url = URL.createObjectURL(blob);

            const a = document.createElement('a');
            a.href = url;
            a.download = saveFilenameInput.value || 'sivo_template.svg';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
        });

        // --- Save/Load Project State ---
        function serializeProject() {
            return JSON.stringify({
                shapes: shapes,
                imgWidth: imgWidth,
                imgHeight: imgHeight,
                bgImageSrc: bgImage.src,
                shapeCounter: shapeCounter
            });
        }

        function loadProjectState(data) {
            try {
                const state = JSON.parse(data);
                shapes = state.shapes || [];
                imgWidth = state.imgWidth || 0;
                imgHeight = state.imgHeight || 0;
                shapeCounter = state.shapeCounter || 1;

                if (state.bgImageSrc) {
                    handleImageLoad(state.bgImageSrc, true);
                } else {
                    updateShapeList();
                    redraw();
                }
                saveState();
            } catch (e) {
                console.error("Failed to load project state", e);
                alert("Failed to load project file. Invalid format.");
            }
        }

        saveProjectBtn.addEventListener('click', () => {
            const data = serializeProject();
            const pyodideInst = getPyodideInstance();
            if (pyodideInst && pyodideInst.FS) {
                const filename = prompt("Enter project filename to save to Pyodide FS:", "sivo_project.json");
                if (!filename) return;
                try {
                    const mountDir = "/sivo_workspace";
                    pyodideInst.FS.writeFile(`${mountDir}/${filename}`, data);
                    pyodideInst.FS.syncfs(false, function(err) {
                        if (err) alert("Sync error: " + err);
                        else {
                            alert("Saved to Pyodide Virtual File System: " + filename);
                            if (window.parent && window.parent.updateFileList) {
                                window.parent.updateFileList();
                            }
                        }
                    });
                } catch (err) {
                    alert("Error saving: " + err);
                }
            } else {
                // Standard browser download
                const blob = new Blob([data], { type: 'application/json' });
                const url = URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = 'sivo_project.json';
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
                URL.revokeObjectURL(url);
            }
        });

        loadProjectBtn.addEventListener('click', () => {
            const pyodideInst = getPyodideInstance();
            if (pyodideInst && pyodideInst.FS) {
                const mountDir = "/sivo_workspace";
                try {
                    const files = pyodideInst.FS.readdir(mountDir).filter(f => f !== '.' && f !== '..');
                    if (files.length === 0) {
                        alert("No files found in Pyodide FS.");
                        return;
                    }

                    const loadModal = document.getElementById('load-modal');
                    const fileListEl = document.getElementById('load-file-list');
                    fileListEl.innerHTML = '';

                    files.forEach(f => {
                        const li = document.createElement('li');
                        li.style.cursor = 'pointer';
                        li.style.padding = '8px';
                        li.style.borderBottom = '1px solid #e5e7eb';
                        li.style.wordBreak = 'break-all';
                        li.innerText = `📄 ${f}`;
                        li.addEventListener('click', () => {
                            try {
                                const data = pyodideInst.FS.readFile(`${mountDir}/${f}`, { encoding: 'utf8' });
                                loadProjectState(data);
                                loadModal.style.display = 'none';
                            } catch (err) {
                                alert(`Error loading ${f}: ` + err);
                            }
                        });
                        li.addEventListener('mouseenter', () => {
                            li.style.backgroundColor = '#f3f4f6';
                        });
                        li.addEventListener('mouseleave', () => {
                            li.style.backgroundColor = 'transparent';
                        });
                        fileListEl.appendChild(li);
                    });

                    loadModal.style.display = 'flex';
                } catch (err) {
                    alert("Error reading directory: " + err);
                }
            } else {
                loadProjectFile.click();
            }
        });

        const loadModal = document.getElementById('load-modal');
        const closeLoadModalBtn = document.getElementById('close-load-modal');
        if (closeLoadModalBtn) {
            closeLoadModalBtn.addEventListener('click', () => {
                loadModal.style.display = 'none';
            });
        }

        loadProjectFile.addEventListener('change', (e) => {
            const file = e.target.files[0];
            if (!file) return;
            const reader = new FileReader();
            reader.onload = (evt) => {
                loadProjectState(evt.target.result);
            };
            reader.readAsText(file);
            loadProjectFile.value = ''; // Reset
        });


        // Detect Pyodide in window or parent to enable IDBFS saving
        function getPyodideInstance() {
            if (window.pyodide) return window.pyodide;
            if (window.parent && window.parent.pyodide) return window.parent.pyodide;
            return null;
        }

        saveIdbfsBtn.addEventListener('click', async () => {
            const pyodideInstance = getPyodideInstance();
            if (!pyodideInstance || !pyodideInstance.FS) return;

            const svgContent = svgOutputArea.value;
            const filename = saveFilenameInput.value || 'sivo_template.svg';
            const mountDir = "/sivo_workspace";

            try {
                // Write to the virtual file system
                pyodideInstance.FS.writeFile(`${mountDir}/${filename}`, svgContent);

                // Sync the virtual file system back to IndexedDB
                pyodideInstance.FS.syncfs(false, function (err) {
                    if (err) {
                        console.error('Error syncing IDBFS:', err);
                        alert('Failed to sync to IndexedDB: ' + err);
                    } else {
                        const originalText = saveIdbfsBtn.innerText;
                        saveIdbfsBtn.innerText = 'Saved!';
                        saveIdbfsBtn.style.backgroundColor = '#059669';
                        if (window.parent && window.parent.updateFileList) {
                            window.parent.updateFileList();
                        }
                        setTimeout(() => {
                            saveIdbfsBtn.innerText = originalText;
                            saveIdbfsBtn.style.backgroundColor = '#10b981';
                        }, 2000);
                    }
                });
            } catch (err) {
                console.error('Error writing to Pyodide FS:', err);
                alert('Failed to write to virtual file system: ' + err);
            }
        });
