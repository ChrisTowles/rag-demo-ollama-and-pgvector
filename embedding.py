from typing import Any, List, Mapping, Sequence
import numpy as np
from ollama import embed
import requests

#response = embed(model='llama3.2', input='Hello, world!')
#print(response['embeddings'])




response = requests.get('https://raw.githubusercontent.com/run-llama/llama_index/main/docs/docs/examples/data/paul_graham/paul_graham_essay.txt')

#print(response.text)

text = response.text
chunk_size = 2048
chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
print(len(chunks))


class EncodingResponse:
    def __init__(self, chunk: str, embedding: Mapping[str, Any]):
        self.chunk: str = chunk
        self.vector_array:  Sequence[float] = embedding['embeddings'],
        self.model: str = embedding['model']

list_embeddings: List[EncodingResponse] = [];

for chunk in chunks:
    embedding = embed(model='llama3.2', input=chunk)
    list_embeddings.append(EncodingResponse(chunk=chunk, embedding=embedding))


for x in list_embeddings:
    print(x.chunk)
    print(x.model)

