"""Containers module."""
from dependency_injector import containers, providers
from .resources_paths import *
from NeuralNetworks.TokenizerBasedNeuralNetwork import TokenizerBasedNeuralNetwork
from NeuralNetworks.PipelineBasedNeuralNetwork import PipelineBasedNeuralNetwork
import torch
from transformers import AutoTokenizer, AutoModelWithLMHead, pipeline

# tokenizer_emo_classification_nn_model_path = './NeuralNetworks/t5-base-finetuned-emotion/'
pipeline_emo_classification_nn_model_path = "./NeuralNetworks/emotion-english-distilroberta-base"

pipeline_emo_classification_nn_model = pipeline("text-classification", model = pipeline_emo_classification_nn_model_path, return_all_scores = True)

# tokenizer_emo_classification_nn_model = AutoModelWithLMHead.from_pretrained(tokenizer_emo_classification_nn_model_path)
# main_emo_classification_nn_tokenizer = AutoTokenizer.from_pretrained(tokenizer_emo_classification_nn_model_path)

class Container(containers.DeclarativeContainer):
    resources_path = providers.Singleton(
        ResourcesPath,
        pipeline_emo_classification_nn_model_path
    )

    """
    tokenizer_neural_network = providers.Singleton(
        TokenizerBasedNeuralNetwork,
        tokenizer_emo_classification_nn_model,
        main_emo_classification_nn_tokenizer,
    )
    """

    pipeline_neural_network = providers.Singleton(
        PipelineBasedNeuralNetwork,
        pipeline_emo_classification_nn_model
    )
