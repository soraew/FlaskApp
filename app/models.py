from datetime import datetime
from app import db
from app import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
# for flask_login to work, we need 
# is_authenticated : bool
# is_active : bool
# is_anonymous : bool
# get_id()
# UserMixin creates these generic implementations


# changes to a database are done in the ocntext of a session

# The flask db migrate command does not make any changes to the database, 
# it just generates the migration script. 
# To apply the changes to the database, 
# the flask db upgrade command must be used.

# String type is called varchar in SQL jargon
class User(UserMixin, db.Model):# Flask-SQLAlchemy uses snake case so this will be user
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    # repr below shows how to pring objects of this class, 
    # which is useful for debugging
    def __repr__(self):
        return "<User {}>".format(self.username)
    
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestemp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))#referencing from user table
    
    def __repr__(self):
        return "<Post {}>".format(self.body)
    
  
@login.user_loader
def load_user(id):
    return User.query.get(int(id))  


    
# when checking things in the python IDE, just 'flask shell'
# for a IDE within the context of the app

# when adding a blog post, 
# >>> u = User.query.get(1)
#     here, I assign an author to a post using the 'author' virtual field
#     instead of having to deal with user IDs.
# >>> p = Post(body='my first post!', author=u)
# >>> db.session.add(p)
# >>> db.session.commit()

#query 例
# >>> # get all posts written by a user
# >>> u = User.query.get(1)
# >>> u
# <User john>
# >>> posts = u.posts.all()
# >>> posts
# [<Post my first post!>]

# >>> # same, but with a user that has no posts
# >>> u = User.query.get(2)
# >>> u
# <User susan>
# >>> u.posts.all()
# []

# >>> # print post author and body for all posts 
# >>> posts = Post.query.all()
# >>> for p in posts:
# ...     print(p.id, p.author.username, p.body)
# ...
# 1 john my first post!

# # get all users in reverse alphabetical order
# >>> User.query.order_by(User.username.desc()).all()
# [<User susan>, <User john>]