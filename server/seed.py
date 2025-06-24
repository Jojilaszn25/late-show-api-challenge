from server.config import app, db
from server.models import User, Guest, Episode, Appearance
from werkzeug.security import generate_password_hash

with app.app_context():
    print("Seeding database...")

    Appearance.query.delete()
    Guest.query.delete()
    Episode.query.delete()
    User.query.delete()

    user = User(username="admin", password_hash=generate_password_hash("12345"))
    db.session.add(user)

    guest1 = Guest(name="Emma Stone", occupation="Actress")
    guest2 = Guest(name="John Mulaney", occupation="Comedian")
    guest3 = Guest(name="Taylor Swift", occupation="Musician")

    db.session.add_all([guest1, guest2, guest3])

    episode1 = Episode(date="2024-06-01", number=1)
    episode2 = Episode(date="2024-06-02", number=2)

    db.session.add_all([episode1, episode2])

    appearance1 = Appearance(rating=9, guest=guest1, episode=episode1)
    appearance2 = Appearance(rating=8, guest=guest2, episode=episode1)
    appearance3 = Appearance(rating=10, guest=guest3, episode=episode2)

    db.session.add_all([appearance1, appearance2, appearance3])

    db.session.commit()
    print("Done seeding!")
