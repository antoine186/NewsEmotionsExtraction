
from dataclasses import dataclass

@dataclass(frozen=True)
class ResourcesPath:
    emotion_classification_nn_path: str
    emotion_classification_tokenizer_path: str

    def __init__(self, emotion_classification_nn_path: str, emotion_classification_tokenizer_path: str) -> None:
        self.emotion_classification_nn_path = emotion_classification_nn_path
        self.emotion_classification_tokenizer_path = emotion_classification_tokenizer_path