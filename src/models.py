from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    username = db.Column(db.String, primary_key=True)
    firstname = db.Column(db.String, nullable=False)
    lastname = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

class Posts(db.Model):
    post_id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    timepost = db.Column(db.String, nullable=False)
    likes = db.Column(db.String, nullable=False)
