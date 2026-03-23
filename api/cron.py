# api/cron.py
from http.server import BaseHTTPRequestHandler
import os

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Optional: Secure your endpoint with a secret key
        auth_header = self.headers.get('Authorization')
        if auth_header != f"Bearer {os.environ.get('CRON_SECRET')}":
            self.send_response(401)
            self.end_headers()
            return

        # --- Your Script Logic Starts Here ---
        print("Script executed by Vercel Cron!")
        # --------------------------------------

        self.send_response(200)
        self.end_headers()
        self.wfile.write("Success".encode())
