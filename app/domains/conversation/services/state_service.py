from app.domains.conversation.models import ConversationState
from app.domains.conversation.repository import ConversationRepository
from app.domains.conversation.services.fact_extractor.schema import ExtractedFacts
from app.domains.vision_analysis.schemas.vision import VisionAnalysisResponse

class ConversationStateService:

    def __init__(
        self,
        repository: ConversationRepository,
    ):

        self.repository = repository

    async def load(self, conversation_id):

        state = await self.repository.get(conversation_id)

        if state:

            return state

        return ConversationState(
            conversation_id=conversation_id
        )

    async def save(self, state):

        await self.repository.save(state)

    async def merge(self, state: ConversationState, facts: ExtractedFacts,):

        if facts.affected_area:

            state.affected_area = facts.affected_area

            state.completed_questions.add("affected_area")

        if facts.duration:

            state.duration = facts.duration

            state.completed_questions.add("duration")

        if facts.symptoms:

            state.symptoms.extend(facts.symptoms)

    async def merge_image(self, state: ConversationState, image_analysis: VisionAnalysisResponse):
       
        if image_analysis:

            state.image_received = True

            state.image_summary = image_analysis.summary

            state.suspected_pest = image_analysis.detected_pest

            state.confidence = image_analysis.confidence.level

            state.completed_questions.add("image")

        return state

async def compute_missing(self, state: ConversationState):

    missing = []

    if not state.affected_area:

        missing.append(
            "affected_area"
        )

    if not state.duration:

        missing.append(
            "duration"
        )

    if not state.image_received:

        missing.append(
            "image"
        )

    return missing