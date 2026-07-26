class CurrentKnowledgeProcessor:
    @staticmethod
    async def process(user_input:str)->list[str]:
        return [
            f"You reported: {user_input}"
        ]