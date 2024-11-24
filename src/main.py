from ollama_utils import (
    generate_embedding_from_text,
    generate_embedding_from_url,
    prompt_with_additional_data,
)
from db import (
    create_db_connection,
    find_embeddings_similar,
    get_embeddings_count,
    batch_insert_embeddings,
)
import inquirer


def prompt_with_question(prompt: str, conn):
    prompt_embedding = generate_embedding_from_text(text=prompt, title="none")

    assert prompt_embedding.__len__() == 1, "really only setup to search with one chunk"

    similar_search_result = find_embeddings_similar(
        conn=conn, query_embedding=prompt_embedding[0]
    )

    assert len(similar_search_result) > 0

    additional_data = "\n".join([x.content for x in similar_search_result])

    reply = prompt_with_additional_data(data=additional_data, prompt=prompt)

    print("----------------PAG Similar Search Result-----------------------")

    for x in similar_search_result:
        print(x.content)
        print("----------------")

    print("----------------Prompt-----------------------")
    print(prompt)

    print("----------------Reply-----------------------")
    print(reply)


def main():

    url = "https://raw.githubusercontent.com/run-llama/llama_index/main/docs/docs/examples/data/paul_graham/paul_graham_essay.txt"

    conn = create_db_connection()

    embeddings_count = get_embeddings_count(conn)
    print(f"embeddings count: {embeddings_count}")

    # Load embeddings if none found.
    if embeddings_count == 0:
        print("no embeddings found in the database so loading them.")
        embeddings_list = generate_embedding_from_url(url_to_raw_text=url)
        batch_insert_embeddings(conn, embeddings_list)
        embeddings_count = get_embeddings_count(conn)
        print(f"embeddings count: {embeddings_count}")

    prompt = "How many stores did they open for business?"
    prompt_with_question(prompt=prompt, conn=conn)

    print("Ask your own question")

    keep_asking = True
    while keep_asking:
        print("enter '/bye' to exit")

        questions = [inquirer.Text("long_text", message="What Question do you have ")]
        answers = inquirer.prompt(questions)

        if answers["long_text"] == "/bye":
            keep_asking = False
        else:
            prompt_with_question(prompt=answers["long_text"], conn=conn)


if __name__ == "__main__":
    main()
