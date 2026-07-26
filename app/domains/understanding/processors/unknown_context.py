class UnknownContextProcessor:
    @staticmethod
    async def process(user_input:str)->list[str]:
        return [
            (
                "Which area of the house "
                "is affected?"
            ),

            (
                "how long has this been happening?"
            )
        ]