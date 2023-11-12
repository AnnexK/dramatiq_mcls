from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton
from dramatiq_mcls.stuff.printer import Printer


class StuffContainer(DeclarativeContainer):
    printer = Singleton(Printer)
