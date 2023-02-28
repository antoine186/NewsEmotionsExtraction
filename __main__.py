import sys
from DependenciesResources.containers import Container

from DependenciesResources.resources_paths import ResourcesPath
from dependency_injector.wiring import inject, Provide

if __name__ == "__main__":

    container = Container()
    container.wire(modules=[sys.modules[__name__]])

    paths = Container.resources_path()
    nns = Container.neural_networks()
