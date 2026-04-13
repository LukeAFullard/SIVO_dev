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
                    console.warn('Running from file:// protocol. Loading local Python wheels via micropip.install("./sivo.whl") will fail due to browser CORS policies. Please start a local HTTP server to fully test the SIVO Python backend.');
                }

                statusEl.innerText = 'Ready!';
                runBtn.disabled = false;

            } catch (err) {
                console.error(err);
                statusEl.innerText = 'Error: Check console.';
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
                console.error(err);
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
                    fileListEl.innerHTML = files.map(f => `<div style="padding: 2px 0; word-break: break-all;">📄 ${f}</div>`).join('');
                }
            } catch (err) {
                console.error("Error reading directory", err);
            }
        }

        async function saveBufferToFS(filename, buffer) {
            try {
                const mountDir = "/sivo_workspace";

                // If it's an XLSX, ideally we would convert to CSV here to save Python memory,
                // but for now we'll write the raw file or handle it directly in Python if the user has openpyxl.
                // We'll write the raw bytes to IDBFS
                pyodide.FS.writeFile(`${mountDir}/${filename}`, new Uint8Array(buffer));

                await new Promise((resolve, reject) => {
                    pyodide.FS.syncfs(false, function(err) {
                        if (err) reject(err);
                        else resolve();
                    });
                });
                updateFileList();
            } catch (err) {
                console.error("Error saving file to IDBFS:", err);
                alert("Error saving file: " + err.message);
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
            dropzone.style.backgroundColor = '#e2e8f0';
        });
        dropzone.addEventListener('dragleave', (e) => {
            e.preventDefault();
            dropzone.style.backgroundColor = '';
        });
        dropzone.addEventListener('drop', async (e) => {
            e.preventDefault();
            dropzone.style.backgroundColor = '';
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
                console.error("Error fetching URL:", err);
                alert("Failed to fetch URL: " + err.message);
            } finally {
                btn.innerText = originalText;
                btn.disabled = false;
            }
        });

        // Start initialization
        initApp();
