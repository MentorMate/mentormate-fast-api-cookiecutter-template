from uuid import UUID

from pydantic import BaseModel, EmailStr, ConfigDict


class BaseUser(BaseModel):
    email: EmailStr


class UserCreateIn(BaseUser):
    password: str


class UserCreateOut(BaseUser):
    model_config = ConfigDict(from_attributes=True)

    id: UUID

