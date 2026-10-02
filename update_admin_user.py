from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    # Get the existing admin user
    admin_user = User.query.filter_by(username='meetraj').first()
    
    if admin_user:
        # Update email and password
        admin_user.email = 'meetraj22426@gmail.com'
        admin_user.password = '12345'
        db.session.commit()
        print("Admin user updated successfully!")
        print(f"Username: {admin_user.username}")
        print(f"Email: {admin_user.email}")
        print(f"Password: 12345")
        print(f"Role: {admin_user.role}")
    else:
        print("Admin user not found!")
