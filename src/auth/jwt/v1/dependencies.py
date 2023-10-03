from typing import Annotated, List

from fastapi import Depends
from jose import jwt, JWTError

from src.auth.jwt.v1.exeptions import credentials_exception
from src.auth.security import oauth2_scheme
from src.config import get_settings
from src.users.v1.crud import UserCRUD
from src.users.v1.dependencies import get_users_crud
from src.users.v1.models import User


async def get_current_user(
        token: Annotated[str, Depends(oauth2_scheme)],
        users_crud: UserCRUD = Depends(get_users_crud)
):
    settings = get_settings()

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception
    users: List[User] = await users_crud.get_users_by_email(email=email)

    if users is None:
        raise credentials_exception
    return users[0]
