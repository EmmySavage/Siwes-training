from flask import Flask,request,session,redirect,url_for,render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash

app = Flask (__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///movies.db"
app.secret_key="temporary key for practice"
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user=User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password,password):
            session["username"]=user.username
            return redirect("/movie.html")
    return render_template("login.html")
@app.route("/movie")
def movie():
    if "username" not in session:
        return redirect(url_for("login"))
    movies=Movie.query.all()
    return render_template("movie.html",movies=movies)
db=SQLAlchemy(app)
@app.route("/add_movie",methods=["GET","POST"])
def add_movie():
    if 'username' not in session:
        return redirect("/login.html")
    if request.method=='POST':
        title = request.form.get('title')
        director = request.form.get('director')
        movie=Movie(title=title,director=director
        )
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for("movie"))
    return render_template ("add_movie.html")


class Movie(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100))
    director=db.Column(db.String(100))
    available=db.Column(db.Boolean)
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)   
    username=db.Column(db.String(100))
    password=db.Column(db.String(100))
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        student = User(username="emma",password=generate_password_hash("emma123"))
        new_movie1=Movie(title="merlin",director="emma",available=True)
        new_movie2=Movie(title="GOT",director="Dragon",available=True)
        new_movie3=Movie(title="inception",director="pecky",available=False)

        db.session.add(new_movie1)
        db.session.add(new_movie2)
        db.session.add(new_movie3)
        db.session.add(student)
        db.session.commit()
    app.run(debug=True)