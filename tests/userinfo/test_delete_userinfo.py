"""Tests for delete user info."""


import allure
from fixtures.constants import ResponseText


@allure.feature("delete user info")
class TestDelUserInfo:
    @allure.story("Удаление пользовательской информации")
    def test_del_user_info(self, app, user_info):
        """
        Steps.

            1. Login user with valid data
            2. Try delete user
            3. Check that status code is 200
            4. Check response
        """
        res = app.user_info.delete_user_info(
            uuid=user_info.user_uuid, header=user_info.header
        )
        assert res.status_code == 200, "Check status code"
        assert res.data.message == ResponseText.MESSAGE_DELETE_USER_INFO
