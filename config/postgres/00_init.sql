
CREATE EXTENSION vector;

CREATE TABLE text_embeddings (
    text_embeddings_id SERIAL PRIMARY KEY,
    title varchar,
    model_name varchar,
    content varchar NOT NULL, -- the chunk
    --tokens integer,
    vector_array vector(768), -- 768 matches "nomic-embed-text" vector embedding size
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- todo - add unique constraint on chunk and title

-- todo add trigger to keep updated_at currentcc