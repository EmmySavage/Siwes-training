from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    movies = ["Interception","Prison break","GOT","Flash"]
    return render_template("home.html", movies=movies)

if __name__ == "__main__":
    app.run(debug=True)