from pydantic import BaseModel, EmailStr


class JWTOut(BaseModel):
    token: str


class UserLoginIn(BaseModel):
    email: EmailStr
    password: str
