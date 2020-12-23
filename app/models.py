from app import db

# String type is called varchar in SQL jargon
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    
    # repr below shows how to pring objects of this class, 
    # which is useful for debugging
    def __repr__(self):
        return "<User {}>".format(self.username)