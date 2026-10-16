import datetime
from flask_login import UserMixin
from extension import db
from werkzeug.security import generate_password_hash,check_password_hash

class User(UserMixin,db.Model):
    __tablename__="users"

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    password=db.Column(db.String(255),nullable=False)
    email=db.Column(db.String(100),unique=True,nullable=False)
    created_at=db.Column(db.DateTime,default=datetime.datetime.now())

    def set_password(self,password):
        self.password=generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password,password )