from app.domains.timeline.schemas.timeline import CreateTimelineSchema

class TimelineCreationValidator:

    @staticmethod
    def validate(data:CreateTimelineSchema)->None:
        TimelineCreationValidator.validate_event_type(
            data.event_type
        )

        TimelineCreationValidator.validate_event_name(
            data.event_name
        )

        TimelineCreationValidator.validate_state(
            data.state
        )

        TimelineCreationValidator.validate_description(
            data.description
        )

    @staticmethod
    def validate_event_type(event_type:str)->None:
        if not event_type.strip():
            raise(
                ValueError(
                    "Event type cannot be empty."
                )
            )

    @staticmethod
    def validate_event_name(event_name:str)->None:
        if not event_name.strip():
            raise(
                ValueError(
                    "Event name cannot be empty."
                )
            )

    @staticmethod
    def validate_state(state:str)->None:
        if not state.strip():
            raise(
                ValueError(
                    "State cannot be empty."
                )
            )

    @staticmethod
    def validate_description(description:str)->None:
        if not description.strip():
            raise(
                ValueError(
                    "Description cannot be empty."
                )
            )

