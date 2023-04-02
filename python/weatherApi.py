import json
import requests


print('Please enter your zip code:')
zip = input()

r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=74ab6e7e5c044d42e337aa299de49547' %zip)
data = r.json()

print(data['weather'][0]['description'])