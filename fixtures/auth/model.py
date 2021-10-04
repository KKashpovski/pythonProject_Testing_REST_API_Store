"""Model for authorization."""

from faker import Faker
import attr
from fixtures.base import BaseClass

fake = Faker()


@attr.s
class Auth(BaseClass):
    """Input data for authorization."""
    username: str = attr.ib(default=None)
    password: str = attr.ib(default=None)

    @staticmethod
    def random():
        """Random data for authorization."""
        return Auth(username=fake.email(), password=fake.password())


@attr.s
class AuthResponse:
    """Output data after authorization."""
    access_token: str = attr.ib()


@attr.s
class AuthUserType:
    header: dict = attr.ib()  # return as token after authorization
    uuid: int = attr.ib()  # return after registration
