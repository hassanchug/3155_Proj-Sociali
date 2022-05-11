from src.models import Users, Post
from src.models import db
class PostRepository:

    def get_all_posts(self):
        all_posts = Post.query.all()
        return all_posts

    def get_post_by_id(self, post_id):
        found_post = Post.query.get_or_404(post_id)
        return found_post

    def create_user(self, first_name, last_name, username, password):
        new_user = Users(first_name=first_name, last_name=last_name, username=username, user_password=password)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    def get_all_users(self):
        all_users = Users.query.all()
        return all_users

    def search_posts(self, username_id):
        found_posts = Post.query.filter(Users.username_id.ilike(f'%{username_id}%')).all()
        print(found_posts)
        return(found_posts)

    def create_post(self, title, replies, likes):
        new_post = Post(title=title, replies=replies, likes=likes)
        db.session.add(new_post)
        db.session.commit()
        return new_post  


# Singleton to be used in other modules
post_repository_singleton = PostRepository()

