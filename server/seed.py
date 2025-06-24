from server.app import app, db
from server.models.user import User

with app.app_context():
    print("Clearing existing data...")
    User.query.delete()

    print("Seeding users...")
    user1 = User(username="admin", email="admin@example.com")
    user1.set_password("password123")  

    user2 = User(username="guest", email="guest@example.com")
    user2.set_password("guest123")

    db.session.add_all([user1, user2])
    db.session.commit()

    print("Seeded users successfully!")
