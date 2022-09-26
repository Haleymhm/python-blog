from datetime import datetime
from myblog import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Colum(db.String(100))
    email = db.Column(db.String(100))
    username = db.Column(db.String(50),unique=True, nullable=False)
    password = db.Column(db.Text)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self,fullname, email, username, password) -> None:
        self.fullname = fullname
        self.email = email
        self.username = username
        self.password = password

    def __repr__(self) -> str:
        return f'User: {self.username}'