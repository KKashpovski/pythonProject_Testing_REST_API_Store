"""Create objects from StoreApp."""


from fixtures.auth.api import AuthUser
from fixtures.register.api import Register
from fixtures.requests import Client
from fixtures.user_info.api import UserInfo


class StoreApp:
    def __init__(self, url):
        self.url = url
        self.client = Client
        self.register = Register(self)
        self.auth = AuthUser(self)
        self.user_info = UserInfo(self)
        # self.store = Store(self)
        # self.item = Item(self)
        # self.items = Items(self)
        # self.balance = Balance(self)
        # self.pay = Pay(self)
