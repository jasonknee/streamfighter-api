from streamfighter import db

class Tournament(db.Model):
	tournament_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(128))