import random
from typing import Any

from app.domains.AI.schemas.llm import LLMResponseSchema
from app.domains.chat.enums.enum import Intent, NextBestStep
from app.domains.decision.schemas.decision import DecisionSchema
from app.domains.recommendations.schemas.recommendation import RecommendationSchema

GREETING_RESPONSES = [
    "Hello! I'm HOME AI OS. How can I help you today?",
    "Hello! It's nice hearing from you. How can I assist you today?",
    "Welcome! I'm HOME AI OS. What would you like help with today?",
]

APPRECIATION_RESPONSES = [
    "You're welcome! I'm always happy to help.",
    "I'm glad I could help. Please let me know if there's anything else I can do for you.",
]

DEFAULT_RESPONSE = (
    "I'm here to help with anything related to your home. "
    "Could you tell me a bit more about what you need?"
)

SIMPLE_INTENTS = {
    Intent.GREETING.value,
    Intent.APPRECIATION.value,
}

ISSUE_INTENTS = {
    Intent.HOME_ISSUE.value,
    Intent.QUESTION.value,
    Intent.GENERAL_HELP.value,
    Intent.PRICE_REQUEST.value,
    Intent.CONTINUE_CONVERSATION.value,
    Intent.UNKNOWN.value,
}


def build_response(
    llm_response: LLMResponseSchema,
    understanding: dict[str, Any] | None = None,
) -> str:
    intent = llm_response.intent

    if intent == Intent.GREETING.value:
        return random.choice(GREETING_RESPONSES)

    if intent == Intent.APPRECIATION.value:
        return random.choice(APPRECIATION_RESPONSES)

    parts: list[str] = []

    if llm_response.summary:
        parts.append(llm_response.summary)

    if understanding:
        image_analysis = understanding.get("image_analysis")
        if image_analysis:
            parts.append(image_analysis.summary)

        recommendation = understanding.get("recommendations")
        if isinstance(recommendation, RecommendationSchema):
            parts.append(recommendation.description)

        next_steps = understanding.get("next_best_step") or []
        if next_steps:
            parts.append(next_steps[0])

        if intent in ISSUE_INTENTS:
            unknown_context = understanding.get("unknown_context") or []
            if unknown_context:
                questions = "\n".join(
                    f"- {question.strip().capitalize()}"
                    for question in unknown_context[:2]
                )
                parts.append(f"To help further:\n{questions}")

    if parts:
        return "\n\n".join(parts)

    return DEFAULT_RESPONSE


def resolve_next_best_step(
    understanding: dict[str, Any] | None,
) -> str | None:
    if not understanding:
        return None

    next_steps = understanding.get("next_best_step") or []
    if next_steps:
        next_step = next_steps[0].lower()
        if "picture" in next_step or "image" in next_step or "upload" in next_step:
            return NextBestStep.UPLOAD_IMAGE.value
        if "information" in next_step or "provide" in next_step:
            return NextBestStep.ASK_MORE_QUESTIONS.value

    decision = understanding.get("decision")
    if isinstance(decision, DecisionSchema):
        if decision.next_action == "ANALYZE_IMAGE":
            return NextBestStep.UPLOAD_IMAGE.value
        if decision.next_action == "CONTINUE_CONVERSATION":
            return NextBestStep.ASK_MORE_QUESTIONS.value

    return NextBestStep.CONTINUE_CONVERSATION.value
