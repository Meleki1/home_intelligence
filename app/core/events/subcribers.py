from abc import ABC, abstractmethod
from app.core.events.base import BaseEvent


class subscriber(ABC):
    @abstractmethod
    async def listen(self, event:BaseEvent)->None:
        pass