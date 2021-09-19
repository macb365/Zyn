import requests
import json

url = 'http://weather-api.eba-jgjmjs6p.eu-west-2.elasticbeanstalk.com/api'

cities_request = requests.get(url + '/cities')
cities_data = json.loads(cities_request.text)

# print(json.dumps(cities, indent=3))
cities_all = {}
# gather city data and append in array
for city in cities_data['cities']:
    # print(city)
    city_request = requests.get(url + '/weather/2/' + city)
    city_data = json.loads(city_request.text)
    city_object = {}
    # for day in city_data:
    #     city_object.update(city_data[day])
    city_object.update(city_data)
    cities_all.update(city_object)

    # print(json.dumps(cities_all, indent=3))
    # print(json.dumps(city_data, indent=3))

for city in cities_all:
    # print(json.dumps(cities_all[city], indent=3))


    # gets the day data from the day key and then uses the key
    # to access the city data and specify the wind speed of each day and each instance reading
    # for days in city_data:
    #     print(days)
    #     day_data = city_data[days]
    #     # for item in day_data:
    #     #     print(item['wind_speed'])
