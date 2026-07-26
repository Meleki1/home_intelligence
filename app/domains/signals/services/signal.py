from app.domains.signals.schemas.signal import SignalSchema
from enum import Enum


class SignalService:
    async def generate(self, signal_type:str, value:str)->SignalSchema:
        return(
            SignalSchema(
                signal_type=signal_type,
                value=value
            )
        )




class Signal(Enum):

    PEST_RELATED="PEST_RELATED"

    WATER_RELATED="WATER_RELATED"

    SEEKING_HELP="SEEKING_HELP"

    LOW_URGENCY="LOW_URGENCY"

    HIGH_URGENCY="HIGH_URGENCY"

    IMAGE_RECOMMENDED=(
        "IMAGE_RECOMMENDED"
    )

    PRICE_REQUEST="PRICE_REQUEST"

    PROFESSIONAL_INTENT=(
        "PROFESSIONAL_INTENT"
    )