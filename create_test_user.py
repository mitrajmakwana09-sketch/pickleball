from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    # Check if test user already exists
    existing_user = User.query.filter_by(email='test@example.com').first()
    if not existing_user:
        test_user = User(
            username='testuser',
            email='test@example.com',
            password='test123',
            role='customer'
        )
        db.session.add(test_user)
        db.session.commit()
        print("Test user created successfully!")
        print(f"Username: testuser")
        print(f"Email: test@example.com")
        print(f"Password: test123")
    else:
        print("Test user already exists!")
