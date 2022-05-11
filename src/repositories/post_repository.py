from src.models import Users, Posts
from src.models import db
class PostRepository:

    def get_all_posts(self):
        all_posts = Posts.query.all()
        return all_posts

    def get_post_by_id(self, post_id):
        found_post = Posts.query.get_or_404(post_id)
        return found_post

    def create_user(self, username_id, first_name, last_name, password):
        new_user = Users(username_id=username_id, first_name=first_name, last_name=last_name, password=password)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    def search_posts(self, username_id):
        found_posts = Posts.query.filter(Users.username_id.ilike(f'%{username_id}%')).all()
        print(found_posts)
        return(found_posts)

    def create_post(self, post_id, title, replies, timepost, likes):
        new_post = Posts(post_id=post_id, title=title, replies=replies, timepost=timepost, likes=likes)
        db.session.add(new_post)
        db.session.commit()
        return new_post  


# Singleton to be used in other modules
post_repository_singleton = PostRepository()

