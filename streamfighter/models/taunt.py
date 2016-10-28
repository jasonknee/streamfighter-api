from streamfighter import db

class Taunt(db.Model):
	taunt_id = db.Column(db.Integer, primary_key=True)
	image_url = db.Column(db.String(128))