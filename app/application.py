from fastapi import FastAPI
from app.core.lifecycle import lifespan
from app.config.settings import get_settings
from app.interfaces.api.router import api_router


def create_app() -> FastAPI:
    """
    Application Factory

    responsible for creating and configuring the FastAPI application
    """

    settings = get_settings()

    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        lifespan=lifespan,
    )

    app.include_router(api_router)

    return app