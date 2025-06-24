from server.app import app, db
from server.models import User

with app.app_context():
    print("Clearing existing data...")
    User.query.delete()

    print("Seeding users...")

    user1 = User(username="admin", email="admin@example.com")
    user1.set_password("admin123")  

    db.session.add(user1)
    db.session.commit()
    print("Done seeding.")
