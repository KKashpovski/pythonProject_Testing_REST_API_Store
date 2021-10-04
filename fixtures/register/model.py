"""Model for registration."""


from faker import Faker
import attr
from fixtures.base import BaseClass

fake = Faker()


@attr.s
class RegisterUser(BaseClass):
    """Input data for registration."""
    username: str = attr.ib(default=None)
    password: str = attr.ib(default=None)

    @staticmethod
    def random():
        """Random data for registration."""
        return RegisterUser(username=fake.email(), password=fake.password())


@attr.s
class RegisterUserResponse:
    """Output data after registration."""
    message: str = attr.ib()
    uuid: int = attr.ib()
