import requests

def getCalcCount():
    apiUrl = 'http://localhost:60002/api/history'
    try:
        response = requests.get(apiUrl)
        if (response.status_code == 200):
            data = response.json()
            history = data.get('history', [])
            calcCount = len(history)
            print(f"Number of calculations: {calcCount}")
        else:
            print(f"Failed to find the number of calculations")
    except requests.RequestException as e:
        print(f"There was an error accessing the API {apiUrl}")
        print(f"Exception is: {e}")
if __name__ == "__main__":
    getCalcCount()