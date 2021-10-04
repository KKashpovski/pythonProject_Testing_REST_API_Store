"""Tests for add user info."""


import allure
import pytest
from fixtures.constants import ResponseText
from fixtures.user_info.model import AddUserInfo, Address


@allure.feature("add user info")
class TestAddUserInfo:
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

    @pytest.mark.xfail
    @pytest.mark.bug
    @allure.story("Добавление пользовательской информации с иным типом данных")
    def test_add_int_user_info(self, app, auth_user):
        """
        Steps.

            1. Login user with valid data
            2. Try add user info for phone, home number type integer
            3. Check that status code is 400
            4. Check response
        """
        data = AddUserInfo(89270000888, "fffff@gmail.com", Address("Boston", "park", 6))
        res = app.user_info.add_user_info(
            uuid=auth_user.user_uuid, data=data, header=auth_user.header
        )
        assert res.status_code == 400

