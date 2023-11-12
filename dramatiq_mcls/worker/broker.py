from dramatiq.brokers.rabbitmq import RabbitmqBroker
from .known_tasks import _known_tasks
from . import wiring as _


_broker = RabbitmqBroker(url="amqp://guest:guest@localhost:5672")
for task in _known_tasks:
    _broker.declare_actor(task.actor())

