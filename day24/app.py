from flask import Flask, request, render_template
import sqlite3 
from werkzeug.security import check_password_hash

app = Flask(__name__)
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
        print("USER:",user)
        print("USER TYPE",type(user))
        connection.close()

        if user:
          stored_hash = user[2]
          if check_password_hash(stored_hash,password):
            return f"Welcome, {username}!"
        else:
            return "Invalid username or password"
        return"Invalid username or password"
    return render_template("login.html")
if __name__ == "__main__":
    app.run(debug=True)
