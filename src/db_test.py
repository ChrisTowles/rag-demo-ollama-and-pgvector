from db import create_db_connection, get_embeddings_count


def test_get_embeddings_count():
    conn = create_db_connection()

    embedding_count = get_embeddings_count(conn)
    assert embedding_count > 0

