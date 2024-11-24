# RAG Demo using ollama and Pgvector


## Python setup

setup enviroment with pyenv

```bash
pyenv virtualenv 3.12 rag_demo_towles
pyenv local rag_demo_towles
pyenv shell rag_demo_towles

```

Be sure to set VS Code as `Python: Selected Interpreter` to use the correct environment.

Install dependencies with pip

```bash
pip install --upgrade pip


pip install -r pip.requirements.txt

```

## Setup Ollama

To use [Ollama](https://github.com/ollama/ollama) for embeddings and run the `nomic-embed-text` model

```bash
ollama run llama3.2 # for chat
ollama run nomic-embed-text # for embeddings

```


## Get dataset

```bash
curl -L -o ./area/postgres/dataset/books-dataset.zip https://www.kaggle.com/api/v1/datasets/download/saurabhbagchi/books-dataset

unzip ./area/postgres/dataset/books-dataset.zip -d ./area/postgres/dataset
```

## Postgres



```bash
docker compose up

# or detached
docker compose up -d

```


## Run App


```bash
python main.py
```

On first load if no embeddings in the DB it will take a second and load them.






## Shutdown 


```bash
# stop containers
docker compose down

# stop containers and remove volumes
docker compose down --volumes
```

remove python environment

```bash
pyenv virtualenv-delete  rag_demo_towles

```


## Links

- https://github.com/phidatahq/phidata/blob/main/cookbook/assistants/llms/groq/rag/README.md?plain=1
- https://github.com/ChingWeiChan/ollama-streamlit-demo/blob/main/main.py
- https://github.com/Azure-Samples/rag-postgres-openai-python
- https://electric-sql.com/blog/2024/02/05/local-first-ai-with-tauri-postgres-pgvector-llama
- https://docs.llamaindex.ai/en/stable/getting_started/starter_tools/rag_cli/
- https://github.com/HamedMP/NextRag
- https://www.theunwindai.com/p/build-a-local-rag-agent-with-llama-3-2-and-vector-database?s=31
- https://www.inferable.ai/blog/posts/sqlite-rag
- https://docs.mistral.ai/guides/rag/#:~:text=Split%20document%20into%20chunks%E2%80%8B,and%20we%20get%2037%20chunks
- https://www.timescale.com/blog/postgresql-as-a-vector-database-create-store-and-query-openai-embeddings-with-pgvector/
  - has some good chunking code
- https://stephencollins.tech/posts/how-to-use-postgresql-to-store-and-query-vector-embeddings
  - good example code and tokenizer libs