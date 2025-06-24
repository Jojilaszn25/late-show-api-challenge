from server.config import db
from datetime import datetime

class Episode(db.Model):
    __tablename__ = "episodes"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    air_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Episode {self.title}>"
