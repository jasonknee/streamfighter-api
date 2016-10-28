from streamfighter import db

class Comment(db.Model):
	comment_id = db.Column(db.Integer, primary_key=True)
	highlight_id = db.Column(db.String(128))
	author_id = db.Column(db.String(128))
	timestamp = db.Column(db.DateTime)
	comment = db.Column(db.String(256))