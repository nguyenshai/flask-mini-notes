# app/models.py

from . import db, login_manager
from flask_login import UserMixin
from datetime import datetime

# load user
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Model user
class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    # relationship: one-to-many
    notes = db.relationship('Note', backref='author', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

# Model note
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    # Lock user
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f'<Note {self.id} by User {self.user_id}>'
