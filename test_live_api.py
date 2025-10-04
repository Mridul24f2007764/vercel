import requests

# Your main domain from the deployment
BASE_URL = "https://vercel-latency-api-alpha.vercel.app"

def test_all_endpoints():
    print("Testing your live Vercel API...")
    
    endpoints = [
        ("GET", "/", "Root endpoint"),
        ("GET", "/health", "Health check"),
        ("GET", "/regions", "Available regions"),
    ]
    
    for method, endpoint, description in endpoints:
        print(f"\n{description}: {BASE_URL}{endpoint}")
        try:
            if method == "GET":
                response = requests.get(f"{BASE_URL}{endpoint}")
            else:
                response = requests.post(f"{BASE_URL}{endpoint}")
            
            print(f"Status: {response.status_code}")
            if response.status_code == 200:
                print(f"Response: {response.json()}")
            else:
                print(f"Error: {response.text}")
        except Exception as e:
            print(f"Failed: {e}")
    
    # Test main API endpoint
    print(f"\nTesting main API: {BASE_URL}/api/")
    try:
        payload = {
            "regions": ["emea", "apac"],
            "threshold_ms": 200
        }
        response = requests.post(f"{BASE_URL}/api/", json=payload)
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            print("API is working correctly! ✅")
            print("Response:", response.json())
        else:
            print(f"API Error: {response.text}")
    except Exception as e:
        print(f"API Test Failed: {e}")

if __name__ == "__main__":
    test_all_endpoints()
