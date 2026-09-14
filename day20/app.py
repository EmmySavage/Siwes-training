from flask import Flask, request,render_template

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("search.html")
@app.route("/results")
def results():
    movie_title = request.args.get("movie_title")
    return f"You searched for:{movie_title}"

if __name__ == "__main__":
    app.run(debug=True)