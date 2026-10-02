from app import create_app, db
from app.models import Booking

app = create_app()

with app.app_context():
    # Let's create a test pending booking
    new_booking = Booking(
        user_id=3,
        court_id=1,
        booking_date='2026-07-05',
        slot='06:00 AM - 07:00 AM',
        status='Pending'
    )
    db.session.add(new_booking)
    db.session.commit()

    print(f"Created test pending booking with ID: {new_booking.id}")
