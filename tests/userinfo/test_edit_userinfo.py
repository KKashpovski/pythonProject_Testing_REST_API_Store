"""Tests for edit user info."""


import allure
from fixtures.constants import ResponseText
from fixtures.user_info.model import AddUserInfo


@allure.feature("edit user info with valid data")
class TestEditUserInfo:
    @allure.story("Изменение пользовательской информации с валидными данными")
    def test_edit_user_info(self, app, user_info):
        """
        Steps.

            1. Login user with valid data
            2. Try edit user info
            3. Check that status code is 200
            4. Check response
        """
        data = AddUserInfo.random()
        res = app.user_info.update_user_info(
            uuid=user_info.user_uuid, data=data, header=user_info.header
        )
        assert res.status_code == 200, "Check status code"
        assert res.data.message == ResponseText.MESSAGE_UPDATE_USER_INFO

    @allure.story("Изменение несуществующей пользовательской информации")
    def test_edit_nonex_user_info(self, app, auth_user):
        """
        Steps.

            1. Login user with valid data for nonexistent user info
            2. Try edit user info
            3. Check that status code is 400
            4. Check response
        """
        data = AddUserInfo.random()
        res = app.user_info.update_user_info(
            uuid=auth_user.user_uuid, data=data, header=auth_user.header
        )
        assert res.status_code == 404, "Check status code"
        assert res.data.message == ResponseText.MESSAGE_INFO_NOT_FOUND_DOT
