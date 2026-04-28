#!/usr/bin/env python3
"""
Simple HTTP Server for Portfolio Website
Serves the portfolio at http://localhost:8000
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

PORT = 8000
DIRECTORY = str(Path(__file__).parent)

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def log_message(self, format, *args):
        print(f"[{self.log_date_time_string()}] {format%args}")

def run_server():
    """Start the HTTP server"""
    os.chdir(DIRECTORY)
    
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print("=" * 60)
        print("🚀 Portfolio Server Started!")
        print("=" * 60)
        print(f"📍 Server running at: http://localhost:{PORT}")
        print(f"📁 Serving files from: {DIRECTORY}")
        print(f"\n✨ Your portfolio is now live!")
        print("Press CTRL+C to stop the server")
        print("=" * 60)
        
        # Open browser automatically
        try:
            webbrowser.open(f'http://localhost:{PORT}')
            print("🌐 Opening portfolio in your default browser...\n")
        except:
            print("📌 If browser doesn't open, visit: http://localhost:8000/index.html\n")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n" + "=" * 60)
            print("✋ Server stopped by user")
            print("=" * 60)
            return

if __name__ == "__main__":
    run_server()
