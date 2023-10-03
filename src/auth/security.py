import bcrypt
from fastapi.security import OAuth2PasswordBearer

# Salt rounds for bcrypt (adjust as needed, higher values are more secure but slower)
BCRYPT_ROUNDS = 12

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/jwt/obtain-token")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    # Use bcrypt to verify the password
    return bcrypt.checkpw(
        plain_password.encode('utf-8'), hashed_password.encode('utf-8')
    )


def get_password_hash(password: str) -> str:
    # Hash the password using bcrypt
    hashed_password = bcrypt.hashpw(
        password.encode('utf-8'), bcrypt.gensalt(BCRYPT_ROUNDS)
    )
    return hashed_password.decode('utf-8')
