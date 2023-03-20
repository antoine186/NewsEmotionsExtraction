from typing import OrderedDict
from transformers import T5TokenizerFast

class NeuralNetwork:
    nn_model: OrderedDict
    nn_tokenizer: T5TokenizerFast

    def __init__(self, nn_model: OrderedDict, nn_tokenizer: T5TokenizerFast) -> None:
        nn_model = self.nn_model = nn_model
        nn_tokenizer = self.nn_tokenizer = nn_tokenizer