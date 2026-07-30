from app.domains.planning.schemas import (
    Plan,
    PlanAction,
)
import logging

logger = llogger = logging.getLogger(__name__)


class PlannerService:

    async def plan(
        self,
        state,
        cognition,
    ) -> Plan:

        missing = []

        if not state.image_received:
            missing.append("image")

        if not state.affected_area:
            missing.append("affected_area")

        if not state.duration:
            missing.append("duration")

        if missing:

            return Plan(
                next_action=PlanAction.ASK_FOLLOW_UP,
                missing_information=missing,
                ask_for_image="image" in missing,
                priority="HIGH",
            )

        logger.info("Plan: %s", Plan.model_dump())

        if cognition.confidence == "LOW":

            return Plan(
                next_action=PlanAction.BOOK_EXPERT,
                recommend_booking=True,
                priority="HIGH",
            )
        
        return Plan(
            next_action=PlanAction.PROVIDE_GUIDANCE,
        )

        