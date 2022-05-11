import os

from dotenv import load_dotenv
from flask import Flask, abort, redirect, render_template, request, session, url_for

from src.models import db, Users
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
        #session.pop('user_id', None)
        username = request.form['username']
        password = request.form['password']

        user = [x for x in Users if x.username == username][0]
        if user and user.password == password:
            session['username_id'] = user.id
            return redirect(url_for('post_feed'))

        return redirect(url_for('user_login'))

    return render_template('user_login.html')

@app.route('/signup', methods=['GET', 'POST'])
def user_signup():
    if(request.method == 'GET'):
        return render_template('user_signup.html')
    elif(request.method == 'POST'):
        first_name = request.form.get('first_name', '')
        last_name = request.form.get('last_name', '')
        username = request.form.get('username', '')
        user_password = request.form.get('password', '')
        new_user = Users(first_name = first_name, last_name = last_name, username = username, user_password = user_password)
        db.session.add(new_user)
        db.session.commit()
    return redirect(url_for('user_login'))

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


