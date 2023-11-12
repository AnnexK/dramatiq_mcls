from .base_task import Task


class Starege(Task[[]]):
    @classmethod
    def handle(cls) -> None:
        print("starege")
