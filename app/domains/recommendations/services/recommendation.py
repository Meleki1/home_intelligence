from app.domains.recommendations.schemas.recommendation import RecommendationSchema


class RecommendationService:
    async def recommend(
        self,
        user_input: str,
        image_uploaded: bool = False,
    ) -> RecommendationSchema:

        if image_uploaded:
            return RecommendationSchema(
                title="Use uploaded image",
                description=(
                    "We'll use the uploaded "
                    "image to better understand "
                    "your situation."
                ),
            )

        return RecommendationSchema(
            title="Provide more information",
            description=(
                "Providing additional "
                "information may help us "
                "better understand the "
                "situation."
            ),
        )
