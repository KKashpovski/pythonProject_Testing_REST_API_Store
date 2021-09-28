import allure
import pytest

from fixtures.constants import ResponseText
from fixtures.register.model import RegisterUser, RegisterUserResponse
from fixtures.auth.model import Auth
from fixtures.user_info.model import AddUserInfo


class TestAddUserInfo:
    @allure.feature("add user info with valid data")
    @allure.story("Добавление пользовательской информации с валидными данными")
    def test_add_user_info(self, app, auth_user):
        """
        Steps.

            1. Login user with valid data
            2. Try add user info
            3. Check that status code is 200
            4. Check response
        """
        data = AddUserInfo.random()
        res = app.user_info.add_user_info(
            uuid=auth_user.user_uuid, data=data, header=auth_user.header
        )
        assert res.status_code == 200, "Check status code"
        assert res.data.message == ResponseText.MESSAGE_ADD_USER_INFO
