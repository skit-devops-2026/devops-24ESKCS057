from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to ShopEase!" in response.data


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_products():
    client = app.test_client()
    response = client.get("/products")
    assert response.status_code == 200
    assert len(response.json) == 3


def test_cart():
    client = app.test_client()
    response = client.get("/cart")
    assert response.status_code == 200
    assert response.json["total"] == 60000


def test_orders():
    client = app.test_client()
    response = client.get("/orders")
    assert response.status_code == 200
    assert len(response.json) == 2
    assert response.json[0]["status"] == "Confirmed"