import requests
import time

def check_latency():
    apiUrl = 'http://localhost:60002/api/history'
    try:
        start_time = time.time()
        response = requests.get(apiUrl)
        end_time = time.time()

        if response.status_code == 200:
            latency = end_time - start_time
            print(f"Latency for API endpoint api/history: {latency:.3f} seconds")
        else:
            print(f"Failed to get a valid response, HTTP Status Code: {response.status_code}")

    except requests.RequestException as e:
        print(f"There was an error accessing the API {apiUrl}")
        print(f"Exception is: {e}")

if __name__ == "__main__":
    check_latency()