from fastapi import APIRouter
from fastapi import Depends
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_session
from app.domains.home.schemas.home_creation import CreateHomeSchema, HomeCreationResponse
from app.domains.home.services.home_creation import HomeCreationService

router = APIRouter(prefix="/home", tags=["Homes"])

@router.post("/", response_model=(HomeCreationResponse))
async def create_home(
    data:CreateHomeSchema,
    session:Annotated[
        AsyncSession,
        Depends(
            get_session
        )
    ]
):
    service = (
        HomeCreationService(
            session
        )
    )

    home = await(
        service.create_home(
            data
        )
    )

    return(
        HomeCreationResponse(
            success=True,
            message=(
                "Home created successfully."
            ),

            home=home
        )
    )