from dependency_injector.wiring import inject, Provide
from dramatiq_mcls.task.base_task import Task
from dramatiq_mcls.stuff.printer import Printer
from dramatiq_mcls.container.stuff_container import StuffContainer


class Jokerge(Task[[]]):
    @classmethod
    @inject
    def handle(cls, printer: Printer = Provide[StuffContainer.printer]) -> None:
        printer.print("jokerge")
