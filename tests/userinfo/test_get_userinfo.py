"""Tests for get user info."""


import allure


@allure.feature("get user info")
class TestGetUserInfo:
    @allure.story("Отображение пользовательской информации")
    def test_get_user_info(self, app, user_info):
        """
        Steps.

            1. Login user with valid data
            2. Try get user
            3. Check that status code is 200
            4. Check response
        """
        res = app.user_info.get_user_info(
            uuid=user_info.user_uuid, header=user_info.header
        )
        assert res.status_code == 200, "Check status code"
        assert res.data.city == user_info.user_info.address.city, "Check city"
        assert res.data.street == user_info.user_info.address.street, "Check street"
        assert res.data.email == user_info.user_info.email, "Check email"
