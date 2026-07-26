from app.domains.decision.schemas.decision import(
    DecisionSchema
)


class DecisionService:


    async def decide(

        self,

        image_uploaded:bool=False

    )->DecisionSchema:


        if image_uploaded:

            return(

                DecisionSchema(

                    next_action=(

                        "ANALYZE_IMAGE"

                    ),

                    reason=(

                        "An image has been "
                        "provided for further "
                        "understanding."

                    )

                )

            )


        return(

            DecisionSchema(

                next_action=(

                    "CONTINUE_CONVERSATION"

                ),

                reason=(

                    "Additional understanding "
                    "may be helpful."

                )

            )

        )