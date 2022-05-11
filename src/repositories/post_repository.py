from src.models import Users, Posts
from src.models import db
class PostRepository:

    def get_all_posts(self):
        return Users.query.all()

    def get_post_by_id(self, post_id):
        return Users.query.get(post_id)

    def create_user(self, username_id, first_name, last_name, password):
        new_user = Users(username_id='HotBoi', first_name='James', last_name='Charles', password='gay')
        self._db.append(Users)
        return new_user

    def search_posts(self, username_id):
        print(('username').ilike('word'))

    def create_post(self, post_id, title, replies, timepost, likes):
        new_post = Posts(post_id='1', title='Cool pics', replies='lovely pics', timepost='3:40pm', likes='sixteen likes')
        db.session.add(new_post)
        db.session.commit()
        return new_post  


# Singleton to be used in other modules
post_repository_singleton = PostRepository()

