import json
import requests
import statistics

url = 'http://weather-api.eba-jgjmjs6p.eu-west-2.elasticbeanstalk.com/api'

class question3():
    r = requests.get(url + '/weather/2/cardiff')
    data3 = json.loads(r.text)

    for temp in data3['friday']:
        temp1 = temp['temperature']

    for temp in data3['thursday']:
        temp2 = temp['temperature']

    for temp in data3['wednesday']:
        temp3 = temp['temperature']

    for temp in data3['tuesday']:
        temp4 = temp['temperature']

    for temp in data3['monday']:
        temp5 = temp['temperature']

    for temp in data3['saturday']:
        temp6 = temp['temperature']

    for temp in data3['sunday']:
        temp7 = temp['temperature']

    tempavg = (temp1, temp2, temp3, temp4, temp5, temp6, temp7)

    print(statistics.mean(tempavg))


question3()