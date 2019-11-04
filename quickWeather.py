#! python3
#quickWeather.py

import json,requests,sys

if len(sys.argv) < 2:
    print('Uzycie quickweather.py lokalizacja')
    sys.exit()

location=''.join(sys.argv[1:])
url ='http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)
response=requests.get(url)
response.raise_for_status()

weatherData = json.loads(response.text)
w=weatherData['list']
print('Aktualna pogoda w %s:' %(location))
print(w[0]['weather'][0]['main'],'-',w[0]['weather'][0]['description'])
print()
print('Jutro:')
print(w[1]['weather'][0]['main'],'-',w[1]['weather'][0]['description'])
print()
print('Pojutrze:')
print(w[2]['weather'][0]['main'],'-',w[2]['weather'][0]['description'])
