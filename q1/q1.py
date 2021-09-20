import json
import requests
import statistics

url = 'http://weather-api.eba-jgjmjs6p.eu-west-2.elasticbeanstalk.com/api'


class question1():
    r = requests.get(url + '/weather/2/bath')
    data1 = json.loads(r.text)
    print(data1['wednesday'][9]['temperature'])


question1()