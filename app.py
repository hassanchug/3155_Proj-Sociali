import os

from dotenv import load_dotenv
from flask import Flask, abort, redirect, render_template, request

from src.models import db, User
from src.repositories.post_repository import post_repository_singleton

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('CLEARDB_DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.get('/')
def index():
    return render_template('user_login.html')

@app.route('/login', methods=['GET', 'POST'])
def user_login():
    if(request.method == 'GET'):
        return render_template('user_login.html')
    elif(request.method == 'POST'):
        (method) (handle route here)

@app.route('/signup', methods=['GET', 'POST'])
def user_signup():
    if(request.method == 'GET'):
        first_name = request.form.get('first_name', '')
        last_name = request.form.get('last_name', '')
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        return render_template('user_signup.html')
    elif(request.method == 'POST'):
        new_user = User(first_name = first_name, last_name = last_name, username = username, password = password)
        db.session.add(new_user)
        db.session.commit()

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


