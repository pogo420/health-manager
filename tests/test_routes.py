from health_manager.main import app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_root():
    """Testing the root route"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json().get("message") is not None
