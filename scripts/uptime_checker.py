import requests

URL = "https://github.com"

try:
    response = requests.get(URL, timeout=5)
    if response.status_code == 200:
        print("✓ Application is UP")
    else:
        print(f"✗ Application is DOWN (Status: {response.status_code})")
except:
    print("✗ Application is DOWN (Connection failed)")
