from prometheus_client import start_http_server, Counter
import time

# Create a metric to track the number of requests
REQUESTS = Counter('hello_world_requests_total', 'Total number of hello world requests')

def app():
    while True:
        REQUESTS.inc()
        time.sleep(1)

if __name__ == '__main__':
    start_http_server(8000)  # Exposes metrics at http://localhost:8000/metrics
    app()
