import requests
import json

def test():
    url=f'https://launchlibrary.net/1.4/launch?startdate=2015-02-10&enddate=2015-05-05'
    req = requests.get(url).json()
    print(req)


test()