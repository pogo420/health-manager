from health_manager.main import app
from fastapi.testclient import TestClient
from unittest.mock import patch
from tests.test_data import ValidUserDataFromServer

client = TestClient(app)


def test_root():
    """Testing the root route"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json().get("message") is not None


@patch('user.service.UserService.get_user', return_value=None)
def test_user_get_none_response(mock_get_user):
    """Testing get user route"""
    response = client.get("/user/sam32")
    assert response.status_code == 200
    assert response.json() is None


@patch('user.service.UserService.get_user', return_value=ValidUserDataFromServer())
def test_user_get_valid_response(mock_get_user):
    """Testing get user route"""
    response = client.get("/user/sam32")
    assert response.status_code == 200
    assert response.json() is None
