from models import User
from models import db
class PostRepository:

    def get_all_posts(self):
        
       
        return User.query.all()

    def get_post_by_id(self, post_id):
        
        
        return User.query.get(post_id)

    def create_user(self, username, firstname, lastname, password):
        
        new_user = User(username='HotBoi', firstname='James', lastname='Charles', password='gay')
        db.session.add(new_user)
        db.session.commit()
        return new_user

    def search_posts(self, username):
        
        print(('username').ilike('word'))
        


# Singleton to be used in other modules
post_repository_singleton = PostRepository()
