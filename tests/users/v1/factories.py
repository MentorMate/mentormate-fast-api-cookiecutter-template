import factory

from src.security import get_password_hash
from src.users.v1.models import User
from src.utils import AsyncFactory

TEST_USERS_DEFAULT_PASSWORD = 'TestPass123!'


class UserFactory(AsyncFactory):
    class Meta:
        model = User
        sqlalchemy_session = None

    id = factory.Faker('uuid4')
    email = factory.Sequence(lambda n: f'user{n}@example.com')
    password = factory.LazyFunction(
        lambda: get_password_hash(
            TEST_USERS_DEFAULT_PASSWORD
        )
    )
