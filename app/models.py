from . import db


class Event(db.Model):

    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    asin = db.Column(db.String(25))
    brand = db.Column(db.String(25))
    event_id = db.Column(db.String(25))
    source = db.Column(db.String(25))
    stars = db.Column(db.Integer)
    timestamp = db.Column(db.Integer)
    def __repr__(self):
        return '<Category %r>' % self.event_id