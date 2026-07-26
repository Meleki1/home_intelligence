

from app.domains.AI.products.pest_control.keywords import(
    PEST_KEYWORDS
)

from app.domains.AI.products.pest_control.prompt import(
    PEST_CONTROL_PROMPT
)


def can_handle(

    message:str

)->bool:


    return any(

        keyword in

        message.lower()

        for keyword in

        PEST_KEYWORDS

    )



def get_prompt()->str:

    return(

        PEST_CONTROL_PROMPT
    )