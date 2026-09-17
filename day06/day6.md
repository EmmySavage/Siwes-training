Day 6 — Database Basics
Books Table
id
title
author
available
1
Things Fall Apart
Chinua Achebe
yes
2
The Hobbit
J.R.R. Tolkien
no
3
Animal Farm
George Orwell
yes
Create Table

CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    available TEXT
);
Insert a Book

INSERT INTO books (id, title, author, available)
VALUES (1, 'Things Fall Apart', 'Chinua Achebe', 'yes');
Select Available Books
SELECT * FROM books
WHERE available = 'yes';