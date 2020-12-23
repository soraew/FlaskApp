from datetime import datetime
from app import db

# The flask db migrate command does not make any changes to the database, 
# it just generates the migration script. 
# To apply the changes to the database, 
# the flask db upgrade command must be used.

# String type is called varchar in SQL jargon
class User(db.Model):# Flask-SQLAlchemy uses snake case so this will be user
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    
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
    
    
