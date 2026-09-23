from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask (__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///movies.db"
db=SQLAlchemy(app)

class Movie (db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100))
    director=db.Column(db.String(100))
    available=db.Column(db.Boolean)
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        new_movie1=Movie(title="merlin",director="emma",available=True)
        new_movie2=Movie(title="GOT",director="Dragon",available=True)
        new_movie3=Movie(title="inception",director="pecky",available=False)

        db.session.add(new_movie1)
        db.session.add(new_movie2)
        db.session.add(new_movie3)
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