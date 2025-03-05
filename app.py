from flask import Flask
from prometheus_client import start_http_server, Counter
import time

app = Flask(__name__)

# Create a metric to track the number of requests
REQUESTS = Counter('hello_world_requests_total', 'Total number of hello world requests')

@app.route('/')
def hello_world():
    REQUESTS.inc()  # Increment the request counter
    return 'Hello, World! This is your page with Prometheus metrics!'

if __name__ == '__main__':
    # Start Prometheus metrics server on port 8000
    start_http_server(8082)
    # Start Flask app on port 8081
    app.run(debug=True, host='0.0.0.0', port=8081)
