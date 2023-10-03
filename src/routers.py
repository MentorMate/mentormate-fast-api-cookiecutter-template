from src.users.v1.routers import router as users_v1
from src.auth.jwt.v1.routes import router as jwt_v1

routers = [
    jwt_v1,
    users_v1
]
