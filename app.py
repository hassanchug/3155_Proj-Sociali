import os

from dotenv import load_dotenv
from flask import Flask, abort, redirect, render_template, request

from src.models import db
from src.repositories.(our repository here) import (our repository)_singleton

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('CLEARDB_DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.get('/login')
def user_login():
    return render_template('user_login.html')

@app.get('/signup')
def user_signup():
    return render_template('user_signup.html')

@app.get('/post_feed')
def post_feed():
    return render_template('post_feed.html')

@app.get('/create_post')
def create_post():
    return render_template('create_a_post.html')
