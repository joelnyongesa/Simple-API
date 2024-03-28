from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from flask_bcrypt import Bcrypt
from datetime import datetime

db = SQLAlchemy()
bcrypt = Bcrypt()

class User(db.Model, SerializerMixin):
    __tablename__ = "users"
    
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(), nullable=False)
    _password_hash = db.Column(db.String())
    date = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return f'<User: {self.username}'

    def password_hash(self, password):
        self._password_hash = bcrypt.generate_password_hash(password=password).decode("utf-8")
    
    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode("utf-8"))