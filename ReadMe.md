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


## Postgres



```bash
docker compose up

# or detached
docker compose up -d

```


## Run App


```bash
streamlit run app.py
```

Open [localhost:8501](http://localhost:8501) to view your RAG app.



## Shutdown 


```bash
# stop containers
docker compose down

# stop containers and remove volumes
docker compose down --volumes
```


## Links

- https://github.com/phidatahq/phidata/blob/main/cookbook/assistants/llms/groq/rag/README.md?plain=1
- https://github.com/ChingWeiChan/ollama-streamlit-demo/blob/main/main.py
