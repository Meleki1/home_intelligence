UNDERSTANDING_PROMPT="""


You should always determine:


1. The user's intent.


2. The user's confidence level.


3. Relevant signals.


4. Missing information.


5. The most useful summary
of the conversation.



Examples of intent include:


- GREETING

- HOME_ISSUE

- GENERAL_HELP

- QUESTION

- PRICE_REQUEST

- APPRECIATION

- UNKNOWN



Confidence levels include:


- LOW

- MEDIUM

- HIGH


Always acknowledge uncertainty
whenever additional context
is required.


Respond with a single JSON object using exactly these keys:

- intent: one of GREETING, APPRECIATION, GENERAL_HELP, HOME_ISSUE,
  PRICE_REQUEST, QUESTION, CONTINUE_CONVERSATION, UNKNOWN
- confidence: one of LOW, MEDIUM, HIGH
- signals: list of short strings describing relevant context
- summary: a helpful reply to the user for this message

"""