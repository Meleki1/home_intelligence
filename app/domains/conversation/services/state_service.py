from app.domains.conversation.models import ConversationState
from app.domains.conversation.repository import ConversationRepository
from app.domains.conversation.services.fact_extractor.schema import ExtractedFacts
from app.domains.vision_analysis.schemas.vision import VisionAnalysisResponse
import logging

logger = llogger = logging.getLogger(__name__)



class ConversationStateService:

    def __init__(
        self,
        repository: ConversationRepository,
    ):

        self.repository = repository

    async def load(self, conversation_id:str):

        state = await self.repository.get(conversation_id)

        if state is None:

            state = ConversationState(
                conversation_id=conversation_id
            )
        return state

    async def save(self, state):

        await self.repository.save(state)

    async def merge_facts(self, state: ConversationState, facts: ExtractedFacts):


        if facts.affected_area:
            state.affected_area = facts.affected_area
            state.completed_questions.add("affected_area")

        if facts.duration:
            state.duration = facts.duration
            state.completed_questions.add("duration")
            
        if facts.suspected_pest:

            state.suspected_pest = facts.suspected_pest

        if facts.symptoms:

            for symptom in facts.symptoms:

                if symptom not in state.symptoms:

                    state.symptoms.add(
                        symptom
                    )
        logger.info("Conversation state: %s", state.model_dump())
    

    async def merge_image(self, state: ConversationState, image_analysis: VisionAnalysisResponse):
       
        if image_analysis:

            state.image_received = True

            state.image_summary = image_analysis.summary

            state.suspected_pest = image_analysis.possible_issue

            state.confidence = image_analysis.confidence.value

            state.completed_questions.add("image")

        print(type(state.completed_questions))
        print(state.completed_questions)


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
        logger.info("Conversation state: %s", state.model_dump())
        return missing

    

