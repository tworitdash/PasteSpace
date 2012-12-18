from app import db


class Paste(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), index=True)
    data = db.Column(db.String())
    language = db.Column(db.String(20), index=True)

    def __repr__(self):
        return '<Paste %r>' % (self.title)
