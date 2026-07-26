class NextBestStepProcessor:
    @staticmethod
    async def process(user_input: str)->list[str]:
        if "insect" in user_input:
            
            return [
                (
                    "Uploading a picture would "
                    "help us better understand "
                    "the situation."
                )
            ]
        
        
        return[
            (
                "Please provide additional "
                "information so we can better "
                "understand the situation."
            )
        ]

            