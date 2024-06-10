from fastapi import APIRouter
from .user.user_controller import user_controller
from .auth.auth_controller import auth_router


router = APIRouter()

# Ruta prueba
@router.get("/test", tags=["Test"])
async def test_api():
    return {"message": "API works!"}

# Ruta endpoints
@router.get("/", tags=["Endpoints"])
async def test_api():
    return {
        "endpoints": {
            "users": "/user/users/<id>",
            "signup": "/user/signup",
            "login": "/user/login",
            "logout": "/user/logout"
        }
    }

# Incluyendo routers de otros módulos
router.include_router(user_controller, prefix="/user", tags=["Auth"])
router.include_router(auth_router, prefix="/user", tags=["Auth"])