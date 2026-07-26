from app.core.events.base import BaseEvent


class EventPublisher:

    def __init__(self):
        self.subscribers=[]

    def subscribe(self, subscriber)->None:

        self.subscribers.append(
            subscriber
        )

    async def publish(self, event:BaseEvent)->None:
        
        for subscriber in(
            self.subscribers
        ):

            try:
                await(
                    subscriber.listen(
                        event
                    )
                )
            except Exception:
                pass

        