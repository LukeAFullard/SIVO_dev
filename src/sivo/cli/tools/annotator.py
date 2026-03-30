import http.server
import socketserver
import webbrowser
import os
import threading
from urllib.parse import urlparse

# Path to the HTML tool
TOOL_HTML_PATH = os.path.join(os.path.dirname(__file__), "annotator.html")

class AnnotatorHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open(TOOL_HTML_PATH, 'rb') as f:
                self.wfile.write(f.read())
        else:
            # Let simplehttp serve files if needed (e.g. user selects local image from directory)
            super().do_GET()

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

def run_annotator_server(port=8080):
    handler = AnnotatorHandler
    with ReusableTCPServer(("127.0.0.1", port), handler) as httpd:
        print(f"Starting SIVO Annotator tool on http://127.0.0.1:{port}")
        # Open in browser
        webbrowser.open(f"http://127.0.0.1:{port}")
        httpd.serve_forever()

def cmd_annotate(args):
    """Starts the local web-based SIVO annotation tool."""
    port = args.port
    # Start server in main thread to keep script alive until user kills it
    try:
         run_annotator_server(port)
    except KeyboardInterrupt:
         print("\nShutting down annotator server.")
