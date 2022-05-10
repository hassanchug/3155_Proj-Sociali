from src.models import Users
from src.models import db
class PostRepository:

    def get_all_posts(self):
        
       
        return User.query.all()

    def get_post_by_id(self, post_id):
        
        
        return User.query.get(post_id)

    def create_user(self, username_id, firstname, lastname, user_password):
        
        new_user = User(username_id='HotBoi', firstname='James', lastname='Charles', user_password='gay')
        db.session.add(new_user)
        db.session.commit()
        return new_user

    def search_posts(self, username_id):
        
        print(('username').ilike('word'))

    def create_post(self, post_id, title, replies, likes):
        new_post = Post(post_id='1', title='Cool pics', replies='lovely pics', likes='sixteen likes')
        db.session.add(new_post)
        db.session.commit()
        return new_post
        


# Singleton to be used in other modules
post_repository_singleton = PostRepository()

