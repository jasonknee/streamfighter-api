from streamfighter import db

class Game(db.Model):
	game_id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(128), unique=True)
	icon_url = db.Column(db.String(128))