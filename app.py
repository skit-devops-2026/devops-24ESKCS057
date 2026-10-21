from flask import Flask, jsonify, request, Response
import os
import time
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Prometheus metrics
REQUEST_COUNT = Counter('app_requests_total', 'Total request count', ['method', 'endpoint'])
REQUEST_LATENCY = Histogram('app_request_latency_seconds', 'Request latency in seconds', ['method', 'endpoint'])

@app.before_request
def start_timer():
    request.start_time = time.time()

@app.after_request
def record_metrics(response):
    if hasattr(request, 'start_time'):
        resp_time = time.time() - request.start_time
        REQUEST_COUNT.labels(request.method, request.path).inc()
        REQUEST_LATENCY.labels(request.method, request.path).observe(resp_time)
    return response


@app.get("/")
def home():
    return "Welcome to ShopEase!"


@app.get("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.get("/products")
def products():
    return jsonify([
        {"id": 1, "name": "Laptop", "price": 55000},
        {"id": 2, "name": "Headphones", "price": 2500},
        {"id": 3, "name": "Keyboard", "price": 1500}
    ])
@app.get("/cart")
def cart():
    return jsonify({
        "items": [
            {"product_id": 1, "quantity": 1},
            {"product_id": 2, "quantity": 2}
        ],
        "total": 60000
    })
@app.get("/orders")
def orders():
    return jsonify([
        {
            "id": 1,
            "product": "Laptop",
            "quantity": 1,
            "status": "Confirmed"
        },
        {
            "id": 2,
            "product": "Headphones",
            "quantity": 2,
            "status": "Shipped"
        }
    ])
@app.get("/search")
def search():
    query = request.args.get("q", "").lower()

    products_list = [
        {"id": 1, "name": "Laptop", "price": 55000},
        {"id": 2, "name": "Headphones", "price": 2500},
        {"id": 3, "name": "Keyboard", "price": 1500}
    ]

    results = [
        product for product in products_list
        if query in product["name"].lower()
    ]

    return jsonify(results)

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)