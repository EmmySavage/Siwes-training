from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app =Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"

print("DATABASE:",app.config.get("SQLALCHEMY_DATABASE_URI"))

db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer,primary_key = True )
    title = db.Column(db.String(100))
    director = db.Column(db.String(100))
    available = db.Column(db.Boolean)




if __name__ == "__main__":

    with app.app_context():
        db.create_all()
    
    app.run(debug=True)
