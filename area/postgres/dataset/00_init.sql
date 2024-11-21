
CREATE TABLE books (
    "ISBN" TEXT,
    "Book-Title" TEXT,
    "Book-Author" TEXT,
    "Year-Of-Publication" TEXT, 
    "Publisher" TEXT,
    "Image-URL-S" TEXT,
    "Image-URL-M" TEXT,
    "Image-URL-L" TEXT
);




-- Import data from CSV file
COPY books
FROM '/docker-entrypoint-initdb.d/books_data/books.csv'
DELIMITER ';'
CSV HEADER;


