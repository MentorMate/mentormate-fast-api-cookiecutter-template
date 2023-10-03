from decouple import config
from pydantic_settings import BaseSettings


class JWTSettings(BaseSettings):
    SECRET_KEY: str = config('SECRET_KEY', cast=str)
    JWT_ACCESS_TOKEN_LIFETIME_MINUTES: int = config('JWT_ACCESS_TOKEN_LIFETIME_MINUTES', cast=int)
    JWT_ALGORITHM: str = config('JWT_ALGORITHM', cast=str)
