#!/usr/bin/python3
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, World!")

        elif self.path == "/data":
            data = {
                "name": "Alice",
                "age": 30,
                "city": "New York"
            }
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Status: OK")

        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Not Found")

def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8080):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print("Starting httpd server on port {}...".format(port))
    httpd.serve_forever()

if __name__ == "__main__":
    run()
