from typing import Generic, ParamSpec
from dramatiq_mcls.task.meta import TaskMeta


_Args = ParamSpec("_Args")


class Task(Generic[_Args], metaclass=TaskMeta):
    class Options:
        abstract = True
        queue_name = "brokerge"

    @classmethod
    def handle(cls, *args: _Args.args, **kwargs: _Args.kwargs) -> None:
        raise NotImplementedError("Реализуйте метод `handle` в подклассах.")

    def run(self, *args: _Args.args, **kwargs: _Args.kwargs) -> None:
        # Задается в mcls
        try:
            type(self).actor().send(*args, **kwargs)
        except AttributeError:
            raise AttributeError("хде актор iбать")
