from app import db

class Player(db.Model):
	player_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(128))
	twitter = db.Column(db.String(128))
	highlights = db.relationship('Highlight', backref='player', lazy='dynamic')

class Game(db.Model):
	game_id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(128), unique=True)
	icon_url = db.Column(db.String(128))

class Tournament(db.Model):
	tournament_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(128))

class Highlight(db.Model):
    highlight_id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer)
    player_one_id = db.Column(db.String(128), index=True, unique=False)
    player_two_id = db.Column(db.String(128), index=True, unique=False)
    tournament_id = db.Column(db.String(128), nullable=True)
    twitch_url = db.Column(db.String(128), unique=True)
    poster = db.Column(db.String(128))
    comments = db.relationship('Comment', backref='highlight', lazy='dynamic')
	timestamp = db.Column(db.DateTime)

    # WIP
    player_one_taunt_id = db.Column(db.String(128))
    player_two_taunt_id = db.Column(db.String(128))
    
    def __init__(self, twitch_url):
        self.twitch_url = twitch_url

    def __repr__(self):
        return '<Highlight %r>' % self.twitch_url

class Comment(db.Model):
	comment_id = db.Column(db.Integer, primary_key=True)
	highlight_id = db.Column(db.String(128))
	author_id = db.Column(db.String(128))
	timestamp = db.Column(db.DateTime)
	comment = db.Column(db.String(256))

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(128), index=True, nullable=False, unique=True)
	player_id = db.Column(db.String(128), nullable=True)


class Taunt(db.Model):
	taunt_id = db.Column(db.Integer, primary_key=True)
	image_url = db.Column(db.String(128))