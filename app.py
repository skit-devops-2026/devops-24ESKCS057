from flask import Flask, jsonify

app = Flask(__name__)


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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)