
CREATE TABLE text_encodings (
    text_encodings_id SERIAL PRIMARY KEY,
    model_name varchar,
    input_text TEXT NOT NULL,
    encoded_text BYTEA NOT NULL,
    embedding vector(1536)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



# Create table to store embeddings and metadata
table_create_command = """
CREATE TABLE embeddings (
            id bigserial primary key, 
            title text,
            url text,
            content text,
            tokens integer,
            embedding vector(1536)
            );
            """

cur.execute(table_create_command)
cur.close()
conn.commit()


-- Import data from CSV file
COPY books
FROM '/docker-entrypoint-initdb.d/books_data/books.csv'
DELIMITER ';'
CSV HEADER;


