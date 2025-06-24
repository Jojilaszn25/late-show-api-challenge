from server.config import db

class Appearance(db.Model):
    __tablename__ = "appearances"

    id = db.Column(db.Integer, primary_key=True)
    guest_id = db.Column(db.Integer, db.ForeignKey("guests.id"), nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey("episodes.id"), nullable=False)
    rating = db.Column(db.Integer, nullable=True)

    guest = db.relationship("Guest", backref="appearances")
    episode = db.relationship("Episode", backref="appearances")

    def __repr__(self):
        return f"<Appearance Guest ID={self.guest_id} Episode ID={self.episode_id}>"
