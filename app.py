import os

from dotenv import load_dotenv
from flask import Flask, abort, redirect, render_template, request

from src.models import db
from src.repositories.post_repository import post_repository_singleton

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('CLEARDB_DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.get('/')
def index():
    return render_template('user_login.html')

@app.get('/login')
def user_login():
    return render_template('user_login.html')

@app.post('/signup')
def user_signup():
    username = request.form.get('Username')
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    password = request.form.get('password')

    post_repository_singleton.create_user(username, firstname, lastname, password)
    return redirect('/signup')

@app.get('/post_feed')
def post_feed():
    return render_template('post_feed.html')

@app.get('/user_profile')
def user_profile():
    return render_template('user_profile.html')

@app.get('/create_post')
def create_post():
    return render_template('create_a_post.html')

@app.get('/edit_post')
def edit_post():
    return render_template('edit_a_post.html')

@app.get('/view_post')
def view_post():
    return render_template('view_individual_post.html')



