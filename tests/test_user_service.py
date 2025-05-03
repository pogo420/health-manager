"""Set of unit test cases for user service
"""
import pytest
from health_manager.user.exceptions import UserIdDataException, UserInvalidException
from health_manager.user.service import UserService
from unittest.mock import patch
from tests.data import validUserDataPayload


def test_get_user_invalid_user_id():
    """Unit test for validating invalid user id,
    In get_user of service. It must raise UserInvalidException
    """

    with pytest.raises(UserInvalidException):
        UserService(None).get_user("")


@patch("health_manager.user.service.UserRepository.get_user")
def test_get_user_valid_user_id(mock_get_user):
    """Unit test for validating valid user id,
    In get_user of service it must query to db if valid user id
    """
    UserService(None).get_user("dummy-9089")
    # validating for db calls
    mock_get_user.assert_called_once()


@patch("health_manager.user.service.generate_user_id")
def test_invalid_user_in_adding_user(mock_user_id_gen):
    """Unit test for validating invalid user id should terminate the db update
    """
    mock_user_id_gen.return_value = None
    with pytest.raises(UserIdDataException):
        UserService(None).add_user(validUserDataPayload)


@patch("health_manager.user.service.UserRepository.add_user")
@patch("health_manager.user.service.generate_user_id")
def test_valid_user_id_should_add_user(mock_user_id_gen, mock_add_user):
    """Unit test for validating. With valid user id,
    data should be updated in the db.
    """
    # mocking the user id
    mock_user_id_gen.return_value = "dummy-12345"
    UserService(None).add_user(validUserDataPayload)
    # validating for db calls
    mock_add_user.assert_called_once()


@pytest.mark.skip
def test_invalid_user_id_in_delete():
    pass


@pytest.mark.skip
def test_valid_user_id_in_delete():
    pass
