from typing import Protocol
from dramatiq import Actor
from dramatiq_mcls.task import Jokerge, Starege


class _ActorContainer(Protocol):
    def actor(self) -> Actor:
        ...

        
_known_tasks: list[_ActorContainer] = [
    Jokerge,
    Starege
]
