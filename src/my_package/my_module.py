
import requests

TIME_URL = "https://timeapi.io/api/Time/current/zone?timeZone=Europe/London"

def welcome():
    print("Hello World!")
    
    r = requests.get(TIME_URL, headers={
        "content-type": "application/json",
        "accept": "application/json"
        })

    if r.status_code == 200:
        print(r.json()["time"])
    else:
        print("Could not determine time")
