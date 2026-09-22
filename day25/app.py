from flask import Flask, request, render_template, session, redirect, url_for
import sqlite3
from werkzeug.security import check_password_hash

app = Flask(__name__)

app.secret_key = "temporary-key-for-practise"


@app.route("/dashboard")
def dashboard():
    if "username" in session:
        return f"Welcome to your dashboard, {session['username']}"
    else:
        return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        connection = sqlite3.connect("users.db")
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        )

        user = cursor.fetchone()

        print("USER:", user)
        print("USER TYPE:", type(user))

        connection.close()

        if user:
            stored_hash = user[2]

            if check_password_hash(stored_hash, password):
                session["username"] = username
                return redirect(url_for("login"))

        return "Invalid username or password"

    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)