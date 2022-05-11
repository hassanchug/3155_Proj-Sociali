import os

from dotenv import load_dotenv
from flask import Flask, abort, redirect, render_template, request, session, flash, url_for

from forms import LoginForm
import bcrypt
import secrets

from src.models import db, Users as Users, Post
from src.repositories.post_repository import post_repository_singleton

load_dotenv()

app = Flask(__name__)

secret_key = secrets.token_hex(16)
app.config['SECRET_KEY'] = secret_key

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('CLEARDB_DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.get('/')
def index():
    return redirect(url_for('user_login'))

@app.route('/login', methods=['POST', 'GET'])
def user_login():
    login_form = LoginForm()

    if login_form.validate_on_submit() and request.method=='POST':
        the_user = db.session.query(Users).filter_by(username=request.form['username']).first()
        
        hashp = bcrypt.hashpw(request.form['password'].encode('utf-8') , bcrypt.gensalt(14))

        if bcrypt.checkpw(request.form['password'].encode('utf-8'), hashp):
            session['username_id'] = the_user.username_id
            return redirect(url_for('post_feed'))
        login_form.password.errors = ["Incorrect username or password."]
        return render_template("user_login.html", form=login_form)
    else:
        return render_template("user_login.html", form=login_form)

@app.route('/logout')
def logout():
    if session.get('username_id'):
        session.clear()
    return redirect(url_for('index'))

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
    all_posts = post_repository_singleton.get_all_posts()
    all_users = post_repository_singleton.get_all_users()
    return render_template('post_feed.html', list_posts_active=True, posts=all_posts, users=all_users)

@app.get('/user_profile')
def user_profile():
    all_posts = post_repository_singleton.get_all_posts()
    all_users = post_repository_singleton.get_all_users()
    return render_template('user_profile.html', list_posts_active=True, posts=all_posts, users=all_users)

@app.post('/create_post')
def create_post():
    all_posts = post_repository_singleton.get_all_posts()
    all_users = post_repository_singleton.get_all_users()
    return render_template('create_a_post.html', list_posts_active=True, posts=all_posts, users=all_users)


@app.get('/edit_post')
def edit_post():
    all_posts = post_repository_singleton.get_all_posts()
    all_users = post_repository_singleton.get_all_users()
    return render_template('edit_a_post.html', list_posts_active=True, posts=all_posts, users=all_users)

@app.get('/view_post')
def view_post():
    single_post = post_repository_singleton.get_post_by_id()
    all_users = post_repository_singleton.get_all_users()
    return render_template('view_individual_post.html', post=single_post, users=all_users)


