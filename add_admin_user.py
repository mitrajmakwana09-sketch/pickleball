from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    # Check if user already exists
    existing_user = User.query.filter_by(email='meetraj22426@gmail.com').first()
    
    if existing_user:
        # Update existing user's password and role if needed
        existing_user.password = '12345'
        existing_user.role = 'admin'
        db.session.commit()
        print("Admin user updated successfully!")
        print(f"Username: {existing_user.username}")
        print(f"Email: meetraj22426@gmail.com")
        print(f"Password: 12345")
        print(f"Role: {existing_user.role}")
    else:
        # Create new admin user
        admin_user = User(
            username='meetraj',
            email='meetraj22426@gmail.com',
            password='12345',
            role='admin'
        )
        db.session.add(admin_user)
        db.session.commit()
        print("Admin user created successfully!")
        print(f"Username: meetraj")
        print(f"Email: meetraj22426@gmail.com")
        print(f"Password: 12345")
        print(f"Role: admin")
