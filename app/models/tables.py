from app import db


class User(db.Model):
    __tablename__ = "users"

    # User("emilycolona", "123", "Emily Colona", "emilycolona27@gmail.com", "admin")
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    profile = db.Column(db.String)

    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_active(self):
        return True
    
    @property
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return str(self.id)

    def __init__(self, username, email, password, name, profile):
        self.username = username
        self.email = email
        self.password = password
        self.name = name
        self.profile = profile

    def __repr__(self):
        return "<User %r>" % self.username
