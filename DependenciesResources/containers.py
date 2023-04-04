"""Containers module."""
from dependency_injector import containers, providers
from .resources_paths import *
from NeuralNetworks.NeuralNetwork import NeuralNetwork
import torch
from transformers import AutoTokenizer, AutoModelWithLMHead

main_emo_classification_nn_model_path = './NeuralNetworks/t5-base-finetuned-emotion/'
main_emo_classification_nn_tokenizer_path = './NeuralNetworks/t5-base-finetuned-emotion/'

main_emo_classification_nn_model = AutoModelWithLMHead.from_pretrained(main_emo_classification_nn_model_path)
main_emo_classification_nn_tokenizer = AutoTokenizer.from_pretrained(main_emo_classification_nn_tokenizer_path)

class Container(containers.DeclarativeContainer):
    resources_path = providers.Singleton(
        ResourcesPath,
        main_emo_classification_nn_model_path,
        main_emo_classification_nn_tokenizer_path,
    )

    neural_networks = providers.Singleton(
        NeuralNetwork,
        main_emo_classification_nn_model,
        main_emo_classification_nn_tokenizer,
    )