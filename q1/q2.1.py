import json
import requests
import statistics

url = 'http://weather-api.eba-jgjmjs6p.eu-west-2.elasticbeanstalk.com/api'


class question2():
    # load in the edinburgh dataset and create a dictionary
    r = requests.get(url + '/weather/2/edinburgh')
    data2 = json.loads(r.text)
# locate the specific day key needed 
    for pressure in data2['friday']:
        # locate the specific element needed within the day key
        pressure = pressure['pressure']
# simple if statement to produce boolean state dependent on the statement conditions
    if pressure < 1000:
        print(True)
    else:
        print(False)


question2()
