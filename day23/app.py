from flask import Flask, request, render_template
import sqlite3 

app = Flask(__name__)
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        connection = sqlite3.connect("users.db")
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?",
            (username, password)
        )
        user = cursor.fetchone()
        connection.close()

        if user:
            return f"Welcome, {username}!"
        else:
            return "Invalid username or password"

    return render_template("login.html")
if __name__ == "__main__":
    app.run(debug=True)
