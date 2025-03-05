from flask import Flask
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from prometheus_client import CollectorRegistry
from flask import Response

app = Flask(__name__)

# Define a Prometheus Counter metric
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests', ['method', 'endpoint'])

@app.route('/')
def hello():
    REQUEST_COUNT.labels(method='GET', endpoint='/').inc()  # Increment the counter
    return "Hello, World! Your Jenkins-Docker-Prometheus integration is successful!"

@app.route('/metrics')
def metrics():
    registry = CollectorRegistry()
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
