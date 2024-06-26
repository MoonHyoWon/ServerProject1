import http.server
import socketserver

# 서버가 열 포트와 임의의 IP 주소를 지정
HOST = '192.168.0.113'  # 모든 인터페이스에서 요청을 수락
PORT = 8080

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer((HOST, PORT), Handler) as httpd:
    print(f"Serving at {HOST}:{PORT}")
    httpd.serve_forever()