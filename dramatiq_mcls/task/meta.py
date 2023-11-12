from typing import Any
from dramatiq import actor, Actor


class TaskMeta(type):
    def __new__(mcls, name: str, bases: tuple[type], attrs: dict[str, Any]) -> "TaskMeta":
        cls = super().__new__(mcls, name, bases, attrs)
        options = getattr(cls, "Options", object())
        
        if not getattr(options, "abstract", False):
            actor_options = mcls._assemble_options(cls)
            actor_options.pop("abstract", False)

            func = getattr(cls, "handle")
            actor_factory = actor_options.pop("actor_factory", actor)
            actor_instance = actor_factory(func, **actor_options)
            setattr(cls, "__actor__", actor_instance)

        setattr(options, "abstract", False)
        return cls

    @classmethod
    def _assemble_options(mcls, cls: "TaskMeta") -> dict[str, Any]:
        options: dict[str, Any] = {}
        for base in reversed(cls.mro()):
            base_options = getattr(base, "Options", object())
            for name in dir(base_options):
                if not name.startswith("_"):
                    options[name] = getattr(base_options, name)
        options["actor_name"] = f"{cls.__module__}:{cls.__qualname__}"
        return options

    def actor(cls) -> Actor:
        try:
            return cls.__actor__ # type: ignore
        except AttributeError:
            raise AttributeError("where actor")
