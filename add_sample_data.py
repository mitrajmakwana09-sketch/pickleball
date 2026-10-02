from app import create_app, db
from app.models import Court

app = create_app()

with app.app_context():
    # Add sample courts
    court1 = Court(
        name="Court A - Main",
        location="Sports Complex, Ground Floor",
        price=300,
        status="Available"
    )
    
    court2 = Court(
        name="Court B - Premium",
        location="Sports Complex, First Floor",
        price=500,
        status="Available"
    )
    
    court3 = Court(
        name="Court C - Practice",
        location="Near Entrance",
        price=200,
        status="Maintenance"
    )
    
    db.session.add_all([court1, court2, court3])
    db.session.commit()
    
    print("Sample courts added successfully!")
