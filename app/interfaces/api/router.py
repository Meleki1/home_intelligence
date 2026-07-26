from fastapi import APIRouter
from app.interfaces.api.health import router as health_router
from app.interfaces.api.chat import router as chat_router
from app.interfaces.api.vision import router as vision_router

api_router = APIRouter()

api_router.include_router(
    health_router,
    prefix="/health",
    tags=["Health"],
)

api_router.include_router(
    chat_router
)

api_router.include_router(
    vision_router,
    prefix="/vision",
    tags=["Vision"],
)

"""app.include_router(
    telegram_router,
    prefix="/webhooks",
    tags=["Telegram"],
)"""