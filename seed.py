from server.app import app
from server.models import db, User

with app.app_context():
    print("Seeding users...")

    User.query.delete()

    user = User(
        username="testuser",
        email="test@example.com"
    )
    user.set_password("password123")  

    db.session.add(user)
    db.session.commit()

    print("Done seeding.")
