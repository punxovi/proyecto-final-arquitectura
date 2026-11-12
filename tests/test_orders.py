from fastapi.testclient import TestClient

from app.main import app, orders


client = TestClient(app)


def setup_function():
    orders.clear()


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_create_order_calculates_total():
    response = client.post(
        "/api/orders",
        json={
            "customer_name": "Ana Pérez",
            "items": [
                {"product_id": "P-1", "name": "Café", "quantity": 2, "unit_price": 1500},
                {"product_id": "P-2", "name": "Pan", "quantity": 1, "unit_price": 800},
            ],
        },
    )
    assert response.status_code == 201
    body = response.json()
    assert body["total"] == 3800
    assert body["status"] == "PENDIENTE"


def test_update_status_for_existing_order():
    created = client.post(
        "/api/orders",
        json={"customer_name": "Luis Soto", "items": [{"product_id": "P-1", "name": "Té", "quantity": 1, "unit_price": 1000}]},
    ).json()
    response = client.patch(f"/api/orders/{created['id']}/status?new_status=CONFIRMADO")
    assert response.status_code == 200
    assert response.json()["status"] == "CONFIRMADO"


def test_update_status_for_missing_order_returns_404():
    response = client.patch("/api/orders/no-existe/status?new_status=CONFIRMADO")
    assert response.status_code == 404
