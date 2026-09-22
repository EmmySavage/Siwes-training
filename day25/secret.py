import sqlite3
from werkzeug.security import generate_password_hash

connection = sqlite3.connect("users.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT
    )
""")
hashed_password = generate_password_hash("password123")
cursor.execute(
    "INSERT INTO users (username, password) VALUES (?, ?)",
    ("emmanuel", hashed_password)
)
connection.commit()
connection.close()
print("created successfuuuuuu")