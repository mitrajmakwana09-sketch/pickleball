from app import create_app, db
from app.models import Court

app = create_app()

with app.app_context():
    with app.test_request_context():
        # Get courts
        courts = Court.query.all()
        
        print(f"Found {len(courts)} courts")
        
        # Try rendering the template
        try:
            from flask import render_template
            rendered = render_template('courts.html', courts=courts)
            print("\nTemplate rendered successfully!")
            print("\nFirst 500 characters of rendered template:")
            print(rendered[:500])
        except Exception as e:
            print(f"\nError rendering template: {type(e).__name__}: {e}")
            import traceback
            print("\nFull traceback:")
            print(traceback.format_exc())
