
from typing import Any, List, Mapping, Sequence
from ollama import embed, generate
import requests


OLLAMA_EMBEDDING_MODEL = "nomic-embed-text"

OLLAMA_CHAT_MODEL = "llama3.2"


class EncodingResponse:
    """ Object to start embedding data"""
    def __init__(self, title: str, content: str, embedding: Mapping[str, Any]):
        self.title: str = title
        self.content: str = content
        self.vector_array: Sequence[float] = (embedding["embeddings"][0],)
        self.model: str = embedding["model"]
        


def generate_embedding_from_url(url_to_raw_text: str) -> List[EncodingResponse]:
    """ load text from url then do embedding"""

    response = requests.get(url_to_raw_text, timeout=10_000)

    text = response.text

    return generate_embedding_from_text(text=text, title=url_to_raw_text)


def generate_embedding_from_text(text: str, title: str) -> List[EncodingResponse]:
    """ convert text to embedding"""

    chunk_size = 512
    chunks = [text[i : i + chunk_size] for i in range(0, len(text), chunk_size)]
    #print(len(chunks))

    list_embeddings: List[EncodingResponse] = []

    for chunk in chunks:
        embedding = embed(model=OLLAMA_EMBEDDING_MODEL, input=chunk)
        list_embeddings.append(
            EncodingResponse(title=title, content=chunk, embedding=embedding)
        )

    # for x in list_embeddings:
    #     print(x.chunk)
    #     print(x.model)

    return list_embeddings


def prompt_with_additional_data(data: str, prompt: str) -> str:
    """ prompt using the rag additional data"""

    # generate a response combining the prompt and data
    output = generate(
        model=OLLAMA_CHAT_MODEL,
        prompt=f"Using this data: {data}. Respond to this prompt: {prompt}",
    )
    return output["response"]
