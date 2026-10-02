from app import create_app

# Create Flask App
app = create_app()

# ----------------------
# Run Application
# ----------------------
if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port=5000
    )
