import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from src.users.v1.crud import UserCRUD
from tests.users.v1.factories import UserFactory


@pytest.mark.users
@pytest.mark.crud
async def test_get_all_users_empty_db(async_session: AsyncSession):
    users = UserCRUD(session=async_session)
    users = await users.get_all_users()
    assert len(users) == 0


@pytest.mark.users
@pytest.mark.crud
async def test_get_all_users_not_empty_db(async_session: AsyncSession):
    await UserFactory.create()
    users = UserCRUD(session=async_session)

    users = await users.get_all_users()
    assert len(users) == 1
