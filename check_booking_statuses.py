from app import create_app, db
from app.models import Booking

app = create_app()

with app.app_context():
    bookings = Booking.query.all()
    print("Current Bookings:")
    print("-" * 60)
    for booking in bookings:
        print(f"ID: {booking.id}, User: {booking.user_id}, Court: {booking.court_id}, Date: {booking.booking_date}, Slot: {booking.slot}, Status: '{booking.status}'")
