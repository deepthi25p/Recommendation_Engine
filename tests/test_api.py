from fastapi.testclient import (
    TestClient
)

from api.app import app

client = TestClient(app)

headers = {
    "x-api-key": "secret123"
}


def test_health():

    response = client.get(
        "/health"
    )

    assert response.status_code == 200


def test_recommend():

    response = client.get(
        "/recommend/1",
        headers=headers
    )

    assert response.status_code == 200


def test_metrics():

    response = client.get(
        "/metrics"
    )

    assert response.status_code == 200