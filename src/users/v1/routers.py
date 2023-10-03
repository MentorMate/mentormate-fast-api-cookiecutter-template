from typing import Optional, List, Annotated
from uuid import UUID

from fastapi import APIRouter, Depends

from src.auth.jwt.v1.dependencies import get_current_user
from src.users.v1.crud import UserCRUD
from src.users.v1.dependencies import get_users_crud, get_users_service
from src.users.v1.models import User
from src.users.v1.schemas import UserCreateIn, UserCreateOut
from src.users.v1.services import UserService

router = APIRouter(
    prefix="/api/v1",
    tags=["users"]
)


@router.get("/users", response_model=List[UserCreateOut])
async def get_users(
        user_id: Optional[UUID] = None,
        users: UserCRUD = Depends(get_users_crud)
):
    if user_id:
        return [await users.get_user_by_id(user_id)]

    return await users.get_all_users()


@router.post("/users", response_model=UserCreateOut)
async def create_user(
        user_data: UserCreateIn,
        user_service: UserService = Depends(get_users_service)
):
    return await user_service.create(**user_data.model_dump())


@router.get("/users/me", response_model=UserCreateOut)
async def get_current_user(
        current_user: Annotated[User, Depends(get_current_user)]
):
    return current_user
