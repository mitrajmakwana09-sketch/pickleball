from app import create_app, db
from app.models import Booking

app = create_app()

with app.app_context():
    bookings = Booking.query.all()
    print("Current bookings in DB:")
    print("-" * 50)
    for b in bookings:
        print(f"ID: {b.id}, Status: '{b.status}'")
