from dramatiq_mcls.container.stuff_container import StuffContainer


stuff = StuffContainer()
stuff.init_resources()
stuff.wire(
    packages=["dramatiq_mcls.task"],
)
