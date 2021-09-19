import json
import requests
import statistics

url = 'http://weather-api.eba-jgjmjs6p.eu-west-2.elasticbeanstalk.com/api'


class question2():
    r = requests.get(url + '/weather/2/edinburgh')
    data2 = json.loads(r.text)

    for pressure in data2['friday']:
        pressure = pressure['pressure']

    if pressure < 1000:
        print("True")
    else:
        print("False")


question2()
