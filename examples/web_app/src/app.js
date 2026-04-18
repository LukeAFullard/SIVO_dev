
window.addEventListener('error', function(event) {
    if (event.message && (event.message.includes('out of memory') || event.message.includes('OOM'))) {
        showToast("CRITICAL: Browser ran out of memory. Please reload the page and use a smaller dataset.", "error");
    } else if (event.filename && event.filename.includes('pyodide')) {
        showToast("Pyodide Engine Error: " + event.message, "error");
    }
});

window.addEventListener('unhandledrejection', function(event) {
    if (event.reason && event.reason.message && event.reason.message.includes('memory')) {
        showToast("CRITICAL: Out of memory executing WASM.", "error");
    }
});

        // Inject the Annotator UI safely into the iframe
        const template = document.getElementById('annotator-template').innerHTML;
        const iframe = document.getElementById('annotator-frame');
        iframe.srcdoc = template;

        // Tab Switching Logic
        function switchTab(tabId) {
            document.querySelectorAll('.main-content').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));

            document.getElementById('view-' + tabId).classList.add('active');

            // Highlight button
            const buttons = document.querySelectorAll('.tab-btn');
            if (tabId === 'annotator') buttons[0].classList.add('active');
            if (tabId === 'workspace') buttons[1].classList.add('active');
            if (tabId === 'builder') buttons[2].classList.add('active');
        }

        let pyodide;
        const statusEl = document.getElementById('status');
        const runBtn = document.getElementById('run-btn');
        const codeInput = document.getElementById('python-code');
        const outputFrame = document.getElementById('output-frame');

        // This function is called by Python (`js.renderOutput`)
        window.renderOutput = function(htmlString) {
            outputFrame.srcdoc = htmlString;
        };

        async function initApp() {
            try {
                // 1. Load Pyodide
                pyodide = await loadPyodide();

                // Expose pyodide globally so the iframe annotator can find it (`window.parent.pyodide`)
                window.pyodide = pyodide;

                statusEl.innerText = 'Mounting IDBFS...';

                // 2. Mount IndexedDB File System (IDBFS) for persistence
                const mountDir = "/sivo_workspace";
                try {
                    pyodide.FS.mkdir(mountDir);
                } catch (e) {
                    if (e.code !== 'EEXIST') throw e;
                }
                pyodide.FS.mount(pyodide.FS.filesystems.IDBFS, {}, mountDir);

                // Sync from IndexedDB into memory
                await new Promise((resolve, reject) => {
                    pyodide.FS.syncfs(true, function(err) {
                        if (err) reject(err);
                        else resolve();
                    });
                });

                // Check Legal Agreement
                const legalFile = `${mountDir}/.legal_accepted`;
                let legalAccepted = false;
                try {
                    pyodide.FS.stat(legalFile);
                    legalAccepted = true;
                } catch (e) {
                    legalAccepted = false;
                }


                if (!legalAccepted) {
                    const modal = document.getElementById('legal-modal');
                    const acceptBtn = document.getElementById('accept-legal-btn');
                    const declineBtn = document.getElementById('decline-legal-btn');
                    const checkbox = document.getElementById('legal-consent-checkbox');

                    modal.classList.remove('hidden');

                    checkbox.addEventListener('change', (e) => {
                        if (e.target.checked) {
                            acceptBtn.disabled = false;
                            acceptBtn.classList.remove('bg-slate-300', 'cursor-not-allowed');
                            acceptBtn.classList.add('bg-blue-600', 'hover:bg-blue-700', 'hover:shadow-md');
                        } else {
                            acceptBtn.disabled = true;
                            acceptBtn.classList.remove('bg-blue-600', 'hover:bg-blue-700', 'hover:shadow-md');
                            acceptBtn.classList.add('bg-slate-300', 'cursor-not-allowed');
                        }
                    });

                    declineBtn.addEventListener('click', () => {
                        document.body.innerHTML = `
                        <div class="flex h-screen items-center justify-center flex-col font-sans bg-slate-50 text-slate-800">
                            <div class="bg-white p-8 rounded-2xl shadow-xl border border-slate-200 text-center max-w-md">
                                <div class="w-16 h-16 bg-red-100 text-red-500 rounded-full flex items-center justify-center mx-auto mb-4">
                                    <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
                                </div>
                                <h2 class="text-2xl font-bold mb-2 text-slate-900">Access Denied</h2>
                                <p class="text-slate-500 mb-6">You must accept the Legal Liability Waiver to use the SIVO Serverless Browser App.</p>
                                <button onclick="location.reload()" class="px-6 py-2.5 bg-blue-600 text-white font-medium rounded-lg hover:bg-blue-700 transition-colors shadow-sm">Return & Reload</button>
                            </div>
                        </div>`;
                    });

                    await new Promise((resolve) => {
                        acceptBtn.addEventListener('click', async () => {
                            if (!checkbox.checked) return;
                            pyodide.FS.writeFile(legalFile, 'accepted');
                            await new Promise((res, rej) => {
                                pyodide.FS.syncfs(false, function(err) {
                                    if (err) rej(err);
                                    else res();
                                });
                            });
                            modal.classList.add('hidden');
                            resolve();
                        }, { once: true });
                    });
                }


                updateFileList();

                statusEl.innerText = 'Installing SIVO...';

                // 3. Load SIVO's core dependencies from Pyodide's pre-compiled wheel repository
                await pyodide.loadPackage("micropip");
                const micropip = pyodide.pyimport("micropip");

                // Install dependencies (lxml is a C-extension, but Pyodide provides it)
                await micropip.install(['lxml', 'pydantic', 'Jinja2']);

                // 4. Install SIVO from local source (or a published wheel)
                // For this example to work locally, we zip the src directory and install it
                // In production, you would build a .whl file and host it statically: `await micropip.install('./sivo-0.1.0-py3-none-any.whl')`
                if (window.location.protocol === 'file:') {
                    showToast('Running from file:// protocol. Loading local Python wheels via micropip.install("./sivo.whl") will fail due to browser CORS policies. Please start a local HTTP server to fully test the SIVO Python backend.', "warning");
                }

                statusEl.innerText = 'Ready!';
                runBtn.disabled = false;

            } catch (err) {
                showToast(err, "error")
                statusEl.innerText = 'Error during initialization.';
                statusEl.style.color = '#ef4444';
            }
        }

        runBtn.addEventListener('click', async () => {
            if (!pyodide) return;

            runBtn.disabled = true;
            runBtn.innerText = 'Running...';
            outputFrame.srcdoc = "<html><body><div style='padding:20px; font-family:sans-serif;'>Generating interactive map...</div></body></html>";

            try {
                // Run the Python code
                await pyodide.runPythonAsync(codeInput.value);
            } catch (err) {
                showToast(err, "error")
                outputFrame.srcdoc = `<html><body><pre style='color:red; padding:20px; white-space:pre-wrap;'>${err.message}</pre></body></html>`;
            } finally {
                runBtn.disabled = false;
                runBtn.innerText = 'Run SIVO';
            }
        });

        function updateFileList() {
            if (!pyodide) return;
            const mountDir = "/sivo_workspace";
            const fileListEl = document.getElementById('file-list');
            try {
                const files = pyodide.FS.readdir(mountDir).filter(f => f !== '.' && f !== '..');
                if (files.length === 0) {
                    fileListEl.innerHTML = '<div style="color: #94a3b8; font-style: italic;">No files uploaded.</div>';
                } else {
                    fileListEl.innerHTML = files.map(f => `
                        <div style="padding: 4px 0; border-bottom: 1px solid #f1f5f9; display: flex; justify-content: space-between; align-items: center; word-break: break-all;">
                            <span>📄 ${f}</span>
                            <div style="display: flex; gap: 4px;">
                                <button onclick="window.viewFile('${f}')" style="font-size: 10px; padding: 2px 4px; cursor: pointer;">View</button>
                                <button onclick="window.deleteFile('${f}')" style="font-size: 10px; padding: 2px 4px; cursor: pointer; color: red;">Del</button>
                            </div>
                        </div>`).join('');
                }
            } catch (err) {
                showToast("Error reading directory", err, "error")
            }
        }

        window.viewFile = function(filename) {
            try {
                const mountDir = "/sivo_workspace";
                // Read as generic binary
                const data = pyodide.FS.readFile(`${mountDir}/${filename}`);

                // Determine mime type based on extension
                let mimeType = 'application/octet-stream';
                if (filename.endsWith('.json')) mimeType = 'application/json';
                else if (filename.endsWith('.svg')) mimeType = 'image/svg+xml';
                else if (filename.endsWith('.csv')) mimeType = 'text/csv';
                else if (filename.endsWith('.txt')) mimeType = 'text/plain';
                else if (filename.endsWith('.png')) mimeType = 'image/png';
                else if (filename.endsWith('.jpg') || filename.endsWith('.jpeg')) mimeType = 'image/jpeg';
                else if (filename.endsWith('.html')) mimeType = 'text/html';

                const blob = new Blob([data], { type: mimeType });
                const url = URL.createObjectURL(blob);
                window.open(url, '_blank');
            } catch (err) {
                showToast("Error viewing file: " + err.message);
            }
        };

        window.deleteFile = async function(filename) {
            if (!confirm(`Are you sure you want to delete ${filename}?`)) return;
            try {
                const mountDir = "/sivo_workspace";
                pyodide.FS.unlink(`${mountDir}/${filename}`);

                // Sync back to IDBFS
                await new Promise((resolve, reject) => {
                    pyodide.FS.syncfs(false, function(err) {
                        if (err) reject(err);
                        else resolve();
                    });
                });
                updateFileList();
            } catch (err) {
                showToast("Error deleting file: " + err.message);
            }
        };

        async function saveBufferToFS(filename, buffer) {
            try {
                const mountDir = "/sivo_workspace";
                let finalFilename = filename;
                let finalData = new Uint8Array(buffer);

                // If it's an XLSX, convert to CSV here to save Python memory
                if (filename.toLowerCase().endsWith('.xlsx') && window.XLSX) {
                    try {
                        const workbook = window.XLSX.read(finalData, { type: 'array' });
                        const firstSheetName = workbook.SheetNames[0];
                        const worksheet = workbook.Sheets[firstSheetName];
                        const csvText = window.XLSX.utils.sheet_to_csv(worksheet);

                        finalFilename = filename.replace(/\.xlsx$/i, '.csv');
                        finalData = new TextEncoder().encode(csvText);
                        showToast(`Converted ${filename} to ${finalFilename}`, "success");
                    } catch (e) {
                        showToast(`Failed to parse XLSX, saving raw file: ${e.message}`, "warning");
                    }
                }

                pyodide.FS.writeFile(`${mountDir}/${finalFilename}`, finalData);

                await new Promise((resolve, reject) => {
                    pyodide.FS.syncfs(false, function(err) {
                        if (err) reject(err);
                        else resolve();
                    });
                });
                updateFileList();
            } catch (err) {
                showToast("Error saving file to IDBFS:", err, "error")
                showToast("Error saving file: " + err.message);
            }
        }

        document.getElementById('file-upload').addEventListener('change', async (e) => {
            if (!pyodide) return;
            const file = e.target.files[0];
            if (!file) return;

            const reader = new FileReader();
            reader.onload = async (evt) => {
                let buffer = evt.target.result;
                await saveBufferToFS(file.name, buffer);
                buffer = null; // Memory cleanup
                e.target.value = ''; // Reset input
            };
            reader.readAsArrayBuffer(file);
        });

        const dropzone = document.getElementById('file-manager-dropzone');
        dropzone.addEventListener('dragover', (e) => {
            e.preventDefault();
            dropzone.classList.add('dropzone-active');
        });
        dropzone.addEventListener('dragleave', (e) => {
            e.preventDefault();
            dropzone.classList.remove('dropzone-active');
        });
        dropzone.addEventListener('drop', async (e) => {
            e.preventDefault();
            dropzone.classList.remove('dropzone-active');
            if (!pyodide) return;

            if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
                const file = e.dataTransfer.files[0];
                const reader = new FileReader();
                reader.onload = async (evt) => {
                    let buffer = evt.target.result;
                    await saveBufferToFS(file.name, buffer);
                    buffer = null; // Memory cleanup
                };
                reader.readAsArrayBuffer(file);
            }
        });

        document.getElementById('url-fetch-btn').addEventListener('click', async () => {
            if (!pyodide) return;
            const urlInput = document.getElementById('url-fetch-input');
            const url = urlInput.value.trim();
            if (!url) return;

            const btn = document.getElementById('url-fetch-btn');
            const originalText = btn.innerText;
            btn.innerText = 'Fetching...';
            btn.disabled = true;

            try {
                const response = await fetch(url);
                if (!response.ok) throw new Error(`HTTP ${response.status}`);
                let buffer = await response.arrayBuffer();

                // Extract filename from URL or use a default
                let filename = url.split('/').pop().split('?')[0] || 'downloaded_file';

                await saveBufferToFS(filename, buffer);
                buffer = null; // Memory cleanup
                urlInput.value = '';
            } catch (err) {
                showToast("Error fetching URL:", err, "error")
                showToast("Failed to fetch URL: " + err.message);
            } finally {
                btn.innerText = originalText;
                btn.disabled = false;
            }
        });

        // Start initialization
        initApp();
