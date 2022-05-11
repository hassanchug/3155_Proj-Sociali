from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    username_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    user_password = db.Column(db.String, nullable=False)

class Posts(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    timepost = db.Column(db.String, nullable=False)
    likes = db.Column(db.Integer, nullable=False)
