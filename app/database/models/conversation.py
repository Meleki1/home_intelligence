"""from app.database.base import Base
class ConversationStateModel(Base):

    __tablename__ = "conversation_states"

    conversation_id = Column(
        UUID,
        primary_key=True,
    )

    affected_area = Column(String)

    duration = Column(String)

    occupants = Column(String)

    suspected_pest = Column(String)

    confidence = Column(String)

    image_received = Column(Boolean)

    image_summary = Column(Text)

    symptoms = Column(JSON)

    completed_questions = Column(JSON)"""