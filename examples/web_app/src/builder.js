
// Safe JSON Parsing fallback
function safeJSONParse(str, fallback = {}) {
    try {
        return JSON.parse(str);
    } catch (e) {
        showToast("Error parsing JSON configuration.", "error");
        return fallback;
    }
}

// Builder State Management
let builderState = {
    history: [],
    historyIndex: -1,
    currentConfig: {
        template: null,
        customSvg: '',
        bgImage: '',
        highlightElements: false,
        elements: {}, // e.g. { 'state-ny': { fill: '#3b82f6', hover: '#60a5fa', tooltip: '...', ... } }
        activeElementId: null
    },
    activeElement: null
};

// --- DOM Elements ---

// Integrations
const propIntegElementId = document.getElementById('prop-integ-element-id');
const propIntegType = document.getElementById('prop-integ-type');
const propIntegUrl = document.getElementById('prop-integ-url');
const btnApplyIntegrations = document.getElementById('btn-apply-integrations');

// A11y & Media
const propA11yElementId = document.getElementById('prop-a11y-element-id');
const propA11yAriaLabel = document.getElementById('prop-a11y-aria-label');
const propA11yTabindex = document.getElementById('prop-a11y-tabindex');
const propA11yMarker = document.getElementById('prop-a11y-marker');
const propA11yVideo = document.getElementById('prop-a11y-video');
const propA11yAudio = document.getElementById('prop-a11y-audio');
const propA11yMarkdown = document.getElementById('prop-a11y-markdown');
const propA11yGallery = document.getElementById('prop-a11y-gallery');
const propA11yEmbedSvg = document.getElementById('prop-a11y-embed-svg');
const propA11yLottie = document.getElementById('prop-a11y-lottie');
const propA11yMorph = document.getElementById('prop-a11y-morph');
const propA11yClip = document.getElementById('prop-a11y-clip');
const propA11yTransform = document.getElementById('prop-a11y-transform');
const propA11yExplode = document.getElementById('prop-a11y-explode');
const propA11yConfetti = document.getElementById('prop-a11y-confetti');
const propA11yLoading = document.getElementById('prop-a11y-loading');
const propA11yZoomTo = document.getElementById('prop-a11y-zoom-to');
const btnApplyA11yMedia = document.getElementById('btn-apply-a11y-media');

// Global Styles
const propGlobalTheme = document.getElementById('prop-global-theme');
const propGlobalAmbient = document.getElementById('prop-global-ambient');
const propGlobalPanelPos = document.getElementById('prop-global-panel-pos');
const propGlobalBgImg = document.getElementById('prop-global-bg-img');
const propGlobalSvgBgImg = document.getElementById('prop-global-svg-bg-img');
const propGlobalBorderImg = document.getElementById('prop-global-border-img');
const propGlobalCss = document.getElementById('prop-global-css');
const propGlobalJs = document.getElementById('prop-global-js');
const btnApplyGlobalStyle = document.getElementById('btn-apply-global-style');

// Buttons & Inputs
const btnNewProject = document.getElementById('btn-new-project');
const btnImportJsonLocal = document.getElementById('btn-import-json-local');
const btnImportJsonIdbfs = document.getElementById('btn-import-json-idbfs');
const jsonUploadLocal = document.getElementById('json-upload-local');

// Canvas Settings Elements
const propCustomSvg = document.getElementById('prop-custom-svg');
const propBgImage = document.getElementById('prop-bg-image');
const propHighlightElements = document.getElementById('prop-highlight-elements');
const btnApplyCanvasSettings = document.getElementById('btn-apply-canvas-settings');

// Modal Elements
const idbfsModal = document.getElementById('idbfs-modal');
const idbfsModalTitle = document.getElementById('idbfs-modal-title');
const idbfsFileList = document.getElementById('idbfs-file-list');
const btnCloseIdbfsModal = document.getElementById('btn-close-idbfs-modal');

const btnUndo = document.getElementById('btn-undo');
const btnRedo = document.getElementById('btn-redo');
const btnAnnotateInspect = document.getElementById('btn-annotate-inspect');
const templateBtns = document.querySelectorAll('.template-btn');

// Preview Pane
const previewFrame = document.getElementById('builder-preview-frame');
const previewOverlay = document.getElementById('builder-preview-overlay');
const btnPreviewRefresh = document.getElementById('btn-preview-refresh');
const btnPreviewGenerate = document.getElementById('btn-preview-generate');
const previewModeBtns = document.querySelectorAll('.preview-mode-btn');
const previewContainer = document.getElementById('preview-container');

// Builder Tabs
const builderTabBtns = document.querySelectorAll('.builder-tab-btn');
const builderTabContents = document.querySelectorAll('.builder-tab-content');

// Properties
const propElementId = document.getElementById('prop-element-id');
const propFillColor = document.getElementById('prop-fill-color');
const propFillColorText = document.getElementById('prop-fill-color-text');
const propHoverColor = document.getElementById('prop-hover-color');
const propHoverColorText = document.getElementById('prop-hover-color-text');
const propTooltip = document.getElementById('prop-tooltip');
const propTooltipZIndex = document.getElementById('prop-tooltip-zindex');
const propHoverEffects = document.getElementById('prop-hover-effects');
const propClickCallback = document.getElementById('prop-click-callback');
const propHoverCallback = document.getElementById('prop-hover-callback');
const btnApplyProps = document.getElementById('btn-apply-props');

// Phase 3 Properties & Elements
const btnSelectDataFile = document.getElementById('btn-select-data-file');
const propDataFile = document.getElementById('prop-data-file');
const propDataIdCol = document.getElementById('prop-data-id-col');
const propDataValueCol = document.getElementById('prop-data-value-col');
const propDataMapType = document.getElementById('prop-data-map-type');
const propDataBaseCol = document.getElementById('prop-data-base-col');
const propDataAlphaCol = document.getElementById('prop-data-alpha-col');
const propDataXCol = document.getElementById('prop-data-x-col');
const propDataYCol = document.getElementById('prop-data-y-col');
const propDataOriginCol = document.getElementById('prop-data-origin-col');
const propDataDestCol = document.getElementById('prop-data-dest-col');

const dataColsIdContainer = document.getElementById('data-cols-id-container');
const dataColsValueContainer = document.getElementById('data-cols-value-container');
const dataColsBivariate = document.getElementById('data-cols-bivariate');
const dataColsHexbin = document.getElementById('data-cols-hexbin');
const dataColsFlow = document.getElementById('data-cols-flow');

const dashboardBlocksContainer = document.getElementById('dashboard-blocks-container');
const btnAddDashboardBlock = document.getElementById('btn-add-dashboard-block');
const propGraphElementId = document.getElementById('prop-graph-element-id');
const propGraphType = document.getElementById('prop-graph-type');
const propGraphTitle = document.getElementById('prop-graph-title');
const btnApplyGraphProps = document.getElementById('btn-apply-graph-props');
const btnValidateProject = document.getElementById("btn-validate-project");
const validationResults = document.getElementById("validation-results");

// Dynamic Property Containers
const propFootnoteContainer = document.getElementById('prop-footnote-container');
const propToggleImageContainer = document.getElementById('prop-toggle-image-container');

// Phase 4 Live Data & Fetch Elements
const propLiveWsUrl = document.getElementById('prop-live-ws-url');
const propLiveWsTopic = document.getElementById('prop-live-ws-topic');
const propLiveApiUrl = document.getElementById('prop-live-api-url');
const propLiveApiInterval = document.getElementById('prop-live-api-interval');
const propLiveApiPath = document.getElementById('prop-live-api-path');

const propTimelineCsvFile = document.getElementById('prop-timeline-csv-file');
const propTimelineTimeCol = document.getElementById('prop-timeline-time-col');
const propTimelineMapType = document.getElementById('prop-timeline-map-type');

const btnApplyLiveData = document.getElementById('btn-apply-live-data');

const propFetchElementId = document.getElementById('prop-fetch-element-id');
const propFetchUrl = document.getElementById('prop-fetch-url');
const propFetchDataPath = document.getElementById('prop-fetch-data-path');
const btnApplyFetchProps = document.getElementById('btn-apply-fetch-props');



// Phase 5 Elements
const propPresentationAutoplay = document.getElementById('prop-presentation-autoplay');
const propPresentationProgress = document.getElementById('prop-presentation-progress');
const propPresentationLaser = document.getElementById('prop-presentation-laser');
const propPresentationNotes = document.getElementById('prop-presentation-notes');
const btnApplyTimeline = document.getElementById('btn-apply-timeline');

const timelineStepsContainer = document.getElementById('timeline-steps-container');
const btnAddTimelineStep = document.getElementById('btn-add-timeline-step');


const propOverlayElementId = document.getElementById('prop-overlay-element-id');
const propOverlayFillZone = document.getElementById('prop-overlay-fill-zone');
const propOverlayClipHtml = document.getElementById('prop-overlay-clip-html');
const propOverlayConnFrom = document.getElementById('prop-overlay-conn-from');
const propOverlayConnTo = document.getElementById('prop-overlay-conn-to');
const propOverlayShapeType = document.getElementById('prop-overlay-shape-type');
const propOverlayImageUrl = document.getElementById('prop-overlay-image-url');
const propOverlayScratchoff = document.getElementById('prop-overlay-scratchoff');
const btnApplyOverlays = document.getElementById('btn-apply-overlays');

const propCtrlZoomUi = document.getElementById('prop-ctrl-zoom-ui');
const propCtrlMinimap = document.getElementById('prop-ctrl-minimap');
const propCtrlZoomClick = document.getElementById('prop-ctrl-zoom-click');
const propCtrlDrawing = document.getElementById('prop-ctrl-drawing');
const propCtrlBrush = document.getElementById('prop-ctrl-brush');
const propCtrlSearch = document.getElementById('prop-ctrl-search');
const propCtrlLayerToggle = document.getElementById('prop-ctrl-layer-toggle');
const propCtrlPanelDismiss = document.getElementById('prop-ctrl-panel-dismiss');
const propCtrlUrlNavId = document.getElementById('prop-ctrl-url-nav-id');
const propCtrlUrlNavUrl = document.getElementById('prop-ctrl-url-nav-url');
const btnApplyControls = document.getElementById('btn-apply-controls');

// Phase 6 Elements
const propGeocodeEnable = document.getElementById('prop-geocode-enable');
const propGeocodeProvider = document.getElementById('prop-geocode-provider');
const propGeocodeApiKey = document.getElementById('prop-geocode-api-key');
const btnApplyGeocoding = document.getElementById('btn-apply-geocoding');

const propMvElementId = document.getElementById('prop-mv-element-id');
const propMvViewId = document.getElementById('prop-mv-view-id');
const btnApplyMultiview = document.getElementById('btn-apply-multiview');

const propExportWatermark = document.getElementById('prop-export-watermark');
const propExportAttribution = document.getElementById('prop-export-attribution');
const propExportE2e = document.getElementById('prop-export-e2e');
const btnApplyExport = document.getElementById('btn-apply-export');

// --- State Management (Undo/Redo) ---
function saveState() {
    // If we're not at the end of history, truncate the future
    if (builderState.historyIndex < builderState.history.length - 1) {
        builderState.history = builderState.history.slice(0, builderState.historyIndex + 1);
    }

    builderState.history.push(JSON.parse(JSON.stringify(builderState.currentConfig)));

    // Cap history length to avoid memory bloat
    if (builderState.history.length > 50) {
        builderState.history.shift();
    } else {
        builderState.historyIndex++;
    }

    updateHistoryButtons();
}

function updateHistoryButtons() {
    btnUndo.disabled = builderState.historyIndex <= 0;
    btnRedo.disabled = builderState.historyIndex >= builderState.history.length - 1;
}

btnUndo.addEventListener('click', () => {
    if (builderState.historyIndex > 0) {
        builderState.historyIndex--;
        builderState.currentConfig = JSON.parse(JSON.stringify(builderState.history[builderState.historyIndex]));
        updateHistoryButtons();
        refreshPropertiesPanel();
        generatePreview();
    }
});

document.addEventListener('keydown', (e) => {
    // Only capture if we are visible/active tab
    const viewBuilder = document.getElementById('view-builder');
    if (!viewBuilder || !viewBuilder.classList.contains('active')) return;

    if ((e.ctrlKey || e.metaKey) && !e.shiftKey && e.key.toLowerCase() === 'z') {
        e.preventDefault();
        btnUndo.click();
    } else if ((e.ctrlKey || e.metaKey) && (e.key.toLowerCase() === 'y' || (e.shiftKey && e.key.toLowerCase() === 'z'))) {
        e.preventDefault();
        btnRedo.click();
    }
});

btnRedo.addEventListener('click', () => {
    if (builderState.historyIndex < builderState.history.length - 1) {
        builderState.historyIndex++;
        builderState.currentConfig = JSON.parse(JSON.stringify(builderState.history[builderState.historyIndex]));
        updateHistoryButtons();
        refreshPropertiesPanel();
        generatePreview();
    }
});

// --- Template Selection ---
templateBtns.forEach(btn => {
    btn.addEventListener('click', async (e) => {
        const templatePath = e.target.getAttribute('data-template');
        builderState.currentConfig.template = templatePath;
        builderState.currentConfig.elements = {}; // Reset elements
        saveState();
        previewOverlay.classList.add('hidden');
        await generatePreview();
    });
});

// --- JSON Import/Export ---
btnImportJsonLocal.addEventListener('click', () => jsonUploadLocal.click());
jsonUploadLocal.addEventListener('change', (e) => {
    const file = e.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (evt) => {
        try {
            const config = JSON.parse(evt.target.result);
            builderState.currentConfig = config;

            // Ensure missing defaults are populated
            if (!builderState.currentConfig.elements) builderState.currentConfig.elements = {};
            if (!builderState.currentConfig.dashboardBlocks) builderState.currentConfig.dashboardBlocks = [];

            // Sync Canvas Settings UI
            propCustomSvg.value = config.customSvg || '';
            propBgImage.value = config.bgImage || '';
            propHighlightElements.checked = !!config.highlightElements;
            propDataFile.value = config.dataFile || "";

            saveState();
            previewOverlay.classList.add('hidden');
            generatePreview();
        } catch (err) {
            showToast("Invalid JSON configuration file.");
        }
    };
    reader.readAsText(file);
    // Reset file input so the same file can be loaded again if needed
    e.target.value = '';
});

btnImportJsonIdbfs.addEventListener('click', () => {
    showIdbfsModal("Select JSON Config", ".json", (filename) => {
        const mountDir = "/sivo_workspace";
        try {
            const data = window.pyodide.FS.readFile(`${mountDir}/${filename}`, { encoding: 'utf8' });
            const config = JSON.parse(data);
            builderState.currentConfig = config;

            // Ensure missing defaults are populated
            if (!builderState.currentConfig.elements) builderState.currentConfig.elements = {};
            if (!builderState.currentConfig.dashboardBlocks) builderState.currentConfig.dashboardBlocks = [];

            // Sync Canvas Settings UI
            propCustomSvg.value = config.customSvg || '';
            propBgImage.value = config.bgImage || '';
            propHighlightElements.checked = !!config.highlightElements;
            propDataFile.value = config.dataFile || "";

            saveState();
            previewOverlay.classList.add('hidden');
            generatePreview();
        } catch(err) {
            showToast(err, "error")
            showToast("Failed to load JSON: " + err.message);
        }
    });
});


// --- Canvas Settings ---
btnApplyCanvasSettings.addEventListener('click', async () => {
    builderState.currentConfig.customSvg = propCustomSvg.value.trim();
    builderState.currentConfig.bgImage = propBgImage.value.trim();
    builderState.currentConfig.highlightElements = propHighlightElements.checked;

    // Memory Profiling Warning: Large files check
    if (builderState.currentConfig.customSvg && !builderState.currentConfig.customSvg.startsWith('<svg') && !builderState.currentConfig.customSvg.startsWith('http')) {
        try {
            const stat = window.pyodide.FS.stat(builderState.currentConfig.customSvg);
            if (stat.size > 5 * 1024 * 1024) { // 5MB
                showToast("Warning: The selected SVG file is very large (" + (stat.size / 1024 / 1024).toFixed(2) + " MB). This might cause browser memory issues or crashes during generation. We recommend optimizing the SVG.");
            }
        } catch(e) {
             // File might not exist yet or is URL, ignore
        }
    }

    // Clear template if using custom SVG
    if (builderState.currentConfig.customSvg) {
        builderState.currentConfig.template = null;
    }

    saveState();
    previewOverlay.classList.add('hidden');
    generatePreview();
});

// --- IDBFS Modal Logic ---
let idbfsCallback = null;

function showIdbfsModal(title, extension, callback) {
    if (!window.pyodide || !window.pyodide.FS) {
        showToast("Pyodide File System is not ready yet.");
        return;
    }
    const mountDir = "/sivo_workspace";
    try {
        let files = window.pyodide.FS.readdir(mountDir).filter(f => f !== '.' && f !== '..');
        if (extension) {
            files = files.filter(f => f.endsWith(extension));
        }

        idbfsModalTitle.innerText = title;
        idbfsFileList.innerHTML = '';

        if (files.length === 0) {
            idbfsFileList.innerHTML = '<li class="text-sm text-slate-500 italic p-2">No files found.</li>';
        } else {
            files.forEach(f => {
                const li = document.createElement('li');
                const btn = document.createElement('button');
                btn.className = 'w-full text-left px-3 py-2 text-sm hover:bg-slate-100 rounded transition-colors';
                btn.innerText = f;
                btn.onclick = () => {
                    closeIdbfsModal();
                    if (callback) callback(f);
                };
                li.appendChild(btn);
                idbfsFileList.appendChild(li);
            });
        }

        idbfsModal.classList.remove('hidden');
    } catch (err) {
        showToast("Error reading IDBFS:", err, "error")
        showToast("Error reading IDBFS: " + err.message);
    }
}

function closeIdbfsModal() {
    idbfsModal.classList.add('hidden');
    idbfsCallback = null;
}

btnCloseIdbfsModal.addEventListener('click', closeIdbfsModal);



// --- Preview Modes ---
previewModeBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
        const mode = e.target.getAttribute('data-mode');

        // Update active class
        previewModeBtns.forEach(b => {
            b.classList.remove('bg-white', 'shadow-sm', 'border-slate-200');
            b.classList.add('hover:bg-slate-200', 'text-slate-600', 'border-transparent');
        });
        e.target.classList.remove('hover:bg-slate-200', 'text-slate-600', 'border-transparent');
        e.target.classList.add('bg-white', 'shadow-sm', 'border-slate-200');

        // Apply dimensions
        previewContainer.className = 'bg-white shadow-md transition-all duration-300 flex items-center justify-center relative';
        if (mode === 'desktop') {
            previewContainer.style.width = '100%';
            previewContainer.style.height = '100%';
        } else if (mode === 'tablet') {
            previewContainer.style.width = '768px';
            previewContainer.style.height = '1024px';
        } else if (mode === 'mobile') {
            previewContainer.style.width = '375px';
            previewContainer.style.height = '812px';
        } else if (mode === 'fullscreen') {
            // Rough approximation of full screen overlay within pane
            previewContainer.style.width = '100%';
            previewContainer.style.height = '100%';
            previewContainer.classList.add('fixed', 'inset-0', 'z-50');
        }
    });
});

// --- Selection via Click in Preview ---
window.addEventListener('message', (event) => {
    if (event.data && event.data.type === 'sivo_element_clicked') {
        const id = event.data.id;

        // Auto-enable highlighting to show the selection visually if not already enabled
        if (!builderState.currentConfig.highlightElements) {
            builderState.currentConfig.highlightElements = true;
            propHighlightElements.checked = true;
        }

        // Set the active element and refresh
        builderState.currentConfig.activeElementId = id;
        propElementId.value = id;
        propFetchElementId.value = id;

        refreshPropertiesPanel();
        generatePreview();
    }
});


// --- Property Inspector Logic ---
// Sync Color inputs
propFillColor.addEventListener('input', (e) => propFillColorText.value = e.target.value);
propFillColorText.addEventListener('input', (e) => propFillColor.value = e.target.value);
propHoverColor.addEventListener('input', (e) => propHoverColorText.value = e.target.value);
propHoverColorText.addEventListener('input', (e) => propHoverColor.value = e.target.value);

// Show/Hide dynamic fields based on selection
propClickCallback.addEventListener('change', (e) => {
    const val = e.target.value;
    propFootnoteContainer.classList.add('hidden');
    propToggleImageContainer.classList.add('hidden');

    if (val === 'footnote') propFootnoteContainer.classList.remove('hidden');
    if (val === 'toggle_image') propToggleImageContainer.classList.remove('hidden');
});

function refreshPropertiesPanel() {

    // Sync globals
    propCustomSvg.value = builderState.currentConfig.customSvg || "";
    propBgImage.value = builderState.currentConfig.bgImage || "";
    propHighlightElements.checked = !!builderState.currentConfig.highlightElements;

    propDataFile.value = builderState.currentConfig.dataFile || "";
    propDataIdCol.value = builderState.currentConfig.dataIdCol || "id";
    propDataValueCol.value = builderState.currentConfig.dataValueCol || "value";

    propDataMapType.value = builderState.currentConfig.dataMapType || "choropleth";
    propDataBaseCol.value = builderState.currentConfig.dataBaseCol || "value1";
    propDataAlphaCol.value = builderState.currentConfig.dataAlphaCol || "value2";
    propDataXCol.value = builderState.currentConfig.dataXCol || "x";
    propDataYCol.value = builderState.currentConfig.dataYCol || "y";
    propDataOriginCol.value = builderState.currentConfig.dataOriginCol || "origin";
    propDataDestCol.value = builderState.currentConfig.dataDestCol || "destination";

    propLiveWsUrl.value = builderState.currentConfig.liveWsUrl || "";
    propLiveWsTopic.value = builderState.currentConfig.liveWsTopic || "";
    propLiveApiUrl.value = builderState.currentConfig.liveApiUrl || "";
    propLiveApiInterval.value = builderState.currentConfig.liveApiInterval || "";

    propLiveApiPath.value = builderState.currentConfig.liveApiPath || "";

    propTimelineCsvFile.value = builderState.currentConfig.timelineCsvFile || "";
    propTimelineTimeCol.value = builderState.currentConfig.timelineTimeCol || "";
    propTimelineMapType.value = builderState.currentConfig.timelineMapType || "choropleth";

    // Phase 5 Globals
    propPresentationAutoplay.value = builderState.currentConfig.presentationAutoplay || "";
    propPresentationProgress.checked = !!builderState.currentConfig.presentationProgress;
    propPresentationLaser.checked = !!builderState.currentConfig.presentationLaser;
    propPresentationNotes.value = builderState.currentConfig.presentationNotes || "";

    propCtrlZoomUi.checked = builderState.currentConfig.ctrlZoomUi !== false;
    propCtrlMinimap.checked = !!builderState.currentConfig.ctrlMinimap;
    propCtrlZoomClick.checked = builderState.currentConfig.ctrlZoomClick !== false;
    propCtrlDrawing.checked = !!builderState.currentConfig.ctrlDrawing;
    propCtrlBrush.checked = !!builderState.currentConfig.ctrlBrush;
    propCtrlSearch.checked = !!builderState.currentConfig.ctrlSearch;
    propCtrlLayerToggle.value = builderState.currentConfig.ctrlLayerToggle || "";
    propCtrlPanelDismiss.value = builderState.currentConfig.ctrlPanelDismiss || "";
    propCtrlUrlNavId.value = builderState.currentConfig.ctrlUrlNavId || "";
    propCtrlUrlNavUrl.value = builderState.currentConfig.ctrlUrlNavUrl || "";

    // Phase 6 Globals
    propGeocodeEnable.checked = !!builderState.currentConfig.geocodeEnable;
    propGeocodeProvider.value = builderState.currentConfig.geocodeProvider || "nominatim";
    propGeocodeApiKey.value = builderState.currentConfig.geocodeApiKey || "";

    propExportWatermark.value = builderState.currentConfig.exportWatermark || "";
    propExportAttribution.value = builderState.currentConfig.exportAttribution || "";
    propExportE2e.checked = !!builderState.currentConfig.exportE2e;


    updateDataMapUI();

    renderDashboardBlocks();
    renderTimelineSteps();

    const id = propElementId.value;
    propGraphElementId.value = id;

    if (!id || !builderState.currentConfig.elements[id]) {

        propFetchUrl.value = "";
        propFetchDataPath.value = "";

        // Phase 5 Reset
        propOverlayElementId.value = "";
        propA11yElementId.value = "";

        if (propA11yAriaLabel) propA11yAriaLabel.value = "";
        if (propA11yTabindex) propA11yTabindex.value = "";
        if (propA11yMarker) propA11yMarker.value = "";
        if (propA11yVideo) propA11yVideo.value = "";
        if (propA11yAudio) propA11yAudio.value = "";
        if (propA11yMarkdown) propA11yMarkdown.value = "";
        if (propA11yGallery) propA11yGallery.value = "";
        if (propA11yEmbedSvg) propA11yEmbedSvg.value = "";
        if (propA11yLottie) propA11yLottie.value = "";
        if (propA11yMorph) propA11yMorph.value = "";
        if (propA11yClip) propA11yClip.value = "";
        if (propA11yTransform) propA11yTransform.value = "";
        if (propA11yExplode) propA11yExplode.checked = false;
        if (propA11yConfetti) propA11yConfetti.checked = false;
        if (propA11yLoading) propA11yLoading.checked = false;
        if (propA11yZoomTo) propA11yZoomTo.value = "";
        propOverlayFillZone.value = "";
        propOverlayClipHtml.value = "";
        propOverlayShapeType.value = "none";
        propOverlayImageUrl.value = "";
        propOverlayScratchoff.checked = false;

        // Phase 6 Reset
        propMvElementId.value = "";
        propMvViewId.value = "";

        // Reset defaults
        propFillColor.value = '#3b82f6';
        propFillColorText.value = '#3b82f6';
        propHoverColor.value = '#60a5fa';
        propHoverColorText.value = '#60a5fa';
        propTooltip.value = '';
        propTooltipZIndex.checked = false;
        propHoverEffects.checked = true;
        propClickCallback.value = 'none';
        propHoverCallback.value = 'none';

        propGraphType.value = 'none';
        propGraphTitle.value = '';

        propFootnoteContainer.classList.add('hidden');
        propToggleImageContainer.classList.add('hidden');
        return;
    }

    const elConfig = builderState.currentConfig.elements[id];
    propFillColor.value = elConfig.fill || '#3b82f6';
    propFillColorText.value = elConfig.fill || '#3b82f6';
    propHoverColor.value = elConfig.hover || '#60a5fa';
    propHoverColorText.value = elConfig.hover || '#60a5fa';
    propTooltip.value = elConfig.tooltip || '';
    propTooltipZIndex.checked = !!elConfig.enforceZIndex;
    propHoverEffects.checked = elConfig.selectiveHover !== false;

    propClickCallback.value = elConfig.clickCallback || 'none';
    propHoverCallback.value = elConfig.hoverCallback || 'none';

    propGraphType.value = elConfig.graphType || 'none';
    propGraphTitle.value = elConfig.graphTitle || '';


    propFetchUrl.value = elConfig.fetchUrl || '';
    propFetchDataPath.value = elConfig.fetchDataPath || '';

    // Phase 5 Element Config
    propOverlayElementId.value = id;
    propA11yElementId.value = id;

    // A11y fields
    if (propA11yAriaLabel) propA11yAriaLabel.value = elConfig.ariaLabel || '';
    if (propA11yTabindex) propA11yTabindex.value = elConfig.tabindex !== undefined ? elConfig.tabindex : '';
    if (propA11yMarker) propA11yMarker.value = elConfig.marker || '';
    if (propA11yVideo) propA11yVideo.value = elConfig.video || '';
    if (propA11yAudio) propA11yAudio.value = elConfig.audio || '';
    if (propA11yMarkdown) propA11yMarkdown.value = elConfig.markdown || '';
    if (propA11yGallery) propA11yGallery.value = elConfig.gallery ? elConfig.gallery.join(', ') : '';
    if (propA11yEmbedSvg) propA11yEmbedSvg.value = elConfig.embed_svg || '';
    if (propA11yLottie) propA11yLottie.value = elConfig.lottie || '';
    if (propA11yMorph) propA11yMorph.value = elConfig.morph_to_path || '';
    if (propA11yClip) propA11yClip.value = elConfig.clip_image_url || '';
    if (propA11yTransform) propA11yTransform.value = elConfig.transform || '';
    if (propA11yExplode) propA11yExplode.checked = !!elConfig.explode;
    if (propA11yConfetti) propA11yConfetti.checked = !!elConfig.confetti;
    if (propA11yLoading) propA11yLoading.checked = !!elConfig.loading;
    if (propA11yZoomTo) propA11yZoomTo.value = elConfig.zoom_to || '';
    propOverlayFillZone.value = elConfig.fillZone || '';
    propOverlayClipHtml.value = elConfig.clipHtml || '';
    propOverlayShapeType.value = elConfig.shapeType || 'none';
    propOverlayImageUrl.value = elConfig.absoluteImageUrl || '';
    propOverlayScratchoff.checked = !!elConfig.scratchoff;

    // Phase 6 Element Config
    propMvElementId.value = id;
    propMvViewId.value = elConfig.drillThroughViewId || '';


    // Refresh dynamic fields
    propClickCallback.dispatchEvent(new Event('change'));
    if (elConfig.clickCallback === 'footnote') document.getElementById('prop-footnote-text').value = elConfig.footnoteText || '';
    if (elConfig.clickCallback === 'toggle_image') document.getElementById('prop-toggle-image-urls').value = elConfig.toggleImageUrls || '';
}

propElementId.addEventListener('input', (e) => {
    builderState.currentConfig.activeElementId = e.target.value.trim() || null;
    refreshPropertiesPanel();

    // Only refresh preview if it's currently generated to avoid spam
    if (previewFrame.srcdoc) {
         generatePreview();
    }
});

btnApplyProps.addEventListener('click', () => {
    const id = propElementId.value.trim();
    if (!id) return showToast("Please enter an Element ID first.");

    if (!builderState.currentConfig.elements[id]) {
        builderState.currentConfig.elements[id] = {};
    }

    const el = builderState.currentConfig.elements[id];
    el.fill = propFillColor.value;
    el.hover = propHoverColor.value;
    el.tooltip = propTooltip.value;
    el.enforceZIndex = propTooltipZIndex.checked;
    el.selectiveHover = propHoverEffects.checked;
    el.clickCallback = propClickCallback.value;
    el.hoverCallback = propHoverCallback.value;

    if (el.clickCallback === 'footnote') el.footnoteText = document.getElementById('prop-footnote-text').value;
    if (el.clickCallback === 'toggle_image') el.toggleImageUrls = document.getElementById('prop-toggle-image-urls').value;

    saveState();
    generatePreview();
});

// --- Preview Generation (Pyodide Integration) ---
btnPreviewRefresh.addEventListener('click', generatePreview);
btnPreviewGenerate.addEventListener('click', generatePreview);

async function generatePreview() {
    if (!window.pyodide) {
        showToast("Pyodide not loaded yet.", "warning");
        return;
    }
    if (!builderState.currentConfig.template) {
        return;
    }

    previewOverlay.innerHTML = 'Generating...';
    previewOverlay.classList.remove('hidden');

    try {
        // Unmount existing iframe document to aid browser GC before injecting massive new HTML string
        previewFrame.srcdoc = "<html><body>Loading...</body></html>";

        // Expose the JSON state to the Python context
        window.builderConfigJson = JSON.stringify(builderState.currentConfig);

        // Load the Python script generated by build.py
        const pyCode = BUILDER_PREVIEW_PY_PLACEHOLDER;

        const resultHtml = await window.pyodide.runPythonAsync(pyCode);
        previewFrame.srcdoc = resultHtml;
        previewOverlay.classList.add('hidden');
    } catch (err) {
        showToast("Preview Generation Error:", err, "error")
        previewOverlay.innerHTML = `<div class="text-red-500 font-bold">Error generating preview</div><div class="text-xs text-red-400 p-4 overflow-auto">${err.message}</div>`;
    }
}

// Scaffold Initial Project

// Integrations
if (btnApplyIntegrations) {
    btnApplyIntegrations.addEventListener('click', () => {
        const id = propIntegElementId.value.trim();
        if (!id) return showToast('Please specify a target element ID.');

        if (!builderState.currentConfig.elements[id]) builderState.currentConfig.elements[id] = {};
        const el = builderState.currentConfig.elements[id];

        const type = propIntegType.value;
        const url = propIntegUrl.value.trim();

        if (type && url) {
            el[type] = url;
        } else {
            ['document', 'map_location', 'ecommerce', 'rich_media', 'bi', 'external_form', 'form', 'social', 'replit'].forEach(t => {
                delete el[t];
            });
        }

        saveState();
        if (window.pyodide) { generatePreview(); }
    });
}

// A11y & Media
if (btnApplyA11yMedia) {
    btnApplyA11yMedia.addEventListener('click', () => {
        const id = propA11yElementId.value.trim();
        if (!id) return showToast('Please specify a target element ID.');

        if (!builderState.currentConfig.elements[id]) builderState.currentConfig.elements[id] = {};
        const el = builderState.currentConfig.elements[id];

                if (propA11yAriaLabel.value) el.ariaLabel = propA11yAriaLabel.value; else delete el.ariaLabel;
        if (propA11yTabindex.value !== '') el.tabindex = parseInt(propA11yTabindex.value); else delete el.tabindex;
        if (propA11yMarker.value) el.marker = propA11yMarker.value; else delete el.marker;
        if (propA11yVideo.value) el.video = propA11yVideo.value; else delete el.video;
        if (propA11yAudio.value) el.audio = propA11yAudio.value; else delete el.audio;
        if (propA11yMarkdown.value) el.markdown = propA11yMarkdown.value; else delete el.markdown;
        if (propA11yGallery.value) el.gallery = propA11yGallery.value.split(',').map(s => s.trim()); else delete el.gallery;
        if (propA11yEmbedSvg.value) el.embed_svg = propA11yEmbedSvg.value; else delete el.embed_svg;
        if (propA11yLottie.value) el.lottie = propA11yLottie.value; else delete el.lottie;
        if (propA11yMorph.value) el.morph_to_path = propA11yMorph.value; else delete el.morph_to_path;
        if (propA11yClip.value) el.clip_image_url = propA11yClip.value; else delete el.clip_image_url;
        if (propA11yTransform.value) el.transform = propA11yTransform.value; else delete el.transform;
        if (propA11yExplode.checked) el.explode = true; else delete el.explode;
        if (propA11yConfetti.checked) el.confetti = true; else delete el.confetti;
        if (propA11yLoading.checked) el.loading = true; else delete el.loading;
        if (propA11yZoomTo.value) el.zoom_to = propA11yZoomTo.value; else delete el.zoom_to;

        saveState();
        if (window.pyodide) { generatePreview(); }
    });
}

// Global Styles
if (btnApplyGlobalStyle) {
    btnApplyGlobalStyle.addEventListener('click', () => {
        if (!builderState.currentConfig.globalSettings) builderState.currentConfig.globalSettings = {};
        const gs = builderState.currentConfig.globalSettings;

        gs.theme = propGlobalTheme.value;
        gs.ambient_effect = propGlobalAmbient.value;
        gs.default_panel_position = propGlobalPanelPos.value;
        gs.background_image_url = propGlobalBgImg.value;
        gs.svg_background_image_url = propGlobalSvgBgImg.value;
        gs.border_image_url = propGlobalBorderImg.value;
        gs.custom_css = propGlobalCss.value;
        gs.custom_js = propGlobalJs.value;

        saveState();
        if (window.pyodide) { generatePreview(); }
    });
}


btnNewProject.addEventListener('click', () => {
   // Switch tab to annotator or prompt for SVG
   if (window.switchTab) {
       window.switchTab('annotator');
   }
});

btnAnnotateInspect.addEventListener('click', () => {
    // Re-purpose the Inspect Elements button to enable highlight mode and guide the user
    if (!builderState.currentConfig.highlightElements) {
        builderState.currentConfig.highlightElements = true;
        propHighlightElements.checked = true;
        saveState();
        generatePreview();
    }

    // Provide user feedback
    const originalText = btnAnnotateInspect.innerText;
    btnAnnotateInspect.innerText = "Click an element in the preview!";
    btnAnnotateInspect.classList.remove('bg-slate-100', 'text-slate-700');
    btnAnnotateInspect.classList.add('bg-blue-100', 'text-blue-700', 'border-blue-300');

    setTimeout(() => {
        btnAnnotateInspect.innerText = originalText;
        btnAnnotateInspect.classList.add('bg-slate-100', 'text-slate-700');
        btnAnnotateInspect.classList.remove('bg-blue-100', 'text-blue-700', 'border-blue-300');
    }, 3000);
});


// --- Phase 3 Graph Properties Logic ---
btnApplyGraphProps.addEventListener('click', () => {
    let activeId = propGraphElementId.value.trim();
    if (!activeId) {
        showToast("Please select or enter a Target Element ID first.");
        return;
    }

    if (!builderState.currentConfig.elements[activeId]) {
        builderState.currentConfig.elements[activeId] = {};
    }
    let elConfig = builderState.currentConfig.elements[activeId];
    elConfig.graphType = propGraphType.value;
    elConfig.graphTitle = propGraphTitle.value;

    saveState();
    generatePreview();
});

// --- Phase 4 Live Data & Fetch Action Logic ---
btnApplyLiveData.addEventListener('click', () => {
    builderState.currentConfig.liveWsUrl = propLiveWsUrl.value.trim();
    builderState.currentConfig.liveWsTopic = propLiveWsTopic.value.trim();
    builderState.currentConfig.liveApiUrl = propLiveApiUrl.value.trim();
    builderState.currentConfig.liveApiInterval = propLiveApiInterval.value.trim();
    builderState.currentConfig.liveApiPath = propLiveApiPath.value.trim();

    builderState.currentConfig.timelineCsvFile = propTimelineCsvFile.value.trim();
    builderState.currentConfig.timelineTimeCol = propTimelineTimeCol.value.trim();
    builderState.currentConfig.timelineMapType = propTimelineMapType.value.trim();

    saveState();
    generatePreview();
});

btnApplyFetchProps.addEventListener('click', () => {
    let activeId = propFetchElementId.value.trim();
    if (!activeId) {
        showToast("Please select or enter a Target Element ID first.");
        return;
    }

    if (!builderState.currentConfig.elements[activeId]) {
        builderState.currentConfig.elements[activeId] = {};
    }
    let elConfig = builderState.currentConfig.elements[activeId];
    elConfig.fetchUrl = propFetchUrl.value.trim();
    elConfig.fetchDataPath = propFetchDataPath.value.trim();

    saveState();
    generatePreview();
});


// --- Phase 5 Logic ---
btnApplyTimeline.addEventListener('click', () => {
    builderState.currentConfig.presentationAutoplay = propPresentationAutoplay.value.trim();
    builderState.currentConfig.presentationProgress = propPresentationProgress.checked;
    builderState.currentConfig.presentationLaser = propPresentationLaser.checked;
    builderState.currentConfig.presentationNotes = propPresentationNotes.value.trim();
    saveState();
    generatePreview();
});

btnApplyOverlays.addEventListener('click', () => {
    // Handle connections
    const fromId = propOverlayConnFrom.value.trim();
    const toId = propOverlayConnTo.value.trim();
    if (fromId && toId) {
        if (!builderState.currentConfig.connections) builderState.currentConfig.connections = [];
        // Only add if not already present
        const exists = builderState.currentConfig.connections.find(c => c.from === fromId && c.to === toId);
        if (!exists) {
            builderState.currentConfig.connections.push({from: fromId, to: toId});
        }
    }

    // Handle element specific overlay config
    let activeId = propOverlayElementId.value.trim();
    if (activeId) {
        if (!builderState.currentConfig.elements[activeId]) {
            builderState.currentConfig.elements[activeId] = {};
        }
        let elConfig = builderState.currentConfig.elements[activeId];
        elConfig.fillZone = propOverlayFillZone.value.trim();
        elConfig.clipHtml = propOverlayClipHtml.value.trim();
        elConfig.shapeType = propOverlayShapeType.value;
        elConfig.absoluteImageUrl = propOverlayImageUrl.value.trim();
        elConfig.scratchoff = propOverlayScratchoff.checked;
    }

    saveState();
    generatePreview();
});

btnApplyControls.addEventListener('click', () => {
    builderState.currentConfig.ctrlZoomUi = propCtrlZoomUi.checked;
    builderState.currentConfig.ctrlMinimap = propCtrlMinimap.checked;
    builderState.currentConfig.ctrlZoomClick = propCtrlZoomClick.checked;
    builderState.currentConfig.ctrlDrawing = propCtrlDrawing.checked;
    builderState.currentConfig.ctrlBrush = propCtrlBrush.checked;
    builderState.currentConfig.ctrlSearch = propCtrlSearch.checked;
    builderState.currentConfig.ctrlLayerToggle = propCtrlLayerToggle.value.trim();
    builderState.currentConfig.ctrlPanelDismiss = propCtrlPanelDismiss.value.trim();
    builderState.currentConfig.ctrlUrlNavId = propCtrlUrlNavId.value.trim();
    builderState.currentConfig.ctrlUrlNavUrl = propCtrlUrlNavUrl.value.trim();
    saveState();
    generatePreview();
});

// Phase 6 Button Listeners
btnApplyGeocoding.addEventListener('click', () => {
    builderState.currentConfig.geocodeEnable = propGeocodeEnable.checked;
    builderState.currentConfig.geocodeProvider = propGeocodeProvider.value;
    builderState.currentConfig.geocodeApiKey = propGeocodeApiKey.value.trim();
    saveState();
    generatePreview();
});

btnApplyMultiview.addEventListener('click', () => {
    const elId = propMvElementId.value.trim();
    const viewId = propMvViewId.value.trim();
    if (elId) {
        if (!builderState.currentConfig.elements) builderState.currentConfig.elements = {};
        if (!builderState.currentConfig.elements[elId]) builderState.currentConfig.elements[elId] = {};
        builderState.currentConfig.elements[elId].drillThroughViewId = viewId;
        saveState();
        generatePreview();
    }
});

btnApplyExport.addEventListener('click', () => {
    builderState.currentConfig.exportWatermark = propExportWatermark.value.trim();
    builderState.currentConfig.exportAttribution = propExportAttribution.value.trim();
    builderState.currentConfig.exportE2e = propExportE2e.checked;
    saveState();
    generatePreview();
});

// --- Builder Sub-Tabs Logic ---
builderTabBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
        // Reset all tabs
        builderTabBtns.forEach(b => {
            b.classList.remove('border-b-2', 'border-blue-600', 'text-blue-600', 'bg-white');
            b.classList.add('border-b-2', 'border-transparent', 'hover:text-blue-600', 'hover:bg-slate-50');
        });
        builderTabContents.forEach(c => {
            c.classList.remove('block');
            c.classList.add('hidden');
        });

        // Activate clicked
        const targetTab = e.target.getAttribute('data-tab');
        e.target.classList.remove('border-transparent', 'hover:text-blue-600', 'hover:bg-slate-50');
        e.target.classList.add('border-blue-600', 'text-blue-600', 'bg-white');
        document.getElementById(`builder-tab-${targetTab}`).classList.remove('hidden');
        document.getElementById(`builder-tab-${targetTab}`).classList.add('block');
    });
});

// Initialize state
saveState();




// --- Phase 3 Features ---
btnSelectDataFile.addEventListener("click", () => {
    showIdbfsModal("Select CSV File", ".csv", (filename) => {
        propDataFile.value = filename;
        builderState.currentConfig.dataFile = filename;

        // Data Binding Wizard Logic: Auto-populate elements if valid CSV
        const mountDir = "/sivo_workspace";
        try {
            const data = window.pyodide.FS.readFile(`${mountDir}/${filename}`, { encoding: 'utf8' });

            const parseCSVLine = (text) => {
                let result = [];
                let cur = '';
                let inQuotes = false;
                for (let i = 0; i < text.length; i++) {
                    let char = text[i];
                    if (inQuotes) {
                        if (char === '"') {
                            if (i + 1 < text.length && text[i+1] === '"') {
                                cur += '"';
                                i++;
                            } else {
                                inQuotes = false;
                            }
                        } else {
                            cur += char;
                        }
                    } else {
                        if (char === '"') {
                            inQuotes = true;
                        } else if (char === ',') {
                            result.push(cur);
                            cur = '';
                        } else {
                            cur += char;
                        }
                    }
                }
                result.push(cur);
                return result.map(s => s.trim());
            };

            // Improved CSV parse to handle quotes and find IDs
            const lines = data.split("\n").filter(l => l.trim() !== "");
            if (lines.length > 1) {
                // Parse header
                const parsedHeader = parseCSVLine(lines[0]);

                const idColName = builderState.currentConfig.dataIdCol || "id";
                const idIdx = parsedHeader.indexOf(idColName);
                if (idIdx !== -1) {
                    for(let i=1; i<lines.length; i++) {
                        const parsedCols = parseCSVLine(lines[i]);

                        if (parsedCols.length > idIdx) {
                            const id = parsedCols[idIdx];
                            if (id && !builderState.currentConfig.elements[id]) {
                                builderState.currentConfig.elements[id] = {
                                    fill: '#3b82f6',
                                    hover: '#60a5fa'
                                };
                            }
                        }
                    }
                }
            }
        } catch(e) {
            showToast(e, "error")
        }

        saveState();
        generatePreview();
    });
});

propDataFile.addEventListener("change", (e) => {
    builderState.currentConfig.dataFile = e.target.value.trim();

    // Memory Profiling Warning: Large data files
    if (builderState.currentConfig.dataFile) {
        try {
            const stat = window.pyodide.FS.stat("/sivo_workspace/" + builderState.currentConfig.dataFile);
            if (stat.size > 10 * 1024 * 1024) { // 10MB
                showToast("Warning: The selected data file is very large (" + (stat.size / 1024 / 1024).toFixed(2) + " MB). Mapping this dataset might consume significant memory and crash the browser tab.");
            }
        } catch(err) {
            // Ignore if file stat fails
        }
    }

    saveState();
    generatePreview();
});

propDataIdCol.addEventListener("change", (e) => {
    builderState.currentConfig.dataIdCol = e.target.value.trim();
    saveState();
    generatePreview();
});

propDataValueCol.addEventListener("change", (e) => {
    builderState.currentConfig.dataValueCol = e.target.value.trim();
    saveState();
    generatePreview();
});

propDataMapType.addEventListener("change", (e) => {
    builderState.currentConfig.dataMapType = e.target.value;
    updateDataMapUI();
    saveState();
    generatePreview();
});

function updateDataMapUI() {
    const mapType = propDataMapType.value;

    // Hide all
    dataColsIdContainer.classList.add('hidden');
    dataColsValueContainer.classList.add('hidden');
    dataColsBivariate.classList.add('hidden');
    dataColsHexbin.classList.add('hidden');
    dataColsFlow.classList.add('hidden');

    // Show relevant based on type
    if (['choropleth', 'categorical', 'dot_density', 'proportional_symbols', 'spike_map'].includes(mapType)) {
        dataColsIdContainer.classList.remove('hidden');
        dataColsValueContainer.classList.remove('hidden');
    } else if (mapType === 'value_by_alpha') {
        dataColsIdContainer.classList.remove('hidden');
        dataColsBivariate.classList.remove('hidden');
    } else if (mapType === 'hexbin') {
        dataColsHexbin.classList.remove('hidden');
    } else if (mapType === 'flow_map') {
        dataColsFlow.classList.remove('hidden');
        dataColsValueContainer.classList.remove('hidden'); // usually flow has a value/weight
    }
}

['prop-data-base-col', 'prop-data-alpha-col', 'prop-data-x-col', 'prop-data-y-col', 'prop-data-origin-col', 'prop-data-dest-col'].forEach(id => {
    const el = document.getElementById(id);
    if (el) {
        el.addEventListener("change", (e) => {
            const key = "data" + id.replace("prop-data-", "").split("-").map(s => s.charAt(0).toUpperCase() + s.slice(1)).join("");
            builderState.currentConfig[key] = e.target.value.trim();
            saveState();
            generatePreview();
        });
    }
});



function renderTimelineSteps() {
    timelineStepsContainer.innerHTML = '';
    const steps = builderState.currentConfig.timelineSteps || [];

    steps.forEach((step, index) => {
        const div = document.createElement('div');
        div.className = "flex flex-col space-y-1 bg-slate-50 p-2 border border-slate-200 rounded";

        const title = (step.title || '').replace(/"/g, '&quot;');
        const content = (step.content || '').replace(/"/g, '&quot;');
        const targetId = (step.targetId || '').replace(/"/g, '&quot;');

        div.innerHTML = `
            <div class="flex justify-between items-center mb-1">
                <span class="text-xs font-bold text-slate-500">Step ${index + 1}</span>
                <button class="step-delete text-red-500 hover:text-red-700 text-xs" data-index="${index}">&times; Remove</button>
            </div>
            <input type="text" placeholder="Title" value="${title}" class="step-title w-full px-2 py-1 text-xs border border-slate-200 rounded" data-index="${index}">
            <textarea placeholder="Content (HTML/Text)" class="step-content w-full px-2 py-1 text-xs border border-slate-200 rounded" data-index="${index}" rows="2">${content}</textarea>
            <input type="text" placeholder="Target Element ID" value="${targetId}" class="step-target w-full px-2 py-1 text-xs border border-slate-200 rounded" data-index="${index}">
        `;
        timelineStepsContainer.appendChild(div);
    });

    timelineStepsContainer.querySelectorAll('.step-title').forEach(input => {
        input.addEventListener('change', (e) => {
            const idx = parseInt(e.target.dataset.index);
            builderState.currentConfig.timelineSteps[idx].title = e.target.value;
            saveState();
            generatePreview();
        });
    });

    timelineStepsContainer.querySelectorAll('.step-content').forEach(input => {
        input.addEventListener('change', (e) => {
            const idx = parseInt(e.target.dataset.index);
            builderState.currentConfig.timelineSteps[idx].content = e.target.value;
            saveState();
            generatePreview();
        });
    });

    timelineStepsContainer.querySelectorAll('.step-target').forEach(input => {
        input.addEventListener('change', (e) => {
            const idx = parseInt(e.target.dataset.index);
            builderState.currentConfig.timelineSteps[idx].targetId = e.target.value;
            saveState();
            generatePreview();
        });
    });

    timelineStepsContainer.querySelectorAll('.step-delete').forEach(btn => {
        btn.addEventListener('click', (e) => {
            const idx = parseInt(e.target.dataset.index);
            builderState.currentConfig.timelineSteps.splice(idx, 1);
            saveState();
            renderTimelineSteps();
            generatePreview();
        });
    });
}

btnAddTimelineStep.addEventListener("click", () => {
    if (!builderState.currentConfig.timelineSteps) {
        builderState.currentConfig.timelineSteps = [];
    }
    const idx = builderState.currentConfig.timelineSteps.length + 1;
    builderState.currentConfig.timelineSteps.push({
        title: "",
        content: "",
        targetId: ""
    });

    renderTimelineSteps();
    saveState();
    generatePreview();
});

function renderDashboardBlocks() {
    dashboardBlocksContainer.innerHTML = '';
    const blocks = builderState.currentConfig.dashboardBlocks || [];

    blocks.forEach((block, index) => {
        const div = document.createElement('div');
        div.className = "flex items-center space-x-2 bg-slate-50 p-2 border border-slate-200 rounded";

        // Escape quotes to prevent breaking HTML attributes
        const title = (block.title || '').replace(/"/g, '&quot;');
        const value = (block.value || '').replace(/"/g, '&quot;');

        div.innerHTML = `
            <div class="flex-1 space-y-1">
                <input type="text" placeholder="Title" value="${title}" class="block-title w-full px-2 py-1 text-xs border border-slate-200 rounded" data-index="${index}">
                <input type="text" placeholder="Value" value="${value}" class="block-value w-full px-2 py-1 text-xs border border-slate-200 rounded" data-index="${index}">
            </div>
            <button class="block-delete text-red-500 hover:text-red-700" data-index="${index}">&times;</button>
        `;
        dashboardBlocksContainer.appendChild(div);
    });

    // Add event listeners
    dashboardBlocksContainer.querySelectorAll('.block-title').forEach(input => {
        input.addEventListener('change', (e) => {
            const idx = parseInt(e.target.dataset.index);
            builderState.currentConfig.dashboardBlocks[idx].title = e.target.value;
            saveState();
            generatePreview();
        });
    });

    dashboardBlocksContainer.querySelectorAll('.block-value').forEach(input => {
        input.addEventListener('change', (e) => {
            const idx = parseInt(e.target.dataset.index);
            builderState.currentConfig.dashboardBlocks[idx].value = e.target.value;
            saveState();
            generatePreview();
        });
    });

    dashboardBlocksContainer.querySelectorAll('.block-delete').forEach(btn => {
        btn.addEventListener('click', (e) => {
            const idx = parseInt(e.target.dataset.index);
            builderState.currentConfig.dashboardBlocks.splice(idx, 1);
            saveState();
            renderDashboardBlocks();
    renderTimelineSteps();
            generatePreview();
        });
    });
}

btnAddDashboardBlock.addEventListener("click", () => {
    if (!builderState.currentConfig.dashboardBlocks) {
        builderState.currentConfig.dashboardBlocks = [];
    }
    const idx = builderState.currentConfig.dashboardBlocks.length + 1;
    builderState.currentConfig.dashboardBlocks.push({
        title: "",
        value: ""
    });

    renderDashboardBlocks();
    saveState();
    generatePreview();
});

btnValidateProject.addEventListener("click", async () => {
    validationResults.classList.remove("hidden");
    validationResults.innerHTML = "Validating...";
    validationResults.className = "mt-2 text-xs text-blue-600 bg-blue-50 border border-blue-200 rounded p-2 max-h-32 overflow-y-auto";

    if (!window.pyodide) {
        validationResults.innerHTML = "Pyodide not loaded yet.";
        validationResults.className = "mt-2 text-xs text-red-600 bg-red-50 border border-red-200 rounded p-2 max-h-32 overflow-y-auto";
        return;
    }

    window.builderConfigJson = JSON.stringify(builderState.currentConfig);
    const pythonCode = `
import json
import traceback

def validate_project():
    try:
        import sivo
        import js
        config = json.loads(js.window.builderConfigJson)

        template_path = config.get('template')
        custom_svg = config.get('customSvg')

        app = None
        if custom_svg:
            if custom_svg.startswith('http'):
                 app = sivo.Sivo.from_svg(custom_svg)
            elif custom_svg.startswith('<svg'):
                 app = sivo.Sivo.from_string(custom_svg)
            else:
                 with open('/sivo_workspace/' + custom_svg.replace('/sivo_workspace/',''), 'r') as f:
                     app = sivo.Sivo.from_string(f.read())
        elif template_path and template_path != 'blank':
             app = sivo.Sivo.from_template(template_path)
        else:
             app = sivo.Sivo.from_string('<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="#f8fafc"/></svg>')

        if hasattr(app, "validate"):
             errors, warnings = app.validate()
        else:
             errors, warnings = [], []

        if config.get("dataFile"):
             df = None
             data_file = config.get("dataFile")
             try:
                 import pandas as pd
                 with open('/sivo_workspace/' + data_file.replace('/sivo_workspace/',''), 'r') as f:
                     if data_file.endswith('.csv'):
                         df = pd.read_csv(f)
                     else:
                         df = pd.read_json(f)
             except Exception as e:
                 errors.append(f"Could not load dataFile {data_file}: {e}")

             if df is not None:
                 if config.get("dataIdCol") and config.get("dataIdCol") not in df.columns:
                     errors.append(f"Data mapping missing ID column: {config.get('dataIdCol')}")
                 if config.get("dataValueCol") and config.get("dataValueCol") not in df.columns:
                     errors.append(f"Data mapping missing Value column: {config.get('dataValueCol')}")

        return json.dumps({"errors": errors, "warnings": warnings})

    except Exception as e:
        return json.dumps({"errors": [f"Validation failed: {str(e)}"], "warnings": []})

validate_project()
`;

    try {
        const resultRaw = await window.pyodide.runPythonAsync(pythonCode);
        const result = JSON.parse(resultRaw);

        if (result.errors.length > 0) {
            validationResults.innerHTML = "<b>Validation Errors:</b><br/>" + result.errors.join("<br/>");
            validationResults.className = "mt-2 text-xs text-red-600 bg-red-50 border border-red-200 rounded p-2 max-h-32 overflow-y-auto";
        } else if (result.warnings.length > 0) {
            validationResults.innerHTML = "<b>Validation Warnings:</b><br/>" + result.warnings.join("<br/>");
            validationResults.className = "mt-2 text-xs text-yellow-600 bg-yellow-50 border border-yellow-200 rounded p-2 max-h-32 overflow-y-auto";
        } else {
            validationResults.innerHTML = "Project is valid!";
            validationResults.className = "mt-2 text-xs text-green-600 bg-green-50 border border-green-200 rounded p-2 max-h-32 overflow-y-auto";
        }
    } catch(e) {
        validationResults.innerHTML = "<b>Validation Script Error:</b><br/>" + e.message;
        validationResults.className = "mt-2 text-xs text-red-600 bg-red-50 border border-red-200 rounded p-2 max-h-32 overflow-y-auto";
    }
});
