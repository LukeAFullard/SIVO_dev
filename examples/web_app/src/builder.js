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


const btnValidateProject = document.getElementById("btn-validate-project");
const validationResults = document.getElementById("validation-results");
const propDataFile = document.getElementById("prop-data-file");
const btnSelectDataFile = document.getElementById("btn-select-data-file");


const propGraphType = document.getElementById("prop-graph-type");

const btnAddDashboardBlock = document.getElementById("btn-add-dashboard-block");


// Dynamic Property Containers
const propFootnoteContainer = document.getElementById('prop-footnote-container');
const propToggleImageContainer = document.getElementById('prop-toggle-image-container');


// --- State Management (Undo/Redo) ---
function saveState() {
    // If we're not at the end of history, truncate the future
    if (builderState.historyIndex < builderState.history.length - 1) {
        builderState.history = builderState.history.slice(0, builderState.historyIndex + 1);
    }

    builderState.history.push(JSON.parse(JSON.stringify(builderState.currentConfig)));
    builderState.historyIndex++;
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

            // Sync Canvas Settings UI
            propCustomSvg.value = config.customSvg || '';
            propBgImage.value = config.bgImage || '';
            propHighlightElements.checked = !!config.highlightElements;
            propDataFile.value = config.dataFile || "";

            saveState();
            previewOverlay.classList.add('hidden');
            generatePreview();
        } catch (err) {
            alert("Invalid JSON configuration file.");
        }
    };
    reader.readAsText(file);
});

btnImportJsonIdbfs.addEventListener('click', () => {
    showIdbfsModal("Select JSON Config", ".json", (filename) => {
        const mountDir = "/sivo_workspace";
        try {
            const data = window.pyodide.FS.readFile(`${mountDir}/${filename}`, { encoding: 'utf8' });
            const config = JSON.parse(data);
            builderState.currentConfig = config;

            // Sync Canvas Settings UI
            propCustomSvg.value = config.customSvg || '';
            propBgImage.value = config.bgImage || '';
            propHighlightElements.checked = !!config.highlightElements;
            propDataFile.value = config.dataFile || "";

            saveState();
            previewOverlay.classList.add('hidden');
            generatePreview();
        } catch(err) {
            console.error(err);
            alert("Failed to load JSON: " + err.message);
        }
    });
});


// --- Canvas Settings ---
btnApplyCanvasSettings.addEventListener('click', () => {
    builderState.currentConfig.customSvg = propCustomSvg.value.trim();
    builderState.currentConfig.bgImage = propBgImage.value.trim();
    builderState.currentConfig.highlightElements = propHighlightElements.checked;

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
        alert("Pyodide File System is not ready yet.");
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
        console.error("Error reading IDBFS:", err);
        alert("Error reading IDBFS: " + err.message);
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

    const id = propElementId.value;
    if (!id || !builderState.currentConfig.elements[id]) {
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
    if (!id) return alert("Please enter an Element ID first.");

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

    el.graphType = propGraphType.value;


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
        console.warn("Pyodide not loaded yet.");
        return;
    }
    if (!builderState.currentConfig.template) {
        return;
    }

    previewOverlay.innerHTML = 'Generating...';
    previewOverlay.classList.remove('hidden');

    try {
        // Expose the JSON state to the Python context
        window.builderConfigJson = JSON.stringify(builderState.currentConfig);

        // Load the Python script generated by build.py
        const pyCode = BUILDER_PREVIEW_PY_PLACEHOLDER;

        const resultHtml = await window.pyodide.runPythonAsync(pyCode);
        previewFrame.srcdoc = resultHtml;
        previewOverlay.classList.add('hidden');
    } catch (err) {
        console.error("Preview Generation Error:", err);
        previewOverlay.innerHTML = `<div class="text-red-500 font-bold">Error generating preview</div><div class="text-xs text-red-400 p-4 overflow-auto">${err.message}</div>`;
    }
}

// Scaffold Initial Project
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
            // Very simple CSV parse to find IDs
            const lines = data.split("\n");
            if (lines.length > 1) {
                const header = lines[0].split(",");
                const idIdx = header.indexOf("id");
                if (idIdx !== -1) {
                    for(let i=1; i<lines.length; i++) {
                        const cols = lines[i].split(",");
                        if (cols.length > idIdx) {
                            const id = cols[idIdx].trim();
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
            console.error(e);
        }

        saveState();
        generatePreview();
    });
});

propDataFile.addEventListener("change", (e) => {
    builderState.currentConfig.dataFile = e.target.value.trim();
    saveState();
    generatePreview();
});


btnAddDashboardBlock.addEventListener("click", () => {
    if (!builderState.currentConfig.dashboardBlocks) {
        builderState.currentConfig.dashboardBlocks = [];
    }
    const idx = builderState.currentConfig.dashboardBlocks.length + 1;
    builderState.currentConfig.dashboardBlocks.push({
        title: "Metric " + idx,
        value: Math.floor(Math.random() * 1000).toString()
    });

    // Quick UI feedback
    btnAddDashboardBlock.innerText = `+ Add Dashboard Block (${idx} added)`;
    setTimeout(() => {
        btnAddDashboardBlock.innerText = "+ Add Dashboard Block";
    }, 1500);

    saveState();
    generatePreview();
});

btnValidateProject.addEventListener("click", () => {
    // Basic validation
    validationResults.classList.remove("hidden");
    let errors = [];
    if (!builderState.currentConfig.template && !builderState.currentConfig.customSvg) {
        errors.push("No template or custom SVG selected.");
    }

    if (Object.keys(builderState.currentConfig.elements || {}).length === 0 && !builderState.currentConfig.dataFile) {
        errors.push("No interactive elements or data bindings configured.");
    }

    if (errors.length > 0) {
        validationResults.innerHTML = "<b>Validation Issues:</b><br/>" + errors.join("<br/>");
        validationResults.className = "mt-2 text-xs text-red-600 bg-red-50 border border-red-200 rounded p-2 max-h-32 overflow-y-auto";
    } else {
        validationResults.innerHTML = "Project is valid!";
        validationResults.className = "mt-2 text-xs text-green-600 bg-green-50 border border-green-200 rounded p-2 max-h-32 overflow-y-auto";
    }
});
