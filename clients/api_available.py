import requests

def checkAvailable():
    apiURL = 'http://localhost:60002/api/history'
    
    try:
        response = requests.get(apiURL)
        if response.status_code == 200:
            print(f"Response code: {response.status_code}")
            print(f"API: {apiURL} is AVAILABLE")
        else:
            print(f"Response code: {response.status_code}")
            print(f"API: {apiURL} is UNAVAILABLE")
    except requests.RequestException as e:
        print(f"There was an error accessing the API {apiURL}")
        print(f"Exception is: {e}")

if __name__ == "__main__":
    checkAvailable()