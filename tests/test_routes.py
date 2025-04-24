"""Test cases collection of API routes
"""
from health_manager.main import app
from fastapi.testclient import TestClient
from unittest.mock import patch
from health_manager.user.exceptions import (
    UserIdDataException,
    UserInvalidException,
    UserReadException,
    UserWriteException
    )
from tests.data import (
    validUserDataFromServer,
    get_user_valid_response,
    validUserDataPayload
    )

client = TestClient(app)


def test_root():
    """Testing the root route"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json().get("message") is not None


@patch('health_manager.user.service.UserService.get_user')
def test_user_get_invalid_user_response(mock_get_user):
    """Testing get user route - invalid user respose case"""
    mock_get_user.side_effect = UserInvalidException
    response = client.get("/user/invalidid3245")
    assert response.status_code == 404
    assert response.json() is not None


@patch('health_manager.user.service.UserService.get_user')
def test_user_get_db_issue_response(mock_get_user):
    """Testing get user route - db issue case case"""
    mock_get_user.side_effect = UserReadException
    response = client.get("/user/invalidid3245")
    assert response.status_code == 500
    assert response.json() is not None


@patch('health_manager.user.service.UserService.get_user')
def test_user_get_valid_response(mock_get_user):
    """Testing get user route - valid response case"""
    mock_get_user.return_value = validUserDataFromServer
    response = client.get("/user/sam32")
    assert response.status_code == 200
    assert response.json() == get_user_valid_response


@patch('health_manager.user.service.UserService.add_user')
def test_invalid_user_id_generation(mock_user_add):
    """Test cases for invalid user id generation.
    Route should return error response
    """
    mock_user_add.side_effect = UserIdDataException
    response = client.post("/user", content=validUserDataPayload.model_dump_json())
    assert response.status_code == 500
    assert response.json() is not None


@patch('health_manager.user.service.UserService.add_user')
def test_issue_in_adding_user_into_db(mock_user_add):
    """Test cases for write query issues.
    Route should return error response
    """
    mock_user_add.side_effect = UserWriteException
    response = client.post("/user", content=validUserDataPayload.model_dump_json())
    assert response.status_code == 500
    assert response.json() is not None


@patch('health_manager.user.service.UserService.add_user')
def test_valid_adding_user_into_db(mock_user_add):
    """Test cases for valid write case.
    Route should return written data for user
    """
    mock_user_add.return_value = validUserDataFromServer
    response = client.post("/user", content=validUserDataPayload.model_dump_json())
    assert response.status_code == 200
    assert response.json() == get_user_valid_response
