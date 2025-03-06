from flask import Flask
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time

app = Flask(__name__)

# Define Prometheus metrics
REQUEST_COUNT = Counter("http_requests_total", "Total HTTP Requests", ["endpoint"])
REQUEST_LATENCY = Histogram("http_request_latency_seconds", "Latency of HTTP Requests", ["endpoint"])

@app.route('/')
def home():
    start_time = time.time()
    REQUEST_COUNT.labels(endpoint="/").inc()  # Increment request counter
    response = "Hello, World! Your Jenkins-Docker integration is successful!"
    REQUEST_LATENCY.labels(endpoint="/").observe(time.time() - start_time)  # Measure latency
    return response

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
