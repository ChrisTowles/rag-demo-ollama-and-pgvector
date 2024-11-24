from typing import List
import numpy as np
import psycopg2

from psycopg2.extras import execute_values
from pgvector.psycopg2 import register_vector

from ollama_utils import EncodingResponse


def create_db_connection():

    username = "local_rag_user"
    password = "password"
    host = "127.0.0.1"
    port = 5432
    database = "local_rag_db"
    connection_string = f"postgresql://{username}:{password}@{host}:{port}/{database}"

    conn = psycopg2.connect(connection_string)

    register_vector(conn)

    return conn


def batch_insert_embeddings(conn, embeddings_list: List[EncodingResponse]):
    """bulk insert text embeddings"""
    cur = conn.cursor()
    # Prepare the list
    data_list = [
        (row.title, row.model, row.content, row.vector_array) for row in embeddings_list
    ]

    # Use execute_values to perform batch insertion
    execute_values(
        cur,
        "INSERT INTO text_embeddings (title, model_name, content, vector_array) VALUES %s",
        data_list,
    )
    conn.commit()


def get_embeddings_count(conn) -> int:
    """ verify count of embeddings"""
    cur = conn.cursor()
    cur.execute("SELECT COUNT(1) as cnt FROM public.text_embeddings;")
    num_records = cur.fetchone()[0]
    return num_records



class EmbeddingTextSearchResult:

    """ Object to from db search embedding"""
    def __init__(self, text_embedding_id: int,  title: str, content: str):
        self.text_embedding_id: str = text_embedding_id
        self.title: str = title
        self.content: str = content

def find_embeddings_similar(conn,  query_embedding:EncodingResponse) -> List[EmbeddingTextSearchResult]:
    """search for similar embeddings"""


    embedding = np.array(query_embedding.vector_array) ##    
    cur = conn.cursor()
    # Perform a cosine similarity search
    cur.execute(
            """SELECT text_embeddings_id, content, title, 1 - (vector_array <=> %s) AS cosine_similarity
               FROM text_embeddings
               ORDER BY cosine_similarity DESC LIMIT 2""",
            (embedding)
        )
 

    list_search_results: List[EmbeddingTextSearchResult] = []

    for x in cur.fetchall():
        list_search_results.append(EmbeddingTextSearchResult(text_embedding_id=x[0],
                                                              title=x[2],
                                                              content=x[1]))

    return list_search_results