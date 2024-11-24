from ollama_utils import (
    generate_embedding_from_text,
    generate_embedding_from_url,
    prompt_with_additional_data,
)

def test_generate_embedding_from_text():
    """test"""

    list_embeddings = generate_embedding_from_text(
        text="test string", title="test_title"
    )

    assert len(list_embeddings) > 0, "Expected non-empty list of embeddings"
    assert list_embeddings[0].vector_array.__len__() > 0


def test_generate_embedding_from_url():

    url = "https://raw.githubusercontent.com/run-llama/llama_index/main/docs/docs/examples/data/paul_graham/paul_graham_essay.txt"
    list_embeddings = generate_embedding_from_url(url_to_raw_text=url)

    assert len(list_embeddings) > 0, "Expected non-empty list of embeddings"
    assert list_embeddings[0].vector_array.__len__() > 0


def test_prompt_with_additional_data():
    # Test data
    data = "The Color of the pen is purple"
    prompt = "what color is the pen?"

    response = prompt_with_additional_data(data, prompt)

    print(response)

    assert response.lower().__contains__("purple")
