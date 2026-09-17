import sqlite3

connection = sqlite3.connect("movies.db")
cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE movies (
    id INTEGER PRIMARY KEY,
    title TEXT,
    director TEXT,
    available TEXT
)
""")

cursor.execute("""
    INSERT INTO movies(title,director,available)
    VALUES 
    ('Interception','Tobi','Yes')
""")
cursor.execute("""
    INSERT INTO movies(title,director,available)
    VALUES 
('GOT','Dragon queen', 'No')
    """)
cursor.execute("""
    INSERT INTO movies(title,director,available)
    VALUES 
    ('Prison Break','micheal scofield','Yes')
""")
cursor.execute("""
    INSERT INTO movies(title,director,available)
    VALUES 
    ('Flash','Marvel','Yes')
    """)
#Read everything from the table
cursor.execute("SELECT * FROM movies")
rows = cursor.fetchall()
for row in rows:
    print(row)
connection.commit()
connection.close()

