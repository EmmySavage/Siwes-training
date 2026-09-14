from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Movie Hub"

@app.route("/about")
def about():
    return "This is the Movie Hub about page"

if __name__ == "__main__":
    app.run(debug=True)