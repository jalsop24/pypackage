
import requests

TIME_URL = "http://worldtimeapi.org/api/timezone/Europe/London"

def welcome():
    print("Hello World!")
    
    r = requests.get(TIME_URL)

    print(r)
