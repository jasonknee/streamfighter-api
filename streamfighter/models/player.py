from streamfighter import db

class Player(db.Model):
	player_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(128))
	twitter = db.Column(db.String(128))
	# highlights = db.relationship('Highlight', backref='player', lazy='dynamic')