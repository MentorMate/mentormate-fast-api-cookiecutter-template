from fastapi import APIRouter, Depends, status, HTTPException

from src.auth.jwt.v1.schemas import JWTOut, UserLoginIn
from src.auth.jwt.v1.services import create_access_token
from src.users.v1.dependencies import get_users_service
from src.users.v1.models import User
from src.users.v1.services import UserService

router = APIRouter(
    prefix="/api/v1",
    tags=["auth"]
)


@router.post("/jwt/obtain-token", response_model=JWTOut)
async def obtain_jwt_token(user_data: UserLoginIn, user_service: UserService = Depends(get_users_service)):
    user: User = await user_service.authenticate(**user_data.model_dump())

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    return {
        "token": create_access_token(user.email)
    }
