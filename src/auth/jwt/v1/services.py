from datetime import datetime, timedelta
from typing import Union, Any

from jose import jwt

from src.config import get_settings


def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    settings = get_settings()

    if expires_delta is not None:
        expires_delta = datetime.utcnow() + timedelta(minutes=expires_delta)
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=settings.JWT_ACCESS_TOKEN_LIFETIME_MINUTES)

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, settings.JWT_ALGORITHM)
    return encoded_jwt
