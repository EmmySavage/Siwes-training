from flask import Flask,request,session,redirect,url_for,render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash,generate_password_hash
app = Flask (__name__)
app.secret_key = "temporary-key-for-practise"
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///movies.db"
db=SQLAlchemy(app)
class User (db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(100))
    password=db.Column(db.String(200))
    role=db.Column(db.String(20))


class Movie (db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100))
    director=db.Column(db.String(100))
    available=db.Column(db.Boolean)
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session["username"] = user.username
            return redirect(url_for("admin_only"))

        return "Invalid username or password"

    return render_template("login.html")
@app.route("/admin-only")
def admin_only():
    if "username" not in session:
        return redirect(url_for("login"))

    user = User.query.filter_by(username=session["username"]).first()

    if user.role != "admin":
        return "Access denied. Admins only."

    return f"Welcome to the admin area, {user.username}!"
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        admin = User(username="admin",password=generate_password_hash("admin123"),role="admin")
        student= User(username="emma",password= generate_password_hash("emma123"),role="student")
        new_movie1=Movie(title="merlin",director="emma",available=True)
        new_movie2=Movie(title="GOT",director="Dragon",available=True)
        new_movie3=Movie(title="inception",director="pecky",available=False)

        db.session.add(new_movie1)
        db.session.add(new_movie2)
        db.session.add(new_movie3)
        db.session.add(admin)
        db.session.add(student)
        db.session.commit()
        #All movies i added
        all_movies = Movie.query.all()
        print(all_movies)
        #All available movies which is true
        available_movies= Movie.query.filter_by(available=True).all()
        print(available_movies)
        #searched for the movie
        title_movies=Movie.query.filter_by(title="GOT").first()
        print(title_movies)
    app.run(debug=True)