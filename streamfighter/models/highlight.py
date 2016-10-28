from streamfighter import db

class Highlight(db.Model):
    highlight_id = db.Column(db.Integer, primary_key=True)
    # game_id = db.Column(db.Integer)
    # player_one_id = db.Column(db.String(128), index=True, unique=False)
    # player_two_id = db.Column(db.String(128), index=True, unique=False)
    # tournament_id = db.Column(db.String(128), nullable=True)
    twitch_url = db.Column(db.String(128), unique=True)
    # poster = db.Column(db.String(128))
    # comments = db.relationship('Comment', backref='highlight', lazy='dynamic')
    # timestamp = db.Column(db.DateTime)

    # WIP
    # player_one_taunt_id = db.Column(db.String(128))
    # player_two_taunt_id = db.Column(db.String(128))
    
    def __init__(self, twitch_url):
        self.twitch_url = twitch_url

    def __repr__(self):
        return '<Highlight %r>' % self.twitch_url