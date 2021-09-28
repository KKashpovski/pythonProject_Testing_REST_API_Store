import pytest
import allure
from fixtures.common_models import MessageResponse
from fixtures.constants import ResponseText
from fixtures.register.model import RegisterUser, RegisterUserResponse


class TestRegisterUser:
    @allure.feature("register user with valid data")
    @allure.story("Регистрация пользователя с валидными данными")
    def test_register_user_with_valid_data(self, app):
        """
        1. Try to register user with valid data
        2. Check that status code is 201
        3. Check response
        """
        data = RegisterUser.random()
        res = app.register.register(data=data, type_response=RegisterUserResponse)
        assert res.status_code == 201, "Check status code"
        assert res.data.message == ResponseText.MESSAGE_REGISTER_USER

    @allure.feature("register user with empty data")
    @allure.story("Попытка регистрации пользователя с пустыми полями")
    @pytest.mark.parametrize("field", ["username", "password"])
    def test_register_user_with_empty_data(self, app, field):
        """
        1. Try to register user with empty data
        2. Check that status code is 400
        3. Check response
        """
        data = RegisterUser.random()
        setattr(data, field, None)
        res = app.register.register(data=data, type_response=MessageResponse)
        assert res.status_code == 400, "Check status code"
        assert res.data.message == ResponseText.MESSAGE_USER_PASSWORD_REQUIRED
