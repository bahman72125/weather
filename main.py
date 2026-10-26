import requests

import time
print(time.ctime(1790864499))
appid="f2f238852603acca0c878c17215c1d12"
city=input('Enter city :')
my_url=f'https://api.openweathermap.org/geo/1.0/direct?q={city}&appid={appid}'
res=requests.get(url=my_url)
print(res.status_code)
if res.status_code==200:
    data=res.json()
    print(data)
    lat=data[0]['lat']
    lon=data[0]['lon']
    print(lat,lon)
    my_url=f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={appid}'
    res1=requests.get(url=my_url)
    print(res1.status_code)
    if res1.status_code==200:
        data1=res1.json()
        print(data1)
else:
    print(res.status_code)         
