import http.server
import socketserver
import threading
import time

PORT = 8080
DIRECTORY = "examples/web_app/src"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def serve():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()

t = threading.Thread(target=serve, daemon=True)
t.start()
time.sleep(1)
