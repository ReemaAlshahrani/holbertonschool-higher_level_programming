import http.server
import json

class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    
    def do_GET(self):
        # 1. Endpoint: Root /
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
            
        # 2. Endpoint: /data
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            data = {"name": "John", "age": 30, "city": "New York"}
            # Convert Python dictionary to JSON string and encode to bytes
            self.wfile.write(json.dumps(data).encode('utf-8'))
            
        # 3. Endpoint: /status
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(b"OK")
            
        # 4. Error Handling: Undefined Endpoints (404)
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

def run():
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, SimpleAPIHandler)
    print("Server running on http://localhost:8000 ...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")

if __name__ == '__main__':
    run()
