from streamfighter import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(128), index=True, nullable=False, unique=True)
	player_id = db.Column(db.String(128), nullable=True)