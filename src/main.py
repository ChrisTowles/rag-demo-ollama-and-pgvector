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

from rich.console import Console


### Globals
console = Console()

def prompt_with_question(prompt: str, conn):
    prompt_embedding = generate_embedding_from_text(text=prompt, title="none")

    assert prompt_embedding.__len__() == 1, "really only setup to search with one chunk"

    similar_search_result = find_embeddings_similar(
        conn=conn, query_embedding=prompt_embedding[0]
    )

    assert len(similar_search_result) > 0

    additional_data = "\n".join([x.content for x in similar_search_result])

    reply = prompt_with_additional_data(data=additional_data, prompt=prompt)

    console.print("----------------PAG Similar Search Result-----------------------", style="yellow")

    for x in similar_search_result:
        print(x.content)
        print("----------------")

    
    console.print("----------------Prompt-----------------------", style="yellow")
    print(prompt)

    console.print("----------------Reply-----------------------", style="yellow")
    print(reply)


def main():

    url = "https://raw.githubusercontent.com/run-llama/llama_index/main/docs/docs/examples/data/paul_graham/paul_graham_essay.txt"

    conn = create_db_connection()

    embeddings_count = get_embeddings_count(conn)
    console.print(f"embeddings count: {embeddings_count}",style="blue")

    # Load embeddings if none found.
    if embeddings_count == 0:
        console.print("no embeddings found in the database so loading them.", style="blue")
        embeddings_list = generate_embedding_from_url(url_to_raw_text=url)
        batch_insert_embeddings(conn, embeddings_list)
        embeddings_count = get_embeddings_count(conn)
        console.print(f"embeddings count: {embeddings_count}", style="blue")

    prompt = "How many stores did they open for business?"
    prompt_with_question(prompt=prompt, conn=conn)

    console.print("Ask your own question", style="green")

    keep_asking = True
    while keep_asking:
        console.print("enter '/bye' to exit", style="green")

        questions = [inquirer.Text("long_text", message="What Question do you have ")]
        answers = inquirer.prompt(questions)

        if answers["long_text"] == "/bye":
            keep_asking = False
            console.print("--------------Done-------------------", style="green")
        else:
            prompt_with_question(prompt=answers["long_text"], conn=conn)


if __name__ == "__main__":
    main()
