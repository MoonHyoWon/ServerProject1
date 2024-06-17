import http.server
import socketserver

# 포트 번호 설정
PORT = 8000

# HTTP 요청을 처리할 핸들러 설정
Handler = http.server.SimpleHTTPRequestHandler

# 소켓 서버 설정
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    # 서버 실행
    httpd.serve_forever()