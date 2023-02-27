import torch
from transformers import AutoTokenizer
import sys
from DependenciesResources.containers import Container

from DependenciesResources.resources_paths import ResourcesPath
from dependency_injector.wiring import inject, Provide

#model = torch.load('./NeuralNetworks/t5-base-finetuned-emotion/pytorch_model.bin', map_location=torch.device('cpu'))
#tokenizer = AutoTokenizer.from_pretrained('./NeuralNetworks/t5-base-finetuned-emotion/')

if __name__ == "__main__":

    container = Container()
    container.wire(modules=[sys.modules[__name__]])

    paths = Container.resources_path()
    print(paths.emotion_classification_nn_path)
