import os

from dotenv import load_dotenv
from flask import Flask, abort, redirect, render_template, request, session, flash, url_for

from forms import LoginForm, SignupForm
from flask_wtf import FlaskForm
import bcrypt

from src.models import db, Users as Users, Post
from src.repositories.post_repository import post_repository_singleton

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('CLEARDB_DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.get('/')
def index():
    return render_template('user_login.html')

@app.route('/login', methods=['POST', 'GET'])
def user_login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        the_user = db.session.query(Users).filter_by(username=request.form['username']).one()
        
        #saltp = bcrypt.gensalt(14)
        #hashp = bcrypt.checkpw(request.form['password'].encode('utf-8') , bcrypt.gensalt(14))

        if bcrypt.checkpw(request.form['password'].encode('utf-8'), the_user.password):
            session['user'] = the_user.username
            session['username_id'] = the_user.id
            return redirect(url_for('post_feed'))
        login_form.password.errors = ["Incorrect username or password."]
        return render_template("login.html", form=login_form)
    else:
        return render_template("login.html", form=login_form)

#@app.route('/logout')
#def logout():
#    if session.get('user'):
#        session.clear()
#    return redirect(url_for('index'))

@app.route('/signup', methods=['GET', 'POST'])
def user_signup():
    form = SignupForm()
    if request.method == 'POST' and form.validate_on_submit():

        h_password = bcrypt.hashpw(
        request.form['password'].encode('utf-8'), bcrypt.gensalt())

        first_name = request.form['first_name']
        last_name = request.form['last_name']
        username = request.form['username']
        password = request.form['password']

        new_user = Users(first_name, last_name, username, password)

        db.session.add(new_user)
        db.session.commit()

        session['username'] = username
        session['username_id'] = new_user.id

        return redirect(url_for('user_login'))

    return render_template('user_signup.html', form=form)

@app.get('/post_feed')
def post_feed():
    all_posts = post_repository_singleton.get_all_posts()
    return render_template('post_feed.html', list_posts_active=True, posts=all_posts)

@app.get('/user_profile')
def user_profile():
    return render_template('user_profile.html')

@app.get('/create_post')
def create_post():
    return render_template('create_a_post.html')

@app.get('/edit_post')
def edit_post():
    return render_template('edit_a_post.html')

@app.get('/view_post/<int:post_id>')
def view_post(post_id):
    single_post = post_repository_singleton.get_post_by_id(post_id)
    return render_template('view_individual_post.html', post=single_post)


