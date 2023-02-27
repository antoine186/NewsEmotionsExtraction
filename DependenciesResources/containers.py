"""Containers module."""
from dependency_injector import containers, providers
from .resources_paths import *

class Container(containers.DeclarativeContainer):
    resources_path = providers.Singleton(
        ResourcesPath,
        './NeuralNetworks/t5-base-finetuned-emotion/pytorch_model.bin',
        './NeuralNetworks/t5-base-finetuned-emotion/',
    )