from http.server import HTTPServer, BaseHTTPRequestHandler
import redis

# Соединяемся с контейнером 'my-redis' внутри сети Докера
db = redis.Redis(host='my-redis', port=6379, decode_responses=True)

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Увеличиваем счетчик
            visits = db.incr('counter')
        except redis.ConnectionError:
            visits = "ОШИБКА! Нет связи с Redis"

        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        
        message = f"<h1>Сборка от Jenkins Автоматизирована!</h1><p>Ты посетитель номер: <b>{visits}</b></p>"
        self.wfile.write(message.encode('utf-8'))

print("Сервер запущен...")
HTTPServer(('0.0.0.0', 8000), SimpleHandler).serve_forever()
