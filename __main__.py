import torch
from transformers import AutoTokenizer

model = torch.load('./NeuralNetworks/t5-base-finetuned-emotion/pytorch_model.bin', map_location=torch.device('cpu'))
tokenizer = AutoTokenizer.from_pretrained('./NeuralNetworks/t5-base-finetuned-emotion/')

print(tokenizer)