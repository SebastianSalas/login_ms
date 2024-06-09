from fastapi import APIRouter
from .user.user_controller import user_controller
from .auth.auth_controller import auth_router


router = APIRouter()

# Ruta prueba
@router.get("/test", tags=["Test"])
async def test_api():
    return {"message": "API works!"}

# Incluyendo routers de otros módulos
router.include_router(user_controller, prefix="/user", tags=["Auth"])
router.include_router(auth_router, prefix="/user", tags=["Auth"])