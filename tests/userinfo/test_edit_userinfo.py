import allure

from fixtures.constants import ResponseText
from fixtures.user_info.model import AddUserInfo


class TestEditUserInfo:
    @allure.feature("edit user info with valid data")
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
