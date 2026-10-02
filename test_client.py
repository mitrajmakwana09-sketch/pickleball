from app import create_app

app = create_app()
client = app.test_client()

print("Testing /courts endpoint...")
response = client.get('/courts')
print(f"Status code: {response.status_code}")
print(f"Response length: {len(response.data)}")
print("\nFirst 1000 characters of response:")
print(response.data.decode('utf-8')[:1000])
