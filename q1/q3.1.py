import json
import requests
import statistics
# read in the api 
url = 'http://weather-api.eba-jgjmjs6p.eu-west-2.elasticbeanstalk.com/api'

class question3():
    # specify the api key needed
    r = requests.get(url + '/weather/2/cardiff')
    # load in as python dict
    data3 = json.loads(r.text)
    # locate the day key and temp object to read in the data for each day 
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
    # clacluate the avergae for each day and store in a varoble for all avergages temperature for the days
    tempavg = (temp1, temp2, temp3, temp4, temp5, temp6, temp7)
    # use the avergaes for each day to calulate the median of these values to find the mean temperature of the week 
    print(statistics.median(tempavg))


question3()