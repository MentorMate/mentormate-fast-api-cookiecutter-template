import random

import pytest
from fastapi import status
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from tests.users.v1.factories import UserFactory


@pytest.mark.users
async def test_all_users_listing_empty(
        async_client: AsyncClient,
        async_session: AsyncSession,
):
    # Arrange

    # Act
    response = await async_client.get("/api/v1/users")

    # Assert
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []


@pytest.mark.users
async def test_all_users_listing_not_empty(
        async_client: AsyncClient,
        async_session: AsyncSession,
):
    # Arrange
    user = await UserFactory.create()

    # Act
    response = await async_client.get("/api/v1/users")
    results = response.json()

    # Assert
    assert response.status_code == status.HTTP_200_OK
    assert len(results) == 1
    assert results[0] == {
        "id": str(user.id),
        "email": user.email
    }


async def test_all_users_listing_not_empty_filtered(
        async_client: AsyncClient,
        async_session: AsyncSession,
):
    # Arrange
    users = await UserFactory.create_batch(10)

    user_ids = list()
    for user in users:
        user_ids.append(str(user.id))

    random_user_id = random.choice(user_ids)

    # Act
    response = await async_client.get(
        f"/api/v1/users?user_id={random_user_id}"
    )
    results = response.json()

    # Assert
    assert response.status_code == 200
    assert len(results) == 1
    assert results[0]["id"] == random_user_id
